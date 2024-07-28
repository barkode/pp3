import pyfiglet
from rich import print as rprint
from rich.table import Table

#Default parameters
from config import LOGO, SLEEP_TIME, USER_NAME
from gsheets_api import (
    check_user_name,
    check_user_name_entering,
    check_user_password,
)
from utils import (
    clear,
    close_app,
    gen_task_id,
    hash_password,
    hide_user_pass,
    sleep,
    time_stamp,
)

user_name = USER_NAME



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
            rprint("[yellow]Y for existing user[/yellow]")
            rprint("[yellow]N for a new user[/yellow]")
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
                rprint("[magenta]Wrong answer. Please enter Y or N.[magenta]")
                sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        clear()
        print_logo(LOGO)
        rprint(f"[orange3]Goog bye {user_name}[/orange3]")
        close_app()


def print_tasks(tasks_lst: list, user_name: str):
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
        rprint("[yellow]Enter your login: [/yellow]")
        u_login = input("Login: ")
        res = check_user_name_entering(u_login)
        if not res["bool"]:
            rprint(f"[magenta]{res['msg']}[/magenta]")
            sleep(SLEEP_TIME)
            continue
        res = check_user_name(res["msg"])
        if not res["bool"]:
            rprint(f"[magenta]{res['msg']}[/magenta]")
            sleep(SLEEP_TIME)
            continue
        return res["msg"]


def print_logo(text: str):
    """Print the ascii app logo"""
    ascii_art = pyfiglet.figlet_format(text, font="banner3-D")
    print(ascii_art)


def log_in_screen():
    """Shows the user login screen.
    Checks if the user and password exist in the base.
    """
    while True:
        clear()
        print_logo(LOGO)
        rprint("[yellow]Input your login.[/yellow]")
        u_login = input("Login: ")
        res = check_user_name_entering(u_login)
        if not res["bool"]:
            rprint(f"[magenta]{res['msg']}[/magenta]")
            sleep(SLEEP_TIME)
            continue
        rprint("[yellow]Please input your password.[yellow]")
        u_pwd = hide_user_pass()
        h_pwd = hash_password(u_pwd)
        check = check_user_password(u_login, h_pwd)
        if check["bool"]:
            return u_login
        else:
            rprint(f"[magenta]{check["msg"]}[/magenta]")
            sleep(SLEEP_TIME)


def add_task_page(user_name: str) -> dict:
    """Print the task page."""
    rprint(
        f"[yellow]{user_name}. Enter Task text and press Enter.[/yellow]"
    )
    task = input("Enter task: ")
    gen_id = gen_task_id()
    time_stmp = time_stamp()
    return {"id": gen_id, "time": time_stmp, "task": task}
