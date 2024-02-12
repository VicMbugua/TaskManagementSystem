from datetime import date
import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        
    def fetch_data(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_user(self, username, password):
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        con.close()
        
    def check_user(self, username):
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"SELECT COUNT(*) FROM users WHERE username = '{username}'")
        result = c.fetchone()
        if result[0] == 1:
            return True
        else:
            return False
        
    def check_password(self, username, password):
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"SELECT COUNT(*) FROM users WHERE username = '{username}' AND password = '{password}'")
        result = c.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def add_task(self, user_id, task_name, priority, due_date, label_name, status, description):
        """Adds a new task to the tasks table."""
        created_at = date.today()
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute("""
        INSERT INTO tasks (user_id, task_name, priority, due_date, label_name, status, description, created_at) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?)""", (user_id, task_name, priority, due_date, label_name, status, description, created_at))
        con.commit()
        con.close()

    def remove_task(self, task_id):
        """Removes a task from the tasks table of the specified task_id."""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
        con.commit()
        con.close()

    def task_completed(self, task_id):
        """Marks a task complete by adding the task to the tasks_done table then removes the task from the tasks table
        of the specified task_id."""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"""
        INSERT INTO tasks_done (task_id, task_name, priority, start_date, end_date)
        SELECT task_id, task_name, priority, start_date, end_date
        FROM tasks
        WHERE task_id = ?""", (task_id,))  # Copies the record from tasks table to tasks_done table.
        c.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
        con.commit()
        con.close()

    def add_subtask(self, task_id, subtask_name):
        """Adds a new subtask to the subtasks table."""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        created_at = date.today()
        status = "Not complete"
        c.execute("INSERT INTO subtasks (task_id, subtask_name, status, created_at) VALUES (?, ?, ?, ?)", (task_id, subtask_name, status, created_at))
        con.commit()
        con.close()

    def number_of_tasks(self):
        """Returns the number of uncompleted tasks"""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Not Started' OR status = 'Started'")
        result = c.fetchone()
        num_records = result[0]
        con.close()
        return num_records

    def add_label(self, label_name):
        """Adds a new label"""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"INSERT INTO labels (label_name) VALUES ({label_name})")
        con.commit()
        con.close()
        
    def edit_task(self, task_id, task_name, priority, due_date, label_name, status, description):
        """Edits a task"""
        con = sqlite3.connect("data/tasks.db")
        c = con.cursor()
        c.execute(f"UPDATE tasks SET task_name = '{task_name}', priority = {priority}, due_date = '{due_date}', label_name = '{label_name}', status = '{status}', description = '{description}' WHERE task_id = {task_id}")
        con.commit()
        con.close()

