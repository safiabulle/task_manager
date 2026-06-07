from datetime import datetime
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Task storage
tasks = []

def add_task(title, description, due_date):
    valid_title, title_msg = validate_task_title(title)
    valid_desc, desc_msg = validate_task_description(description)
    valid_date, date_msg = validate_due_date(due_date)

    if not valid_title:
        print(title_msg)
        return
    if not valid_desc:
        print(desc_msg)
        return
    if not valid_date:
        print(date_msg)
        return

    task = {
        "title": title_msg,
        "description": desc_msg,
        "due_date": date_msg,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending):
        print(f"{i}. {task['title']} - {task['description']} (Due: {task['due_date']})")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = len([t for t in tasks if t["completed"]])
        progress = (completed / len(tasks)) * 100

    print(f"Progress: {progress:.2f}%")
    return progress