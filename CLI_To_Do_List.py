tasks = []


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task_name = input("Enter task: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for number, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{number}. {task['name']} [{status}]")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to complete: "))
        task_index = task_number - 1

        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        task_index = task_number - 1

        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Deleted: {deleted_task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose between 1 and 5.")