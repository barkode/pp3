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

# wh = SHEET.worksheet("test")


def clear():
    """Clear screen"""
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


def worksheet_append_row(ws_name: str, row: list):
    ws = SHEET.worksheet(ws_name)
    ws.append_row(row)


def add_user(user_name: str, user_password: str, user_role="user"):
    """
    Function add the new user to the users base
    """
    user = [user_name, user_password, user_role]
    worksheet_append_row("users", user)


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
    """
    Create a worksheet for each user
    """
    user_wsp = SHEET.add_worksheet(title=name, rows=1, cols=5)
    user_wsp.append_row(["task_description", "status", "category", "time_stamp"])


# def delete_user_tasks_page(name="1"):
#     wks_lst = SHEET.worksheets()
#     print(wks_lst)
# SHEET.del_worksheet(name)


def add_task(user_name: str, task: str):
    user_task = [task, "active", "category", "time"]
    worksheet_append_row(user_name, user_task)


def delete_task(user_name: str, task_id: str):
    wh = SHEET.worksheet(user_name)
    cell = wh.find(task_id)
    wh.delete_rows(cell.row)


def print_tasks(tasks_lst: list):
    for count, el in enumerate(tasks_lst, start=1):
        print(
            f"| {count:02} | {el['task_description']} | {el['status']} | {el['category']} | {el['time_stamp']} | {el['id']} |"
        )


def show_tasks(user_name: str) -> list:
    wh = SHEET.worksheet(user_name)
    return wh.get_all_records()


def edit_task():
    # TODO document why this method is empty
    pass


def show_task_by_status(user_name: str, status: str) -> tuple:
    wh = SHEET.worksheet(user_name)
    all_records = wh.get_all_records()
    filtered_elements = tuple(
        filter((lambda el: True if el["status"] == status else False), all_records)
    )
    return filtered_elements


def enter_user_name():
    """
    User input name. Function check if the name exist.
    """
    print("Please enter your name:")
    user_name = input()

    return user_name


def main():
    """
    Main function. It runs all other functions
    """
    clear()
    # print(wh)
    # wks_id =
    # SHEET.del_worksheet_by_id("")
    # print("Hello, dear friend. Let's meet?\n")
    # print("Enter Y if you are a 'New User',\n")
    # print("or N if you are already registered.\n")
    # is_register = input()
    # if is_register in "yY":
    #     # TODO: Add implementation
    #     pass
    # elif is_register in "nN":
    #     # TODO: Add implementation
    #     pass
    # else:
    #     print("Please enter correct answer")

    # while True:
    #     print("Please enter your name:")
    #     user_name = input()
    #     print("Please enter your password:")
    #     user_password = input()

    while True:
        # clear()
        print("Please enter your name:")
        user_name = input()
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
            # pw = hash_password()
            # print(pw)
            # add_user(user_name, pw)
            # print(check_user_password(user_name, pw))
            # create_user_tasks_page(user_name)
            # add_task("test", "ththththth")
            # all_tasks = show_tasks("test")
            # print_tasks(all_tasks)
            closed_tasks = show_task_by_status("test", "close")
            print_tasks(closed_tasks)
            # open_tasks = show_task_by_status("test", "open")
            # print_tasks(open_tasks)
            delete_task("test", "34")
            # show_tasks("test")
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
