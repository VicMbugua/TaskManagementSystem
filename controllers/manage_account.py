from ui.manage_account_ui import Ui_ManageAccount
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEvent, Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from data.database_manager import DatabaseManager
import ctypes


class ManageAccountDialog(QDialog):
    def __init__(self, user_id: int, widget, parent=None):
        super(ManageAccountDialog, self).__init__(parent)

        self.ui = Ui_ManageAccount()
        self.ui.setupUi(self)

        self.parent = parent

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.change_username_btn.setChecked(True)
        self.widget = widget
        self.db_manager = DatabaseManager()
        self.user_id = user_id
        username = self.db_manager.fetch_data(
            f"SELECT username FROM users WHERE user_id = {self.user_id}"
        )
        self.username = username[0][0]
        self.ui.current_username.setText(f"Change username {self.username}.")
        regex = QRegExp("^[a-zA-Z][a-zA-Z0-9_]*$")
        self.validator = QRegExpValidator(regex, self.ui.new_username)
        self.ui.new_username.setValidator(self.validator)
        self.ui.error_message.setText("")
        self.ui.error_message_2.setText("")
        self.ui.error_message_3.setText("")
        self.ui.reset_btn.clicked.connect(self.handle_reset)
        self.ui.change_username_btn_2.clicked.connect(self.handle_change_username)
        self.ui.reset_btn_2.clicked.connect(self.handle_reset_2)
        self.ui.change_password_btn_2.clicked.connect(self.handle_change_password)
        self.ui.delete_account_btn_2.clicked.connect(self.delete_account)
        self.ui.reset_btn_3.clicked.connect(self.handle_reset_3)
        self.installEventFilter(self)
        self.caps_lock_on = ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1
        self.toggle_caps_lock_label()
        self.clearFocus()

    def on_change_username_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_change_password_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_delete_account_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def toggle_caps_lock_label(self):
        if self.caps_lock_on:
            self.ui.caps_lock.setText("Caps lock is on")
            self.ui.caps_lock_2.setText("Caps lock is on")
            self.ui.caps_lock_3.setText("Caps lock is on")
        else:
            self.ui.caps_lock.setText("")
            self.ui.caps_lock_2.setText("")
            self.ui.caps_lock_3.setText("")

    def eventFilter(self, obj, event) -> bool:
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_CapsLock:
                self.caps_lock_on = not self.caps_lock_on
                self.toggle_caps_lock_label()
        return super().eventFilter(obj, event)

    def handle_reset(self):
        """Clears the fields in the change username page."""
        self.ui.new_username.setText("")
        self.ui.password.setText("")
        self.ui.new_username.setFocus()

    def handle_change_username(self):
        """Change the username if the new username is available."""
        new_username = self.ui.new_username.text()
        username_exists = self.db_manager.check_user(new_username)
        password = self.ui.password.text()
        valid_username = self.valid_username(new_username)
        valid_password = self.db_manager.check_password(self.username, password)
        if new_username == "" or password == "":
            self.ui.error_message.setText(
                "Please fill all the fields before continuing."
            )
        elif valid_username is not True:
            self.ui.error_message.setText(valid_username)
            self.ui.new_username.setText("")
            self.ui.new_username.setFocus() 
        elif username_exists is True:
            self.ui.error_message.setText("Username already exists. Enter another name.")
            self.ui.new_username.setText("")
            self.ui.password.setText("")
            self.ui.new_username.setFocus()
        elif valid_password is False:
            self.ui.error_message.setText("Wrong password. Please try again.")
            self.ui.password.setText("")
        else:
            self.db_manager.execute_query(
                f"UPDATE users SET username = '{new_username}' WHERE user_id = {self.user_id}"
            )
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText(
                f"Successfully changed username from {self.username} to {new_username}."
            )
            information.setWindowTitle("Success")
            information.exec()
            self.username = new_username
            self.ui.current_username.setText(f"Change username {self.username}.")
            self.ui.new_username.setText("")
            self.ui.password.setText("")
            self.ui.error_message.setText("")
            
    def valid_username(self, username):
        if len(username) < 3:
            return "Username has to be 3 characters long or longer."
        if all(username.count(char) == len(username) for char in username):
            return "Username cannot have only one letter repeated."
        return True

    def handle_reset_2(self):
        """Clears the fields in the change password page."""
        self.ui.current_password.setText("")
        self.ui.new_password.setText("")
        self.ui.confirm_new_password.setText("")
        self.ui.current_password.setFocus()

    def handle_change_password(self):
        """Changes the user's password."""
        current_password = self.ui.current_password.text()
        new_password = self.ui.new_password.text()
        confirm_new_password = self.ui.confirm_new_password.text()
        valid_password = self.db_manager.check_password(self.username, current_password)
        valid_new_password = self.valid_new_password(new_password)
        if current_password == "" or new_password == "" or confirm_new_password == "":
            self.ui.error_message_2.setText(
                "Please fill all the fields before continuing."
            )
        elif valid_password is False:
            self.ui.error_message_2.setText("Wrong password. Please try again.")
            self.ui.current_password.setText("")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.current_password.setFocus()
        elif valid_new_password is not True:
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.error_message_2.setText(valid_new_password)
            self.ui.password.setFocus()
        elif new_password != confirm_new_password:
            self.ui.error_message_2.setText("Passwords don't match.")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.new_password.setFocus()
        else:
            self.db_manager.execute_query(
                f"UPDATE users SET password = '{new_password}' WHERE user_id = {self.user_id}"
            )
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText(f"Successfully changed your password.")
            information.setWindowTitle("Success")
            information.exec()
            self.ui.current_password.setText("")
            self.ui.new_password.setText("")
            self.ui.confirm_new_password.setText("")
            self.ui.error_message_2.setText("")

    def valid_new_password(self, password):
        if len(password) < 5:
            return "The new password has to be 5 characters or longer."
        if all(password.count(char) == len(password) for char in password):
            return "The new password cannot have only one character repeated."
        return True
    
    def delete_account(self):
        """Deletes the user's account."""
        password = self.ui.password_2.text()
        valid_password = self.db_manager.check_password(self.username, password)
        if password == "":
            self.ui.error_message_3.setText("Please enter your password.")
        elif valid_password is False:
            self.ui.error_message_3.setText("Wrong password. Please try again.")
            self.ui.password_2.setText("")
            self.ui.password_2.setFocus()
        else:
            confirmation = QMessageBox()
            confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            confirmation.setWindowTitle("Confirmation")
            confirmation.setText(f"Are you sure you want to delete your account? This action cannot be undone.")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.db_manager.remove_user(self.user_id)
                self.parent.close()
                self.close()
                self.widget.show()

    def handle_reset_3(self):
        """Clears the field in the delete account page."""
        self.ui.password_2.setText("")
        self.ui.password_2.setFocus()
