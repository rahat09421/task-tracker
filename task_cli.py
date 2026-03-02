import sys, json, os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)
        
def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_task(description):
    tasks = load_tasks()
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        "id" : new_id,
        "description" : description,
        "status": "todo",
        "createdAt": get_now(),
        "updatedAt" : get_now()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")
    
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = description
            task["UpdateAt"] = get_now()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
        print(f"Error: Task {task_id} not foud.")
        
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t['id'] != int(task_id)]
    if len(tasks) == len(updated_tasks):
        print(f"Error: Task {task_id} not found")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted successfully.")

def mark_status(task_id, status):
    tasks = load_tasks()
    found = False
    
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = status
            task['updatedAt'] = get_now()
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status}.")
    else:
        print(f"Error: Task {task_id} not found.")
        
def list_tasks(status_filter = None):
    tasks = load_tasks()
    filtered = [t for t in tasks if t['status'] == status_filter] if status_filter else tasks
    
    if not filtered:
        print("No tasks found.")
        return
    
    print(f"{'ID':<5} {'Status': <15} {'Description'}")
    print("-" * 40)
    for t in filtered:
        print(f"{t['id']:<5} {t['status']:<15} {t['description']}")
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py add | update | delete | list | mark-in-progress | mark-done")
        return
    command = sys.argv[1]
    
    try:
        if command == "add":
            add_task(sys.argv[2])
        elif command == "update":
            update_task(sys.argv[2], sys.argv[3])
        elif command == "delete":
            delete_task(sys.argv[2])
        elif command == "mark-in-progress":
            mark_status(sys.argv[2], "in-progress")
        elif command == "mark-done":
            mark_status(sys.argv[2], "done")
        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else None
            list_tasks(status)
        else:
            print("Unknown command.")
    except IndexError:
        print("Error: Missing arguments for command.")
    except ValueError:
        print("Error: ID must be a number.")
        
if __name__ == "__main__":
    main()