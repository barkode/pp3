# import from rich library for draw tables
import pyfiglet
from rich import print as rprint
from rich.table import Table

from gsheets_api import (
    add_task,
    add_task_page,
    add_user_to_base,
    check_edit_enter,
    check_user_name,
    check_user_name_entering,
    check_user_password,
    create_user_tasks_page,
    delete_task,
    edit_task,
    show_tasks,
)
from utils import (
    clear,
    close_app,
    hash_password,
    hide_user_pass,
    print_text,
    sleep,
)

# Default user name
user_name = "Dear User"
LOGO = "stodo"
SLEEP_TIME = 2


def print_tasks(tasks_lst: list):
    """Print the table with tasks. Used the Rich library."""
    rprint(f"[green]Hello, {user_name}. Your Tasks.[/green]")
    table = Table(
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Number", style="dim", justify="center", width=12)
    table.add_column("Tasks", justify="center")
    table.add_column("Date", justify="center")
    for count, el in enumerate(tasks_lst, start=1):
        table.add_row(f"{count:02}", f'{el["task"]}', f'{el["time_stamp"]}')
    rprint(table)


def sign_in_screen():
    """Called when the user is not registered in the system.
    Shows a screen inviting the user to register with the system.
    """
    clear()
    while True:
        clear()
        print_logo(LOGO)
        print_text("Enter your login:", "yellow")
        u_login = input("Login: ")
        res = check_user_name_entering(u_login)
        if not res["bool"]:
            print_text(f"{res['msg']}", "magenta")
            sleep(SLEEP_TIME)
            continue
        res = check_user_name(res["msg"])
        if not res["bool"]:
            print_text(f"{res['msg']}", "magenta")
            sleep(SLEEP_TIME)
            continue
        return res["msg"]


def log_in_screen():
    """Shows the user login screen.
    Checks if the user and password exist in the base.
    """
    while True:
        clear()
        print_logo(LOGO)
        print_text("Input your login.", "yellow")
        u_login = input("Login: ")
        res = check_user_name_entering(u_login)
        if not res["bool"]:
            print(f"{res['msg']}")
            sleep(SLEEP_TIME)
            continue
        print_text("Input your password.", "yellow")
        u_pwd = hide_user_pass()
        h_pwd = hash_password(u_pwd)
        check = check_user_password(u_login, h_pwd)
        if check["bool"]:
            return u_login
        else:
            print_text(check["msg"], "magenta")
            sleep(SLEEP_TIME)


def print_logo(text: str):
    """Print the ascii app logo"""
    ascii_art = pyfiglet.figlet_format(text, font="banner3-D")
    print(ascii_art)


def welcome_screen(user_name: str) -> dict:
    """
    The function checks whether the user is in the system.
    If the user is logged in, it returns True.
    If omitted, the function returns False.
    If a character different from N or Y is entered,
    an error is displayed to the user.
    """
    try:
        while True:
            clear()
            print_logo(LOGO)
            rprint("[bold red]Are you registered?[/bold red]")
            print("")
            print_text("Y for existing user", "yellow")
            print_text("N for a new user", "yellow")
            print("")
            is_register = input("Enter: ")
            if is_register in "yY" and len(is_register) != 0:
                return {
                    "bool": True,
                    "msg": "Greetings. Welcome back. Please enter your name.",
                }
            elif is_register in "nN" and len(is_register) != 0:
                return {"bool": False, "msg": "You need to register."}
            else:
                print_text(
                    "Wrong answer. Please enter Y or N.", style="magenta"
                )
                sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        clear()
        print_logo(LOGO)
        print_text(f"Goog bye {user_name}", "orange3")
        close_app()


def main():
    """
    Main function. It runs all other functions
    """
    clear()
    global user_name
    is_register = welcome_screen(user_name)
    try:
        if is_register["bool"]:
            user_name = log_in_screen()
        else:
            user_name = sign_in_screen()
            print_text("Enter your password: ", "yellow")
            user_pw = input("Password: ")
            hashed_pw = hash_password(user_pw)
            add_user_to_base(user_name, hashed_pw)
            create_user_tasks_page(user_name)

        while True:
            all_tasks = show_tasks(user_name)
            clear()
            print_tasks(all_tasks)
            print_text("Menu:", "yellow")
            print(
                "(A)dd task",
                "Show (T)asks",
                "(E)dit task",
                "(D)elete task",
                "(Q)uit",
                sep=" | ",
            )
            answer = input()
            sleep(SLEEP_TIME)
            if answer in "qQ":
                clear()
                print(f"Bye {user_name}")
                sleep(SLEEP_TIME)
                break
            elif answer in "aA":
                clear()
                # rprint("Enter task text :")
                # input_task = input("Task text: ")
                new_task = add_task_page(user_name)
                add_task(user_name, new_task)
                sleep(SLEEP_TIME)
            elif answer in "tT":
                all_tasks = show_tasks(user_name)
                clear()
                print_tasks(all_tasks)
                sleep(SLEEP_TIME)
            elif answer in "eE":
                tsk_num = input("Enter number of task to edit:")
                res = check_edit_enter(user_name, tsk_num)

                if res["bool"]:
                    edit_task(user_name, res["msg"])
                else:
                    rprint(f"{res['msg']}")
                sleep(SLEEP_TIME)
            elif answer in "dD":
                tsk_num = input("Enter task ID: ")
                delete_task(user_name, tsk_num)
                sleep(SLEEP_TIME)
            else:
                print("Enter correct letter")
                sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        clear()
        print_logo(LOGO)
        print_text(f"Goog bye {user_name}", "orange3")
        close_app()


if __name__ == "__main__":
    main()
