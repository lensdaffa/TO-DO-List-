tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task_desc = input("Enter task: ")
    task = {"task": task_desc, "done": False}
    tasks.append(task)
    print(f"Task '{task_desc}' added!")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
        return
    
    print("\nYOUR TASKS:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to mark done: "))
        index = task_num - 1 
        
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Marked task {task_num} as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        index = task_num - 1
        
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
