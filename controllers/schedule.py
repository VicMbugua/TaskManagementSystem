from ui.schedule_ui import Ui_ScheduleDialog
from data.database_manager import DatabaseManager
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate, Qt, QTime


class ScheduleDialog(QDialog):
    def __init__(self, task_id, parent=None) -> None:
        super(ScheduleDialog, self).__init__(parent)
        
        self.ui = Ui_ScheduleDialog()
        self.ui.setupUi(self)
        
        self.task_id = task_id
        self.db_manager = DatabaseManager()
        task_name = self.db_manager.fetch_data(
            f"SELECT task_name FROM tasks WHERE task_id = {self.task_id}"
        )
        self.task_name = task_name[0][0]
        self.ui.task_name.setText(f"Schedule {self.task_name}")
        
        self.ui.start_date.setMinimumDate(QDate.currentDate())
        self.ui.start_date.dateChanged.connect(self.start_date_changed)
        self.ui.due_date.setMinimumDate(QDate.currentDate())
        self.ui.end_date.setMinimumDate(QDate.currentDate())
        result = self.db_manager.fetch_data(f"SELECT due_date FROM tasks WHERE task_id = {self.task_id}")
        self.due_date = result[0][0]
        self.due_date = QDate.fromString(self.due_date, "yyyy-MM-dd")
        self.ui.due_date.setDate(self.due_date)
        self.ui.start_time.setTime(QTime.currentTime())
        self.ui.start_time.timeChanged.connect(self.start_time_changed)
        self.ui.end_time.setTime(QTime.currentTime().addSecs(2*60*60))
        self.ui.end_time.setMinimumTime(self.ui.start_time.time())
        self.ui.end_date.setDate(QDate.currentDate().addDays(7))
        
        self.ui.repeat.toggled.connect(lambda checked: self.handle_repeat(checked))
        self.ui.save_btn.clicked.connect(self.save_schedule)
        self.ui.cancel_btn.clicked.connect(self.handle_cancel)
        
    def start_date_changed(self, new_date):
        self.ui.end_date.setMinimumDate(new_date)
        self.ui.end_date.setDate(new_date.addDays(7))
        self.ui.due_date.setMinimumDate(new_date)
        
        
    def start_time_changed(self, new_time):
        self.ui.end_time.setMinimumTime(new_time)
        self.ui.end_time.setTime(new_time.addSecs(2*60*60))
        
        
    def handle_repeat(self, checked):
        if checked:
            self.ui.end_date.setEnabled(True)
            self.ui.sunday.setEnabled(True)
            self.ui.monday.setEnabled(True)
            self.ui.tuesday.setEnabled(True)
            self.ui.wednesday.setEnabled(True)
            self.ui.thursday.setEnabled(True)
            self.ui.friday.setEnabled(True)
            self.ui.saturday.setEnabled(True)
        else:
            self.ui.end_date.setEnabled(False)
            self.ui.sunday.setEnabled(False)
            self.ui.monday.setEnabled(False)
            self.ui.tuesday.setEnabled(False)
            self.ui.wednesday.setEnabled(False)
            self.ui.thursday.setEnabled(False)
            self.ui.friday.setEnabled(False)
            self.ui.saturday.setEnabled(False)
            
    def save_schedule(self):
        start_date = self.ui.start_date.date()
        start_time = self.ui.start_time.time()
        end_time = self.ui.end_time.time()
        if self.ui.repeat.isChecked():
            end_date = self.ui.end_date.date()
            day_of_week = start_date.dayOfWeek()
            print(day_of_week)
            day_index = 1
            no_of_days = start_date.daysTo(end_date)
            print(no_of_days)
            list_of_dates = []
            j = 0
            for i in range(no_of_days // 7 + 2):
                if self.ui.monday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.tuesday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.wednesday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.thursday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.friday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.saturday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index += 1
                if self.ui.sunday.isChecked() and day_of_week <= day_index and j <= no_of_days:
                    list_of_dates.append(start_date.addDays(j).toString("yyyy-MM-dd"))
                j = j + 1 if day_of_week <= day_index else j
                day_index = 1
                day_of_week = 1
            print(list_of_dates)
            for date in list_of_dates:
                print(f"{date} {start_time.toString("HH:mm")} {end_time.toString("HH:mm")}")
    
    def handle_save(self):
        pass
            
    def handle_cancel(self):
        confirmation = QMessageBox()
        confirmation.setText(f"Are you sure you want to cancel?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirmation.setDefaultButton(QMessageBox.Cancel)
        confirmation.setIcon(QMessageBox.Warning)
        response = confirmation.exec()
        if response == QMessageBox.Yes:
            self.close()