import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
from controllers.login import LogInWindow
from controllers.sign_up import SignUpWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QStackedWidget()
        widget.setFixedSize(330, 300)
        login_window = LogInWindow(widget)
        sign_up_window = SignUpWindow(widget)
        widget.addWidget(login_window)
        widget.addWidget(sign_up_window)
        widget.setWindowTitle("Task Management System")
        widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    window = MyApp()
    sys.exit(app.exec())
