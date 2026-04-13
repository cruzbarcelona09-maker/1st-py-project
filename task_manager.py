#Task Manager 


import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(title, description=""):
    """Add a new task"""
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Task added: {title}")

def list_tasks(show_all=True):
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\n" + "="*50)
    print("YOUR TASKS")
    print("="*50)
    
    for task in tasks:
        if show_all or not task["completed"]:
            status = "✓" if task["completed"] else " "
            print(f"[{status}] {task['id']}. {task['title']}")
            if task["description"]:
                print(f"    {task['description']}")
            

def complete_task(task_id):
    """Mark a task as complete"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✓ Completed: {task['title']}")
            return
    print("Task not found!")

def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"✓ Task deleted")

def edit_task(task_id):
    """Edit a task"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            print(f"Current title: {task['title']}")
            print(f"Current description: {task['description']}")
            new_title = input("New title (leave empty to keep current): ").strip()
            new_desc = input("New description (leave empty to keep current): ").strip()
            if new_title:
                task["title"] = new_title
            if new_desc:
                task["description"] = new_desc
            save_tasks(tasks)
            print(f"✓ Task updated: {task['title']}")
            return
    print("Task not found!")

def show_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("       PERSONAL TASK MANAGER")
    print("="*50)
    print("1. Add new task")
    print("2. List all tasks")
    print("3. List pending tasks")
    print("4. Mark task as complete")
    print("5. Delete a task")
    print("6. Edit a task")
    print("7. Exit")
    print("="*50)

def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                desc = input("Description (optional): ").strip()
                add_task(title, desc)
            else:
                print("Title cannot be empty!")
                
        elif choice == "2":
            list_tasks(show_all=True)
            
        elif choice == "3":
            list_tasks(show_all=False)
            
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "6":
            try:
                task_id = int(input("Enter task ID to edit: "))
                edit_task(task_id)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "7":
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid option! Please choose 1-7")

if __name__ == "__main__":
    main()
