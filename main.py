from book import book_menu
from todo import todo_menu
from utilities.helper_funcs import clear
from utilities.commands import print_commands
from utils import *


def main():
    """Entry function of the program"""
    if user_input == "track":
        dir_creation()
    elif user_input == "list":
        list_tasks()
    elif user_input == "clear":
        clear()
    elif user_input == "save":
        save_info()
    elif user_input == "commands":
        print_commands()
    elif user_input == "hours check":
        print_found_hours()
    elif user_input == "todo":
        todo_menu()
    elif user_input == "book":
        book_menu()
    else:
        print("Invalid input")


if __name__ == "__main__":
    print("Welcome to TaskTrack!")
    print(f"To see all available commands, type 'commands'!")
    user_input = input("Choose a command to begin: ").lower()
    while user_input != "quit":
        clear()
        main()
        user_input = input("Choose a command to begin: ").lower()
    print("Quiting the app...")
