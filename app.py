PROJECT_NAME = "Git Practice Lab"
GREETING = "Hello from the feature branch"
PROJECT_STATUS = "feature-ready"

def show_tasks():
    tasks = [
        "Inspect the Git status",
        "Make a change",
        "Create a commit",
    ]
    print(GREETING)
    print(f"Project: {PROJECT_NAME}")
    print(f"Status: {PROJECT_STATUS}")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

if __name__ == "__main__":
    show_tasks()
