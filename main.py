from PyQt5.QtCore import QDate, QObject, Qt, QModelIndex, QVariant,QSortFilterProxyModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, qApp, QDialog, QMessageBox, QStyledItemDelegate, QInputDialog, QComboBox, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import record
from interface_ui import Ui_MainWindow
from add_task_ui import Ui_AddTask
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
        
        no_of_tasks = record.number_of_tasks()
        self.ui.no_of_tasks.setText(f"Number of tasks {no_of_tasks}")
        self.ui.add_task_btn.clicked.connect(self.open_add_task)
        self.display_tasks()
        
    def display_tasks(self):
        self.table = self.ui.tasks_list
        
        self.db_manager = DatabaseManager("tasks.db")
        query = "SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks"
        result = self.db_manager.fetch_data(query)
        headers = ["Task ID","Tasks Name", "Priority", "Due Date", "Labels", "Status", "Description", "Created At", "Edit"]
        
        self.model = QStandardItemModel(len(result), len(headers))
        self.model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.model.setItem(row_num, col_num, item)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnHidden(0, True)
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(self.table.model())
        self.table.setModel(proxy_model)
        self.table.setSortingEnabled(True)
        for row in range(self.model.rowCount()):
            self.button = QComboBox()
            self.button.addItems(["Select...","Done", "Edit", "Delete"])
            self.button.currentIndexChanged.connect(lambda index, row=row: self.handle_action(index, row))
            self.table.setIndexWidget(self.model.index(row, self.model.columnCount() - 1), self.button)
            self.button.setCurrentText("Select...")
        self.show()
        
    def handle_action(self, index, row):
        selected_action = self.sender().currentText()
        record_id = self.model.index(row, 0).data()
        if selected_action == "Done":
            print(f"Done selected for record {record_id}")
        elif selected_action == "Edit":
            print(f"Edit selected for record {record_id}")
            self.open_add_task()
        elif selected_action == "Delete":
            confirmation = QMessageBox()
            confirmation.setText("Are you sure you want to delete")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                print(f"Delete selected for record {record_id}")
                self.display_tasks()
        
        
    def handle_edit_button(self):
        button = qApp.focusWidget()
        index = self.table.indexAt(button.pos())
        if index.isValid():
            print(f"row {index.row()}, column {index.column()}")

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
        self.task_ui.labels.setText("")
        self.task_ui.due_date.setDate(QDate.currentDate())
        self.task_ui.priority.setCurrentIndex(0)
        self.task_ui.description.setText("")
        
    def handle_save_btn(self):
        task_name = self.task_ui.task_name.text()
        date = self.task_ui.due_date.date()
        due_date = date.toString("yyyy-MM-dd")
        priority = self.task_ui.priority.currentText()
        label_name = self.task_ui.labels.text()
        description = self.task_ui.description.toPlainText()
        status = "Not Started"
        user_id = 1
        record.add_task(user_id, task_name, priority, due_date, label_name, status, description)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Successfully added {task_name}.")
        msg_box.setWindowTitle("Success")
        msg_box.exec()
        self.handle_reset_btn()
        self.display_tasks()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.setWindowTitle("Task Management System")
    # window.display_tasks()
    window.show()
    sys.exit(app.exec())