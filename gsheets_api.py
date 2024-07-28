from time import sleep

import gspread
from google.oauth2.service_account import Credentials

from config import SLEEP_TIME

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


def update_cell(user_name: str, row: int, col: int, data: str):
    """Update a specific cell."""
    ws = SHEET.worksheet(user_name)
    ws.update_cell(row, col, data)


def delete_task(user_name: str, task_num: str):
    """Deleting a task by number"""
    ws = SHEET.worksheet(user_name)
    row_num = int(task_num) + 1
    ws.delete_rows(row_num)


def check_edit_enter(user_name: str, task_num: str) -> dict:
    """Check the task number entered by the user"""
    tasks_quantity = len(show_tasks(user_name))

    if not task_num.isnumeric():
        return {"bool": False, "msg": "Please enter only number"}

    if int(task_num) > tasks_quantity:
        return {
            "bool": False,
            "msg": f"The number should not be larger {tasks_quantity}",
        }
    return {"bool": True, "msg": task_num}


def edit_task(user_name: str, task_num: str):
    """Edit the task function"""

    ws = SHEET.worksheet(user_name)
    row_data = ws.row_values(int(task_num) + 1)
    cell = ws.find(row_data[2])
    changed_data = input("Enter your new task text: ")
    update_cell(user_name, cell.row, 1, changed_data)
    sleep(SLEEP_TIME)


def show_tasks(user_name: str) -> list:
    """Show the user tasks"""
    ws = SHEET.worksheet(user_name)
    return ws.get_all_records()


def worksheet_append_row(ws_name: str, row: list):
    """Add the new row with task to the user worksheet list"""
    ws = SHEET.worksheet(ws_name)
    ws.append_row(row)


def add_user_to_base(user_name: str, user_password: str, user_role="user"):
    """
    Function add the new user to the users base
    """
    user = [user_name, user_password, user_role]
    worksheet_append_row("users", user)


def check_user_name(user_name: str) -> dict:
    """
    Function check if user name exist in base
    """
    ws = SHEET.worksheet("users")
    users = ws.col_values(1)[1:]
    if user_name in users:
        return {
            "bool": False,
            "msg": "Sorry this name exist in base. Try other name.",
        }
    return {"bool": True, "msg": user_name}


def check_user_password(user_name: str, user_password: str) -> dict:
    """"""
    ws = SHEET.worksheet("users")
    lst = ws.get_all_values()
    for el in lst:
        if (el[0] == user_name) and (el[1] == user_password):
            return {"bool": True, "msg": "Login and password is correct"}
    return {"bool": False, "msg": "Login or password isn't correct"}


def create_user_tasks_page(name: str):
    """
    Create a own worksheet for each user
    """
    user_wsp = SHEET.add_worksheet(title=name, rows=1, cols=2)
    user_wsp.append_row(["task", "time_stamp", "id"])


def add_task(user_name: str, new_task: dict):
    """Add the task to user worksheet page"""
    task = new_task["task"]
    time = new_task["time"]
    gen_id = new_task["id"]
    user_task = [task, time, gen_id]
    worksheet_append_row(user_name, user_task)


def check_user_name_entering(user_name: str) -> dict:
    """
    Input user name. Check if user enter not empty string.
    """
    if len(user_name) > 30:
        return {
            "bool": False,
            "msg": "The length cannot be more than 30 characters",
        }

    if len(user_name) < 1:
        return {"bool": False, "msg": "The length cannot be empty string"}

    for char in user_name:
        if (
            char
            not in """
            aAbBcCdDeEfFgGhHiIgGkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890_
            """
        ):
            return {
                "bool": False,
                "msg": """
                The login must contain letters, numbers and an underscore""",
            }
    return {"bool": True, "msg": user_name}
