### Task Tracker CLI
A simple Command Line Interface (CLI) application to manage your daily tasks, built with Python. This project tracks task statuses (todo, in-progress, done) and persists data locally using a JSON file.

#### 🚀 Features
No Dependencies: Built entirely using Python's native libraries (json, os, sys, datetime).

Persistent Storage: Tasks are saved in a tasks.json file in the project directory.

Task Management: Add, update, and delete tasks easily.

Status Tracking: Mark tasks as "in-progress" or "done".

Filtering: View all tasks or filter them by their current status.

#### 🛠️ Installation
Clone the repository:

Bash
git clone https://github.com/rahat09421/task-tracker.git
cd task-tracker
No installation required:
As long as you have Python 3 installed, you are ready to go!

#### 📖 Usage
Run the script using python task_cli.py followed by a command.

Adding Tasks
Bash
python task_cli.py add "Buy groceries"
 // Output: Task added successfully (ID: 1)
Updating and Deleting
Bash
python task_cli.py update 1 "Buy groceries and cook dinner"
python task_cli.py delete 1
Changing Task Status
Bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
Listing Tasks
Bash
// List all tasks
python task_cli.py list

// List by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
#### 📂 Data Structure
Tasks are stored in tasks.json with the following format:

JSON
{
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2024-05-20 10:00:00",
    "updatedAt": "2024-05-20 10:05:00"
}

#### Project URL
https://roadmap.sh/projects/task-tracker
