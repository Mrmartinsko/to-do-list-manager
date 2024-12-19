import os

TASK_FILE = "data/todo_tasks.txt"

def load_tasks(): 
    tasks = []

    # otevře soubor
    with open(TASK_FILE, 'r', encoding="utf-8") as file:
        file_lines = file.readlines()

    # loopuje přes řádky 
    for file_line in file_lines:
        # rozdělí řadky do listu podle ; 
        task_parts = file_line.split(";")
        # vytvoří slovník s rozdělenými částmi úkolu
        task = {
            "id" : int(task_parts[0]),
            "name" : task_parts[1],
            "priority" : task_parts[2],
            "deadline" : task_parts[3],
            "state" : True if task_parts[4].lower() == "ano" else False,
        }

        tasks.append(task)

    return tasks

def save_tasks(tasks):
    # otevře soubor
    with open(TASK_FILE, 'w', encoding="utf-8") as file:
        #loopuje přes úkoly
        for task in tasks:
            #udělá ze slovníku string
            new_line = f"{task['id']};{task['name']};{task['priority']};{task['deadline']};{"Ano" if task["state"] == True else "Ne"}\n"
            file.write(new_line)

def get_user_filter():   
    choice = input("Chcete filtrovat? (priority, stav, ne): ").lower()
    filter = {}

    if choice == "stav":
        state = input("Zadejte stav (Ano / Ne): ").lower()
        filter["state"] = True if state == "ano" else False
    elif choice == "priority":
        priority = input("Zadejte prioritu (Vysoká / Střední / Nízká): ")
        filter["priority"] = priority
    elif choice == "ne":
        return None  # Bez filtru
    else:
        print("Neplatná volba. Nebude použito žádné filtrování.")
        return None
    
    return filter

    


def list_tasks(tasks, filter=None):
    # Nastavíme šířky sloupců
    col_widths = {
        "id": 5,
        "name": 20,
        "priority": 10,
        "deadline": 15,
        "state": 10
    }
    
    # Hlavička tabulky
    header = f"{'ID'.ljust(col_widths['id'])} | {'ÚKOL'.ljust(col_widths['name'])} | {'PRIORITA'.ljust(col_widths['priority'])} | {'TERMÍN DOKONČENÍ'.ljust(col_widths['deadline'])} | {'STAV'.ljust(col_widths['state'])}"
    print(header)
    print("-" * len(header))
    
    # Obsah tabulky
    for task in tasks:
        if filter:
            if filter.get("priority") and task['priority'] != filter['priority']:
                continue
            if filter.get("status") and task['status'] != filter['status']:
                continue

        state = "Ano" if task["state"] == True else "Ne"
        row = (
            f"{str(task['id']).ljust(col_widths['id'])} | "
            f"{task['name'].ljust(col_widths['name'])} | "
            f"{task['priority'].ljust(col_widths['priority'])} | "
            f"{task['deadline'].ljust(col_widths['deadline'])} | "
            f"{state.ljust(col_widths['state'])}"
        )
        print(row)

def add_command(tasks):
    # načtu si potřebné údaje od uživatele
    task_id = max([task["id"] for task in tasks]) + 1 # id pridaneho tasku bude vzdy o 1 vetsi nez je nejvetsi id
    name = input("Zadejte název úkolu: ")
    importance = input("Zadejte důležitost úkolu (Vysoká, Střední, Nízká)") or "Střední"
    date = input("Zadejte do kdy potřebujete úlohu splnit (YYYY-MM-DD): ")
    # uložím uživatelovi údaje do slovníku
    tasks.append({
        "id": task_id,
        "name": name,
        "priority": importance,
        "deadline": date,
        "state": "ne"
    })
    print("Úkol byl přidán!")
    return tasks

def remove_task(tasks):
    remove_id = int(input("Zadej ID úkolu, který chceš vymazat?:"))
    # Loopuju task  
    for task in tasks:
        # Když je input roven ID tasku odstraním jej 
        if remove_id == task['id']:
            tasks.remove(task)
    return tasks

def complete_task(tasks):
    complete_id = int(input("Zadejte ID úkolu, který chcete označit jako dokončený: "))
    for task in tasks:
        if complete_id == task['id']:
            task['state'] = True 
    return tasks


def edit(tasks):
    edit_id = int(input("Zadejte ID úkolu, který chcete upravit: "))
    new_name = input(f"Nový název úkolu (aktuálně {task['name']}): ")
    new_priority = input(f"Nový název úkolu (aktuálně {task['priority']})")
    new_deadline = input(f"Nový termín splnění (aktuálně {task['deadline']})")
    for task in tasks:
        if edit_id == task['id']:
            task['name'] = new_name
            task['priority'] = new_priority
            task['deadline'] = new_deadline
    return tasks           


def main():
    tasks = load_tasks()

    print("=== To Do List Manager - aktuální seznam úkolů ===")
    list_tasks(tasks)
   
  

    

if __name__ == "__main__":
    os.system("cls")
    main()
    