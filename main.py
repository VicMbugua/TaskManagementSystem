from PyQt5.QtCore import QDate, QObject, Qt, QModelIndex, QVariant,QSortFilterProxyModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, qApp, QDialog, QMessageBox, QStyledItemDelegate, QInputDialog, QComboBox, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import record
from interface_ui import Ui_MainWindow
from add_task_ui import Ui_AddTask
from edit_task_ui import Ui_EditTask
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        
    def fetch_data(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.icons_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        
        self.display_number_of_tasks()
        self.ui.add_task_btn.clicked.connect(self.open_add_task)
        self.display_tasks()
        self.display_completed_tasks()
        
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_tasks_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_tasks_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_completed_tasks_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_completed_tasks_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_calender_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_calender_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
# HOME PAGE BEGIN

    def display_number_of_tasks(self):
        no_of_tasks = record.number_of_tasks()
        self.ui.no_of_tasks.setText(f"Number of tasks {no_of_tasks}")

# HOME PAGE END

# TASKS PAGE BEGIN

    def display_tasks(self):
        table = self.ui.tasks_list
        db_manager = DatabaseManager("tasks.db")
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
        db_manager = db_manager = DatabaseManager("tasks.db")
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
                record.remove_task(task_id)
                self.display_tasks()
                self.display_number_of_tasks()
    
    def open_edit_task(self, task_id):
        self.edit_window = QDialog()
        self.edit_task_ui = Ui_EditTask()
        self.edit_task_ui.setupUi(self.edit_window)
        self.edit_task_ui.due_date.setMinimumDate(QDate.currentDate())
        db_manager = DatabaseManager("tasks.db")
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {task_id}"
        result = db_manager.fetch_data(query)
        self.edit_task_ui.task_name.setText(result[0][0])
        self.edit_task_ui.label_name.setEditText(result[0][3])
        date = result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.edit_task_ui.due_date.setDate(due_date)
        self.edit_task_ui.status.setCurrentIndex(self.edit_task_ui.status.findData(result[0][4], Qt.DisplayRole))
        self.edit_task_ui.priority.setCurrentIndex(self.edit_task_ui.priority.findData(result[0][1], Qt.DisplayRole))
        self.edit_task_ui.description.setText(result[0][5])
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
        record.edit_task(task_id ,task_name, priority, due_date, label_name, status, description)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Successfully edited {task_name}.")
        msg_box.setWindowTitle("Success")
        msg_box.exec()
        self.handle_close_btn()
    
    def handle_close_btn(self):
        self.display_tasks()
        self.edit_window.close()

    def open_add_task(self):
        self.window = QDialog()
        self.task_ui = Ui_AddTask()
        self.task_ui.setupUi(self.window)
        self.task_ui.due_date.setMinimumDate(QDate.currentDate())
        self.task_ui.reset_btn.clicked.connect(self.handle_reset_btn)
        self.task_ui.save_btn.clicked.connect(self.handle_save_btn)
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
        record.add_task(user_id, task_name, priority, due_date, label_name, status, description)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Successfully added {task_name}.")
        msg_box.setWindowTitle("Success")
        msg_box.exec()
        self.handle_reset_btn()
        self.display_tasks()
        self.display_number_of_tasks()

# TASKS PAGE END

# COMPLETED TASKS PAGE BEGIN

    def display_completed_tasks(self):
        table = self.ui.completed_tasks
        db_manager = DatabaseManager("tasks.db")
        query = "SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks WHERE status = 'Completed'"
        result = db_manager.fetch_data(query)
        headers = ["Task ID","Tasks Name", "Priority", "Due Date", "Label", "Status", "Description", "Created At", "Edit"]
        self.completed_tasks_model = QStandardItemModel(len(result), len(headers))
        self.completed_tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.completed_tasks_model.setItem(row_num, col_num, item)
        table.setModel(self.completed_tasks_model)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()
        table.setSortingEnabled(True)
        table.sortByColumn(self.tasks_model.columnCount() - 2, Qt.AscendingOrder)
        for row in range(self.completed_tasks_model.rowCount()):
            button = QComboBox()
            button.addItems(["Select...","Not Done", "Delete"])
            button.currentIndexChanged.connect(lambda index, row=row: self.handle_action_completed(index, row))
            table.setIndexWidget(self.completed_tasks_model.index(row, self.completed_tasks_model.columnCount() - 1), button)
        self.show()
        
    def handle_action_completed(self, index, row):
        selected_action = self.sender().currentText()
        task_id = self.completed_tasks_model.index(row, 0).data()
        db_manager = db_manager = DatabaseManager("tasks.db")
        tasks_name = db_manager.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {task_id}")
        tasks_name = tasks_name[0][0]
        if selected_action == "Not Done":
            # print(f"Done selected for record {task_id}")
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to mark {tasks_name} as not done")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            confirmation.setWindowTitle("Confirmation")
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                query = f"UPDATE tasks SET status = 'Started' WHERE task_id = {task_id}"
                db_manager.execute_query(query)
                self.display_tasks()
                self.display_completed_tasks()
                self.display_number_of_tasks()
            else:
                self.display_tasks()
        elif selected_action == "Delete":
            confirmation = QMessageBox()
            confirmation.setText(f"Are you sure you want to delete {tasks_name}")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                record.remove_task(task_id)
                self.display_completed_tasks()

# COMPLETED TASKS PAGE END

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.setWindowTitle("Task Management System")
    window.show()
    sys.exit(app.exec())