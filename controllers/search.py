from cProfile import label
from cgitb import text
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (
    QDialog,
    QMessageBox,
    QAbstractItemView,
    QMenu,
    QAction,
    QPushButton,
)
from controllers.edit_tasks import EditTaskDialog
from controllers.schedule import ScheduleDialog
from controllers.subtasks import SubtasksDialog
from data.database_manager import DatabaseManager
from ui.search_ui import Ui_SearchDialog

class SearchDialog(QDialog):
    def __init__(self, user_id, parent):
        super(SearchDialog, self).__init__(parent)
        
        self.ui = Ui_SearchDialog()
        self.ui.setupUi(self)
        
        self.parent = parent
        self.db_manager = DatabaseManager()
        self.user_id = user_id
        self.display_tasks()
        self.labels_list()
        self.ui.show_all_btn.clicked.connect(self.refresh_table)
        self.ui.labels.currentIndexChanged.connect(self.handle_label_change)
        self.ui.search_btn.clicked.connect(self.handle_search)
    
    def closeEvent(self, event) -> None:
        self.parent.refresh_table()
        self.parent.display_completed_tasks()
        self.parent.display_number_of_tasks()
        
        return super().closeEvent(event)
    
    
    def handle_search(self):
        search_text = self.ui.task_search.text()
        if search_text != "":
            self.filter_table(search_text)
            
    def display_tasks(self):
        """Shows a list of all uncompleted tasks present."""
        self.tasks_table = self.ui.tasks_list
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started' OR status = 'Started')"""
        result = self.db_manager.fetch_data(query)
        default_task = True
        if len(result) > 1:
            result.pop(0)
            default_task = False
        headers = [
            "Task ID",
            "Tasks Name",
            "Priority",
            "Due Date",
            "Label",
            "Status",
            "Description",
            "Created At",
            "Options",
        ]
        self.tasks_model = QStandardItemModel(len(result), len(headers))
        self.tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                item.setToolTip(f"Double click to add subtasks for {row_data[1]}.")
                self.tasks_model.setItem(row_num, col_num, item)
        self.tasks_table.setModel(self.tasks_model)
        self.tasks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tasks_table.setColumnHidden(0, True)
        if default_task is True:
            self.tasks_table.setRowHidden(0, True)
        else:
            self.tasks_table.setRowHidden(0, False)
        self.tasks_table.resizeColumnsToContents()
        self.tasks_table.setColumnWidth(self.tasks_model.columnCount() - 1, 100)
        self.tasks_table.setSortingEnabled(True)
        self.tasks_table.doubleClicked.connect(self.record_clicked)
        self.tasks_table.sortByColumn(
            self.tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        for row in range(self.tasks_model.rowCount()):
            button = QPushButton("Options")
            button.setToolTip("Click to manage the task.")
            button.setAutoDefault(True)
            menu = QMenu()
            schedule_action = QAction("Schedule", self)
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            started_action = QAction("Started", self)
            not_started_action = QAction("Not Started", self)
            status = self.tasks_model.index(row, 5).data()
            schedule_action.triggered.connect(
                lambda index, row=row: self.handle_schedule(row, self.tasks_model)
            )
            done_action.triggered.connect(
                lambda index, row=row: self.handle_done(row, self.tasks_model)
            )
            edit_action.triggered.connect(
                lambda index, row=row: self.handle_edit(row, self.tasks_model)
            )
            delete_action.triggered.connect(
                lambda index, row=row: self.handle_delete(row, self.tasks_model)
            )
            started_action.triggered.connect(
                lambda index, row=row: self.handle_started(row, self.tasks_model)
            )
            not_started_action.triggered.connect(
                lambda index, row=row: self.handle_not_started(row, self.tasks_model)
            )
            menu.addAction(schedule_action)
            if status == "Not Started":
                menu.addAction(started_action)
            else:
                menu.addAction(not_started_action)
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            self.tasks_table.setIndexWidget(
                self.tasks_model.index(row, self.tasks_model.columnCount() - 1), button
            )
        self.show()
        
    def display_tasks_by_label(self, label_name):
        """Shows a list of all uncompleted tasks present."""
        self.tasks_table = self.ui.tasks_list
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started' OR status = 'Started') AND label_name = '{label_name}'"""
        result = self.db_manager.fetch_data(query)
        headers = [
            "Task ID",
            "Tasks Name",
            "Priority",
            "Due Date",
            "Label",
            "Status",
            "Description",
            "Created At",
            "Options",
        ]
        self.tasks_model = QStandardItemModel(len(result), len(headers))
        self.tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                item.setToolTip(f"Double click to add subtasks for {row_data[1]}.")
                self.tasks_model.setItem(row_num, col_num, item)
        self.tasks_table.setModel(self.tasks_model)
        self.tasks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tasks_table.setColumnHidden(0, True)
        self.tasks_table.resizeColumnsToContents()
        self.tasks_table.setColumnWidth(self.tasks_model.columnCount() - 1, 100)
        self.tasks_table.setSortingEnabled(True)
        self.tasks_table.doubleClicked.connect(self.record_clicked)
        self.tasks_table.sortByColumn(
            self.tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        for row in range(self.tasks_model.rowCount()):
            button = QPushButton("Options")
            button.setToolTip("Click to manage the task.")
            button.setAutoDefault(True)
            menu = QMenu()
            schedule_action = QAction("Schedule", self)
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            started_action = QAction("Started", self)
            not_started_action = QAction("Not Started", self)
            status = self.tasks_model.index(row, 5).data()
            schedule_action.triggered.connect(
                lambda index, row=row: self.handle_schedule(row, self.tasks_model)
            )
            done_action.triggered.connect(
                lambda index, row=row: self.handle_done(row, self.tasks_model)
            )
            edit_action.triggered.connect(
                lambda index, row=row: self.handle_edit(row, self.tasks_model)
            )
            delete_action.triggered.connect(
                lambda index, row=row: self.handle_delete(row, self.tasks_model)
            )
            started_action.triggered.connect(
                lambda index, row=row: self.handle_started(row, self.tasks_model)
            )
            not_started_action.triggered.connect(
                lambda index, row=row: self.handle_not_started(row, self.tasks_model)
            )
            menu.addAction(schedule_action)
            if status == "Not Started":
                menu.addAction(started_action)
            else:
                menu.addAction(not_started_action)
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            self.tasks_table.setIndexWidget(
                self.tasks_model.index(row, self.tasks_model.columnCount() - 1), button
            )
        self.show()
        
    def handle_label_change(self, index):
        label_name = self.ui.labels.itemText(index)
        if label_name == "All":
            self.display_tasks()
        else:
            self.display_tasks_by_label(label_name)
        
    def labels_list(self) -> None:
        labels = self.db_manager.fetch_data(
            f"SELECT label_name FROM labels WHERE user_id = {self.user_id}"
        )
        if len(labels) != 0:
            self.ui.labels.addItem("All")
            for row in labels:
                self.ui.labels.addItem(row[0])
                
    def filter_table(self, text):
        # TODO: Change it to not be case sensitive
        for row in range(self.tasks_model.rowCount()):
            if any(text in str(self.tasks_model.data(self.tasks_model.index(row, col))) for col in range(self.tasks_model.columnCount())):
                self.tasks_table.setRowHidden(row, False)
            else:
                self.tasks_table.setRowHidden(row, True)
                
        
    def refresh_table(self):
        """Refresh the given tables."""
        self.tasks_table.doubleClicked.disconnect()
        self.display_tasks()
        
    def record_clicked(self, index):
        """Opens the subtasks dialog to add subtasks to a given task when that task is double clicked."""
        row = index.row()
        task_id = self.tasks_model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
        subtask.show()

    def handle_schedule(self, row, model):
        task_id = model.index(row, 0).data()
        schedule_dialog = ScheduleDialog(task_id, self)
        schedule_dialog.show()

    def handle_done(self, row, model):
        """Marks a given task as done."""
        task_id = model.index(row, 0).data()
        tasks_name = self.db_manager.fetch_data(
            f"SELECT task_name FROM tasks WHERE task_id = {task_id}"
        )
        tasks_name = tasks_name[0][0]
        confirmation = QMessageBox()
        confirmation.setText(f"Are you sure you want to mark {tasks_name} as done?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        confirmation.setWindowTitle("Confirmation")
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            query = f"UPDATE tasks SET status = 'Completed' WHERE task_id = {task_id}"
            self.db_manager.execute_query(query)
            self.refresh_table()

    def handle_edit(self, row, model):
        """Opens the edit dialog responsible for editing a given task."""
        task_id = model.index(row, 0).data()
        edit_task_window = EditTaskDialog(task_id, self)
        edit_task_window.show()

    def handle_delete(self, row, model):
        """Removes a given task from the database."""
        task_id = model.index(row, 0).data()
        tasks_name = self.db_manager.fetch_data(
            f"SELECT task_name FROM tasks WHERE task_id = {task_id}"
        )
        tasks_name = tasks_name[0][0]
        confirmation = QMessageBox()
        confirmation.setText(f"Are you sure you want to delete {tasks_name}?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            self.db_manager.remove_task(task_id)
            self.refresh_table()
            
    def handle_started(self, row, model):
        """Changes the status of a task to started."""
        task_id = model.index(row, 0).data()
        self.db_manager.execute_query(
            f"UPDATE tasks SET status = 'Started' WHERE task_id = {task_id}"
        )
        self.refresh_table()

    def handle_not_started(self, row, model):
        """Changes the status of a task to not started."""
        task_id = model.index(row, 0).data()
        self.db_manager.execute_query(
            f"UPDATE tasks SET status = 'Not Started' WHERE task_id = {task_id}"
        )
        self.refresh_table()
