from datetime import date, datetime
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QStandardItem, QStandardItemModel
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
        self.doubleClicked_connected = False
        self.display_tasks()
        self.labels_list()
        
        self.ui.show_all_btn.clicked.connect(self.handle_show_all)
        self.ui.labels.currentIndexChanged.connect(self.handle_label_change)
        self.ui.due_date.currentIndexChanged.connect(self.handle_due_date_change)
        self.ui.search_btn.clicked.connect(self.handle_search)
    
    def closeEvent(self, event) -> None:
        self.parent.display_tasks()
        self.parent.display_completed_tasks()
        self.parent.display_number_of_tasks()
        
        return super().closeEvent(event)
    
    def handle_search(self):
        search_text = self.ui.task_search.text().lower()
        if search_text != "":
            self.ui.labels.setCurrentIndex(0)
            self.ui.due_date.setCurrentIndex(0)
            self.filter_table(search_text)
            
    def handle_show_all(self):
        self.display_tasks()
        self.ui.labels.setCurrentIndex(0)
        self.ui.due_date.setCurrentIndex(0)
        self.ui.task_search.setText("")
        
    
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
        for row in range(self.tasks_model.rowCount()):
            self.tasks_table.setRowHidden(row, False)
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
        if self.doubleClicked_connected == True:
            self.tasks_table.doubleClicked.disconnect()
            self.doubleClicked_connected = False
        self.tasks_table.doubleClicked.connect(self.record_clicked)
        self.doubleClicked_connected = True
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
        
    def display_tasks_by(self, result):
        self.tasks_table = self.ui.tasks_list
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
        for row in range(self.tasks_model.rowCount()):
            self.tasks_table.setRowHidden(row, False)
        self.tasks_table.setModel(self.tasks_model)
        self.tasks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tasks_table.setColumnHidden(0, True)
        self.tasks_table.resizeColumnsToContents()
        self.tasks_table.setColumnWidth(self.tasks_model.columnCount() - 1, 100)
        self.tasks_table.setSortingEnabled(True)
        if self.doubleClicked_connected == True:
            self.tasks_table.doubleClicked.disconnect()
            self.doubleClicked_connected = False
        self.tasks_table.doubleClicked.connect(self.record_clicked)
        self.doubleClicked_connected = True
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
    
    def handle_due_date_change(self, index):
        due_date = self.ui.due_date.itemText(index)
        if due_date == "All":
            self.display_tasks()
        elif due_date == "Passed":
            self.passed_tasks()
        else:
            self.not_passed_tasks()
        self.ui.task_search.setText("")
        
    def tasks_by_label(self, label_name):
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started' OR status = 'Started') AND label_name = '{label_name}'"""
        result = self.db_manager.fetch_data(query)
        self.display_tasks_by(result)
        
    def passed_tasks(self):
        today = date.today().strftime("%Y-%m-%d")
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started' OR status = 'Started')"""
        result = self.db_manager.fetch_data(query)
        result.pop(0)
        new_result = []
        today = date.today().strftime("%Y-%m-%d")
        for item in result:
            if datetime.strptime(item[3], "%Y-%m-%d") < datetime.strptime(
                today, "%Y-%m-%d"
            ):
                new_result.append(item)
        self.display_tasks_by(new_result)
    
    def not_passed_tasks(self):
        today = date.today().strftime("%Y-%m-%d")
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started' OR status = 'Started')"""
        result = self.db_manager.fetch_data(query)
        result.pop(0)
        new_result = []
        today = date.today().strftime("%Y-%m-%d")
        for item in result:
            if datetime.strptime(item[3], "%Y-%m-%d") >= datetime.strptime(
                today, "%Y-%m-%d"
            ):
                new_result.append(item)
        self.display_tasks_by(new_result)
        
    def handle_label_change(self, index):
        label_name = self.ui.labels.itemText(index)
        if label_name == "All":
            self.display_tasks()
        else:
            self.tasks_by_label(label_name)
        self.ui.task_search.setText("")
        
    def labels_list(self) -> None:
        self.ui.labels.clear()
        labels = self.db_manager.fetch_data(
            f"SELECT label_name FROM labels WHERE user_id = {self.user_id}"
        )
        if len(labels) != 0:
            self.ui.labels.addItem("All")
            for row in labels:
                self.ui.labels.addItem(row[0])
                
    def filter_table(self, text):
        self.tasks_table.setSortingEnabled(False)
        
        for row in range(self.tasks_model.rowCount()):
            self.tasks_table.setRowHidden(row, True)
            
        for row in range(self.tasks_model.rowCount()):
            for col in range(self.tasks_model.columnCount() - 1):
                cell_text = self.tasks_model.item(row, col).text().lower()
                if text in cell_text:
                    self.tasks_table.setRowHidden(row, False)
                    break
                
        self.tasks_table.setSortingEnabled(True)
        
    # def display_tasks(self):
    #     """Refresh the given tables."""
    #     self.display_tasks()
        
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
            self.display_tasks()

    def handle_edit(self, row, model):
        """Opens the edit dialog responsible for editing a given task."""
        task_id = model.index(row, 0).data()
        edit_task_window = EditTaskDialog(task_id, self)
        edit_task_window.show()
        
    def delete_label(self, label_name):
        labels = self.db_manager.fetch_data(f"SELECT COUNT(*) FROM tasks WHERE user_id = {self.user_id} AND label_name = '{label_name}'")
        print(labels)
        label_exists = True
        if labels[0][0] == 0:
            label_exists = False
        if label_exists is False:
            self.db_manager.delete_label(self.user_id, label_name)

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
            label_name = self.db_manager.fetch_data(f"SELECT label_name FROM tasks WHERE task_id = {task_id}")
            label_name = label_name[0][0]
            self.db_manager.remove_task(task_id)
            self.delete_label(label_name)
            self.labels_list()
            self.display_tasks()
            
    def handle_started(self, row, model):
        """Changes the status of a task to started."""
        task_id = model.index(row, 0).data()
        self.db_manager.execute_query(
            f"UPDATE tasks SET status = 'Started' WHERE task_id = {task_id}"
        )
        self.display_tasks()

    def handle_not_started(self, row, model):
        """Changes the status of a task to not started."""
        task_id = model.index(row, 0).data()
        self.db_manager.execute_query(
            f"UPDATE tasks SET status = 'Not Started' WHERE task_id = {task_id}"
        )
        self.display_tasks()
