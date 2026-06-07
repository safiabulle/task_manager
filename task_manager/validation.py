from datetime import datetime

def validate_task_title(title):
    if not title or len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."
    return True, title.strip()


def validate_task_description(description):
    if not description or len(description.strip()) < 5:
        return False, "Description must be at least 5 characters long."
    return True, description.strip()


def validate_due_date(due_date):
    try:
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        if date_obj < datetime.now():
            return False, "Due date cannot be in the past."
        return True, due_date
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."