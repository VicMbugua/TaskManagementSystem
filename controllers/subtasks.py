from PyQt5.QtCore import Qt
from ui.subtasks_ui import Ui_SubtaskWindow
from PyQt5.QtWidgets import QDialog, QCheckBox, QAbstractItemView, QPushButton, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from data.database_manager import DatabaseManager


class SubtasksWindow(QDialog):
    def __init__(self, task_id, parent=None):
        super(SubtasksWindow, self).__init__(parent)

        self.ui = Ui_SubtaskWindow()
        self.ui.setupUi(self)

        self.task_id = task_id
        self.db_manager = DatabaseManager()
        task_name = self.db_manager.fetch_data(
            f"SELECT task_name FROM tasks WHERE task_id = {self.task_id}"
        )
        self.task_name = task_name[0][0]
        self.ui.task_name.setText(f"Subtasks for {self.task_name}")

        self.ui.add_subtask_btn.clicked.connect(self.add_subtask)
        self.display_subtasks()
        
    def display_subtasks(self):
        table = self.ui.subtasks_table
        query = f"SELECT subtask_id, subtask_name, status FROM subtasks WHERE task_id = {self.task_id}"
        result = self.db_manager.fetch_data(query)
        headers = ["Check","Subtask ID","Subtask Name", "Status", "Remove"]
        self.subtasks_model = QStandardItemModel(len(result), len(headers))
        self.subtasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.subtasks_model.setItem(row_num, col_num + 1, item)
        table.setModel(self.subtasks_model)
        table.resizeColumnsToContents()
        table.setColumnHidden(1, True)
        table.setColumnHidden(3, True)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSortingEnabled(True)
        table.sortByColumn(3, Qt.DescendingOrder)
        for row in range(self.subtasks_model.rowCount()):
            checkbox = QCheckBox()
            status = self.subtasks_model.index(row, 3).data()
            if status == "Completed":
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)
            checkbox.toggled.connect(lambda checked, row=row: self.on_checkbox_toggled(checked, row))
            table.setIndexWidget(
                self.subtasks_model.index(row, 0),
                checkbox,
            )
        for row in range(self.subtasks_model.rowCount()):
            button = QPushButton()
            button.setText("Remove")
            button.setToolTip("Click to remove subtask")
            button.clicked.connect(lambda index, row=row: self.handle_remove(row))
            table.setIndexWidget(
                self.subtasks_model.index(row, 4),
                button,
            )
            
    def on_checkbox_toggled(self, checked, row):
        if checked:
            subtask_id = self.subtasks_model.index(row, 1).data()
            self.db_manager.execute_query(f"UPDATE subtasks SET status = 'Completed' WHERE subtask_id = {subtask_id}")
            self.display_subtasks()
        else:
            subtask_id = self.subtasks_model.index(row, 1).data()
            self.db_manager.execute_query(f"UPDATE subtasks SET status = 'Not complete' WHERE subtask_id = {subtask_id}")
            self.display_subtasks()
            
    def handle_remove(self, row):
        subtask_id = self.subtasks_model.index(row, 1).data()
        subtask_name = self.subtasks_model.index(row, 2).data()
        confirmation = QMessageBox()
        confirmation.setText(f"Are you sure you want to delete {subtask_name}?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            self.db_manager.remove_subtask(subtask_id)
            self.display_subtasks()

    def add_subtask(self):
        subtask_name = self.ui.subtask_name.text()
        if subtask_name != "":
            self.db_manager.add_subtask(self.task_id, subtask_name)
            self.ui.subtask_name.setText("")
            self.display_subtasks()
