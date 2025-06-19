import json
from datetime import date
import os
from task import Task


TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        file = open(TASKS_FILE,"r")
        data = json.load(file)
        return [Task(**task) for task in data]
    except:
        print("Unable to read from the file")
    finally:
        file.close()

def save_tasks(tasks):

        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

        file.close()

def get_next_id(tasks):
     return max((task.id for task in tasks), default=0) + 1

def get_today_tasks(tasks):
    today = date.today()
    return [
        task for task in tasks
        if task.due_date == today and not task.completed
    ]