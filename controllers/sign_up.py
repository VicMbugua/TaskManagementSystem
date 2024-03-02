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
        self.ui.sign_up.clicked.connect(self.handle_sign_up)
        self.ui.login.clicked.connect(self.handle_login)
        
        self.db_manager = DatabaseManager()
        
    def handle_sign_up(self):
        """Creates a new user if the username is available."""
        username = self.ui.username.text().lower().strip()
        password = self.ui.password.text()
        confirm_password = self.ui.confirm_password.text()
        username_exists = self.db_manager.check_user(username)
        if username == "" or password == "" or confirm_password == "":
            self.ui.error_message.setText("Please fill all the fields before continuing.")
        elif username_exists is True:
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
            self.ui.error_message.setText("Username already exists")
            self.ui.username.setFocus()
        elif password != confirm_password:
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
            self.ui.error_message.setText("Passwords don't match")
            self.ui.password.setFocus()
        else:
            self.db_manager.add_user(username, password)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("User added successfully. You can now login.")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.handle_login()
            
    def handle_login(self):
        """Opens the login window."""
        self.ui.username.setFocus()
        self.ui.username.setText("")
        self.ui.password.setText("")
        self.ui.confirm_password.setText("")
        self.ui.error_message.setText("")
        self.widget.setCurrentIndex(0)
