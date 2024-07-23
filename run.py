# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# import only system from os
# To hash password
import hashlib
from os import name, system

# import sleep to show output for some time period
from time import sleep

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open used google sheets document
SHEET = GSPREAD_CLIENT.open("stodo")


# define our clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def check_user_name(user_name: str) -> bool:
    """
    Function check if user name exist in base
    """
    wks = SHEET.worksheet("users")
    users = wks.col_values(1)[1:]
    if user_name not in users:
        print("Sorry need other name")
        return True
    return False


def add_user(user_name: str, user_password: str, user_role="user"):
    """
    Function add the new user to the users base
    """
    wks = SHEET.worksheet("users")
    user = [user_name, user_password, user_role]
    wks.append_row(user)


def hash_password(password: str) -> str:
    """
    Function hash user password and return hashed password
    """
    # Hash the password
    pw = hashlib.sha256(password.encode("utf-8"))
    return pw.hexdigest()


def check_user_password(user_name: str, user_password: str) -> bool:
    wks = SHEET.worksheet("users")
    lst = wks.get_all_values()
    for el in lst:
        if (el[0] == user_name) and (el[1] == user_password):
            return True
    return False


def create_user_tasks_page(name: str):
    SHEET.add_worksheet(title=name, rows=100, cols=5)


def delete_user_tasks_page(name):
    SHEET.del_worksheet(name)


def add_task(task):
    pass


def delete_task(task_id: int):
    pass


def show_tasks():
    pass


def edit_task():
    pass


def show_closed_tasks():
    pass


def show_active_tasks():
    pass


def main():
    """
    Main function. Starts
    """
    clear()
    print("Please enter your name:")
    user_name = input()
    while True:
        # clear()
        print("Enter your chose:")
        print("(F) TEST FUNCTIONS")
        print("(A) Add task")
        print("(T) Show Tasks")
        print("(E) Edit task")
        print("(D) Delete task")
        print("(Q) Quit")
        answer = input()
        sleep(1)
        if answer in "qQ":
            clear()
            print(f"Bye {user_name}")
            sleep(2)
            break
        elif answer in "fF":
            pw = hash_password()
            print(pw)
            add_user(user_name, pw)
            print(check_user_password(user_name, pw))
            # create_user_tasks_page(user_name)
            # delete_user_tasks_page("id:1271026672")
            sleep(10)
        elif answer in "aA":
            print(f"{user_name} you can add the task")
            sleep(2)
        elif answer in "tT":
            print(f"{user_name} i show you your tasks")
            sleep(2)
        elif answer in "eE":
            print(f"{user_name} you can edit the task")
            sleep(2)
        elif answer in "dD":
            print(f"{user_name} you can delete the task")
            sleep(2)
        else:
            print("Enter correct letter")
            sleep(2)


main()
