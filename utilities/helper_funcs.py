import os
import time


def clear() -> None:
    """Clears the terminal input"""
    os.system("clear")


def resolve_action() -> None:
    """Function to resolve input from user"""
    time.sleep(0.6)
    input("Press any key to continue: ")
    clear()