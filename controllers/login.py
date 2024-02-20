from PyQt5.QtWidgets import QMainWindow
from ui.login_ui import Ui_LogIn
from data.database_manager import DatabaseManager
from controllers.main_window import MainWindow


class LogInWindow(QMainWindow):
    def __init__(self, widget):
        super(LogInWindow, self).__init__()

        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        self.widget = widget
        self.ui.error_message.setText("")
        self.ui.sign_up.clicked.connect(self.handle_sign_up)
        self.ui.login.clicked.connect(self.handle_login)
        self.db_manager = DatabaseManager("data/tasks.db")

    def handle_login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        # TODO change username to lowercase

        valid_user = self.db_manager.check_user(username)
        valid_password = self.db_manager.check_password(username, password)
        if username == "" or password == "":
            self.ui.error_message.setText("Please fill all the fields before continuing.")
        elif valid_user is False:
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.error_message.setText("Username does not exist. Do you want to sign up?")
            self.ui.username.setFocus()
        elif valid_password is False:
            self.ui.password.setText("")
            self.ui.error_message.setText("Wrong password. Please try again.")
        else:
            self.ui.username.setText("")
            self.ui.password.setText("")
            self.ui.username.setFocus()
            self.widget.close()
            self.user_id = self.db_manager.fetch_data(f"SELECT user_id FROM users WHERE username = '{username}'")
            self.user_id = int(self.user_id[0][0])
            window = MainWindow(self.user_id, self.widget)
            window.show()

    def handle_sign_up(self):
        self.ui.username.setFocus()
        self.widget.setCurrentIndex(1)
