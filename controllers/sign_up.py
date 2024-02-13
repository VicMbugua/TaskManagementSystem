from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.sign_up_ui import Ui_SignUp
from data.database_manager import DatabaseManager

class SignUpWindow(QMainWindow):
    def __init__(self, widget):
        super(SignUpWindow, self).__init__()
        
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        
        self.widget = widget
        
        self.ui.sign_up.clicked.connect(self.handle_sign_up)
        self.ui.login.clicked.connect(self.handle_login)
        
        self.db_manager = DatabaseManager("data/tasks.db")
        
    def handle_sign_up(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        confirm_password = self.ui.confirm_password.text()
        
        username_exists = self.db_manager.check_user(username)
        if username == "" or password == "" or confirm_password == "":
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please fill all the fields before continuing.")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
        elif username_exists is True:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Username already exists!")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
        elif password != confirm_password:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Passwords don't match!")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
            self.ui.password.setText("")
            self.ui.confirm_password.setText("")
        else:
            self.db_manager.add_user(username, password)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("User added successfully. You can now login.")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.widget.setCurrentIndex(0)
            
    def handle_login(self):
        self.widget.setCurrentIndex(0)
