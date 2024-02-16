from ui.subtasks_ui import Ui_SubtaskWindow
from PyQt5.QtWidgets import QDialog, QCheckBox, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from data.database_manager import DatabaseManager

class SubtasksWindow(QDialog):
    def __init__(self, task_id, parent=None):
        super(SubtasksWindow, self).__init__(parent)
        
        self.ui = Ui_SubtaskWindow()
        self.ui.setupUi(self)
        
        self.task_id = task_id
        self.db = DatabaseManager("data/tasks.db")
        task_name = self.db.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {self.task_id}")
        self.task_name = task_name[0][0]
        self.ui.task_name.setText(self.task_name)
        
        self.ui.add_subtask_btn.clicked.connect(self.add_subtask)
        self.display_subtasks()
        
    def display_subtasks(self):
        table = self.ui.subtasks_table
        query = f"SELECT subtask_id, subtask_name, status FROM subtasks WHERE task_id = {self.task_id}"
        result = self.db.fetch_data(query)
        headers = ["Subtask ID", "Subtask Name", "Status", "Check"]
        self.subtasks_model = QStandardItemModel(len(result), len(headers))
        self.subtasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.subtasks_model.setItem(row_num, col_num, item)
        table.setModel(self.subtasks_model)
        table.resizeColumnsToContents()
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSortingEnabled(True)
        self
        for row in range(self.subtasks_model.rowCount()):
            checkbox = QCheckBox()
            table.setIndexWidget(self.subtasks_model.index(row, self.subtasks_model.columnCount() - 1), checkbox)
        
    def add_subtask(self):
        subtask_name = self.ui.subtask_name.text()
        if subtask_name != "":
            self.db.add_subtask(self.task_id, subtask_name)
            self.ui.subtask_name.setText("")
            self.display_subtasks()