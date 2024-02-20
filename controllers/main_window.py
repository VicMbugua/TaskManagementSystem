from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QAbstractItemView, QMenu, QAction, QPushButton
from controllers.edit_tasks import AddTaskWindow, EditTaskWindow
from controllers.manage_account import ManageAccount
from controllers.subtasks import SubtasksWindow
from controllers.schedule import Schedule
from data.database_manager import DatabaseManager
from ui.add_task_ui import Ui_AddTask
from ui.edit_task_ui import Ui_EditTask
from ui.interface_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, user_id, widget, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = widget

        self.ui.icons_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        self.edit_window = QDialog()
        self.edit_task_ui = Ui_EditTask()
        self.edit_task_ui.setupUi(self.edit_window)
        self.add_window = QDialog()
        self.task_ui = Ui_AddTask()
        self.task_ui.setupUi(self.add_window)

        self.db_manager = DatabaseManager("data/tasks.db")
        self.user_id = user_id

        user_button = self.ui.user_btn
        user_menu = QMenu()
        manage_account = user_menu.addAction("Manage Account")
        log_out = user_menu.addAction("Log Out")

        manage_account.triggered.connect(self.open_manage_account)
        log_out.triggered.connect(self.logout)
        user_button.setMenu(user_menu)
        user_button.setStyleSheet("::menu-indicator {image:none;}")

        self.ui.add_task_btn.clicked.connect(self.open_task_window)
        self.display_number_of_tasks()
        self.display_filtered_tasks()
        self.display_tasks()
        self.display_completed_tasks()

    def on_menu_btn_pressed(self):
        if self.ui.full_name_widget.isVisible():
            self.ui.full_name_widget.hide()
            self.ui.menu_label.hide()
            self.ui.icons_only_widget.show()
        else:
            self.ui.full_name_widget.show()
            self.ui.menu_label.show()
            self.ui.icons_only_widget.hide()

    def logout(self):
        self.widget.show()
        self.close()

    def open_task_window(self):
        add_task = AddTaskWindow(self.user_id, self)
        add_task.show()

    def open_manage_account(self):
        manage_account = ManageAccount(self.user_id, self.widget, self)
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
        no_of_tasks = self.db_manager.number_of_tasks(self.user_id) - 1
        if no_of_tasks == 0:
            self.ui.no_of_tasks.setText(f"You have no tasks.")
        else:
            self.ui.no_of_tasks.setText(f"Number of tasks {no_of_tasks}")
            
    def display_filtered_tasks(self):
        table = self.ui.filtered_tasks
        schedule = Schedule(self.user_id)
        result = schedule.arrange_tasks()
        print(result)
        headers = ["Task ID", "Tasks Name", "Priority", "Due Date", "Label", "Status", "Description", "Created At", "Edit"]
        self.filtered_tasks_model = QStandardItemModel(len(result), len(headers))
        self.filtered_tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.filtered_tasks_model.setItem(row_num, col_num, item)
        table.setModel(self.filtered_tasks_model)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()
        table.setColumnWidth(self.filtered_tasks_model.columnCount() - 1, 100)
        table.setSortingEnabled(True)
        table.clicked.connect(self.record_clicked_2)
        self.subtask_dialog_open = False
        table.sortByColumn(self.filtered_tasks_model.columnCount() - 2, Qt.AscendingOrder)
        for row in range(self.filtered_tasks_model.rowCount()):
            button = QPushButton("Menu")
            menu = QMenu()
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            done_action.triggered.connect(lambda index, row=row: self.handle_done(row, self.filtered_tasks_model))
            edit_action.triggered.connect(lambda index, row=row: self.handle_edit(row, self.filtered_tasks_model))
            delete_action.triggered.connect(lambda index, row=row: self.handle_delete(row, self.filtered_tasks_model))
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            table.setIndexWidget(self.filtered_tasks_model.index(row, self.filtered_tasks_model.columnCount() - 1), button)
        self.show()
        
    def record_clicked_2(self, index):
        row = index.row()
        task_id = self.filtered_tasks_model.index(row, 0).data()
        self.subtask = SubtasksWindow(task_id, self)
        self.subtask.show()

    # HOME PAGE END

    # TASKS PAGE BEGIN

    def display_tasks(self):
        table = self.ui.tasks_list
        query = f"SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks WHERE user_id = '{self.user_id}' AND (status = 'Not Started' OR status = 'Started')"
        result = self.db_manager.fetch_data(query)
        default_task = True
        if len(result) > 1:
            result.pop(0)
            default_task = False
        headers = ["Task ID", "Tasks Name", "Priority", "Due Date", "Label", "Status", "Description", "Created At", "Edit"]
        self.tasks_model = QStandardItemModel(len(result), len(headers))
        self.tasks_model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                self.tasks_model.setItem(row_num, col_num, item)
        table.setModel(self.tasks_model)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnHidden(0, True)
        if default_task is True:
            table.setRowHidden(0, True)
        else:
            table.setRowHidden(0, False)
        table.resizeColumnsToContents()
        table.setColumnWidth(self.tasks_model.columnCount() - 1, 100)
        table.setSortingEnabled(True)
        table.clicked.connect(self.record_clicked)
        table.sortByColumn(self.tasks_model.columnCount() - 2, Qt.AscendingOrder)
        for row in range(self.tasks_model.rowCount()):
            button = QPushButton("Menu")
            menu = QMenu()
            done_action = QAction("Done", self)
            edit_action = QAction("Edit", self)
            delete_action = QAction("Delete", self)
            done_action.triggered.connect(lambda index, row=row: self.handle_done(row, self.tasks_model))
            edit_action.triggered.connect(lambda index, row=row: self.handle_edit(row, self.tasks_model))
            delete_action.triggered.connect(lambda index, row=row: self.handle_delete(row, self.tasks_model))
            menu.addAction(done_action)
            menu.addAction(edit_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            table.setIndexWidget(self.tasks_model.index(row, self.tasks_model.columnCount() - 1), button)
        self.show()

    def record_clicked(self, index):
        row = index.row()
        task_id = self.tasks_model.index(row, 0).data()
        self.subtask = SubtasksWindow(task_id, self)
        self.subtask.show()

    def handle_done(self, row, model):
        task_id = model.index(row, 0).data()
        db_manager = db_manager = DatabaseManager("data/tasks.db")
        tasks_name = db_manager.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {task_id}")
        tasks_name = tasks_name[0][0]
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
            self.display_filtered_tasks()
            self.display_completed_tasks()
            self.display_number_of_tasks()

    def handle_edit(self, row, model):
        task_id = model.index(row, 0).data()
        edit_task_window = EditTaskWindow(task_id, self)
        edit_task_window.show()

    def handle_delete(self, row, model):
        task_id = model.index(row, 0).data()
        db_manager = db_manager = DatabaseManager("data/tasks.db")
        tasks_name = db_manager.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {task_id}")
        tasks_name = tasks_name[0][0]
        confirmation = QMessageBox()
        confirmation.setText(f"Are you sure you want to delete {tasks_name}?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            self.db_manager.remove_task(task_id)
            self.display_filtered_tasks()
            self.display_tasks()
            self.display_completed_tasks()
            self.display_number_of_tasks()

    # TASKS PAGE END

    # COMPLETED TASKS PAGE BEGIN

    def display_completed_tasks(self):
        table = self.ui.completed_tasks
        query = f"SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks WHERE status = 'Completed' AND user_id = '{self.user_id}'"
        result = self.db_manager.fetch_data(query)
        headers = ["Task ID", "Tasks Name", "Priority", "Due Date", "Label", "Status", "Description", "Created At", "Edit"]
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
        table.sortByColumn(self.completed_tasks_model.columnCount() - 2, Qt.AscendingOrder)
        for row in range(self.completed_tasks_model.rowCount()):
            button = QPushButton("Menu")
            menu = QMenu()
            done_action = QAction("Not Done", self)
            delete_action = QAction("Delete", self)
            done_action.triggered.connect(lambda index, row=row: self.handle_not_done(row))
            delete_action.triggered.connect(lambda index, row=row: self.handle_delete(row, self.completed_tasks_model))
            menu.addAction(done_action)
            menu.addAction(delete_action)
            button.setMenu(menu)
            table.setIndexWidget(self.completed_tasks_model.index(row, self.completed_tasks_model.columnCount() - 1), button)
        self.show()

    def handle_not_done(self, row):
        task_id = self.completed_tasks_model.index(row, 0).data()
        db_manager = db_manager = DatabaseManager("data/tasks.db")
        tasks_name = db_manager.fetch_data(f"SELECT task_name FROM tasks WHERE task_id = {task_id}")
        tasks_name = tasks_name[0][0]
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
            self.display_filtered_tasks()
            self.display_completed_tasks()
            self.display_number_of_tasks()

# COMPLETED TASKS PAGE END
