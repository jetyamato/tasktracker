import argparse
from taskcli.taskcli import (
    Taskcli,
    Task
)

def main():
    taskcli = Taskcli()

    parser = argparse.ArgumentParser(description="A CLI Task Tracker", epilog='Example: task-cli add "Sample Task"')
    subparsers = parser.add_subparsers(title="Command", dest="command")

    add_parser = subparsers.add_parser("add", help="Adds a new task (marked as todo by default)")
    add_parser.add_argument("desc", help="Task Description")

    update_parser = subparsers.add_parser("update", help="Updates an existing task's description")
    update_parser.add_argument("task_id", type=int, help="Task ID to update")
    update_parser.add_argument("desc", help="New task description")

    delete_parser = subparsers.add_parser("delete", help="Deletes an existing task")
    delete_parser.add_argument("task_id", type=int, help="Task ID to delete")

    list_parser = subparsers.add_parser("list", help="Lists tasks by status")
    list_parser.add_argument("status", help="Task Status (todo, in-progress, done; if not provided, all tasks will be listed)", nargs="?", default="all")

    mark_todo_parser = subparsers.add_parser("mark-todo", help='Mark a task as "todo"')
    mark_todo_parser.add_argument("task_id", type=int, help="Task ID to mark")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help='Mark a task as "in-progress"')
    mark_in_progress_parser.add_argument("task_id", type=int, help="Task ID to mark")

    mark_done_parser = subparsers.add_parser("mark-done", help='Mark a task as "done"')
    mark_done_parser.add_argument("task_id", type=int, help="Task ID to mark")

    args = parser.parse_args()

    if args.command == "add":
        newTask = Task(len(taskcli.tasks) + 1, args.desc)
        taskcli.add(newTask)
    elif args.command == "update":
        taskcli.update(args.task_id, args.desc)
    elif args.command == "delete":
        taskcli.delete(args.task_id)
    elif args.command == "list":
        taskcli.list_tasks(args.status)
    elif args.command == "mark-todo":
        taskcli.mark_todo(args.task_id)
    elif args.command == "mark-in-progress":
        taskcli.mark_in_progress(args.task_id)
    elif args.command == "mark-done":
        taskcli.mark_done(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()