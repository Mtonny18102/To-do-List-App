# to_do_list.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")

def remove_task():
    show_tasks()
    if tasks:
        try:
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")