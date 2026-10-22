tasks = []


def add_task(task):
    tasks.append({"name": task, "completed": False})
    print(f"Task added: {task}")


def show_tasks():
    print("\nMy Tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")


def complete_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Completed: {tasks[task_number - 1]['name']}")
    else:
        print("Invalid task number")


if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Push code to GitHub")
    complete_task(1)
    show_tasks()