import json
from datetime import datetime

# Initialize tasks data
tasks_data = []

# Load tasks from JSON if the file exists
try:
    with open("tasks.json", "r") as file:
        tasks_data = json.load(file)
except FileNotFoundError:
    pass


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file, indent=4)


def add_task():
    task = input("Enter a task: ")

    # Validate due date format
    while True:
        date = input("Enter due date (DD/MM/YYYY): ")
        try:
            datetime.strptime(date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")

    importance_map = {
        "vi": "Very Important",
        "i": "Important",
        "nsi": "Not So Important"
    }

    while True:
        important = input("Enter importance (VI, I, NSI): ").lower()
        if important in importance_map:
            important = importance_map[important]
            break
        else:
            print("Invalid input. Choose from VI, I, NSI.")

    task_info = {
        "task": task,
        "due_date": date,
        "importance": important
    }

    tasks_data.append(task_info)
    sort_tasks()  # Automatically sort after adding
    save_tasks()
    print("Task added and sorted by importance.\n")


def remove_task():
    while True:
        try:
            if len(tasks_data) < 1:
                print("No tasks added yet\n")
                break
            else:
                for index, task in enumerate(tasks_data, start=1):
                    print(f'{index}. {task["task"]} ----> {task["due_date"]} ----> {task["importance"]}')

                remove = int(input("Enter the number of the task you want to delete: "))
                remove = remove - 1
                tasks_data.pop(remove)
                save_tasks()
                print("Task successfully removed\n")
                break
        except ValueError:
            print("Enter valid number\n")
        except IndexError:
            print("No task with that number\n")


def sort_tasks():
    importance_priority = {
        "Very Important": 3,
        "Important": 2,
        "Not So Important": 1
    }

    # Sort by due date (earliest first), then by importance (most important first)
    tasks_data.sort(
        key=lambda task: (
            datetime.strptime(task["due_date"], "%d/%m/%Y"),
            -importance_priority.get(task["importance"], 0)
        )
    )


def view_task():
    if len(tasks_data) < 1:
        print("No tasks added yet\n")
    else:
        print("---------- YOUR TASKS ----------")
        for index, task in enumerate(tasks_data, start=1):
            print(f'{index}. {task["task"]} ----> {task["due_date"]} ----> {task["importance"]}')
        print("\n")


while True:
    print("1. Add task (1)\n2. Remove task (2)\n3. View tasks (3)\n4. Quit (0) ")
    try:
        operation = int(input("Choose an operation: "))

        if operation == 1:
            add_task()
        elif operation == 2:
            remove_task()
        elif operation == 3:
            view_task()
        elif operation == 0:
            break
    except ValueError:
        print("Only enter numbers\n")
