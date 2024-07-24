# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# import only system from os
# To hash password
import hashlib

# import sleep to show output for some time period
import time
from os import name, system

import gspread
from google.oauth2.service_account import Credentials

# import from rich library for draw tables
from rich.console import Console
from rich.table import Table

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

# Default user name
DEFAULT_USERNAME = "Dear User"


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
    if user_name in users:
        print("Sorry the name is exist. Try other name.\n")
        return False
    return True


def worksheet_append_row(ws_name: str, row: list):
    ws = SHEET.worksheet(ws_name)
    ws.append_row(row)


def add_user_to_base(user_name: str, user_password: str, user_role="user"):
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
    user_wsp = SHEET.add_worksheet(title=name, rows=1, cols=2)
    user_wsp.append_row(["task", "time_stamp"])


def add_task(user_name: str, task: str):
    time = time_stamp()
    gen_id = gen_task_id()
    user_task = [task, time, gen_id]
    return worksheet_append_row(user_name, user_task)


def gen_task_id():
    # Generate a timestamp-based ID
    gen_id = str(int(time.time()))
    return gen_id


def delete_task(user_name: str, task_num: str):
    ws = SHEET.worksheet(user_name)
    row_num = int(task_num) + 1
    ws.delete_rows(row_num)


def print_tasks(tasks_lst: list):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Number", style="dim", width=12)
    table.add_column("Tasks")
    table.add_column("Date", justify="right")
    for count, el in enumerate(tasks_lst, start=1):
        table.add_row(f"{count:02}", f'{el["task"]}', f'{el["time_stamp"]}')
    # for count, el in enumerate(tasks_lst, start=1):
    #     print(f"| {count:02} | {el['task']}  | {el['time_stamp']} |")
    console.print(table)


def time_stamp():
    time_now = time.localtime()
    return time.strftime("%Y-%m-%d", time_now)


def show_tasks(user_name: str) -> list:
    ws = SHEET.worksheet(user_name)
    return ws.get_all_records()


def sleep(sec):
    time.sleep(sec)


def edit_task(user_name: str, task_num: str):
    ws = SHEET.worksheet(user_name)
    row_data = ws.row_values(int(task_num) + 1)
    print(row_data)
    print(row_data[2])
    cell = ws.find(row_data[2])
    changed_data = input()
    update_cell(ws, cell.row, 1, changed_data)
    sleep(10)


def update_cell(ws, row: int, col: int, data: str):
    ws.update_cell(row, col, data)


def check_user_name_entering(user_name):
    """
    Input user name. Check if user enter not empty string.
    """
    if len(user_name) > 30:
        return {"bool": False, "msg": "The length cannot be more than 30 characters"}
    for char in user_name:
        if (
            char
            not in "aAbBcCdDeEfFgGhHiIgGkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890_"
        ):
            return {
                "bool": False,
                "msg": "The login must contain letters, numbers and an underscore",
            }
    return {"bool": True, "msg": user_name.strip()}


def add_new_user(user_name):
    pass


def welcome_screen(user_name):
    """
    The function checks whether the user is in the system.
    If the user is logged in, it returns True.
    If omitted, the function returns False.
    If a character different from N or Y is entered, an error is displayed to the user.
    """
    try:
        while True:
            clear()
            print("Are you registered? (Y)es or (N)o:")
            is_in_system = input()
            if is_in_system in "yY":
                print("Greetings. Welcome back. Please enter your name.")
                return True
            elif is_in_system in "nN":
                print("You need to register.")
                return False
            else:
                print("Wrong answer. Please enter Y or N.")
                sleep(3)
    except KeyboardInterrupt:
        print(f"Bye {user_name}")


def main():
    """
    Main function. It runs all other functions
    """
    clear()
    user_name = DEFAULT_USERNAME
    user_in_system = welcome_screen(user_name)
    if user_in_system:
        pass
    else:
        pass
    try:
        # except KeyboardInterrupt:
        #     print(f"Bye {user_name}")

        # Check username
        # try:
        while True:
            print("Please enter your name:")
            user_name = input()
            if_user_exist = check_user_name(user_name)
            break
        # except KeyboardInterrupt:
        #     print(f"Bye {user_name}")

        # Show menu
        # try:
        while True:
            # user_name = "test"
            all_tasks = show_tasks(user_name)
            clear()
            print_tasks(all_tasks)
            print("Enter your chose:")
            print(
                "(A)dd task",
                "Show (T)asks",
                "(E)dit task",
                "(D)elete task",
                "(Q)uit",
                sep=" |",
            )
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
                tsk_num = input("Enter number of task to edit:")
                edit_task(user_name, tsk_num)
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
