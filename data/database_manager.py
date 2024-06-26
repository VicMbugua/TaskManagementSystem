import sqlite3
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_file="data/tasks.db") -> None:
        self.db_file = db_file
        try:
            self.connection = sqlite3.connect(self.db_file)
        except sqlite3.OperationalError as e:
            self.create_database()

    def create_database(self) -> None:
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        query = """
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER,
	"username"	TEXT UNIQUE,
	"password"	TEXT,
	PRIMARY KEY("user_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "subtasks" (
	"subtask_id"	INTEGER,
	"task_id"	INTEGER,
	"subtask_name"	TEXT,
	"status"	TEXT,
	"created_at"	TEXT,
	PRIMARY KEY("subtask_id" AUTOINCREMENT),
	FOREIGN KEY("task_id") REFERENCES "tasks"("task_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "projects" (
	"project_id"	INTEGER,
	"user_id"	INTEGER,
	"project_name"	TEXT,
	"created_at"	TEXT,
	PRIMARY KEY("project_id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id")
);
CREATE TABLE IF NOT EXISTS "tasks" (
	"task_id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"project_id"	INTEGER,
	"task_name"	TEXT NOT NULL,
	"priority"	INTEGER,
	"due_date"	TEXT,
	"label_name"	TEXT,
	"status"	TEXT,
	"description"	TEXT,
	"created_at"	TEXT,
	PRIMARY KEY("task_id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "labels" (
	"label_id"	INTEGER,
	"user_id"	INTEGER,
	"label_name"	TEXT,
	PRIMARY KEY("label_id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id")
);
CREATE TABLE IF NOT EXISTS "schedules" (
	"schedule_id"	INTEGER,
	"user_id"	INTEGER,
	"task_id"	INTEGER,
	"date"	TEXT,
	"start_time"	TEXT,
	"end_time"	TEXT,
	FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
	FOREIGN KEY("task_id") REFERENCES "tasks"("task_id"),
	PRIMARY KEY("schedule_id" AUTOINCREMENT)
);
CREATE TRIGGER delete_subtasks
AFTER DELETE ON tasks
BEGIN
DELETE FROM subtasks WHERE task_id = OLD.task_id;
END;
CREATE TRIGGER delete_projects
AFTER DELETE ON users
BEGIN
DELETE FROM projects WHERE user_id = OLD.user_id;
END;
CREATE TRIGGER delete_tasks
AFTER DELETE ON projects
BEGIN
DELETE FROM tasks WHERE project_id = OLD.project_id;
END;
CREATE TRIGGER delete_labels
AFTER DELETE ON users
BEGIN
DELETE FROM labels WHERE user_id = OLD.user_id;
END;
CREATE TRIGGER delete_schedules
AFTER DELETE ON tasks
BEGIN
DELETE FROM schedules WHERE task_id = OLD.task_id;
END;
COMMIT;
        """
        cursor.execute(query)
        connection.commit()
        connection.close()

    def execute_query(self, query, params=None) -> None:
        if params:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            connection.close()
        else:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()

    def fetch_data(self, query, params=None) -> list:
        if params:
            try:
                connection = sqlite3.connect(self.db_file)
                cursor = connection.cursor()
                cursor.execute(query, params)
                results = cursor.fetchall()
                connection.commit()
                return results
            except sqlite3.Error as error:
                return []
            finally:
                if connection:
                    connection.close()
        else:
            try:
                connection = sqlite3.connect(self.db_file)
                cursor = connection.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                connection.commit()
                return results
            except sqlite3.Error as error:
                return []
            finally:
                if connection:
                    connection.close()

    def add_user(self, username: str, password: str) -> None:
        """Adds a new user to the database."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
        )
        connection.commit()
        connection.close()
        user_id = self.fetch_data(
            "SELECT user_id FROM users WHERE username = ?", (username, )
        )
        user_id = int(user_id[0][0])
        self.add_project(user_id, "Default")
        project_id = self.fetch_data(
            f"SELECT project_id FROM projects WHERE user_id = {user_id} AND project_name = 'Default'")
        project_id = project_id[0][0]
        self.add_task(
            user_id, project_id,
            "Example",
            5,
            "1970-01-01",
            "",
            "Not Started",
            "This is an example of a task.",
        )

    def remove_user(self, user_id: int) -> None:
        """Removes a user from the database."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
        connection.commit()
        connection.close()

    def check_user(self, username: str) -> bool:
        """Checks if the username given already exists in the database."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username, ))
        result = cursor.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def check_password(self, username: str, password: str) -> bool:
        """Checks if the password is correct for the given username."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", (username, password)
        )
        result = cursor.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def add_project(self, user_id, project_name):
        now = datetime.now()
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO projects (user_id, project_name, created_at) VALUES (?, ?, ?)",
                       (user_id, project_name, created_at))
        connection.commit()
        connection.close()

    def add_task(
            self, user_id: int, project_id: int, task_name: str, priority: int, due_date: str, label_name: str,
            status: str, description: str
    ):
        """Adds a new task to the tasks table."""
        now = datetime.now()
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(
            """
        INSERT INTO tasks (user_id, project_id, task_name, priority, due_date, label_name, status, description, created_at) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                user_id,
                project_id,
                task_name,
                priority,
                due_date,
                label_name,
                status,
                description,
                created_at,
            ),
        )
        connection.commit()
        connection.close()

    def remove_task(self, task_id: int) -> None:
        """Removes a task from the tasks table of the specified task id."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
        connection.commit()
        connection.close()

    def delete_completed_tasks(self, user_id):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE status = 'Completed' AND user_id = {user_id}")
        connection.commit()
        connection.close()

    def add_subtask(self, task_id: int, subtask_name: str) -> None:
        """Adds a new subtask to the subtasks table."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        now = datetime.now()
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        status = "Not complete"
        cursor.execute(
            "INSERT INTO subtasks (task_id, subtask_name, status, created_at) VALUES (?, ?, ?, ?)",
            (task_id, subtask_name, status, created_at),
        )
        connection.commit()
        connection.close()

    def remove_subtask(self, subtask_id: int) -> None:
        """Removes a subtask from the subtask table."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM subtasks WHERE subtask_id = {subtask_id}")
        connection.commit()
        connection.close()

    def number_of_tasks(self, user_id: int) -> int:
        """Returns the number of uncompleted tasks"""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM tasks WHERE user_id = {
            user_id} AND (status = 'Not Started' OR status = 'Started')"
        )
        result = cursor.fetchone()
        num_records: int = result[0]
        connection.close()
        return num_records

    def edit_task(
            self, task_id: int, task_name: str, priority: int, due_date: str, label_name: str, status: str,
            description: str
    ) -> None:
        """Edits the given task."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET task_name = ?, priority = ?, due_date = ?, label_name = ?, status = ?, description = ? WHERE task_id = ?", 
            (task_name, priority, due_date, label_name, status, description, task_id)
        )
        connection.commit()
        connection.close()

    def add_schedule(self, user_id, task_id, date, start_time, end_time):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO schedules (user_id, task_id, date, start_time, end_time) VALUES (?, ?, ?, ?, ?)",
                       (user_id, task_id, date, start_time, end_time))
        connection.commit()
        connection.close()

    def delete_schedules(self, task_id):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM schedules WHERE task_id = {task_id}")
        connection.commit()
        connection.close()

    def add_label(self, user_id, label_name):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO labels (user_id, label_name) VALUES (?, ?)", (user_id, label_name))
        connection.commit()
        connection.close()

    def delete_label(self, user_id, label_name):
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM labels WHERE user_id = ? AND label_name = ?", (user_id, label_name))
        connection.commit()
        connection.close()
