# import from rich library for draw tables

from rich.console import Console
from rich.table import Table

from google_sheets_api import (
    add_user_to_base,
    check_user_name,
    check_user_name_entering,
    create_user_tasks_page,
)
from utils import clear, close_app, hash_password, sleep

# Default user name
user_name = "Dear User"


def print_tasks(tasks_lst: list):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Number", style="dim", width=12)
    table.add_column("Tasks")
    table.add_column("Date", justify="right")
    for count, el in enumerate(tasks_lst, start=1):
        table.add_row(f"{count:02}", f'{el["task"]}', f'{el["time_stamp"]}')
    console.print(table)


def sign_in_screen():
    clear()
    try:
        while True:
            clear()
            print("Enter your reg name:\n")
            uname = input()
            res = check_user_name_entering(uname)
            if not res["bool"]:
                print(f"{res['msg']}")
                sleep(3)
                continue
            res = check_user_name(res["msg"])
            if not res["bool"]:
                print(f"{res['msg']}")
                sleep(3)
                continue
            return res["msg"]
    except KeyboardInterrupt:
        print(f"Bye {user_name}")
        sleep(3)
        close_app()


def log_in_screen(user_name):
    print("HELLO I AM LOG IN")


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
                sleep(2)
                return True
            elif is_in_system in "nN":
                print("You need to register.")
                sleep(2)
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
    global user_name
    user_in_system = welcome_screen(user_name)
    try:
        if user_in_system:
            log_in_screen(user_name)
        else:
            user_name = sign_in_screen()
            user_pw = input("Enter password")
            hashed_pw = hash_password(user_pw)
            add_user_to_base(user_name, hashed_pw)
            create_user_tasks_page(user_name)
    except KeyboardInterrupt:
        print(f"Bye {user_name}")

    # try:
    #     # except KeyboardInterrupt:
    #     #     print(f"Bye {user_name}")

    #     # Check username
    #     # try:
    #     while True:
    #         print("Please enter your name:")
    #         user_name = input()
    #         if_user_exist = check_user_name(user_name)["bool"]
    #         break
    #     # except KeyboardInterrupt:
    #     #     print(f"Bye {user_name}")

    #     # Show menu
    #     # try:
    #     while True:
    #         # user_name = "test"
    #         all_tasks = show_tasks(user_name)
    #         clear()
    #         print_tasks(all_tasks)
    #         print("Enter your chose:")
    #         print(
    #             "(A)dd task",
    #             "Show (T)asks",
    #             "(E)dit task",
    #             "(D)elete task",
    #             "(Q)uit",
    #             sep=" |",
    #         )
    #         answer = input()
    #         sleep(1)
    #         if answer in "qQ":
    #             clear()
    #             print(f"Bye {user_name}")
    #             sleep(2)
    #             break
    #         elif answer in "aA":
    #             clear()
    #             print(f"{user_name} you can add the new task\n")
    #             input_task = input()
    #             add_task(user_name, input_task)
    #             sleep(2)
    #         elif answer in "tT":
    #             print(f"{user_name} i show your tasks")
    #             all_tasks = show_tasks(user_name)
    #             clear()
    #             print_tasks(all_tasks)
    #             sleep(2)
    #         elif answer in "eE":
    #             print(f"{user_name} you can edit the task")
    #             tsk_num = input("Enter number of task to edit:")
    #             edit_task(user_name, tsk_num)
    #             sleep(2)
    #         elif answer in "dD":
    #             print(f"{user_name} you can delete the task")
    #             tsk_id = input("Enter task ID: ")
    #             delete_task(user_name, tsk_id)
    #             sleep(2)
    #         else:
    #             print("Enter correct letter")
    #             sleep(2)
    # except KeyboardInterrupt:
    #     print(f"Bye {user_name}")


if __name__ == "__main__":
    main()
