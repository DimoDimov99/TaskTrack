import os
from time_handler import time_to_num, display_time
from datetime import datetime
from utilities.helper_funcs import clear, resolve_action
from utilities.commands import DAYS_OF_WEEK
from utilities.delimiters import BIG_DELIMITER, ULTRA_BIG_DELIMITER


HOME_PATH = os.getcwd()  # get user main directory path


def display_work_directory_txt_files() -> None:
    """Function to display all txt files inside the current directory"""
    txt_files = []
    for x in os.listdir():
        if x.endswith(".txt"):
            txt_files.append(x)
    if len(txt_files) > 0:
        print("All txt files:")
        for txt in txt_files:
            print(txt)


def list_all_dirs() -> None:
    """Function to display all directories inside the current directory"""
    folder = os.getcwd()
    subfolders = [f.name for f in os.scandir(folder) if f.is_dir() and f.name in DAYS_OF_WEEK]
    print("All directories: ")
    for folders in subfolders:
        print(folders)


def display_working_dir() -> None:
    """Displaying current working directory"""
    print(f"current working directory is: {os.getcwd()}")


def write_task_to_file() -> None:  # helper function now!
    """Write the given task to txt file"""
    clear()
    text_file_name = datetime.today().strftime("%A")
    text_file_name += "_work_done.txt"  # extension
    work_beginning = input("Beginning of the day (Y/N)?: ")
    if work_beginning.lower() == "y":
        delimiter()
    elif work_beginning.lower() == "n":
        print("Delimiter not addded!")
    else:
        print("Invalid input please double check!")
        return -1
    user_input = input("Please enter the task you are working on: ")
    activity_begin = input(f"Begin the task: [{user_input}]: Y/N ? : ")
    if activity_begin.lower() == "y":
        begin_time = datetime.now().strftime('%H:%M:%S')
        begin_time_int = time_to_num(begin_time)
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Activity -> [{user_input}] is started at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}] | ")
        activity_end = input(
            f"Done with the current task [{user_input}]: Y/N ? : ")
    elif activity_begin.lower() == "n":
        print(f"Activity [{user_input}] aborted!")
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Activity -> [{user_input}] is ABORTED at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}]")
            file.write("\n")
            file.write(ULTRA_BIG_DELIMITER)
            file.write("\n")
        return -1
    elif activity_begin.lower() != "n" and activity_begin.lower() != "y":
        print("Invalid input please double check!")
        return -1
    if activity_end.lower() == "y":
        end_time = datetime.now().strftime('%H:%M:%S')
        end_time_int = time_to_num(end_time)
        result = end_time_int - begin_time_int
        print(f"Task finished! Activity duration: [ {display_time(result)} ]")

        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"[FINISHED at {datetime.now().strftime('%B %d %Y %H:%M:%S')}] [{user_input}] took [{display_time(result)}]")
            file.write("\n")
            file.write(ULTRA_BIG_DELIMITER)
            file.write("\n")
    elif activity_end.lower() == "n":
        print(f"Task [ {user_input} ] aborted!")
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"ABORTED at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}]")
            file.write("\n")
            file.write(ULTRA_BIG_DELIMITER)
            file.write("\n")
    elif activity_end.lower() != "y" and activity_end.lower() != "n":
        print("Invalid input please double check!")
        return -1
    work_ending = input("End of the day (Y/N)?: ")
    if work_ending.lower() == "y":
        delimiter()
    elif work_ending.lower() == "n":
        print("delimiter not addded!")
    else:
        print("Invalid input please double check!")
        return -1


def dir_creation() -> None:
    """Switch to the daily work directory. If directory does not exist, it creates one"""
    current_path = os.getcwd()
    print(current_path)
    if current_path != HOME_PATH:
        os.chdir(HOME_PATH)
        current_path = HOME_PATH
    current_day = datetime.today().strftime("%A")
    destination_path = f"{current_path}/{current_day}"
    if current_day and os.path.exists(destination_path):
        os.chdir(destination_path)
        write_task_to_file()
    else:
        os.makedirs(destination_path)
        os.chdir(destination_path)
        write_task_to_file()


def list_tasks() -> None:
    clear()
    """Listing all tasks in .txt file in certain directory"""
    default_path = os.getcwd()
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    list_all_dirs()
    print(BIG_DELIMITER)
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    clear()
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    display_work_directory_txt_files()
    txt_input = input("Which txt file woud you like to list: ")
    txt_input += ".txt"
    try:
        clear()
        with open(txt_input, "rt", encoding="utf8") as task_file:
            lines = task_file.readlines()
            if len(lines) == 0:
                print("The file is empty")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Looks like the file {txt_input} does not exist!")



def save_info() -> None:
    """Saves the content of a given .txt file to a txt file"""
    default_path = os.getcwd()
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    clear()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    display_work_directory_txt_files()
    filename = input(
        "Enter the filename that you want to copy the information: ")
    filename += ".txt"
    new_filename = input("Enter the name of the file, where the information will be saved: ")
    new_filename += ".txt"
    try:
        with open(filename, "r", encoding="utf8") as file:
            with open(new_filename, "a", encoding="utf8") as saved_info:
                for line in file:
                    saved_info.write(line)
            print(
                f"Succesfuly saved the content of {filename} saved into {new_filename} inside: {os.getcwd()}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist!")


def print_found_hours() -> None:
    """Print the tasks done for given Month/Day"""
    default_path = os.getcwd()  # better naming
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    clear()
    list_all_dirs()
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.capitalize()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    clear()
    display_work_directory_txt_files()
    check_phrase_month = input("For which month you want to check?: ")
    check_phrase_day = input("For which day you want to check?: ")
    check_phrase_year = input("For wtich year you want to check: ")
    phrase = f"FINISHED at {check_phrase_month.capitalize()} {check_phrase_day} {check_phrase_year}"
    filename = input("Enter the filename you need to check working hours: ")
    filename += ".txt"
    info = []
    if os.path.isfile(f"{filename}"):
        """Print the lines in the file that contains the given phrase."""
        with open(filename, "r") as file:
            clear()
            for line in file:
                if phrase in line:
                    print(line.replace("\n", ""))
                    info.append(line)
                    print(100 * "-")
            prompt = input("Do you want to save this information (Y/N)?: ")
            if prompt.lower() == "y":
                location = os.getcwd()
                os.chdir(location)
                filename_with_worked_hours = f"{check_phrase_month}_{check_phrase_day}_{check_phrase_year}.txt"
                with open(filename_with_worked_hours, "a", encoding="utf8") as file:
                    for i in info:
                        file.write(i)
                        file.write(ULTRA_BIG_DELIMITER)
                        file.write("\n")
                print("Information saved!")
            else:
                print("Information not saved!")
    else:
        print(f"The file {filename} does not exist!")
        return -1


def delimiter():
    """Add delimiter to given work file"""
    text_file_name = datetime.today().strftime("%A")
    text_file_name += "_work_done.txt"  # extension
    current_day = datetime.now().strftime("%A")
    current_day_of_month = datetime.now().strftime("%B")
    current_month = datetime.now().strftime("%d")
    current_year = datetime.now().strftime("%Y")
    with open(text_file_name, "a", encoding="utf8") as file:
        file.write(
            f"{current_day} [{current_day_of_month} {current_month} {current_year}]".center(100, "="))
        file.write("\n")
        print("Delimiter added!")