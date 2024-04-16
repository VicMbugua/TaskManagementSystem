from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from ui.add_task_ui import Ui_AddTask
from data.database_manager import DatabaseManager


class AddTaskDialog(QDialog):
    def __init__(self, user_id: int, project_name: str, parent) -> None:
        super(AddTaskDialog, self).__init__(parent)

        self.ui = Ui_AddTask()
        self.ui.setupUi(self)

        self.parent = parent
        self.db_manager = DatabaseManager()
        project_id = self.db_manager.fetch_data(
            "SELECT project_id FROM projects WHERE user_id = ? AND project_name = ?",
            (user_id, project_name))
        self.project_id: int = project_id[0][0]
        self.user_id = user_id
        self.ui.task_name.setFocus()
        self.ui.priority.setCurrentIndex(4)
        self.ui.due_date.setMinimumDate(QDate.currentDate())
        self.ui.reset_btn.clicked.connect(self.handle_reset_btn)
        self.ui.save_btn.clicked.connect(self.handle_save_btn)
        self.ui.cancel_btn.clicked.connect(self.handle_cancel_btn)

    def closeEvent(self, event) -> None:
        self.parent.refresh_table()
        self.parent.display_number_of_tasks()

        return super().closeEvent(event)

    def handle_reset_btn(self) -> None:
        """Clears everything entered in the fields."""
        self.ui.task_name.setText("")
        self.ui.label_name.setCurrentIndex(0)
        self.ui.due_date.setDate(QDate.currentDate())
        self.ui.priority.setCurrentIndex(4)
        self.ui.status.setCurrentIndex(0)
        self.ui.description.setText("")

    def handle_save_btn(self) -> None:
        """Saves the new task to the database."""
        task_name: str = self.ui.task_name.text()
        date: str = self.ui.due_date.date()
        due_date: str = date.toString("yyyy-MM-dd")
        priority: int = int(self.ui.priority.currentText())
        label_name: str = self.ui.label_name.currentText().capitalize()
        description: str = self.ui.description.toPlainText()
        status: str = self.ui.status.currentText()
        if task_name != "":
            self.db_manager.add_task(
                self.user_id,
                self.project_id,
                task_name,
                priority,
                due_date,
                label_name,
                status,
                description,
            )
            self.add_label(label_name)
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText(f"Successfully added {task_name}.")
            information.setWindowTitle("Success")
            information.exec()
            self.handle_reset_btn()
            self.close()
        else:
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Warning)
            information.setText("Please enter a task name.")
            information.setWindowTitle("Invalid")
            information.exec()
            self.ui.task_name.setFocus()

    def add_label(self, label_name):
        labels = self.db_manager.fetch_data("SELECT COUNT(*) FROM labels WHERE user_id = ? AND label_name = ?", (self.user_id, label_name))
        label_exists = False
        if labels[0][0] == 1:
            label_exists = True
        if label_exists is False:
            self.db_manager.add_label(self.user_id, label_name)

    def handle_cancel_btn(self) -> None:
        """Closes the add task dialog without saving anything."""
        task_name = self.ui.task_name.text()
        if task_name != "":
            confirmation = QMessageBox()
            confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            confirmation.setWindowTitle("Confirmation")
            confirmation.setText("Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.handle_reset_btn()
                self.close()
        else:
            self.close()


class EditTaskDialog(QDialog):
    def __init__(self, task_id: int, parent) -> None:
        super(EditTaskDialog, self).__init__(parent)

        self.ui = Ui_AddTask()
        self.ui.setupUi(self)

        self.db_manager = DatabaseManager()
        self.parent = parent
        self.task_id = task_id
        user_id = self.db_manager.fetch_data(f"SELECT user_id FROM tasks WHERE task_id = {self.task_id}")
        self.user_id = user_id[0][0]

        self.ui.due_date.setMinimumDate(QDate.currentDate())
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {self.task_id}"
        self.task_result = self.db_manager.fetch_data(query)
        self.ui.dialog_title.setText("Edit task")
        self.ui.task_name.setText(self.task_result[0][0])
        self.ui.label_name.setEditText(self.task_result[0][3])
        self.label_name = self.task_result[0][3]
        date = self.task_result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.ui.due_date.setDate(due_date)
        self.ui.status.setCurrentIndex(
            self.ui.status.findData(self.task_result[0][4], Qt.DisplayRole)
        )
        self.ui.priority.setCurrentIndex(
            self.ui.priority.findData(self.task_result[0][1], Qt.DisplayRole)
        )
        self.ui.description.setText(self.task_result[0][5])
        self.ui.save_btn.clicked.connect(self.handle_edit_btn)
        self.ui.cancel_btn.clicked.connect(self.handle_cancel_btn)
        self.ui.reset_btn.clicked.connect(self.handle_edit_reset_btn)

    def closeEvent(self, event) -> None:
        self.parent.refresh_table()

        return super().closeEvent(event)

    def handle_edit_btn(self) -> None:
        """Saves the edited information of the edited task."""
        task_name: str = self.ui.task_name.text()
        date = self.ui.due_date.date()
        due_date: str = date.toString("yyyy-MM-dd")
        priority: int = int(self.ui.priority.currentText())
        label_name: str = self.ui.label_name.currentText()
        description: str = self.ui.description.toPlainText()
        status: str = self.ui.status.currentText()
        if task_name != "":
            self.add_label(label_name)
            self.db_manager.edit_task(
                self.task_id, task_name, priority, due_date, label_name, status, description
            )
            self.delete_label(self.label_name)
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Information)
            information.setText(f"Successfully edited {task_name}.")
            information.setWindowTitle("Success")
            information.exec()
            self.close()
        else:
            information = QMessageBox()
            information.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            information.setIcon(QMessageBox.Warning)
            information.setText("Please enter a task name.")
            information.setWindowTitle("Invalid")
            information.exec()
            self.ui.task_name.setFocus()

    def add_label(self, label_name):
        labels = self.db_manager.fetch_data("SELECT COUNT(*) FROM labels WHERE user_id = ? AND label_name = ?", (self.user_id, label_name))
        label_exists = False
        if labels[0][0] == 1:
            label_exists = True
        if label_exists is False:
            self.db_manager.add_label(self.user_id, label_name)
    
    def delete_label(self, label_name):
        labels = self.db_manager.fetch_data("SELECT COUNT(*) FROM tasks WHERE user_id = ? AND label_name = ? AND status != 'Completed'", (self.user_id, label_name))
        label_exists = False
        if labels[0][0] == 1:
            label_exists = True
        if label_exists is False:
            self.db_manager.delete_label(self.user_id, label_name)

    def handle_edit_reset_btn(self) -> None:
        """Resets the fields to their original value."""
        query = f"SELECT task_name, priority, due_date, label_name, status, description FROM tasks WHERE task_id = {self.task_id}"
        self.task_result = self.db_manager.fetch_data(query)
        self.ui.task_name.setText(self.task_result[0][0])
        self.ui.label_name.setEditText(self.task_result[0][3])
        date = self.task_result[0][2]
        due_date = QDate.fromString(date, "yyyy-MM-dd")
        self.ui.due_date.setDate(due_date)
        self.ui.status.setCurrentIndex(
            self.ui.status.findData(self.task_result[0][4], Qt.DisplayRole)
        )
        self.ui.priority.setCurrentIndex(
            self.ui.priority.findData(self.task_result[0][1], Qt.DisplayRole)
        )
        self.ui.description.setText(self.task_result[0][5])

    def handle_cancel_btn(self) -> None:
        """Closes the edit dialog without saving anything."""
        current_task_name = self.task_result[0][0]
        new_task_name = self.ui.task_name.text()
        if new_task_name != current_task_name:
            confirmation = QMessageBox()
            confirmation.setWindowIcon(QIcon("icons/9054813_bx_task_icon.svg"))
            confirmation.setWindowTitle("Confirmation")
            confirmation.setText("Are you sure you want to cancel?")
            confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            confirmation.setDefaultButton(QMessageBox.Cancel)
            confirmation.setIcon(QMessageBox.Warning)
            response = confirmation.exec()
            if response == QMessageBox.Yes:
                self.close()
        else:
            self.close()
