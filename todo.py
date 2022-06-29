from database import todo_db
from utilities.delimiters import BIG_DELIMITER, MEDIUM_DELIMITER, ULTRA_BIG_DELIMITER
from utils import clear
from utilities.commands import TODO_COMMANDS
from utilities.helper_funcs import clear, resolve_action


def todo_menu():
    clear()
    todo_db.create_todo_table()
    user_input = input(TODO_COMMANDS)
    while user_input != 'quit':
        if user_input == 'add':
            clear()
            insert_todo()
        elif user_input == 'list':
            clear()
            list_todos()
        elif user_input == 'done':
            clear()
            todo_db.mark_todo_finished()
        elif user_input == 'not finished':
            clear()
            todo_db.mark_todo_not_finished()
        elif user_input == 'delete':
            clear()
            prompt_delete_todo()
        else:
            clear()
            print("Invalid command!")
        user_input = input(TODO_COMMANDS)
    if user_input == "quit":
        clear()
        print("[Quting the todo app and resolving to TaskTrack app...]")


def insert_todo():
    print("All currently available todos: ")
    for todo in todo_db.get_all_todos():
        print(todo['todo_name'])
        print(MEDIUM_DELIMITER)
    todo_name = input("Enter Todo: ")
    todo_db.insert_todo(todo_name)
    resolve_action()


def list_todos():
    all_todos = []
    clear()
    for todo in todo_db.get_all_todos():
        all_todos.append(todo)
    if len(all_todos) == 0:
        print("No available Todos!")
        resolve_action()
        return -1
    for todo in todo_db.get_all_todos():
        finished = 'Done' if todo['finished'] else 'Not done'
        print(
            f"[TODO]: {todo['todo_name']}\
 [DAY]: {todo['current_day']}\
 [CREATED AT]: {todo['current_time']}\
 [STATUS]: {finished}\n{BIG_DELIMITER}\n\
[LAST UPDATED] [{todo['time_stamp']}]")
        print(BIG_DELIMITER)
    resolve_action()


def prompt_delete_todo():
    all_todos = []
    print("All current todos: ")
    for todo in todo_db.get_all_todos():
        finished = 'Done' if todo['finished'] else 'Not done'
        print(f"TODO: [{todo['todo_name']}] STATUS: [{finished}]")
        print(f"{MEDIUM_DELIMITER}")
        all_todos.append(todo['todo_name'])
    if len(all_todos) == 0:
        print("No available todos!")
        resolve_action()
        return -1
    name = input('Enter the name of the todo you wish to delete: ')
    for t in all_todos:
        if name not in all_todos:
            print(
                f"Sorry, the todo '{name}' does not exist! Please double check")
            return -1
    else:
        todo_db.delete_todo(name)
        print(f"The todo: [{name}] is succesfuly deleted!")
        resolve_action()
