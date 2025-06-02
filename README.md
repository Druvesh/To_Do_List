** To_Do_List (Terminal-Based) **

This is a simple to-do list app I made in Python. It runs in the terminal and lets you:

Add tasks with a due date and importance level

View all tasks (sorted by due date and how important they are)

Remove tasks by number

Saves everything to a JSON file so your list doesn't get wiped

** How It Works **

When adding a task, you enter:

Task name

Due date (DD/MM/YYYY format)

Importance level: VI (Very Important), I (Important), or NSI (Not So Important)

Tasks are automatically sorted:

First by the soonest due date

Then by importance (Very Important > Important > Not So Important)

** Data Storage **

All tasks are saved in tasks.json

Located in the same folder as the Python script

** How to Run **

bash
Copy
Edit
python task_manager.py
Make sure you’re using Python 3

** Notes **

If you mess up a date or importance level, it’ll ask you again instead of crashing

It's all in the terminal, but I might build a GUI version later
