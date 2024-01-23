from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QLabel
import sys
import record
from interface_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icons_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

    def on_stackWidget_currentChanged(self, index):
        btn_list = self.ui.icons_only_widget.findChildren(QPushButton) \
                   + self.ui.full_name_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [4, 5]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
