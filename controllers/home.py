from PyQt5.QtWidgets import QMainWindow, QWidget
from data import database_manager
from ui.interface_ui import Ui_MainWindow


class HomePage(QMainWindow):
    def __init__(self, ui):
        super(HomePage, self).__init__()
        self.ui = ui
        
        
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.display_number_of_tasks()
        print("hello")
        
    def display_number_of_tasks(self):
        no_of_tasks = database_manager.number_of_tasks()
        self.ui.no_of_tasks.setText(f"Number of tasks {no_of_tasks}")