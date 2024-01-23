from datetime import date
import sqlite3


def add_user(username, password, email):
    con = sqlite3.connect("tasks.db")
    c = con.cursor()
    c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
    con.commit()
    con.close()


def add_task(user_id, task_name, priority, due_date, label_name, status, description):
    """Adds a new task to the tasks table."""
    created_at = date.today()
    con = sqlite3.connect("tasks.db")
    c = con.cursor()
    c.execute("""
    INSERT INTO tasks (user_id, task_name, priority, due_date, label_name, status, description, created_at) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?)""", (user_id, task_name, priority, due_date, label_name, status, description, created_at))
    con.commit()
    con.close()


def remove_task(task_id):
    """Removes a task from the tasks table of the specified task_id."""
    con = sqlite3.connect("tasks.db")
    c = con.cursor()
    c.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
    con.commit()
    con.close()


def task_completed(task_id):
    """Marks a task complete by adding the task to the tasks_done table then removes the task from the tasks table
     of the specified task_id."""
    con = sqlite3.connect("tasks.db")
    c = con.cursor()
    c.execute(f"""
    INSERT INTO tasks_done (task_id, task_name, priority, start_date, end_date)
    SELECT task_id, task_name, priority, start_date, end_date
    FROM tasks
    WHERE task_id = ?""", (task_id,))  # Copies the record from tasks table to tasks_done table.
    c.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")
    con.commit()
    con.close()


def add_subtask(task_id, subtask_name):
    """Adds a new subtask to the subtasks table."""
    con = sqlite3.connect("tasks.db")
    c = con.cursor()
    c.execute("INSERT INTO subtasks (task_id, subtask_name) VALUES (?, ?)", (task_id, subtask_name))
    con.commit()
    con.close()


add_task(1, "Read", 1, "2023-12-30", "Basic", "pending", "Read for your exam")
