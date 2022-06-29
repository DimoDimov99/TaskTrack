import sqlite3
from datetime import datetime
from utilities.delimiters import BIG_DELIMITER
from utilities.helper_funcs import resolve_action

def create_book_table():
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books(book_name text primary key, book_author text, current_day text, current_time text, finished integer, current_page integer, time_stamp text)")

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    # [(name, author, read), (name, author, read)]
    book = [{"book_name": row[0], "book_author": row[1], "current_day": row[2], "current_time": row[3], "finished": row[4], "current_page": row[5], "time_stamp": row[6]}
            for row in cursor.fetchall()]
    connection.close()
    return book


def mark_book_finished():
    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    print("All current books: ")
    for book in get_all_books():
        print(f"Book: {book['book_name']} by author: {book['book_author']}")
        print(BIG_DELIMITER)
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No available books!")
        resolve_action()
        return -1
    user_input = input(
        "Enter the name of the book you want to mark as finished: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book '{user_input}' is found! Updating it's status!")
        cursor.execute(
            f"UPDATE books SET finished='1' WHERE book_name=?", (
                user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided book '{user_input}' is not presented in the books list, double check!")
    resolve_action()
    connection.commit()
    connection.close()


def update_book_page():
    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    for book in get_all_books():
        print(f"Book: {book['book_name']} by author: {book['book_author']}")
        print(BIG_DELIMITER)
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No available books!")
        resolve_action()
        return -1
    user_input = input(
        "Enter the name of the book you want to update page/s read: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book '{user_input}' is found!")
        pages_read = int(input("Enter the page you are currently at: "))
        cursor.execute(
            f"UPDATE books SET current_page='{pages_read}' WHERE book_name=?", (
                user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
        print(f"The book '{user_input}' has been successfully updated!")
    else:
        print(
            f"Sorry the provided book '{user_input}' is not presented in the books list, double check!")
    resolve_action()
    connection.commit()
    connection.close()


def mark_book_not_finished():
    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    for book in get_all_books():
        print(f"Book: {book['book_name']} by author: {book['book_author']}")
        print(BIG_DELIMITER)
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No available books!")
        resolve_action()
        return -1
    user_input = input(
        "Enter the name of the book you want to mark as unfinished: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book '{user_input}' is found! Update his status!")
        cursor.execute(
            "UPDATE books SET finished='0' WHERE book_name=?", (user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided book '{user_input}' is not presented in the books list, double check!")
    resolve_action()
    connection.commit()
    connection.close()


def insert_book(book_name, book_author):
    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    current_day = datetime.now().strftime("%A")
    # ",0); DROP TABLE books;
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    try:
        # time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?, 0, 0, ?)",
                       (book_name, book_author, current_day, current_time, ""))
        print(
            f"The book '{book_name}' with author '{book_author}' is successfully added!")
    except sqlite3.IntegrityError:
        print(f"The book '{book_name}' already exist!")
    connection.commit()
    connection.close


def delete_book(name):
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE book_name=?", (name,))
    connection.commit()
    connection.close()