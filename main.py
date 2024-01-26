from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, qApp
import sys
import record
from interface_ui import Ui_MainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

# class ButtonDelegate(QItemDelegate):
#     def __init__(self, parent = None):
#         super().__init__(parent)
        
#     def createEditor(self, parent, option, index):
#         button = QPushButton("Edit", parent)
#         button.clicked.connect(self.buttonClicked)
#         return button
    
#     def setEditorData(self, editor, index):
#         editor.setText(index.data())
        
#     def buttonClicked(self):
#         button = self.sender()
#         index = self.parent().indexAt(button.pos())
        
#         print(f"row {index.row()}, column {index.column()}")
        
        
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
        
    def display_tasks(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("tasks.db")
        if not db.open():
            print("Error: could not open database")
            
        model = QSqlTableModel()
        model.setTable("tasks")
        model.select()
        
        self.table = self.ui.tasks_list
        self.table.setModel(model)
        
        row_count = model.rowCount()
        
        for index in range(row_count):
            self.btn_edit = QPushButton('Edit')
            # self.btn_edit.clicked.connect(self.handle_edit_button())
            # self.table.setCellWidget(index, 2, self.btn_edit)
        
        
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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    window = MainWindow()
    window.display_tasks()
    window.show()
    sys.exit(app.exec())
