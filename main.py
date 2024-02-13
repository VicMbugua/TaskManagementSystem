from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from controllers.login import LogInWindow
from controllers.sign_up import SignUpWindow
from controllers.main_window import MainWindow 


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # # Loading stylesheet file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)
    
    
    # window = MainWindow()
    # window.setWindowTitle("Task Management System")
    # window.show()
    widget = QStackedWidget()
    login_window = LogInWindow(widget)
    sign_up_window = SignUpWindow(widget)
    widget.addWidget(login_window)
    widget.addWidget(sign_up_window)
    widget.setFixedSize(350, 350)
    widget.setWindowTitle("Task Management System")
    widget.show()
    sys.exit(app.exec())