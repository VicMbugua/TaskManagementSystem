from ui.manage_account_ui import Ui_ManageAccount
from PyQt5.QtWidgets import QDialog, QMessageBox
from data.database_manager import DatabaseManager

class ManageAccount(QDialog):
    def __init__(self, user_id, widget, parent=None):
        super(ManageAccount, self).__init__(parent)
        
        self.ui = Ui_ManageAccount()
        self.ui.setupUi(self)
        
        self.parent = parent
        
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.change_username_btn.setChecked(True)
        self.widget = widget
        self.db_manager = DatabaseManager("data/tasks.db")
        self.user_id = user_id
        username = self.db_manager.fetch_data(f"SELECT username FROM users WHERE user_id = {self.user_id}")
        self.username = username[0][0]
        self.ui.current_username.setText(f"Change username {self.username}")
        self.ui.error_message.setText("")
        self.ui.error_message_2.setText("")
        self.ui.error_message_3.setText("")
        self.ui.reset_btn.clicked.connect(self.handle_reset)
        self.ui.change_username_btn_2.clicked.connect(self.handle_change_username)
        self.ui.reset_btn_2.clicked.connect(self.handle_reset_2)
        self.ui.change_password_btn_2.clicked.connect(self.handle_change_password)
        self.ui.delete_account_btn_2.clicked.connect(self.delete_account)
        
    def on_change_username_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def on_change_password_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def on_delete_account_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def handle_reset(self):
        self.ui.new_username.setText("")
        self.ui.password.setText("")
        
    def handle_change_username(self):
        new_username = self.ui.new_username.text()
        username_exists = self.db_manager.check_user(new_username)
        password = self.ui.password.text()
        valid_password = self.db_manager.check_password(self.username, password)
        if new_username == "" or password == "":
            self.ui.error_message.setText("Please fill all the fields before continuing.")
        elif username_exists is True:
            self.ui.error_message.setText("Username already exists!")
            self.ui.new_username.setText("")
            self.ui.password.setText("")
            self.ui.new_username.setFocus()
        elif valid_password is False:
            self.ui.error_message.setText("Wrong password. Please try again.")
            self.ui.password.setText("")
        else:
            self.db_manager.execute_query(f"UPDATE users SET username = '{new_username}' WHERE user_id = {self.user_id}")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Successfully changed username from {self.username} to {new_username}")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.username = new_username
            self.ui.current_username.setText(f"Change username {self.username}")
            self.ui.new_username.setText("")
            self.ui.password.setText("")
            
    def handle_reset_2(self):
        self.ui.current_password.setText("")
        self.ui.new_password.setText("")
        self.ui.confirm_new_password.setText("")
        
    def handle_change_password(self):
        current_password = self.ui.current_password.text()
        new_password = self.ui.new_password.text()
        confirm_new_password = self.ui.confirm_new_password.text()
        valid_password = self.db_manager.check_password(self.username, current_password)
        if current_password == "" or new_password == "" or confirm_new_password == "":
            self.ui.error_message_2.setText("Please fill all the fields before continuing.")
        elif valid_password is False:
            self.ui.error_message_2.setText("Wrong password. Please try again.")
            self.ui.current_password.setText("")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.current_password.setFocus()
        elif new_password != confirm_new_password:
            self.ui.error_message_2.setText("Passwords don't match!")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.new_password.setFocus()
        else:
            self.db_manager.execute_query(f"UPDATE users SET password = '{new_password}' WHERE user_id = {self.user_id}")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Successfully changed your password")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.ui.current_password.setText("")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            
    def delete_account(self):
        password = self.ui.password_2.text()
        valid_password = self.db_manager.check_password(self.username, password)
        if password == "":
            self.ui.error_message_3.setText("Please enter your password")
        elif valid_password is False:
            self.ui.error_message_3.setText("Wrong password")
            self.ui.password_2.setText("")
            self.ui.password_2.setFocus()
        else:
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to delete your account?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.db_manager.remove_user(self.user_id)
                self.parent.close()
                self.close()
                self.widget.show()