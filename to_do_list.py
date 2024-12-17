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

def list_tasks(tasks):
    print("ID | ÚKOL | PRIORITA | TERMÍN DOKONČENÍ | STAV ")
    for task in tasks:
        print(f"{task['id']}|{task['name']}|{task['priority']}|{task['deadline']}|{"Ano" if task["state"] == True else "Ne"}")

def add_command(tasks):
    # načtu si potřebné údaje od uživatele
    task_id = max([task["id"] for task in tasks]) + 1 # id pridaneho tasku bude vzdy o 1 vetsi nez je nejvetsi id
    name = input("Zadejte název úkolu: ")
    importance = input("Zadejte jak důležitý je úkol (Vysoká, Střední, Nízká)")
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
    
        

def main():
    tasks = load_tasks()

    print("=== To Do List Manager - aktuální seznam úkolů ===")
    list_tasks(tasks)
       
    # kod...

    # uložit úkoly
  

    

if __name__ == "__main__":
    os.system("cls")
    main()