from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    valid_title, t = validate_task_title(title)
    valid_desc, d = validate_task_description(description)
    valid_date, du = validate_due_date(due_date)

    if not valid_title:
        print(t)
        return
    if not valid_desc:
        print(d)
        return
    if not valid_date:
        print(du)
        return

    task = {
        "title": t,
        "description": d,
        "due_date": du,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    try:
       
        adjusted_index = int(index) - 1
    except ValueError:
        print("Invalid task index.")
        return
    
    if len(tasks) == 0 or adjusted_index < 0 or adjusted_index >= len(tasks):
        print("Invalid task index.")
        return

    tasks[adjusted_index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

   
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i + 1}. {task['title']} - {task['description']} ({task['due_date']})")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0

    completed = len([t for t in tasks if t["completed"]])
    return (completed / len(tasks)) * 100