import ctypes
import hashlib
from PyQt5.QtCore import QEvent, Qt, QRegExp
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from ui.login_ui import Ui_LogIn
from data.database_manager import DatabaseManager
from controllers.main_window import MainWindow

class LoginWindow(QMainWindow):
    def __init__(self, widget):
        super(LoginWindow, self).__init__()

        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        self.widget = widget
        self.ui.view_password_btn.clicked.connect(self.handle_view_password)
        self.show_password = False
        self.ui.error_message.setText("")
        self.ui.sign_up_btn.clicked.connect(self.handle_sign_up)
        self.ui.login_btn.clicked.connect(self.handle_login)
        self.db_manager = DatabaseManager()
        self.installEventFilter(self)
        
        self.ui.username.textChanged.connect(self.handle_key_press)
        self.caps_lock_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1
        self.toggle_caps_lock_label()
        
    def showEvent(self, event) -> None:
        super().showEvent(event)
        self.caps_lock_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1
        self.toggle_caps_lock_label()
        self.ui.username.setFocus()
        self.ui.username.setText("")
        self.ui.password.setText("")
        self.ui.error_message.setText("")
        self.ui.password.setEchoMode(QLineEdit.Password)
        self.ui.view_password_btn.setIcon(QIcon("icons/hidden_eye_icon.svg"))
        self.ui.view_password_btn.setToolTip("View Password")
        
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
            
    def handle_view_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            self.ui.password.setEchoMode(QLineEdit.Normal)
            self.ui.view_password_btn.setIcon(QIcon("icons/eye_icon.svg"))
            self.ui.view_password_btn.setToolTip("Hide Password")
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)
            self.ui.view_password_btn.setIcon(QIcon("icons/hidden_eye_icon.svg"))
            self.ui.view_password_btn.setToolTip("View Password")
            

    def handle_login(self) -> None:
        """Checks if the username and password are correct then logins the user if they are correct."""
        username: str = self.ui.username.text().lower().strip()
        password: str = self.ui.password.text()
        bytes_password = password.encode()
        hashed_password = hashlib.sha256(bytes_password).hexdigest()
        valid_user: bool = self.db_manager.check_user(username)
        valid_password: bool = self.db_manager.check_password(username, hashed_password)
        if username == "" or password == "":
            self.ui.error_message.setText(
                "Please fill all the fields before continuing."
            )
        elif valid_user is False:
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.error_message.setText("Username does not exist.")
            self.ui.username.setFocus()
        elif valid_password is False:
            self.ui.password.setText("")
            self.ui.error_message.setText("Wrong password. Please try again.")
        else:
            self.widget.close()
            self.user_id = self.db_manager.fetch_data(
                f"SELECT user_id FROM users WHERE username = ?", (username, )
            )
            self.user_id = int(self.user_id[0][0])
            window = MainWindow(self.user_id, self.widget)
            window.show()

    def handle_sign_up(self) -> None:
        """Opens the sign-up window."""
        self.widget.setCurrentIndex(1)
