from datetime import date, datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QAbstractItemView,
    QMenu,
    QAction,
    QPushButton,
)

from controllers.add_project import AddProjectDialog, RenameProjectDialog
from controllers.arrange import Arrange
from controllers.edit_tasks import AddTaskDialog, EditTaskDialog
from controllers.manage_account import ManageAccountDialog
from controllers.schedule import ScheduleDialog
from controllers.search import SearchDialog
from controllers.subtasks import SubtasksDialog
from data.database_manager import DatabaseManager
from ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, user_id, widget, parent=None) -> None:
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = widget

        self.ui.icons_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        self.db_manager = DatabaseManager()
        self.user_id = user_id

        self.ui.search_btn.clicked.connect(self.open_search)
        user_button = self.ui.user_btn
        user_menu = QMenu()
        manage_account = user_menu.addAction("Manage Account")
        log_out = user_menu.addAction("Log Out")

        manage_account.triggered.connect(self.open_manage_account)
        log_out.triggered.connect(self.logout)
        user_button.setMenu(user_menu)
        user_button.setStyleSheet("::menu-indicator {image:none;}")

        self.project_name = "Default"
        self.project_list()

        project_menu = QMenu()
        rename_project = project_menu.addAction("Rename Project")
        delete_project = project_menu.addAction("Delete Project")
        rename_project.triggered.connect(self.rename_project)
        delete_project.triggered.connect(self.delete_project)
        project_button = self.ui.manage_project_btn
        project_button.setMenu(project_menu)

        self.ui.project.currentIndexChanged.connect(self.handle_project_change)
        self.ui.add_project_btn.clicked.connect(self.open_add_project)
        self.ui.manage_project_btn.setToolTip(
            f"Rename or delete {self.project_name} project"
        )
        self.ui.add_task_btn.clicked.connect(self.open_task_dialog)
        self.ui.add_task_btn.setToolTip(f"Add new task to {self.project_name} project")
        self.ui.clear_all_btn.clicked.connect(self.handle_clear_all)
        self.display_day_tasks(date=date.today())
        self.installEventFilter(self)
        self.ui.calendar.selectionChanged.connect(self.date_changed)
        today_date = datetime.today().strftime("%d %B %Y")
        self.ui.schedules_for.setText(f"Tasks scheduled for {today_date}")

    def showEvent(self, event):
        super().showEvent(event)
        self.display_tasks()
        self.date_changed()
        self.display_completed_tasks()
        self.display_filtered_tasks()
        self.display_number_of_tasks()

    def on_menu_btn_pressed(self) -> None:
        if self.ui.full_name_widget.isVisible():
            self.ui.menu_btn.setToolTip("Expand menu")
            self.ui.full_name_widget.hide()
            self.ui.menu_label.hide()
            self.ui.icons_only_widget.show()
        else:
            self.ui.menu_btn.setToolTip("Collapse menu")
            self.ui.full_name_widget.show()
            self.ui.menu_label.show()
            self.ui.icons_only_widget.hide()

    def open_search(self):
        search_dialog = SearchDialog(self.user_id, self)
        search_dialog.show()

    def logout(self) -> None:
        """It logs you out of the application."""
        self.widget.show()
        self.close()

    def project_list(self) -> None:
        self.ui.project.clear()
        projects = self.db_manager.fetch_data(
            f"SELECT project_name FROM projects WHERE user_id = {self.user_id}"
        )
        for row in projects:
            self.ui.project.addItem(row[0])

    def handle_project_change(self, index) -> None:
        """Changes the name of a project."""
        self.project_name = self.ui.project.itemText(index)
        self.refresh_table()
        self.ui.add_task_btn.setToolTip(f"Add new task to {self.project_name} project")

    def open_add_project(self) -> None:
        add_project = AddProjectDialog(self.user_id, self)
        add_project.setFixedSize(300, 200)
        add_project.show()

    def rename_project(self):
        if self.project_name == "Default":
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText("You cannot rename the Default project.")
            information.setWindowTitle("Information")
            information.exec()
        else:
            rename_project = RenameProjectDialog(self.user_id, self.project_name, self)
            rename_project.setFixedSize(300, 200)
            rename_project.show()

    def delete_project(self) -> None:
        if self.project_name == "Default":
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText("You cannot delete the Default project.")
            information.setWindowTitle("Information")
            information.exec()
        else:
            confirmation = QMessageBox()
            confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            confirmation.setWindowTitle("Confirmation")
            confirmation.setText(
                f'Are you sure you want to delete the project "{self.project_name}"?'
            )
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.db_manager.execute_query(
                    f"DELETE FROM projects WHERE project_name = '{self.project_name}' AND user_id = {self.user_id}"
                )
                index: int = self.ui.project.findText(self.project_name)
                self.ui.project.removeItem(index)
                self.ui.project.setCurrentIndex(0)
                self.display_number_of_tasks()
                self.display_filtered_tasks()

    def open_task_dialog(self) -> None:
        """Opens the dialog responsible for adding new tasks."""
        add_task = AddTaskDialog(self.user_id, self.project_name, self)
        add_task.show()

    def open_manage_account(self) -> None:
        """Opens the dialog responsible for managing the user's account."""
        manage_account = ManageAccountDialog(self.user_id, self.widget, self)
        manage_account.show()

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

    def on_calendar_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_calendar_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    # HOME PAGE BEGIN

    def display_number_of_tasks(self):
        """Displays number of tasks present."""
        no_of_tasks = self.db_manager.number_of_tasks(self.user_id) - 1
        if no_of_tasks == 0:
            self.ui.no_of_tasks.setText("You have no tasks.")
        else:
            self.ui.no_of_tasks.setText(f"Number of tasks: {no_of_tasks}")
        overdue_tasks = self.passed_tasks()
        if overdue_tasks == 0:
            self.ui.no_of_overdue_tasks.setText("You have no overdue tasks")
        else:
            self.ui.no_of_overdue_tasks.setText(f"Number of overdue tasks: {overdue_tasks}")
        query = f"SELECT COUNT(*) FROM tasks WHERE user_id = {self.user_id} AND status = 'Completed'"
        completed_tasks = self.db_manager.fetch_data(query)
        completed_tasks = completed_tasks[0][0]
        if completed_tasks == 0:
            self.ui.number_of_completed_tasks.setText("You have no completed task.")
        else:
            self.ui.number_of_completed_tasks.setText(f"Number of completed tasks: {completed_tasks}")
            

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
        return len(new_result)

    def display_filtered_tasks(self):
        """Shows a list of tasks based on their importance."""
        self.filtered_table = self.ui.filtered_tasks
        schedule = Arrange(self.user_id)
        result = schedule.arrange_tasks()
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
        self.filtered_tasks_model = QStandardItemModel(len(result), len(headers))
        self.filtered_tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                item.setToolTip(f"Double click to add subtasks for {row_data[1]}.")
                self.filtered_tasks_model.setItem(row_num, col_num, item)
        self.filtered_table.setModel(self.filtered_tasks_model)
        self.filtered_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.filtered_table.setColumnHidden(0, True)
        self.filtered_table.resizeColumnsToContents()
        self.filtered_table.setColumnWidth(
            self.filtered_tasks_model.columnCount() - 1, 100
        )
        self.filtered_table.doubleClicked.connect(self.record_clicked_2)
        self.setFocusPolicy(Qt.NoFocus)
        for row in range(self.filtered_tasks_model.rowCount()):
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
            status = self.filtered_tasks_model.index(row, 5).data()
            schedule_action.triggered.connect(
                lambda index, row=row: self.handle_schedule(row, self.filtered_tasks_model)
            )
            done_action.triggered.connect(
                lambda index, row=row: self.handle_done(row, self.filtered_tasks_model)
            )
            edit_action.triggered.connect(
                lambda index, row=row: self.handle_edit(row, self.filtered_tasks_model)
            )
            delete_action.triggered.connect(
                lambda index, row=row: self.handle_delete(
                    row, self.filtered_tasks_model
                )
            )
            started_action.triggered.connect(
                lambda index, row=row: self.handle_started(
                    row, self.filtered_tasks_model
                )
            )
            not_started_action.triggered.connect(
                lambda index, row=row: self.handle_not_started(
                    row, self.filtered_tasks_model
                )
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
            self.filtered_table.setIndexWidget(
                self.filtered_tasks_model.index(
                    row, self.filtered_tasks_model.columnCount() - 1
                ),
                button,
            )
        self.show()

    def record_clicked_2(self, index):
        """Opens the subtasks dialog to add subtasks to a given task when that task is double-clicked."""
        row = index.row()
        task_id = self.filtered_tasks_model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
        subtask.show()

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

    # HOME PAGE END

    # TASKS PAGE BEGIN

    def display_tasks(self):
        """Shows a list of all uncompleted tasks present."""
        self.tasks_table = self.ui.tasks_list
        project_id = self.db_manager.fetch_data(
            f"SELECT project_id FROM projects WHERE user_id = ? AND project_name = ?", (self.user_id, self.project_name)
        )
        project_id = project_id[0][0]
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE user_id = {self.user_id} AND project_id = {project_id} AND (status = 'Not Started' OR status = 'Started')"""
        result = self.db_manager.fetch_data(query)
        default_task = True
        if len(result) > 1 and self.project_name == "Default":
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
        if default_task is True and self.project_name == "Default":
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
            status = self.tasks_model.index(row, 5).data()
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

    def refresh_table(self):
        """Refresh the given tables."""
        self.filtered_table.doubleClicked.disconnect()
        self.tasks_table.doubleClicked.disconnect()
        self.display_filtered_tasks()
        self.display_tasks()
        self.date_changed()

    def record_clicked(self, index):
        """Opens the subtasks dialog to add subtasks to a given task when that task is double clicked."""
        row = index.row()
        task_id = self.tasks_model.index(row, 0).data()
        subtask = SubtasksDialog(task_id, self)
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
        confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
        confirmation.setWindowTitle("Confirmation")
        confirmation.setText(f"Are you sure you want to mark {tasks_name} as done?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            query = f"UPDATE tasks SET status = 'Completed' WHERE task_id = {task_id}"
            self.db_manager.execute_query(query)
            self.refresh_table()
            self.display_completed_tasks()
            self.display_number_of_tasks()

    def handle_edit(self, row, model):
        """Opens the edit dialog responsible for editing a given task."""
        task_id = model.index(row, 0).data()
        edit_task_window = EditTaskDialog(task_id, self)
        edit_task_window.show()

    def delete_label(self, label_name):
        labels = self.db_manager.fetch_data(
            f"SELECT COUNT(*) FROM tasks WHERE user_id = {self.user_id} AND label_name = '{label_name}'")
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
        confirmation.setWindowTitle("Delete task")
        confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
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
            self.refresh_table()
            self.display_completed_tasks()
            self.display_number_of_tasks()

    # TASKS PAGE END

    # COMPLETED TASKS PAGE BEGIN

    def display_completed_tasks(self):
        """Shows a list of all completed tasks present."""
        table = self.ui.completed_tasks
        query = f"""SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at 
        FROM tasks WHERE status = 'Completed' AND user_id = {self.user_id}"""
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
        table.setColumnWidth(self.completed_tasks_model.columnCount() - 1, 100)
        table.setSortingEnabled(True)
        table.sortByColumn(
            self.completed_tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        for row in range(self.completed_tasks_model.rowCount()):
            button = QPushButton("Options")
            button.setToolTip("Click to manage the task.")
            menu = QMenu()
            done_action = QAction("Not Done", self)
            delete_action = QAction("Delete", self)
            done_action.triggered.connect(
                lambda index, row=row: self.handle_not_done(row)
            )
            delete_action.triggered.connect(
                lambda index, row=row: self.handle_delete(
                    row, self.completed_tasks_model
                )
            )
            menu.addAction(done_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            table.setIndexWidget(
                self.completed_tasks_model.index(
                    row, self.completed_tasks_model.columnCount() - 1
                ),
                button,
            )
        self.show()

    def handle_not_done(self, row):
        """Marks a given task as not done."""
        task_id = self.completed_tasks_model.index(row, 0).data()
        tasks_name = self.db_manager.fetch_data(
            f"SELECT task_name FROM tasks WHERE task_id = {task_id}"
        )
        tasks_name = tasks_name[0][0]
        confirmation = QMessageBox()
        confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
        confirmation.setText(f"Are you sure you want to mark {tasks_name} as not done")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        confirmation.setWindowTitle("Confirmation")
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            query = f"UPDATE tasks SET status = 'Started' WHERE task_id = {task_id}"
            self.db_manager.execute_query(query)
            self.refresh_table()
            self.display_completed_tasks()
            self.display_number_of_tasks()
            
    def handle_clear_all(self):
        query = f"SELECT COUNT(*) FROM tasks WHERE user_id = {self.user_id} AND status = 'Completed'"
        completed_tasks = self.db_manager.fetch_data(query)
        completed_tasks = completed_tasks[0][0]
        if completed_tasks != 0:
            confirmation = QMessageBox()
            confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            confirmation.setText(f"Are you sure you want to delete all completed tasks?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            confirmation.setWindowTitle("Confirmation")
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.db_manager.delete_completed_tasks(self.user_id)
                self.display_completed_tasks()
                self.display_number_of_tasks()
        else:
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setText("You have no completed tasks.")
            information.setIcon(QMessageBox.Information)
            information.setWindowTitle("Information")
            information.exec()

    # COMPLETED TASKS PAGE END

    # CALENDAR PAGE BEGIN

    def date_changed(self):
        """Refreshes the calendar table when a different date is selected."""
        date = self.ui.calendar.selectedDate().toString("yyyy-MM-dd")
        self.display_day_tasks(date)
        full_date = self.ui.calendar.selectedDate().toString("dd MMMM yyyy")
        self.ui.schedules_for.setText(f"Tasks scheduled for {full_date}")

    def display_day_tasks(self, date):
        """Shows a list of tasks scheduled for that day."""
        self.calendar_table = self.ui.calendar_table
        query = f"""SELECT task_id, start_time, end_time FROM schedules WHERE date = '{date}' and user_id={self.user_id}"""
        result = self.db_manager.fetch_data(query)
        headers = ["Task Name", "Start Time", "End Time"]
        self.calendar_tasks_model = QStandardItemModel(len(result), len(headers))
        self.calendar_tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                if col_num == 0:
                    task_name = self.db_manager.fetch_data(
                        f"SELECT task_name FROM tasks WHERE task_id = {col_data}"
                    )
                    item = QStandardItem(task_name[0][0])
                else:
                    item = QStandardItem(str(col_data))
                self.calendar_tasks_model.setItem(row_num, col_num, item)
        self.calendar_table.setModel(self.calendar_tasks_model)
        self.calendar_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.calendar_table.resizeColumnsToContents()
        self.calendar_table.setColumnWidth(
            self.calendar_tasks_model.columnCount() - 1, 100
        )
        self.calendar_table.setSortingEnabled(True)
        self.calendar_table.sortByColumn(
            self.calendar_tasks_model.columnCount() - 2, Qt.AscendingOrder
        )
        self.show()

# CALENDAR PAGE END
