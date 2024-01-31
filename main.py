from PyQt5.QtCore import QDate, QObject, Qt, QModelIndex, QVariant
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, qApp, QDialog, QMessageBox, QStyledItemDelegate, QInputDialog, QComboBox, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import record
from interface_ui import Ui_MainWindow
from add_task_ui import Ui_AddTask
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3

        
class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    # Override the createEditor() method to return a QPushButton
    def paint(self, painter, option, index):
        if index.column() == 9:
            button = QPushButton("Edit")
        # Connect the clicked signal to a custom slot
            button.clicked.connect(lambda: self.editTask(index))
            button.setGeometry(option.rect)
            button.show()
        else:
            super().paint(painter, option, index)

        
    def editTask(self, index):
        # Get the model and the task id from the index
        model = index.model()
        task_id = model.data(model.index(index.row(), 0))
        # Prompt the user for a new task name
        new_task, ok = QInputDialog.getText(None, "Edit Task", "Enter a new task name:")
        if ok and new_task:
            # Update the model and the database with the new task name
            model.setData(index, new_task)
            model.submitAll()
            model.database().commit()
            
class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent = None) -> None:
        super(ComboBoxDelegate, self).__init__(parent)
    
    def createEditor(self, parent, option, index):
        combo_box = QComboBox(parent)
        combo_box.addItems(["Done", "Edit", "Delete"])
        return combo_box
    
    def setEditorData(self, editor, index):
        current_text = index.model().data(index, Qt.EditRole)
        combo_box = editor
        combo_box.setCurrentText(current_text)
        
    def setModelData(self, editor, model, index):
        combo_box = editor
        selected_text = combo_box.currentText()
        model.setData(index, selected_text, Qt.EditRole)
        
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
        
    def display_tasks(self):
        self.table = self.ui.tasks_list
        
        self.db_manager = DatabaseManager("tasks.db")
        query = "SELECT task_name, priority, due_date, label_name, status, description, created_at FROM tasks"
        result = self.db_manager.fetch_data(query)
        headers = ["Tasks Name", "Priority", "Due Date", "Labels", "Status", "Description", "Created At"]
        
        model = QStandardItemModel(len(result), len(headers))
        model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                model.setItem(row_num, col_num, item)
        self.table.setModel(model)
        self.delegate = ComboBoxDelegate(self.table)
        self.table.setItemDelegateForColumn(7, self.delegate)
        self.show()
        
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
        window = MainWindow()
        window.display_tasks()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.setWindowTitle("Task Management System")
    window.display_tasks()
    window.show()
    sys.exit(app.exec())