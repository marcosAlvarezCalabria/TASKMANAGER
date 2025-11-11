# Simple Task Manager

from task_manager import Task, TaskManager
from ai_service import create_simple_task


def show_menu():
    """Display the menu options"""
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Improve Task with AI")
    print("3. View Tasks")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")


def main():
    # Create TaskManager instance
    manager = TaskManager()

    # Load tasks from JSON file
    manager.load_tasks()

    # Main program loop
    while True:
        show_menu()
        option = input("Choose an option: ")

        match option:
            # Option 1: Add new task
            case '1':
                description = input("Enter task description: ")
                new_task = Task(0, description, False)
                manager.add_task(new_task)
                print("Task added!")

            # Option 2: Improve task with AI
            case '2':
                task_description = input("Enter task description")
                # TODO: Implement AI improvement functionality
                subtasks = create_simple_task(task_description)
                for subtask in subtasks:
                    if not subtask.startswith("error"):
                        manager.add_task(Task(0, subtask, False))
                    else:
                        print(subtask)  
                        break

            # Option 3: View all tasks
            case '3':
                tasks = manager.list_tasks()
                if len(tasks) == 0:
                    print("No tasks.")
                else:
                    for task in tasks:
                        status = "✔" if task.status else " "
                        print(f"{task.id}. [{status}] {task.description}")

            # Option 4: Mark task as completed
            case '4':
                try:
                    task_id = int(input("Which task did you complete? (ID): "))
                    manager.complete_task(task_id)
                except ValueError:
                    print("Invalid number. Please try again.")

            # Option 5: Delete task
            case '5':
                try:
                    task_id = int(input("Which task do you want to delete? (ID): "))
                    # Find task by ID
                    task_to_delete = None
                    for task in manager.tasks:
                        if task.id == task_id:
                            task_to_delete = task
                            break

                    if task_to_delete:
                        manager.delete_task(task_to_delete)
                        print(f"Task '{task_to_delete.description}' deleted.")
                    else:
                        print(f"Task with ID {task_id} not found.")
                except ValueError:
                    print("Invalid number. Please try again.")

            # Option 6: Exit program
            case '6':
                print("Goodbye!")
                break

            # Invalid option
            case _:
                print("Invalid option. Try again.")


# Run the program
if __name__ == "__main__":
    main()
