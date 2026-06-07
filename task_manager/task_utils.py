from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    valid_title, title_val = validate_task_title(title)
    valid_desc, desc_val = validate_task_description(description)
    valid_date, date_val = validate_due_date(due_date)

    if not valid_title:
        print(title_val)
        return
    if not valid_desc:
        print(desc_val)
        return
    if not valid_date:
        print(date_val)
        return

    task = {
        "title": title_val,
        "description": desc_val,
        "due_date": date_val,
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

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending):
        print(f"{i}. {task['title']} - {task['description']} ({task['due_date']})")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0

    completed = len([t for t in tasks if t["completed"]])
    progress = (completed / len(tasks)) * 100

    return progress