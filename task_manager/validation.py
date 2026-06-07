from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        return False, "Invalid title"
    return True, title.strip()


def validate_task_description(description):
    if len(description.strip()) == 0:
        return False, "Invalid description"
    return True, description.strip()


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, due_date
    except ValueError:
        return False, "Invalid date format"