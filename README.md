# Prg24-26_Project_02_ToDo_list_manager_app

Project_02_ToDo_list_manager_app.py

Vytvořte terminálovou aplikaci, která bude sloužit jako ToDo list. 
Aplikace umožní uživateli spravovat úkoly, ukládat je do souboru a načítat při startu aplikace. 

## Funkcionalita aplikace
* Přidání úkolu - aplikace umožní uživateli přidat nový úkol. 
  Každý úkol bude obsahovat následující vlastnosti:
        Název úkolu (povinný)
        Priorita úkolu (nízká, střední, vysoká) – volitelné, výchozí je střední.
        Termín splnění úkolu ve formátu YYYY-MM-DD (volitelné, může být prázdné).
        Status úkolu (hotovo/nehotovo), který se bude standardně nastavovat na "nehotovo" při vytvoření nového úkolu.
* Zobrazení seznamu úkolů - uživatel může zobrazit seznam všech úkolů. 
  Seznam bude obsahovat všechny úkoly s jejich vlastnostmi. Uživatel může také filtrovat úkoly podle:
        Priorit (zobrazí jen úkoly s konkrétní prioritou)
        Stavu úkolu (hotovo/nehotovo)
        Termínu splnění (úkoly s blížícím se termínem)
* Odstranění úkolu - aplikace umožní odstranit úkol ze seznamu podle ID nebo názvu.
* Označení úkolu jako dokončeného - uživatel může označit libovolný úkol jako "hotovo". 
  Tento úkol bude v seznamu označen jako dokončený, ale zůstane uložený pro případné další zobrazení.
* Editace úkolu - uživatel může změnit vlastnosti již existujícího úkolu. 
  Bude možné upravit název, prioritu, termín nebo status úkolu.
* Uložení a načtení úkolů ze souboru - při ukončení aplikace se všechny úkoly uloží do souboru 
  ve formátu CSV nebo JSON. Aplikace při spuštění tento soubor načte a pokračuje v práci s dříve uloženými úkoly.

## Formát souboru s úkoly
Seznam úkolů bude uložen v textovém souboru ve složce data, který bude mít následující strukturu:
    Každý úkol bude na jednom řádku a jednotlivé vlastnosti budou odděleny středníkem.
    Pokud nebude zadán termín, zůstane pole prázdné.

## Ukázkový soubor todo_tasks.txt:
        1;Nakoupit potraviny;Vysoká;2024-10-15;Ne
        2;Dokončit projekt;Střední;;Ne
        3;Udělat domácí úkol;Nízká;2024-10-20;Ne
        4;Zavolat babičce;Střední;;Ano

## Příkazy aplikace:
* add
  Přidání nového úkolu. Aplikace požádá uživatele o název úkolu, prioritu a termín. 
  Pokud uživatel nezadá prioritu, nastaví se střední. Termín je volitelný.
* list
  Zobrazení seznamu úkolů. Uživatel může zadat parametr pro filtrování podle priority, stavu nebo termínu.
* remove
  Odstranění úkolu. Uživatel zadá ID nebo název úkolu, který chce odstranit.
* complete
  Označení úkolu jako hotového. Uživatel zadá ID nebo název úkolu, který chce označit jako hotový.
* edit
  Umožní uživateli upravit název, prioritu, termín nebo status existujícího úkolu.
* save
  Ruční uložení změn do souboru todo_tasks.txt.
* exit
  Automatické uložení všech změn do souboru a ukončení programu.

## Struktura souborů:
* main.py
  Hlavní soubor aplikace, který bude obsahovat logiku pro zpracování příkazů.
* data/todo_tasks.txt
  Soubor s úkoly, který se bude načítat při startu aplikace a ukládat při ukončení.


## Ukázkový výpis aplikace:
        === ToDo List Manager ===
        Nápověda: použijte příkazy 'add', 'list', 'remove', 'complete', 'edit', 'save', 'exit' pro práci s úkoly.

        > add
        Zadejte název úkolu: Nakoupit potraviny
        Zadejte prioritu (Nízká, Střední, Vysoká): Vysoká
        Zadejte termín splnění (YYYY-MM-DD, volitelně): 2024-10-15
        Úkol byl přidán!

        > list
        ID | Úkol                | Priorita | Termín      | Stav
        -----------------------------------------------------------
        1  | Nakoupit potraviny   | Vysoká   | 2024-10-15  | Ne
        2  | Dokončit projekt     | Střední  |             | Ne

        > complete 1
        Úkol "Nakoupit potraviny" byl označen jako dokončený.

        > list
        ID | Úkol                | Priorita | Termín      | Stav
        -----------------------------------------------------------
        1  | Nakoupit potraviny   | Vysoká   | 2024-10-15  | Ano
        2  | Dokončit projekt     | Střední  |             | Ne

        > remove 2
        Úkol "Dokončit projekt" byl odstraněn.

        > save
        Úkoly byly uloženy do souboru.

        > exit
        Úkoly byly uloženy. Ukončuji aplikaci.

## Detailní popis jednotlivých funkcí:
* load_tasks()
  Funkce pro načtení všech úkolů z textového souboru při spuštění aplikace. Pokud soubor neexistuje, vytvoří se prázdná seznamová struktura.
* save_tasks()
  Uloží aktuální stav seznamu úkolů do souboru. Při ukončení aplikace dojde k automatickému uložení, ale uživatel může zadat příkaz save pro ruční uložení kdykoliv.
* add_task()
  Přidá nový úkol. Uživatel zadá název, prioritu a termín. Pokud není zadaný termín, pole termínu zůstane prázdné. Každý úkol je přiřazen ID, které je automaticky generováno.
* list_tasks()
  Zobrazí všechny úkoly ve formě tabulky. Uživatel může filtrovat úkoly podle priority, termínu nebo statusu (hotovo/nehotovo).
* remove_task()
  Umožňuje odstranit úkol podle ID nebo názvu.
* complete_task()
  Označí úkol jako dokončený. Uživatel zadá ID nebo název úkolu.
* edit_task()
  Umožňuje uživateli upravit název, prioritu, termín nebo status existujícího úkolu.

## Závěrečné poznámky:
Všechny změny se ukládají do souboru todo_tasks.txt, který je přístupný v podadresáři data.
Po spuštění aplikace se úkoly automaticky načtou, takže uživatel může pokračovat tam, kde skončil.
Data jsou ukládána ve formátu, který umožňuje jednoduchou editaci i mimo aplikaci (např. v textovém editoru).