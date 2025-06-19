
from datetime import date
from task import Task
from utils import load_tasks, save_tasks, get_next_id, get_today_tasks

def add_task(args):
    tasks = load_tasks()
    task = Task(
        id=get_next_id(tasks),
        title=args.title,
        description=args.description,
        due_date=args.due_date
    )
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def list_tasks(args):
    tasks =  load_tasks()
    if args.today:
        tasks = get_today_tasks(tasks)
    for task in tasks:
        print(task)

def complete_task(args):
    tasks = load_tasks()
    for task in tasks:
        if args.id == task.id:
            task.mark_complete()
            save_tasks(tasks)
            print("✅ Task completed")
            return
    
    print("❌ Task not found!")

def delete_task(args):
    tasks = load_tasks()
    tasks=[task for task in tasks if task.id != args.id]
    save_tasks(tasks)
    print("🗑️ Task deleted!")

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CLI to do list app")
    subparser = parser.add_subparsers(dest="command")

    # add tasks parser
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--title")
    add_parser.add_argument("--description")
    add_parser.add_argument("--due_date", required=False)
    add_parser.set_defaults(func= add_task)

    # list tasks
    list_parser = subparser.add_parser("list")
    list_parser.add_argument("--today", action="store_true")
    list_parser.set_defaults(func= list_tasks)

    #complete task
    complete_parser = subparser.add_parser("complete")
    complete_parser.add_argument("id", type=int)
    complete_parser.set_defaults(func=complete_task)

    # delete task
    delete_parser = subparser.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    delete_parser.set_defaults(func=delete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
