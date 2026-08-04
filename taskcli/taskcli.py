import json
from pathlib import Path
from datetime import datetime
from tabulate import tabulate

class Taskcli:
    def __init__(self):
        self.tasks = []

        filepath = Path("tasks.json")
        if not filepath.exists():
            open("tasks.json", "x")
        elif filepath.exists() and filepath.stat().st_size > 0:
            with open("tasks.json", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]

    def add(self, task: Task):
        self.tasks.append(task)
        self.writeToJson()
        print(f"Task added successfully (ID: {task.id})")

    def update(self, id: int, description):
        for task in self.tasks:
            if id == task.id:
                task.description = description
                task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.writeToJson()
                print("Task updated successfully")
                return
        print("Task not found")

    def delete(self, id: int):
        for index, task in enumerate(self.tasks):
            if id == task.id:
                self.tasks.pop(index)
                self.writeToJson()
                print("Task deleted successfully")
                return
        print("Task not found")

    def list_tasks(self, status):
        headers = ["ID", "Description", "Status"]
        rows = []

        for task in self.tasks:
            if status == "all" or task.status == status:
                rows.append([
                    task.id,
                    task.description,
                    task.status
                ])

        print(tabulate(rows, headers, tablefmt="rounded_outline"))

    def mark_done(self, id: int):
        for task in self.tasks: 
            if id == task.id:
                task.status = "done"
                task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.writeToJson()
                print("Task updated successfully")
                return
        print("Task not found")

    def mark_todo(self, id: int):
        for task in self.tasks:
            if id == task.id:
                task.status = "todo"
                task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.writeToJson()
                print("Task updated successfully")
                return
        print("Task not found")

    def mark_in_progress(self, id: int):
        for task in self.tasks:
            if id == task.id:
                task.status = "in-progress"
                task.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.writeToJson()
                print("Task updated successfully")
                return
        print("Task not found")

    def writeToJson(self):
        json_string = json.dumps(self.tasks, default=lambda o: o.__dict__, indent=4)

        with open("tasks.json", "w") as f:
            f.write(json_string)

class Task:
    def __init__(
        self,
        id,
        description,
        status="todo",
        createdAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        updatedAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt