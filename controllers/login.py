from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDialog, QMessageBox, QComboBox, QAbstractItemView
from ui.login_ui import Ui_LogIn
from data.database_manager import DatabaseManager
from controllers.main_window import MainWindow


class LogInWindow(QMainWindow):
    def __init__(self, widget):
        super(LogInWindow, self).__init__()
        
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)
        
        self.widget = widget
        self.ui.sign_up.clicked.connect(self.handle_sign_up)
        self.ui.login.clicked.connect(self.handle_login)
        self.db_manager = DatabaseManager("data/tasks.db")
        
    def handle_login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        
        valid_user = self.db_manager.check_user(username)
        valid_password = self.db_manager.check_password(username, password)
        if username == "" or password == "":
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please fill all the fields before continuing.")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
        elif valid_user is False:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("User Name does not exist. Do you want to sign up?")
            msg_box.setWindowTitle("Invalid")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            response = msg_box.exec()
            if response == QMessageBox.Yes:
                self.handle_sign_up()
            self.ui.username.setText("")
            self.ui.password.setText("")
        elif valid_password is False:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Wrong password. Please try again.")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
            self.ui.password.setText("")
        else:
            self.widget.close()
            window = MainWindow(username)
            window.show()
            
            
    def handle_sign_up(self):
        # window = SignUpWindow()
        # window.show()
        self.widget.setCurrentIndex(1)