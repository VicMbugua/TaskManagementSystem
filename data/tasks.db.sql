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
CREATE TABLE IF NOT EXISTS "reminders" (
	"reminder_id"	INTEGER,
	"date_time"	TEXT,
	PRIMARY KEY("reminder_id" AUTOINCREMENT)
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
