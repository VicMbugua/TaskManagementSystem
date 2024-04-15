import ctypes
import hashlib
from PyQt5.QtCore import QEvent, Qt, QRegExp
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from ui.sign_up_ui import Ui_SignUp
from data.database_manager import DatabaseManager


class SignUpWindow(QMainWindow):
    def __init__(self, widget):
        super(SignUpWindow, self).__init__()

        self.ui = Ui_SignUp()
        self.ui.setupUi(self)

        self.widget = widget
        self.ui.view_password_btn.clicked.connect(lambda: self.handle_view_password(self.ui.password, self.ui.view_password_btn))
        self.ui.view_password_btn_2.clicked.connect(lambda: self.handle_view_password(self.ui.confirm_password, self.ui.view_password_btn_2))
        self.ui.error_message.setText("")
        self.ui.sign_up_btn.clicked.connect(self.handle_sign_up)
        self.ui.login_btn.clicked.connect(self.handle_login)
        self.ui.username.textChanged.connect(self.handle_key_press)
        
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
        self.ui.password.setEchoMode(QLineEdit.Password)
        self.ui.confirm_password.setEchoMode(QLineEdit.Password)
        self.ui.view_password_btn.setIcon(QIcon("icons/hidden_eye_icon.svg"))
        self.ui.view_password_btn.setToolTip("View Password")
        self.ui.view_password_btn_2.setIcon(QIcon("icons/hidden_eye_icon.svg"))
        self.ui.view_password_btn_2.setToolTip("View Password")
    
    def handle_key_press(self, input):
        regex = QRegExp("^[a-zA-Z][a-zA-Z0-9_]*$")
        if input == "":
            self.ui.error_message.setText("")
        elif not regex.exactMatch(input):
            self.ui.error_message.setText("Usernames can only start with a letter and can only contain\nletters, numbers and underscores.")
            self.ui.username.textChanged.disconnect()
            self.ui.username.setText(input[:-1])
            self.ui.username.textChanged.connect(self.handle_key_press)
        else:
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
            
    def handle_view_password(self, line_edit, push_button):
        if line_edit.echoMode() == 2:
            line_edit.setEchoMode(QLineEdit.Normal)
            push_button.setIcon(QIcon("icons/eye_icon.svg"))
            push_button.setToolTip("Hide Password")
        else:
            line_edit.setEchoMode(QLineEdit.Password)
            push_button.setIcon(QIcon("icons/hidden_eye_icon.svg"))
            push_button.setToolTip("View Password")

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
            bytes_password = password.encode()
            hashed_password = hashlib.sha256(bytes_password).hexdigest()
            self.db_manager.add_user(username, hashed_password)
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
