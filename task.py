from datetime import datetime, date

class Task:

    def __init__(self, id, title, description, due_date=None, completed=False):
        if isinstance(due_date, str):
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        elif isinstance(due_date, date):
            self.due_date = due_date
        else:
            self.due_date = None

        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "due_date":self.due_date.isoformat() if self.due_date else None,
            "completed":self.completed
        }
    
    def __str__(self):
        status = "✅"if self.completed else "❌"
        due = self.due_date.isoformat() if self.due_date else "N/A"
        return f"[{status}] {self.id}:{self.title} (Due:{due})"