import json
import csv

with open("tasks.json", "r") as file:
    data = json.load(file)

print("Task List:\n" + "-" * 40)
for task in data:
    status = "✅" if task["completed"] else "❌"
    print(f"ID: {task['id']} | Task: {task['task']} | Status: {status} | Priority: {task['priority']}")

task_id = int(input("Enter task ID to update: "))
for task in data:
    if task["id"] == task_id:
        task["completed"] = input("Mark as completed? (yes/no): ").strip().lower() == "yes"
        break

with open("tasks.json", "w") as file:
    json.dump(data, file, indent=4)

total_tasks = len(data)
completed_tasks = sum(1 for task in data if task["completed"])
pending_tasks = total_tasks - completed_tasks
average_priority = round(sum(task["priority"] for task in data) / total_tasks, 2)

print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Pending tasks: {pending_tasks}")
print(f"Average priority: {average_priority}")

with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task Name", "Completed Status", "Priority"])
    for task in data:
        writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

print("✅ tasks.csv has been created successfully!")
