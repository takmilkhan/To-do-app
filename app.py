# Import necessary module
import datetime

# Hint: This is a class that represents a task in the to-do list.
class Task:
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.datetime.now()
        self.completed = False

    # Hint: This method marks the task as complete.
    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} - {status} (Created on: {self.created_at.strftime('%Y-%m-%d %H:%M')})"

# Hint: This is a class for managing a to-do list, which can hold multiple tasks.
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Hint: Adds a new task to the to-do list.
    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f"Task '{description}' added.")

    # Hint: Lists all tasks in the to-do list.
    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    # Hint: Marks a task as completed by its index in the list.
    def complete_task(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            task.mark_complete()
            print(f"Task '{task.description}' marked as completed.")
        except IndexError:
            print("Invalid task number.")

    # Hint: Deletes a task by its index in the list.
    def delete_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task.description}' deleted.")
        except IndexError:
            print("Invalid task number.")

# Main program to interact with the to-do list
def main():
    todo_list = ToDoList()
    
    while True:
        print("\nSimple To-Do App")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        
        elif choice == '2':
            todo_list.show_tasks()
        
        elif choice == '3':
            task_number = int(input("Enter task number to mark as complete: "))
            todo_list.complete_task(task_number)
        
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Hint: Run the main function if this script is run directly.
if __name__ == "__main__":
    main()
