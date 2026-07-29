# Tasktracker: CLI TODO App

## 📖 Description

**Tasktracker** is a lightweight command-line interface (CLI) application for efficient task management.  
It allows you to **add, update, delete, list, and track tasks** directly from your terminal.

---

## ✨ Features

- **Add a Task** → Create tasks with descriptions. Each task gets a unique ID and a default `todo` status.
- **Update a Task** → Modify the description or status of a task.
- **Mark as Todo** → Quickly change a task’s status to `todo`.
- **Mark as In-Progress** → Quickly change a task’s status to `in-progress`.
- **Mark as Done** → Quickly change a task’s status to `done`.
- **Delete a Task** → Remove tasks by their ID.
- **List Tasks** → Display all tasks or filter them by:
  - **status**: `todo`, `in-progress`, `done`

## 🗂 Project Structure

- **taskcli.py** → Class implementations for Taskcli and Task

  - Taskcli class

    - `__init__()` → Initializes the program by reading the JSON file. If the file does not exist, it is created.
    - `add(task)` → Adds a new task, marked as todo by default.
    - `update(id, description)` → Updates a task's description.
    - `delete(id)` → Deletes a task.
    - `mark_in_todo(id)` → Marks a task as _todo_.
    - `mark_in_progress(id)` → Marks a task as _in-progress_.
    - `mark_done(id)` → Marks a task as _done_.
    - `list_tasks(status)` → Lists tasks with a optional filter for the status. By default, all tasks will be listed.
    - `writeToJson()` → Writes the list of tasks to the JSON file. If the file does not exist, it is created.

  - Task class

    - `id` → Task ID
    - `description` → Task Description
    - `status` → Task Status (todo, in-progress, done)
    - `createdAt` → Date and time for when the task was created
    - `updatedAt` → Date and time for when the tass was updated

- **__main__.py** → Parser implementation. It calls the appropriate Taskcli function depending on the called command.

- **setup.py** → Project metadata, dependencies, and packaging config.

## ⚡ Installation

You can install Task CLI directly from GitHub:

```bash
pip install git+https://github.com/jetyamato/tasktracker
```

## 🚀 Usage

```bash
$ task-cli add [-h] desc

$ task-cli update [-h] task_id desc

$ task-cli delete [-h] task_id

$ task-cli mark-todo [-h] task_id

$ task-cli mark-done [-h] task_id

$ task-cli mark-in-progress [-h] task_id

$ task-cli list [-h] [status]
```

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.