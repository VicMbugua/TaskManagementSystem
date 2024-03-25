import ctypes
import re
from PyQt5.QtCore import QEvent, Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.sign_up_ui import Ui_SignUp
from data.database_manager import DatabaseManager


class SignUpWindow(QMainWindow):
    def __init__(self, widget):
        super(SignUpWindow, self).__init__()

        self.ui = Ui_SignUp()
        self.ui.setupUi(self)

        self.widget = widget
        self.ui.error_message.setText("")
        self.ui.sign_up_btn.clicked.connect(self.handle_sign_up)
        self.ui.login_btn.clicked.connect(self.handle_login)
        regex = QRegExp("^[a-zA-Z][a-zA-Z0-9_]*$")
        self.validator = QRegExpValidator(regex, self.ui.username)
        self.ui.username.setValidator(self.validator)

        self.db_manager = DatabaseManager()
        self.installEventFilter(self)
        self.caps_lock_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1
        self.toggle_caps_lock_label()

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self.caps_lock_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1
        self.toggle_caps_lock_label()
        self.ui.username.setFocus()
        self.ui.username.setText("")
        self.ui.password.setText("")
        self.ui.confirm_password.setText("")
        self.ui.error_message.setText("")
            
    def eventFilter(self, obj, event) -> bool:
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_CapsLock:
                self.caps_lock_on = not self.caps_lock_on
                self.toggle_caps_lock_label()
        return super().eventFilter(obj, event)

    def toggle_caps_lock_label(self):
        if self.caps_lock_on:
            self.ui.caps_lock.setText("Caps lock is on")
        else:
            self.ui.caps_lock.setText("")

    def handle_sign_up(self):
        """Creates a new user if the username is available."""
        username = self.ui.username.text().lower().strip()
        password = self.ui.password.text()
        confirm_password = self.ui.confirm_password.text()
        valid_username = self.valid_username(username)
        valid_password = self.valid_password(password)
        if username == "" or password == "" or confirm_password == "":
            self.ui.error_message.setText("Please fill all the fields before continuing.")
        elif valid_username is not True:
            self.ui.error_message.setText(valid_username)
            self.ui.username.setText("")
            self.ui.username.setFocus()
        elif self.db_manager.check_user(username):
            self.ui.username.setText("")
            self.ui.error_message.setText("Username already exists")
            self.ui.username.setFocus()
        elif valid_password is not True:
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
            self.ui.error_message.setText(valid_password)
            self.ui.password.setFocus()
        elif password != confirm_password:
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
            self.ui.error_message.setText("Passwords don't match")
            self.ui.password.setFocus()
        else:
            self.db_manager.add_user(username, password)
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText("User added successfully. You can now login.")
            information.setWindowTitle("Success")
            information.exec()
            self.handle_login()
            
    def valid_username(self, username):
        if len(username) < 3:
            return "Username has to be 3 characters long or longer."
        if not username[0].isalpha():
            return "Username can only start with a letter."
        if not re.match(r"^[a-zA-Z0-9_.]*$", username):
            return "Username can only have letters, digits, underscores or periods."
        if all(username.count(char) == len(username) for char in username):
            return "Username cannot have only one letter repeated."
        return True
    
    def valid_password(self, password):
        if len(password) < 5:
            return "Password has to be 5 characters or longer."
        if all(password.count(char) == len(password) for char in password):
            return "Password cannot have only one character repeated."
        return True

    def handle_login(self):
        """Opens the login window."""
        self.widget.setCurrentIndex(0)
