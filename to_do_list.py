import os

TASK_FILE = "data/todo_tasks.txt"

def load_tasks(): 
    """
    Načte úkoly ze souboru a vrátí je jako seznam slovníků.
    
    :return: Seznam úkolů
    """
    tasks = []

    # Otevře soubor a načte řádky
    with open(TASK_FILE, 'r', encoding="utf-8") as file:
        file_lines = file.readlines()

    # Loopuje přes řádky a rozdělí je do slovníku
    for file_line in file_lines:
        task_parts = file_line.split(";")
        task = {
            "id": int(task_parts[0]),
            "name": task_parts[1],
            "priority": task_parts[2],
            "deadline": task_parts[3],
            "state": True if task_parts[4].strip().lower() == "ano" else False,
        }
        tasks.append(task)

    return tasks

def save_tasks(tasks):
    """
    Uloží seznam úkolů do souboru.
    
    :param tasks: Seznam úkolů
    """
    with open(TASK_FILE, 'w', encoding="utf-8") as file:
        for task in tasks:
            # Vytvoří řádek pro uložení
            new_line = f"{task['id']};{task['name']};{task['priority']};{task['deadline']};{"Ano" if task['state'] else "Ne"}\n"
            file.write(new_line)

def get_user_filter():   
    """
    Získá filtr od uživatele a vrátí ho jako slovník.
    
    :return: Slovník filtru nebo None, pokud filtr není nastaven
    """
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
    """
    Vypíše seznam úkolů podle zadaného filtru.
    
    :param tasks: Seznam úkolů
    :param filter: Slovník s filtrem (např. podle priority nebo stavu)
    """
    # Nastavení šířek sloupců
    col_widths = {
        "id": 5,
        "name": 20,
        "priority": 10,
        "deadline": 15,
        "state": 10
    }
    
    # Hlavička tabulky
    header = f"{'ID'.ljust(col_widths['id'])} | {'Úkol'.ljust(col_widths['name'])} | {'Priorita'.ljust(col_widths['priority'])} | {'Termín dokončení'.ljust(col_widths['deadline'])} | {'Stav'.ljust(col_widths['state'])}"
    print(header)
    print("-" * len(header))
    
    # Obsah tabulky
    for task in tasks:
        if filter:
            # Aplikace filtru
            if filter.get("priority") and task['priority'] != filter['priority']:
                continue
            if filter.get("state") is not None and task['state'] != filter['state']:
                continue

        state = "Ano" if task["state"] else "Ne"
        row = (
            f"{str(task['id']).ljust(col_widths['id'])} | "
            f"{task['name'].ljust(col_widths['name'])} | "
            f"{task['priority'].ljust(col_widths['priority'])} | "
            f"{task['deadline'].ljust(col_widths['deadline'])} | "
            f"{state.ljust(col_widths['state'])}"
        )
        print(row)

def add_command(tasks):
    """
    Přidá nový úkol na základě uživatelského vstupu.
    
    :param tasks: Seznam existujících úkolů
    :return: Aktualizovaný seznam úkolů
    """
    task_id = max([task["id"] for task in tasks]) + 1 if tasks else 1  # Pokud nejsou úkoly, id = 1
    name = input("Zadejte název úkolu: ")
    importance = input("Zadejte důležitost úkolu (Vysoká, Střední, Nízká): ") or "Střední"
    date = input("Zadejte do kdy potřebujete úlohu splnit (YYYY-MM-DD): ")
    
    tasks.append({
        "id": task_id,
        "name": name,
        "priority": importance,
        "deadline": date,
        "state": False
    })
    print("Úkol byl přidán!")
    return tasks

def remove_task(tasks):
    """
    Odstraní úkol podle zadaného ID.
    
    :param tasks: Seznam úkolů
    :return: Aktualizovaný seznam úkolů
    """
    remove_id = int(input("Zadej ID úkolu, který chceš vymazat: "))
    for task in tasks:
        if remove_id == task['id']:
            tasks.remove(task)
            print("Úkol byl odstraněn.")
            break
    else:
        print("Úkol s tímto ID nebyl nalezen.")
    return tasks

def complete_task(tasks):
    """
    Označí zadaný úkol jako dokončený podle ID.
    
    :param tasks: Seznam úkolů
    :return: Aktualizovaný seznam úkolů
    """
    complete_id = int(input("Zadejte ID úkolu, který chcete označit jako dokončený: "))
    for task in tasks:
        if complete_id == task['id']:
            task['state'] = True
            print("Úkol byl označen jako dokončený.")
            break
    else:
        print("Úkol s tímto ID nebyl nalezen.")
    return tasks

def edit(tasks):
    """
    Upraví zadaný úkol podle ID.
    
    :param tasks: Seznam úkolů
    :return: Aktualizovaný seznam úkolů
    """
    edit_id = int(input("Zadejte ID úkolu, který chcete upravit: "))
    for task in tasks:
        if edit_id == task['id']:
            task['name'] = input(f"Nový název úkolu (aktuálně {task['name']}): ") or task['name']
            task['priority'] = input(f"Nová priorita úkolu (aktuálně {task['priority']}): ") or task['priority']
            task['deadline'] = input(f"Nový termín splnění (aktuálně {task['deadline']}): ") or task['deadline']
            print("Úkol byl upraven.")
            break
    else:
        print("Úkol s tímto ID nebyl nalezen.")
    return tasks

def main(tasks, command):
    """
    Zpracování příkazů zadaných uživatelem.
    
    :param tasks: Seznam úkolů
    :param command: Příkaz zadaný uživatelem
    :return: Aktualizovaný seznam úkolů
    """
    if command == "add":
        tasks = add_command(tasks)
    elif command == "list":
        choice = get_user_filter()
        list_tasks(tasks, choice)
    elif command == "remove":
        tasks = remove_task(tasks)
    elif command == "complete":
        tasks = complete_task(tasks)
    elif command == "edit":
        tasks = edit(tasks)
    elif command == "save":
        save_tasks(tasks)
        print("Úkoly byly uloženy.")
    else:
        print("Neznámý příkaz, prosím zkuste to znovu.")
    
    return tasks

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")  # Vyčistění obrazovky
    print("\n=== ToDo List Manager - aktuální seznam úkolů ===")
    tasks = load_tasks()
    list_tasks(tasks)

    while True:
        print("\n=== ToDo List Manager ===")
        print("Příkazy: 'add', 'list', 'remove', 'complete', 'edit', 'save', 'exit'")
        command = input("Zadejte příkaz: ").strip().lower()
        if command == "exit":
            save_tasks(tasks)
            print("Úkoly byly uloženy. Ukončuji aplikaci.")
            break
        else:
            tasks = main(tasks, command)
