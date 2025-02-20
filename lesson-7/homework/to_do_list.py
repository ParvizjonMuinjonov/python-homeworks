import json
import csv
from typing import List

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data["due_date"], data["status"])

class TaskManager:
    def __init__(self, file_format="json"):
        self.tasks: List[Task] = []
        self.file_format = file_format
        self.file_name = f"to_do_list.{file_format}"

    def add_task(self, task: Task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input(f"Enter new title ({task.title}): ") or task.title
                task.description = input(f"Enter new description ({task.description}): ") or task.description
                task.due_date = input(f"Enter new due date ({task.due_date}): ") or task.due_date
                task.status = input(f"Enter new status ({task.status}): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print("No tasks found with the specified status.")
            return
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        if self.file_format == "json":
            with open(self.file_name, "w") as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        elif self.file_format == "csv":
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])
                for task in self.tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        print("Tasks saved successfully!")

    def load_tasks(self):
        try:
            if self.file_format == "json":
                with open(self.file_name, "r") as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(item) for item in data]
            elif self.file_format == "csv":
                with open(self.file_name, "r") as file:
                    reader = csv.DictReader(file)
                    self.tasks = [Task.from_dict(row) for row in reader]
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found.")

def main():
    file_format = input("Choose file format (json/csv): ").lower()
    manager = TaskManager(file_format)
    
    while True:
        print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            task = Task(
                input("Enter Task ID: "),
                input("Enter Title: "),
                input("Enter Description: "),
                input("Enter Due Date (YYYY-MM-DD): "),
                input("Enter Status (Pending/Completed): ")
            )
            manager.add_task(task)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task(input("Enter Task ID to update: "))
        elif choice == "4":
            manager.delete_task(input("Enter Task ID to delete: "))
        elif choice == "5":
            manager.filter_tasks(input("Enter status to filter (Pending/Completed): "))
        elif choice == "6":
            manager.save_tasks()
        elif choice == "7":
            manager.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
