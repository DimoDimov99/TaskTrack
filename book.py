from database import book_db
from utilities.helper_funcs import clear, resolve_action
from utilities.commands import BOOK_COMMANDS
from utilities.delimiters import MEDIUM_DELIMITER, BIG_DELIMITER


def book_menu():
    clear()
    book_db.create_book_table()
    user_input = input(BOOK_COMMANDS)
    while user_input != 'quit':
        if user_input == 'add':
            clear()
            insert_book()
        elif user_input == 'list':
            clear()
            list_books()
        elif user_input == 'done':
            clear()
            book_db.mark_book_finished()
        elif user_input == 'not finished':
            clear()
            book_db.mark_book_not_finished()
        elif user_input == 'delete':
            clear()
            prompt_delete_book()
        elif user_input == 'update page':
            clear()
            book_db.update_book_page()
        else:
            clear()
            print("Invalid command!")
        user_input = input(BOOK_COMMANDS)
    if user_input == "quit":
        clear()
        print("[Quting the book app and resolving to TaskTrack app...]")


def insert_book():
    print("All currently available books: ")
    for book in book_db.get_all_books():
        print(f"{book['book_name']} by {book['book_author']}")
        print(MEDIUM_DELIMITER)
    book_name = input("Enter book: ")
    book_author = input("Enter book author: ")
    book_db.insert_book(book_name, book_author)
    resolve_action()


def list_books():
    all_books = []
    for book in book_db.get_all_books():
        all_books.append(book)
    if len(all_books) == 0:
        print("No available books!")
        resolve_action()
        return -1
    for book in book_db.get_all_books():
        finished = 'FINISHED' if book['finished'] else 'NOT FINISHED'
        is_finished = book['current_page'] = 'FINISHED' if book['finished'] else book['current_page']
        print(
            f"Book: {book['book_name']} from Author: {book['book_author']} is addded at: {book['current_time']}\
 current page: [PAGE {is_finished}]\
 [STATUS]: [{finished}]\n{BIG_DELIMITER}\n\
[LAST UPDATED]: [{book['time_stamp']}]")
        print(BIG_DELIMITER)
    resolve_action()


def prompt_delete_book():
    all_books = []
    print("All current books: ")
    for book in book_db.get_all_books():
        print(f"Book: {book['book_name']} by author: {book['book_author']}")
        print(BIG_DELIMITER)
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No available books!")
        resolve_action()
        return -1
    name = input('Enter the name of the book you wish to delete: ')
    for _ in all_books:
        if name not in all_books:
            print(
                f"Sorry, the book '{name}' does not exist! Please double check")
            resolve_action()
            return -1
    else:
        book_db.delete_book(name)
        print(f"The book: [{name}] is succesfuly deleted!")
        resolve_action()
