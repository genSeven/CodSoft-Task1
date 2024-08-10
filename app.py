import argparse as arg

DBname = "db.txt"

def add_itemsTODO(item):
    return f"\x1b[9m{item}\x1b[0m"  

def add_todo(item):
    with open(DBname, "a") as file:
        file.write(f"{item}\n")
    print(f"Added item: {item}")

def list_todos():
    try:
        with open(DBname, "r") as file:
            tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks in the list.")
    except FileNotFoundError:
        print("No tasks in the list.")

def mark_done(index):
    try:
        with open(DBname, "r") as file:
            tasks = file.readlines()
        if 0 < index <= len(tasks):
            tasks[index - 1] = add_itemsTODO(tasks[index - 1].strip()) + "\n"
            with open(DBname, "w") as file:
                file.writelines(tasks)
            print(f"Marked item {index} as done.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to mark as done.")

def main():
    parser = arg.ArgumentParser(description="Simple CLI To-Do App")
    parser.add_argument("command", choices=["add", "list", "done"], help="Command to execute")
    parser.add_argument("item", nargs="?", help="Item to add or mark as done (by number)")

    args = parser.parse_args()

    if args.command == "add":
        if args.item:
            add_todo(args.item)
        else:
            print("Please provide an item to add.")
    elif args.command == "list":
        list_todos()
    elif args.command == "done":
        if args.item and args.item.isdigit():
            mark_done(int(args.item))
        else:
            print("Please provide a valid task number to mark as done.")

if __name__ == "__main__":
    main()


