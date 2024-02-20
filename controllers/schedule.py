from data.database_manager import DatabaseManager
from PyQt5.QtCore import QDate
from datetime import datetime, date

class Schedule:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        
        self.db_manager = DatabaseManager("data/tasks.db")
        
    def arrange_tasks(self):
        query = f"SELECT task_id, task_name, priority, due_date, label_name, status, description, created_at FROM tasks WHERE user_id = '{self.user_id}' AND (status = 'Not Started' OR status = 'Started')"
        result = self.db_manager.fetch_data(query)
        result.pop(0)
        new_result = []
        today = date.today().strftime("%Y-%m-%d")
        for item in result:
            if item[2] == 1:
                new_result.append(item)
            if datetime.strptime(item[3], "%Y-%m-%d") < datetime.strptime(today, "%Y-%m-%d"):
                new_result.append(item)
        new_result = list(set(new_result))
        return new_result