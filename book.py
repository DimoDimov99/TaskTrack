from database import db
from utils import clear
import time


USER_CHOICE = """
Enter:
- 'add' to add a new book
- 'list' to list all book/s
- 'done' to mark a book as done
- 'not finished' to mark a book as not finished yet
- 'update page' to update a book page
- 'delete' to delete a book
- 'quit' to quit
Your choice: """


def book_menu():
    clear()
    db.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'quit':
        if user_input == 'add':
            clear()
            insert_book()
        elif user_input == 'list':
            clear()
            list_books()
        elif user_input == 'done':
            clear()
            db.mark_book_finished()
        elif user_input == 'not finished':
            clear()
            db.mark_book_not_finished()
        elif user_input == 'delete':
            clear()
            prompt_delete_book()
        elif user_input == 'update page':
            clear()
            db.update_book_page()
        elif user_input == 'test':
            db.test()
        user_input = input(USER_CHOICE)
    if user_input == "quit":
        print("[Quting the book app and resolving to main screen...]")
        print("\n")


def insert_book():
    book_name = input("Enter book: ")
    book_author = input("Enter book author: ")
    db.insert_book(book_name, book_author)
    # Stupid but good fix for now
    test_input = input("Resolve the program? : (Y): ")


def list_books():
    clear()
    for book in db.get_all_books():
        # book[3] will be a falsy value (0) if not read
        finished = 'Done' if book['finished'] else 'Not finished'
        is_finished = book['current_page'] = 'FINISHED' if book['finished'] else book['current_page']
        print("\n")
        print(
            f"[Book]: {book['book_name']} [Author]: {book['book_author']} [CREATED]: {book['current_time']} Current page [{book['current_page']}] — Status: [ {finished} ]\n--------------------------------------------------\n\n[LAST UPDATED] [{book['time_stamp']}]")
        print(50 * "-")
    time.sleep(0.6)
    # Stupid but good fix for now
    test_input = input("Resolve the program? : (Y): ")


def prompt_delete_book():
    all_books = []
    print("All current books:\n")
    for book in db.get_all_books():
        print(f"[ {book['book_name']} ]")
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No books!!!. Quiting")
        return -1
    print("---------------------------\n")
    name = input('Enter the name of the book you wish to delete: ')
    for b in all_books:
        if name not in all_books:
            # print(all_books)
            print(
                f"Sorry, the book '{name}' does not exist! Please double check")
            return -1
    else:
        db.delete_book(name)
        print(f"The book: [{name}] is succesfuly deleted!")
        # Stupid but good fix for now
        test_input = input("Resolve the program? : (Y): ")
