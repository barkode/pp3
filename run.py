# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# import only system from os
# To hash password
import hashlib
from datetime import datetime
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


def clear():
    """Clear screen"""
    # for windows
    system("cls") if name == "nt" else system("clear")


def check_user_name(user_name: str) -> bool:
    """
    Function check if user name exist in base
    """
    ws = SHEET.worksheet("users")
    users = ws.col_values(1)[1:]
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
    ws = SHEET.worksheet("users")
    lst = ws.get_all_values()
    for el in lst:
        if (el[0] == user_name) and (el[1] == user_password):
            return True
    return False


def create_user_tasks_page(name: str):
    """
    Create a worksheet for each user
    """
    user_wsp = SHEET.add_worksheet(title=name, rows=1, cols=3)
    user_wsp.append_row(["task", "time_stamp", "id"])


def add_task(user_name: str, task: str):
    time = time_stamp()
    gen_id = gen_task_id(user_name)
    print(time)
    user_task = [task, time, gen_id]
    return worksheet_append_row(user_name, user_task)


def gen_task_id(user_name):
    ws = SHEET.worksheet(user_name)
    cell = ws.find("id")
    gen_id = len(ws.col_values(cell.col))
    return gen_id


def delete_task(user_name: str, task_id: str):
    ws = SHEET.worksheet(user_name)
    cell = ws.find(task_id)
    ws.delete_rows(cell.row)


def print_tasks(tasks_lst: list):
    for count, el in enumerate(tasks_lst, start=1):
        print(f"| {count:02} | {el['task']}  | {el['time_stamp']} | {el['id']} |")


def time_stamp():
    dn = datetime.now()

    return dn.strftime("%Y-%m-%d")


def show_tasks(user_name: str) -> list:
    ws = SHEET.worksheet(user_name)
    return ws.get_all_records()


def edit_task(user_name: str, task_id: str):
    ws = SHEET.worksheet(user_name)
    cell = ws.find(task_id)
    print(f"{cell.value} change to: ")
    changed_data = input()
    update_cell(ws, cell.row, 1, changed_data)


def update_cell(ws, row: int, col: int, data: str):
    ws.update_cell(row, col, data)


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
    user_name = "Dear user"
    try:
        while True:
            # print("Please enter your name:")
            # user_name = input()
            user_name = "test"
            all_tasks = show_tasks(user_name)
            clear()
            print_tasks(all_tasks)
            print("Enter your chose:")
            print(
                "(A)dd task", "Show (T)asks", "(E)dit task", "(D)elete task", "(Q)uit"
            )
            # print("Show (T)asks")
            # print("(E)dit task")
            # print("(D)elete task")
            # print("(Q)uit")
            answer = input()
            sleep(1)
            if answer in "qQ":
                clear()
                print(f"Bye {user_name}")
                sleep(2)
                break
            elif answer in "aA":
                clear()
                print(f"{user_name} you can add the new task\n")
                input_task = input()
                add_task(user_name, input_task)
                sleep(2)
            elif answer in "tT":
                print(f"{user_name} i show your tasks")
                all_tasks = show_tasks(user_name)
                clear()
                print_tasks(all_tasks)
                sleep(2)
            elif answer in "eE":
                print(f"{user_name} you can edit the task")
                sleep(2)
            elif answer in "dD":
                print(f"{user_name} you can delete the task")
                tsk_id = input("Enter task ID: ")
                delete_task(user_name, tsk_id)
                sleep(2)
            else:
                print("Enter correct letter")
                sleep(2)
    except KeyboardInterrupt:
        print(f"Bye {user_name}")


main()
