from utilities.helper_funcs import clear

BOOK_COMMANDS = """Enter:
- 'add' to add a new book
- 'list' to list all book/s
- 'done' to mark a book as done
- 'not finished' to mark a book as not finished yet
- 'update page' to update a book page
- 'delete' to delete a book
- 'quit' to quit
Your choice: """


TODO_COMMANDS = """Enter:
- 'add' to add a new todo
- 'list' to list all todo/s
- 'done' to mark a todo as done
- 'not finished' to mark a todo as not finished yet
- 'delete' to delete a todo
- 'quit' to quit
Your choice: """


task_track_commands = {
    "track": "begin to track a activity",
    "list": "list the content of selected txt file",
    "clear": "clear output in the terminal",
    "save": "save all content from txt file inside full_info.txt in the respective directory",
    "quit": "quit the application",
    "hours check": "list how much work is done for specific day",
    "todo": "trigger todo app menu",
    "book": "trigger book app menu",
}


DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def print_commands() -> None:
    """Print all available commands"""
    clear()
    print(40 * "*")
    for key, value in task_track_commands.items():
        print(f"{key} -> {value}\n")
    print(40 * "*")