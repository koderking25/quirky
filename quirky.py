import sys
import json
import os
import random
import time

FILE = os.path.expanduser("~/quirky_tasks.json")


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


tasks = load_tasks()


fun_messages = [
    "Nice! Future you will be proud 😎",
    "Task conquered! 🏆",
    "Boom! Another thing off the list 🚀",
    "Productivity level increased 📈",
    "Tiny victory unlocked ✨"
]


def show_tasks():
    if not tasks:
        print("\n📭 Your list is empty. A peaceful void... for now.")
        return

    print("\n📝 Your To-Do List:")

    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['name']}")


def add_task(task):
    tasks.append({
        "name": task,
        "done": False
    })

    save_tasks()
    print(f"✨ Added: {task}")


def complete_task(number):
    try:
        index = int(number) - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks()
            print(random.choice(fun_messages))
        else:
            print("🤨 That task doesn't exist.")

    except ValueError:
        print("Please enter a task number.")


def delete_task(number):
    try:
        index = int(number) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"💨 Deleted: {removed['name']}")
        else:
            print("That task doesn't exist.")

    except ValueError:
        print("Please enter a task number.")


def loading():
    print("\nLoading productivity machine", end="")

    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")

    print("\n")


# COMMAND MODE

if len(sys.argv) > 1:

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) > 2:
            add_task(" ".join(sys.argv[2:]))
        else:
            print("🤔 Tell me what task to add.")


    elif command == "list":
        show_tasks()


    elif command == "done":
        if len(sys.argv) > 2:
            complete_task(sys.argv[2])
        else:
            print("🤔 Which task number?")


    elif command == "delete":
        if len(sys.argv) > 2:
            delete_task(sys.argv[2])
        else:
            print("🤔 Which task number?")


    else:
        print("🤖 Unknown command.")

    sys.exit()


# INTERACTIVE MODE

while True:

    loading()

    print("""
========================
 🌟 QUIRKY TO-DO APP 🌟
========================

1. 📋 Show tasks
2. ➕ Add task
3. ✅ Complete task
4. 🗑️ Delete task
5. 🚪 Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("\n✏️ What do you want to add? ")
        add_task(task)

    elif choice == "3":
        show_tasks()
        number = input("\n🎯 Which task did you finish? ")
        complete_task(number)

    elif choice == "4":
        show_tasks()
        number = input("\n🗑️ Which task should disappear? ")
        delete_task(number)

    elif choice == "5":
        print("\n👋 Goodbye! Go crush those goals!")
        break

    else:
        print("🤖 My robot brain doesn't understand that.")
