tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    print("\nMy Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create a GitHub repository")
    show_tasks()