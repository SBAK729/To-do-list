# 📝 Python CLI Todo App

A simple and effective command-line todo list manager written in Python. Create, view, complete, and delete tasks — all from your terminal.

---

## 📦 Repository

👉 [GitHub Repo](https://github.com/SBAK729/To-do-list.git)

---

## 💡 Features

- ✅ Add new tasks with title, description, and due date
- 📋 List all tasks with status indicators
- ✅ Mark tasks as completed
- ❌ Delete tasks by ID
- 📅 (Bonus) List only tasks due today
- 💾 Persistent storage using `tasks.json`

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/SBAK729/To-do-list.git
cd To-do-list
```

````

2. **Set up a virtual environment**

```bash
python -m venv .venv
# Activate it:
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt  # If you have one
# OR manually if none:
pip install argparse
```

---

## 🚀 Usage

Use the following commands from the terminal (inside the project folder):

### ➕ Add a Task

```bash
python app.py add --title "My Task" --description "Something important" --due_date 2025-06-20
```

### 📋 List All Tasks

```bash
python app.py list
```

### ✅ Complete a Task

```bash
python app.py complete 1
```

### ❌ Delete a Task

```bash
python app.py delete 2
```

### 📅 List Only Tasks Due Today

```bash
python app.py list --today
```

---

## 🧪 Running Tests

```bash
python test_utils.py
```

---

## 🖼️ Screenshot

Here's an example of the CLI app in action:

---

## 📁 Project Structure

```
To-do-list/
├── app.py
├── task.py
├── utils.py
├── tasks.json
├── test_utils.py
├── README.md
```

---

## 🧼 Code Quality

- Uses `argparse` for CLI
- Includes unit tests via `unittest`
- Compatible with `flake8` for linting

---

Feel free to fork or contribute to improve it! 💻

```

---

Would you like me to save this as a `.md` file or push it directly if you connect your GitHub account?
```
````
