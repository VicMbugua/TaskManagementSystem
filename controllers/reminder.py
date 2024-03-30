import sys
from datetime import datetime, timedelta
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

class ReminderManager:
    def __init__(self):
        self.reminders = []
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon
        self.tray_icon.setIcon(QIcon("icons/9054813_bx_task_icon.svg"))  # Replace with your icon path
        self.tray_icon.setVisible(True)

        self.create_menu()
        self.tray_icon.activated.connect(self.handle_tray_click)
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_reminders)
        self.timer.start(1000)  # Check every second

    def create_menu(self):
        self.menu = QMenu()
        self.show_reminders_action = QAction("Show Reminders", self.menu)
        self.exit_action = QAction("Exit", self.menu)
        self.menu.addAction(self.show_reminders_action)
        self.menu.addAction(self.exit_action)
        self.tray_icon.setContextMenu(self.menu)
        self.exit_action.triggered.connect(self.exit_app)

    def handle_tray_click(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.menu.popup(self.tray_icon.geometry().bottomLeftCorner())

    def exit_app(self):
        self.timer.stop()
        QApplication.quit()

    def add_reminder(self, date_time, message):
        """
        Adds a reminder to the manager.

        Args:
            date_time (datetime): The date and time for the reminder.
            message (str): The message to display for the reminder.
        """
        self.reminders.append((date_time, message))

    def check_reminders(self):
        """
        Checks for reminders that are due and displays a notification.
        """
        now = datetime.now()
        for reminder, message in self.reminders:
            if reminder <= now:
                self.show_notification(message)
                self.reminders.remove((reminder, message))

    def show_notification(self, message):
        """
        Displays a notification on the system tray with the reminder message.

        Args:
            message (str): The message to display in the notification.
        """
        self.tray_icon.showMessage(
            "Reminder", message, QSystemTrayIcon.Information, 10000  # 10 seconds
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reminder_manager = ReminderManager()

    # Add some example reminders (replace with your logic)
    future_time = datetime.now() + timedelta(minutes=1)
    reminder_manager.add_reminder(future_time, "Take a break!")

    sys.exit(app.exec_())

