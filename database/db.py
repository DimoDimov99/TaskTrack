from multiprocessing import connection
import sqlite3
from datetime import datetime

from utils import current_time


def create_todo_table():
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS todos(todo_name text primary key, current_day text, current_time text, finished integer, time_stamp text)")

    connection.commit()
    connection.close()


def get_all_todos():
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM todos")
    # [(name, author, read), (name, author, read)]
    todo = [{"todo_name": row[0], "current_day": row[1], "current_time": row[2], "finished": row[3], "time_stamp": row[4]}
            for row in cursor.fetchall()]
    connection.close()
    return todo


def mark_todo_finished():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("todo_data.db")
    all_todos = []
    print("All current todos:\n")
    for todo in get_all_todos():
        print(f"[ {todo['todo_name']} ]")
        all_todos.append(todo['todo_name'])
    if len(all_todos) == 0:
        print("No todos!!!. Quiting")
        return -1
    print("---------------------------\n")
    cursor = connection.cursor()
    user_input = input(
        "Enter the name of the todo you want to mark as finished: ")
    check = cursor.execute(
        "SELECT * FROM todos WHERE todo_name=?", (user_input,))
    is_in_todos = list(check)
    if is_in_todos:
        print(f"The todo [{user_input}] is found! Updating it's status!")
        cursor.execute(
            f"UPDATE todos SET finished='1' WHERE todo_name=?", (
                user_input,))
        cursor.execute(
            f"UPDATE todos SET time_stamp=? WHERE todo_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided todo [{user_input}] is not presented in the todos, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def mark_todo_not_finished():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    all_todos = []
    print("All current todos:\n")
    for todo in get_all_todos():
        print(f"[ {todo['todo_name']} ]")
        all_todos.append(todo['todo_name'])
    if len(all_todos) == 0:
        print("No todos!!!. Quiting")
        return -1
    print("---------------------------\n")
    user_input = input(
        "Enter the name of the todo you want to mark as unfinished: ")
    check = cursor.execute(
        "SELECT * FROM todos WHERE todo_name=?", (user_input,))
    is_in_todos = list(check)
    if is_in_todos:
        print(f"The todo [{user_input}] is found! Update his status!")
        cursor.execute(
            "UPDATE todos SET finished='0' WHERE todo_name=?", (user_input,))
        cursor.execute(
            f"UPDATE todos SET time_stamp=? WHERE todo_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided todo [{user_input}] is not presented in the todos, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def insert_todo(todo_name):
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    current_day = datetime.now().strftime("%A")
    # ",0); DROP TABLE books;
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    try:
        # time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        cursor.execute("INSERT INTO todos VALUES(?, ?, ?, 0, ?)",
                       (todo_name, current_day, current_time, ""))
        print("The todo is successfully added!")
    except sqlite3.IntegrityError:
        print(f"The todo {todo_name} already exist!")
    connection.commit()
    connection.close


def delete_todo(name):
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos WHERE todo_name=?", (name,))
    connection.commit()
    connection.close()

############################ Books ################################


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
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    print("All current books:\n")
    for book in get_all_books():
        print(f"[ {book['book_name']} ]")
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No books!!!. Quiting")
        return -1
    print("---------------------------\n")
    user_input = input(
        "Enter the name of the book you want to mark as finished: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book [{user_input}] is found! Updating it's status!")
        cursor.execute(
            f"UPDATE books SET finished='1' WHERE book_name=?", (
                user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided book [{user_input}] is not presented in the books list, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def update_book_page():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    print("All current books:\n")
    for book in get_all_books():
        print(f"[ {book['book_name']} ]")
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No books!!!. Quiting")
        return -1
    print("---------------------------\n")
    user_input = input(
        "Enter the name of the book you want to update page/s read: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book [{user_input}] is found!")
        pages_read = int(input("Enter the page you are currently at: "))
        cursor.execute(
            f"UPDATE books SET current_page='{pages_read}' WHERE book_name=?", (
                user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
        print(f"The book [{user_input}] has been successfully updated!")
    else:
        print(
            f"Sorry the provided book [{user_input}] is not presented in the books list, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def mark_book_not_finished():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("book_data.db")
    cursor = connection.cursor()
    all_books = []
    print("All current books:\n")
    for book in get_all_books():
        print(f"[ {book['book_name']} ]")
        all_books.append(book['book_name'])
    if len(all_books) == 0:
        print("No books!!!. Quiting")
        return -1
    print("---------------------------\n")
    user_input = input(
        "Enter the name of the book you want to mark as unfinished: ")
    check = cursor.execute(
        "SELECT * FROM books WHERE book_name=?", (user_input,))
    is_in_books = list(check)
    if is_in_books:
        print(f"The book [{user_input}] is found! Update his status!")
        cursor.execute(
            "UPDATE books SET finished='0' WHERE book_name=?", (user_input,))
        cursor.execute(
            f"UPDATE books SET time_stamp=? WHERE book_name=?", (current_time, user_input))
    else:
        print(
            f"Sorry the provided book [{user_input}] is not presented in the books list, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def insert_book(book_name, book_author):
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
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


############################ Books ################################
