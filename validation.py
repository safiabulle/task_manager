from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        return False, "Invalid title"
    if len(title) < 3:
        return False, "Invalid title"
    return True, title


def validate_task_description(description):
    
    if len(description) > 500:
        return False, "Description is too long"
        
    if len(description.strip()) == 0:
        return False, "Invalid description"
    if len(description) < 5:
        return False, "Invalid description"
    return True, description


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, due_date
    except ValueError:
        
        raise ValueError("Invalid date format")