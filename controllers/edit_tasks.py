from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.edit_task_ui import Ui_EditTask
from ui.add_task_ui import Ui_AddTask
from data.database_manager import DatabaseManager


class EditTaskWindow(QDialog):
    def __init__(self, task_id, parent):
        super(EditTaskWindow, self).__init__(parent)
        self.edit_window = QDialog()
        self.ui = Ui_EditTask()
        self.ui.setupUi(self)
        
        self.db_manager = DatabaseManager()
        self.parent = parent
        
        self.ui.due_date.setMinimumDate(QDate.currentDate())
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {task_id}"
        self.result = self.db_manager.fetch_data(query)
        self.ui.task_name.setText(self.result[0][0])
        self.ui.label_name.setEditText(self.result[0][3])
        date = self.result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.ui.due_date.setDate(due_date)
        self.ui.status.setCurrentIndex(self.ui.status.findData(self.result[0][4], Qt.DisplayRole))
        self.ui.priority.setCurrentIndex(self.ui.priority.findData(self.result[0][1], Qt.DisplayRole))
        self.ui.description.setText(self.result[0][5])
        self.ui.save_btn.clicked.connect(lambda: self.handle_edit_btn(task_id))
        self.ui.cancel_btn.clicked.connect(self.handle_cancel_btn)
        self.ui.reset_btn.clicked.connect(lambda: self.handle_edit_reset_btn(task_id))
        
    def handle_edit_btn(self, task_id):
        task_name = self.ui.task_name.text()
        date = self.ui.due_date.date()
        due_date = date.toString("yyyy-MM-dd")
        priority = self.ui.priority.currentText()
        label_name = self.ui.label_name.currentText()
        description = self.ui.description.toPlainText()
        status = self.ui.status.currentText()
        self.db_manager.edit_task(task_id ,task_name, priority, due_date, label_name, status, description)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Successfully edited {task_name}.")
        msg_box.setWindowTitle("Success")
        msg_box.exec()
        self.parent.refresh_table()
        self.close()
        
    def handle_edit_reset_btn(self, task_id):
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {task_id}"
        self.result = self.db_manager.fetch_data(query)
        self.ui.task_name.setText(self.result[0][0])
        self.ui.label_name.setEditText(self.result[0][3])
        date = self.result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.ui.due_date.setDate(due_date)
        self.ui.status.setCurrentIndex(self.ui.status.findData(self.result[0][4], Qt.DisplayRole))
        self.ui.priority.setCurrentIndex(self.ui.priority.findData(self.result[0][1], Qt.DisplayRole))
        self.ui.description.setText(self.result[0][5])
    
    def handle_cancel_btn(self):
        current_task_name = self.result[0][0]
        new_task_name = self.ui.task_name.text()
        if new_task_name != current_task_name:
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.close()
        else:
            self.close()


class AddTaskWindow(QDialog):
    def __init__(self, user_id, parent):
        super(AddTaskWindow, self).__init__(parent)
        
        self.ui = Ui_AddTask()
        self.ui.setupUi(self)
        
        self.parent = parent
        self.db_manager = DatabaseManager()
        self.user_id = user_id
        
        self.ui.due_date.setMinimumDate(QDate.currentDate())
        self.ui.reset_btn.clicked.connect(self.handle_reset_btn)
        self.ui.save_btn.clicked.connect(self.handle_save_btn)
        self.ui.cancel_btn.clicked.connect(self.handle_cancel_btn)
        
    def handle_reset_btn(self):
        self.ui.task_name.setText("")
        self.ui.label_name.setCurrentIndex(0)
        self.ui.due_date.setDate(QDate.currentDate())
        self.ui.priority.setCurrentIndex(0)
        self.ui.status.setCurrentIndex(0)
        self.ui.description.setText("")
        
    def handle_save_btn(self):
        task_name = self.ui.task_name.text()
        date = self.ui.due_date.date()
        due_date = date.toString("yyyy-MM-dd")
        priority = self.ui.priority.currentText()
        label_name = self.ui.label_name.currentText()
        description = self.ui.description.toPlainText()
        status = self.ui.status.currentText()
        if task_name != "":
            self.db_manager.add_task(self.user_id, task_name, priority, due_date, label_name, status, description)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Successfully added {task_name}.")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.handle_reset_btn()
            self.parent.refresh_table()
            self.parent.display_number_of_tasks()
            self.close()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please enter a task name.")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
            self.ui.task_name.setFocus()
            
    def handle_cancel_btn(self):
        task_name = self.ui.task_name.text()
        if task_name != "":
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.handle_reset_btn()
                self.close()
        else:
            self.close()