import datetime

class Task:

    def __init__(self, id, title, description, due_date=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%y-%m-%d").date() if due_date else None
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