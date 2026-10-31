def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def todo_app():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            if not tasks:
                print("\nYour to-do list is currently empty!")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            task = input("\nEnter the task description: ").strip()
            if task:
                tasks.append(task)
                print(f"'{task}' has been added successfully!")
            else:
                print("Task cannot be empty.")
                
        elif choice == '3':
            if not tasks:
                print("\nNo tasks available to delete!")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("\nEnter the number of the task to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"'{removed}' has been removed.")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '4':
            print("\nGoodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    todo_app()