import os
import sqlite3
from datetime import date, timedelta


class DatabaseManager:
    def __init__(self, db_file="data/tasks.db") -> None:
        self.db_file = db_file
        if os.path.isfile(self.db_file):
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
        else:
            self.create_database()

    def create_database(self) -> None:
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        users = """CREATE TABLE "users" (
                "user_id"	INTEGER,
                "username"	TEXT UNIQUE,
                "password"	TEXT,
                PRIMARY KEY("user_id" AUTOINCREMENT))"""
        tasks = """CREATE TABLE "tasks" (
                "task_id"	INTEGER NOT NULL,
                "user_id"	INTEGER,
                "task_name"	TEXT NOT NULL,
                "priority"	INTEGER,
                "due_date"	TEXT,
                "label_name"	TEXT,
                "status"	TEXT,
                "description"	TEXT,
                "created_at"	TEXT,
                FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE,
                PRIMARY KEY("task_id" AUTOINCREMENT))"""
        subtasks = """CREATE TABLE "subtasks" (
                "subtask_id"	INTEGER,
                "task_id"	INTEGER,
                "subtask_name"	TEXT,
                "status"	TEXT,
                "created_at"	TEXT,
                FOREIGN KEY("task_id") REFERENCES "tasks"("task_id") ON DELETE CASCADE,
                PRIMARY KEY("subtask_id" AUTOINCREMENT))"""
        delete_tasks = """CREATE TRIGGER delete_tasks
                AFTER DELETE ON users
                BEGIN
                DELETE FROM tasks WHERE user_id = OLD.user_id;
                END"""
        delete_subtasks = """CREATE TRIGGER delete_subtasks
                AFTER DELETE ON tasks
                BEGIN
                DELETE FROM subtasks WHERE task_id = OLD.task_id;
                END"""

        cursor.execute(users)
        cursor.execute(tasks)
        cursor.execute(subtasks)
        cursor.execute(delete_tasks)
        cursor.execute(delete_subtasks)
        connection.commit()
        connection.close()

    def execute_query(self, query) -> None:
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def fetch_data(self, query, params=None) -> list:
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        # connection.close()
        # return result

    def add_user(self, username: str, password: str) -> None:
        """Adds a new user to the database."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
        )
        con.commit()
        con.close()
        user_id: list = self.fetch_data(
            f"SELECT user_id FROM users WHERE username = '{username}'"
        )
        user_id: int = int(user_id[0][0])
        self.add_task(
            user_id,
            "Example",
            1,
            "1970-01-01",
            "Pleasure",
            "Not Started",
            "This is an example of a task.",
        )

    def remove_user(self, user_id: int) -> None:
        """Removes a user from the database."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(f"DELETE FROM users WHERE user_id = {user_id}")
        con.commit()
        con.close()

    def check_user(self, username: str) -> bool:
        """Checks if the username given already exists in the database."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(f"SELECT COUNT(*) FROM users WHERE username = '{username}'")
        result = c.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def check_password(self, username: str, password: str) -> bool:
        """Checks if the password is correct for the given username."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(
            f"SELECT COUNT(*) FROM users WHERE username = '{
                username}' AND password = '{password}'"
        )
        result = c.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def add_task(
            self, user_id: int, task_name: str, priority: int, due_date: str, label_name: str, status: str, description: str
    ):
        """Adds a new task to the tasks table."""
        created_at = date.today()
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(
            """
        INSERT INTO tasks (user_id, task_name, priority, due_date, label_name, status, description, created_at) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                user_id,
                task_name,
                priority,
                due_date,
                label_name,
                status,
                description,
                created_at,
            ),
        )
        con.commit()
        con.close()

    def remove_task(self, task_id: int) -> None:
        """Removes a task from the tasks table of the specified task_id."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
        con.commit()
        con.close()

    def add_subtask(self, task_id: int, subtask_name: str) -> None:
        """Adds a new subtask to the subtasks table."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        created_at = date.today()
        status = "Not complete"
        c.execute(
            "INSERT INTO subtasks (task_id, subtask_name, status, created_at) VALUES (?, ?, ?, ?)",
            (task_id, subtask_name, status, created_at),
        )
        con.commit()
        con.close()

    def remove_subtask(self, subtask_id: int) -> None:
        """Removes a subtask from the subtask table."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(f"DELETE FROM subtasks WHERE subtask_id = {subtask_id}")
        con.commit()
        con.close()

    def number_of_tasks(self, user_id: int) -> int:
        """Returns the number of uncompleted tasks"""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(
            f"SELECT COUNT(*) FROM tasks WHERE user_id = {
                user_id} AND (status = 'Not Started' OR status = 'Started')"
        )
        result = c.fetchone()
        num_records: int = result[0]
        con.close()
        return num_records

    def edit_task(
            self, task_id: int, task_name: str, priority: int, due_date: str, label_name: str, status: str, description: str
    ) -> None:
        """Edits the given task."""
        con = sqlite3.connect(self.db_file)
        c = con.cursor()
        c.execute(
            f"UPDATE tasks SET task_name = '{task_name}', priority = {priority}, due_date = '{due_date}', label_name = '{
                label_name}', status = '{status}', description = '{description}' WHERE task_id = {task_id}"
        )
        con.commit()
        con.close()
