from datetime import datetime

def validate_task_title(title):
    if len(title) < 3:
        return False, "Invalid title"
    return True, title


def validate_task_description(description):
    if len(description) < 5:
        return False, "Invalid description"
    return True, description


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Invalid date format"