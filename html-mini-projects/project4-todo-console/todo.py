
# todo.py - Fullstack Console-Based To-Do List App with Persistence
import os
import json

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Complete/Incomplete")
    print("5. Remove Task")
    print("6. Clear All Tasks")
    print("7. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['text']}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"text": task, "done": False})
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_text = input("Enter new task text: ").strip()
            if new_text:
                tasks[num-1]["text"] = new_text
                print("Task updated.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to toggle complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = not tasks[num-1]["done"]
            status = "completed" if tasks[num-1]["done"] else "incomplete"
            print(f"Task marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed['text']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Clear cancelled.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_complete(tasks)
            save_tasks(tasks)
        elif choice == "5":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            clear_tasks(tasks)
            save_tasks(tasks)
        elif choice == "7":
            print("Exiting To-Do List. Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
