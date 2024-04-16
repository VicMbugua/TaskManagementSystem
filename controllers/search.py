from datetime import date, datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (
    QDialog,
    QMessageBox,
    QAbstractItemView,
    QMenu,
    QAction,
    QPushButton,
)
from controllers.add_tasks import EditTaskDialog
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
        self.double_clicked_connected = False
        self.display_tasks()
        self.labels_list()

        self.ui.show_all_btn.clicked.connect(self.handle_show_all)
        self.ui.labels.currentIndexChanged.connect(self.handle_label_change)
        self.ui.due_date.currentIndexChanged.connect(self.handle_due_date_change)
        self.ui.status.currentIndexChanged.connect(self.handle_status_change)
        self.ui.search_btn_2.clicked.connect(self.handle_search)

    def closeEvent(self, event) -> None:
        self.parent.refresh_table()
        self.parent.display_completed_tasks()
        self.parent.display_number_of_tasks()

        return super().closeEvent(event)

    def refresh_table(self):
        label = self.ui.labels.currentText()
        due_date = self.ui.due_date.currentText()
        status = self.ui.status.currentText()
        self.labels_list()
        self.filtered_tasks(label, due_date, status)

    def handle_search(self):
        original_text = self.ui.task_search.text()
        search_text = original_text.lower()
        if search_text != "":
            self.ui.labels.setCurrentIndex(0)
            self.ui.due_date.setCurrentIndex(0)
            self.ui.status.setCurrentIndex(0)
            self.filter_table(search_text)
            text = self.ui.task_search.text()
            if text == "":
                self.ui.task_search.setText(original_text)

    def handle_show_all(self):
        self.display_tasks()
        self.ui.labels.setCurrentIndex(0)
        self.ui.due_date.setCurrentIndex(0)
        self.ui.status.setCurrentIndex(0)
        self.ui.task_search.setText("")

    def display_tasks(self):
        """Shows a list of all uncompleted tasks present."""
        self.tasks_table = self.ui.tasks_list
        self.tasks_table.verticalHeader().setDefaultSectionSize(40)
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
        if self.double_clicked_connected:
            self.tasks_table.doubleClicked.disconnect()
            self.double_clicked_connected = False
        self.tasks_table.doubleClicked.connect(self.record_clicked)
        self.double_clicked_connected = True
        self.tasks_table.sortByColumn(
            self.tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        for row in range(self.tasks_model.rowCount()):
            button = QPushButton("Options")
            button.setProperty("groupName", "options")
            button.setFocusPolicy(Qt.TabFocus)
            button.setToolTip("Click to manage the task.")
            button.setAutoDefault(True)
            menu = QMenu()
            schedule_action = QAction("Schedule", self)
            subtasks_action = QAction("Add Subtasks", self)
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            started_action = QAction("Started", self)
            not_started_action = QAction("Not Started", self)
            status = self.tasks_model.index(row, 5).data()
            schedule_action.triggered.connect(
                lambda index, row=row: self.handle_schedule(row, self.tasks_model)
            )
            subtasks_action.triggered.connect(
                lambda index, row=row: self.handle_subtasks(
                    row, self.tasks_model)
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
            menu.addAction(subtasks_action)
            if status == "Not Started":
                menu.addAction(started_action)
            else:
                menu.addAction(not_started_action)
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            menu.setToolTipsVisible(True)
            schedule_action.setToolTip("Schedule the given task.")
            subtasks_action.setToolTip("Add subtasks for the given task.")
            done_action.setToolTip("Mark the given task as done/completed.")
            edit_action.setToolTip("Edit the given task.")
            delete_action.setToolTip("Delete the given task.")
            started_action.setToolTip("Mark the given task as started.")
            not_started_action.setToolTip("Mark the given task as not started.")
            button.setMenu(menu)
            self.tasks_table.setIndexWidget(
                self.tasks_model.index(row, self.tasks_model.columnCount() - 1), button
            )
        self.show()

    def display_tasks_by(self, result):
        self.tasks_table = self.ui.tasks_list
        self.tasks_table.verticalHeader().setDefaultSectionSize(40)
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
        self.grouped_tasks_model = QStandardItemModel(len(result), len(headers))
        self.grouped_tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                item.setToolTip(f"Double click to add subtasks for {row_data[1]}.")
                self.grouped_tasks_model.setItem(row_num, col_num, item)
        for row in range(self.grouped_tasks_model.rowCount()):
            self.tasks_table.setRowHidden(row, False)
        self.tasks_table.setModel(self.grouped_tasks_model)
        self.tasks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tasks_table.setColumnHidden(0, True)
        self.tasks_table.resizeColumnsToContents()
        self.tasks_table.setColumnWidth(self.grouped_tasks_model.columnCount() - 1, 100)
        self.tasks_table.setSortingEnabled(True)
        if self.double_clicked_connected:
            self.tasks_table.doubleClicked.disconnect()
            self.double_clicked_connected = False
        self.tasks_table.doubleClicked.connect(self.record_clicked_2)
        self.double_clicked_connected = True
        self.tasks_table.sortByColumn(
            self.grouped_tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        for row in range(self.grouped_tasks_model.rowCount()):
            button = QPushButton("Options")
            button.setProperty("groupName", "options")
            button.setFocusPolicy(Qt.TabFocus)
            button.setToolTip("Click to manage the task.")
            button.setAutoDefault(True)
            menu = QMenu()
            schedule_action = QAction("Schedule", self)
            subtasks_action = QAction("Add Subtasks", self)
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            started_action = QAction("Started", self)
            not_started_action = QAction("Not Started", self)
            status = self.grouped_tasks_model.index(row, 5).data()
            schedule_action.triggered.connect(
                lambda index, row=row: self.handle_schedule(row, self.grouped_tasks_model)
            )
            subtasks_action.triggered.connect(
                lambda index, row=row: self.handle_subtasks(
                    row, self.grouped_tasks_model)
            )
            done_action.triggered.connect(
                lambda index, row=row: self.handle_done(row, self.grouped_tasks_model)
            )
            edit_action.triggered.connect(
                lambda index, row=row: self.handle_edit(row, self.grouped_tasks_model)
            )
            delete_action.triggered.connect(
                lambda index, row=row: self.handle_delete(row, self.grouped_tasks_model)
            )
            started_action.triggered.connect(
                lambda index, row=row: self.handle_started(row, self.grouped_tasks_model)
            )
            not_started_action.triggered.connect(
                lambda index, row=row: self.handle_not_started(row, self.grouped_tasks_model)
            )
            menu.addAction(schedule_action)
            menu.addAction(subtasks_action)
            if status == "Not Started":
                menu.addAction(started_action)
            else:
                menu.addAction(not_started_action)
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            menu.setToolTipsVisible(True)
            schedule_action.setToolTip("Schedule the given task.")
            subtasks_action.setToolTip("Add subtasks for the given task.")
            done_action.setToolTip("Mark the given task as done/completed.")
            edit_action.setToolTip("Edit the given task.")
            delete_action.setToolTip("Delete the given task.")
            started_action.setToolTip("Mark the given task as started.")
            not_started_action.setToolTip("Mark the given task as not started.")
            button.setMenu(menu)
            self.tasks_table.setIndexWidget(
                self.grouped_tasks_model.index(row, self.grouped_tasks_model.columnCount() - 1), button
            )
        self.show()
        
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

    def tasks_by_label(self, label_name):
        query = """SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = ? AND (status = 'Not Started' OR status = 'Started') AND label_name = ?"""
        result = self.db_manager.fetch_data(query, (self.user_id, label_name))
        return result

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
        return new_result

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
        return new_result

    def not_started_tasks(self):
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Not Started')"""
        result = self.db_manager.fetch_data(query)
        result.pop(0)
        return result

    def started_tasks(self):
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND (status = 'Started')"""
        result = self.db_manager.fetch_data(query)
        return result

    def handle_status_change(self, index):
        status = self.ui.status.itemText(index)
        label = self.ui.labels.currentText()
        due_date = self.ui.due_date.currentText()
        self.filtered_tasks(label, due_date, status)
        self.ui.task_search.setText("")

    def handle_due_date_change(self, index):
        due_date = self.ui.due_date.itemText(index)
        label = self.ui.labels.currentText()
        status = self.ui.status.currentText()
        self.filtered_tasks(label, due_date, status)
        self.ui.task_search.setText("")

    def handle_label_change(self, index):
        label = self.ui.labels.itemText(index)
        due_date = self.ui.due_date.currentText()
        status = self.ui.status.currentText()
        self.filtered_tasks(label, due_date, status)
        self.ui.task_search.setText("")

    def filtered_tasks(self, label, due_date, status):
        if label == "All" and due_date == "All" and status == "All":
            self.display_tasks()
        elif label == "All" and due_date == "All":
            if status == "Started":
                result = self.started_tasks()
            else:
                result = self.not_started_tasks()
            self.display_tasks_by(result)
        elif label == "All" and status == "All":
            if due_date == "Passed":
                result = self.passed_tasks()
            else:
                result = self.not_passed_tasks()
            self.display_tasks_by(result)
        elif due_date == "All" and status == "All":
            result = self.tasks_by_label(label)
            self.display_tasks_by(result)
        elif label == "All":
            if status == "Started":
                result1 = self.started_tasks()
            else:
                result1 = self.not_started_tasks()
            if due_date == "Passed":
                result2 = self.passed_tasks()
            else:
                result2 = self.not_passed_tasks()
            common_items = set(result1) & set(result2)
            result = list(common_items)
            self.display_tasks_by(result)
        elif due_date == "All":
            result1 = self.tasks_by_label(label)
            if status == "Started":
                result2 = self.started_tasks()
            else:
                result2 = self.not_started_tasks()
            common_items = set(result1) & set(result2)
            result = list(common_items)
            self.display_tasks_by(result)
        elif status == "All":
            result1 = self.tasks_by_label(label)
            if due_date == "Passed":
                result2 = self.passed_tasks()
            else:
                result2 = self.not_passed_tasks()
            common_items = set(result1) & set(result2)
            result = list(common_items)
            self.display_tasks_by(result)
        else:
            result1 = self.tasks_by_label(label)
            if due_date == "Passed":
                result2 = self.passed_tasks()
            else:
                result2 = self.not_passed_tasks()
            if status == "Started":
                result3 = self.started_tasks()
            else:
                result3 = self.not_started_tasks()
            common_items = set(result1) & set(result2) & set(result3)
            result = list(common_items)
            self.display_tasks_by(result)

    def labels_list(self) -> None:
        self.ui.labels.clear()
        labels = self.db_manager.fetch_data(
            f"SELECT label_name FROM labels WHERE user_id = {self.user_id}"
        )
        self.ui.labels.addItem("All")
        if len(labels) != 0:
            for row in labels:
                self.ui.labels.addItem(row[0])

    def handle_subtasks(self, row, model):
        task_id = model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
        subtask.setFixedSize(550, 400)
        subtask.show()

    def record_clicked(self, index):
        """Opens the subtasks dialog to add subtasks to a given task when that task is double-clicked."""
        row = index.row()
        task_id = self.tasks_model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
        subtask.setFixedSize(550, 400)
        subtask.show()

    def record_clicked_2(self, index):
        """Opens the subtasks dialog to add subtasks to a given task when that task is double-clicked."""
        row = index.row()
        task_id = self.grouped_tasks_model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
        subtask.setFixedSize(550, 400)
        subtask.show()

    def handle_schedule(self, row, model):
        task_id = model.index(row, 0).data()
        schedule_dialog = ScheduleDialog(self.user_id, task_id, self)
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
            self.db_manager.delete_schedules(task_id)
            self.refresh_table()

    def handle_edit(self, row, model):
        """Opens the edit dialog responsible for editing a given task."""
        task_id = model.index(row, 0).data()
        edit_task_window = EditTaskDialog(task_id, self)
        edit_task_window.setFixedSize(450, 450)
        edit_task_window.show()

    def delete_label(self, label_name):
        labels = self.db_manager.fetch_data(
            "SELECT COUNT(*) FROM tasks WHERE user_id = ? AND label_name = ? AND status != 'Completed'", (self.user_id, label_name))
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
