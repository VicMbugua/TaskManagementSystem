from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QComboBox, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
from data.database_manager import DatabaseManager
import data.database_manager as database_manager

class TasksPage(QMainWindow):
    def __init__(self, ui,edit_task_ui, task_ui):
        super(TasksPage, self).__init__()
        self.ui = ui
        self.edit_task_ui = edit_task_ui
        self.task_ui = task_ui
        self.ui.add_task_btn.clicked.connect(self.open_add_task)
        self.display_tasks()
        
    def display_tasks(self):
        table = self.ui.tasks_list
        db_manager = DatabaseManager("data/tasks.db")
        query = "SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks WHERE status = 'Not Started' OR status = 'Started'"
        result = db_manager.fetch_data(query)
        headers = ["Task ID","Tasks Name", "Priority", "Due Date", "Label", "Status", "Description", "Created At", "Edit"]
        self.tasks_model = QStandardItemModel(len(result), len(headers))
        self.tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.tasks_model.setItem(row_num, col_num, item)
        table.setModel(self.tasks_model)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()
        table.setColumnWidth(self.tasks_model.columnCount() - 1, 100)
        table.setSortingEnabled(True)
        table.sortByColumn(self.tasks_model.columnCount() - 2, Qt.AscendingOrder)
        for row in range(self.tasks_model.rowCount()):
            button = QComboBox()
            button.addItems(["Select...","Done", "Edit", "Delete"])
            button.currentIndexChanged.connect(lambda index, row=row: self.handle_action(index, row))
            table.setIndexWidget(self.tasks_model.index(row, self.tasks_model.columnCount() - 1), button)
            # self.task_id = model.index(row, 0).data()
        self.show()
        
    def handle_action(self, index, row):
        selected_action = self.sender().currentText()
        task_id = self.tasks_model.index(row, 0).data()
        db_manager = db_manager = DatabaseManager("data/tasks.db")
        tasks_name = db_manager.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {task_id}")
        tasks_name = tasks_name[0][0]
        if selected_action == "Done":
            # print(f"Done selected for record {task_id}")
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to mark {tasks_name} as done")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            confirmation.setWindowTitle("Confirmation")
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                query = f"UPDATE tasks SET status = 'Completed' WHERE task_id = {task_id}"
                db_manager.execute_query(query)
                self.display_tasks()
                self.display_completed_tasks()
                self.display_number_of_tasks()
            else:
                self.display_tasks()
        elif selected_action == "Edit":
            self.open_edit_task(task_id)
        elif selected_action == "Delete":
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to delete {tasks_name}")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                database_manager.remove_task(task_id)
                self.display_tasks()
                self.display_number_of_tasks()
            else:
                self.display_tasks()
    
    def open_edit_task(self, task_id):
        self.edit_window = QDialog()
        # self.edit_task_ui = Ui_EditTask()
        # self.edit_task_ui.setupUi(self.edit_window)
        self.edit_task_ui.due_date.setMinimumDate(QDate.currentDate())
        db_manager = DatabaseManager("data/tasks.db")
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {task_id}"
        self.result = db_manager.fetch_data(query)
        self.edit_task_ui.task_name.setText(self.result[0][0])
        self.edit_task_ui.label_name.setEditText(self.result[0][3])
        date = self.result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.edit_task_ui.due_date.setDate(due_date)
        self.edit_task_ui.status.setCurrentIndex(self.edit_task_ui.status.findData(self.result[0][4], Qt.DisplayRole))
        self.edit_task_ui.priority.setCurrentIndex(self.edit_task_ui.priority.findData(self.result[0][1], Qt.DisplayRole))
        self.edit_task_ui.description.setText(self.result[0][5])
        self.edit_task_ui.edit_btn.clicked.connect(lambda: self.handle_edit_btn(task_id))
        self.edit_task_ui.cancel_btn.clicked.connect(self.handle_close_btn)
        self.edit_window.show()
        
    def handle_edit_btn(self, task_id):
        task_name = self.edit_task_ui.task_name.text()
        date = self.edit_task_ui.due_date.date()
        due_date = date.toString("yyyy-MM-dd")
        priority = self.edit_task_ui.priority.currentText()
        label_name = self.edit_task_ui.label_name.currentText()
        description = self.edit_task_ui.description.toPlainText()
        status = self.edit_task_ui.status.currentText()
        database_manager.edit_task(task_id ,task_name, priority, due_date, label_name, status, description)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Successfully edited {task_name}.")
        msg_box.setWindowTitle("Success")
        msg_box.exec()
        self.display_tasks()
        self.edit_window.close()
    
    def handle_close_btn(self):
        current_task_name = self.result[0][0]
        new_task_name = self.edit_task_ui.task_name.text()
        if new_task_name != current_task_name:
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.display_tasks()
                self.edit_window.close()
        else:
            self.edit_window.close()

    def open_add_task(self):
        # self.window = QDialog()
        # self.task_ui = Ui_AddTask()
        # self.task_ui.setupUi(self.window)
        self.task_ui.due_date.setMinimumDate(QDate.currentDate())
        self.task_ui.reset_btn.clicked.connect(self.handle_reset_btn)
        self.task_ui.save_btn.clicked.connect(self.handle_save_btn)
        self.task_ui.cancel_btn.clicked.connect(self.handle_cancel_btn)
        self.window.show()
        
    def handle_reset_btn(self):
        self.task_ui.task_name.setText("")
        self.task_ui.label_name.setCurrentIndex(0)
        self.task_ui.due_date.setDate(QDate.currentDate())
        self.task_ui.priority.setCurrentIndex(0)
        self.task_ui.status.setCurrentIndex(0)
        self.task_ui.description.setText("")
        
    def handle_save_btn(self):
        task_name = self.task_ui.task_name.text()
        date = self.task_ui.due_date.date()
        due_date = date.toString("yyyy-MM-dd")
        priority = self.task_ui.priority.currentText()
        label_name = self.task_ui.label_name.currentText()
        description = self.task_ui.description.toPlainText()
        status = self.task_ui.status.currentText()
        user_id = 1
        if task_name != "":
            database_manager.add_task(user_id, task_name, priority, due_date, label_name, status, description)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Successfully added {task_name}.")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            self.handle_reset_btn()
            self.display_tasks()
            self.display_number_of_tasks()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Please enter a task name.")
            msg_box.setWindowTitle("Invalid")
            msg_box.exec()
            
    def handle_cancel_btn(self):
        task_name = self.task_ui.task_name.text()
        if task_name != "":
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.display_tasks()
                self.window.close()
        else:
            self.window.close()
