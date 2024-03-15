from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.project_ui import Ui_AddProject
from data.database_manager import DatabaseManager


class AddProjectDialog(QDialog):
    def __init__(self, user_id, parent):
        super(AddProjectDialog, self).__init__(parent)

        self.ui = Ui_AddProject()
        self.ui.setupUi(self)

        self.db_manager = DatabaseManager()
        self.parent = parent

        self.user_id = user_id
        self.ui.error_message.setText("")

        self.ui.save_btn.clicked.connect(self.handle_save)

    def handle_save(self):
        project_name = self.ui.project_name.text().capitalize().strip()
        result = self.db_manager.fetch_data(
            f"SELECT COUNT(*) FROM projects WHERE project_name = '{project_name}' AND user_id = {self.user_id}"
        )
        if result[0][0] == 1:
            valid_name = False
        else:
            valid_name = True
        if project_name == "":
            self.ui.error_message.setText("Please enter a project name.")
        elif valid_name is False:
            self.ui.error_message.setText("Project name already exists.")
            self.ui.project_name.setText("")
        else:
            self.db_manager.add_project(self.user_id, project_name)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"Successfully added {project_name}.")
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            # self.ui.project_name.setText("")
            self.parent.project_name = project_name
            self.parent.ui.project.addItem(project_name)
            self.parent.ui.project.setCurrentText(project_name)
            self.close()


class RenameProjectDialog(QDialog):
    def __init__(self, user_id, project_name, parent):
        super(RenameProjectDialog, self).__init__(parent)

        self.ui = Ui_AddProject()
        self.ui.setupUi(self)

        self.db_manager = DatabaseManager()
        self.setWindowTitle("Rename Project")
        self.parent = parent
        self.user_id = user_id
        self.project_name = project_name
        project_id = self.db_manager.fetch_data(
            f"SELECT project_id FROM projects WHERE user_id = {self.user_id} AND project_name = '{self.project_name}'"
        )
        self.project_id = project_id[0][0]
        self.ui.error_message.setText("")
        self.ui.dialog_title.setText(f"Rename {self.project_name}")
        self.ui.project_name.setText(self.project_name)

        self.ui.save_btn.clicked.connect(self.handle_save)

    def handle_save(self):
        project_name = self.ui.project_name.text().capitalize().strip()
        result = self.db_manager.fetch_data(
            f"SELECT COUNT(*) FROM projects WHERE project_name = '{project_name}' AND user_id = {self.user_id}"
        )
        if result[0][0] == 1:
            valid_name = False
        else:
            valid_name = True
        if project_name == "":
            self.ui.error_message.setText("Please enter a project name.")
        elif valid_name is False:
            self.ui.error_message.setText("Project name already exists.")
            self.ui.project_name.setText("")
        else:
            self.db_manager.execute_query(
                f"UPDATE projects SET project_name = '{project_name}' WHERE project_id = {self.project_id}"
            )
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(
                f"Successfully changed {self.project_name} to {project_name}."
            )
            msg_box.setWindowTitle("Success")
            msg_box.exec()
            index = self.parent.ui.project.currentIndex()
            self.parent.ui.project.removeItem(index)
            self.parent.ui.project.insertItem(index, project_name)
            self.parent.project_name = project_name
            self.parent.ui.project.setCurrentText(project_name)
            self.close()
