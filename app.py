import argparse as arg

DBname = "db.txt"

def add_itemsTODO(item):
    return f"\x1b[9m{item}\x1b[0m"

def add_todo(item):
    with open(DBname,"a") as file:
        file.write(f"{item}\n")
        file.close()
    print(f"Added item: {item}")

