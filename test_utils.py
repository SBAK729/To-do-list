import unittest
from datetime import date
from task import Task
from utils import get_today_tasks, get_next_id

class TestUtils(unittest.TestCase):
    def test_get_next_id(self):
        tasks = [Task(id=1, title="A", description="x"), Task(id=5, title="B", description="y")]
        self.assertEqual(get_next_id(tasks), 6)

    def test_get_today_tasks(self):
        today = date.today()
        tasks = [
            Task(id=1, title="Today", description="desc", due_date=today, completed=False),
            Task(id=2, title="Not today", description="desc", due_date=date(2000, 1, 1), completed=False)
        ]
        today_tasks = get_today_tasks(tasks)
        self.assertEqual(len(today_tasks), 1)

if __name__ == "__main__":
    unittest.main()
