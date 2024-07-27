# import from rich library for draw tables

from rich import print as rprint

from gsheets_api import (
    add_task,
    add_task_page,
    add_user_to_base,
    check_edit_enter,
    create_user_tasks_page,
    delete_task,
    edit_task,
    show_tasks,
)
from ui import (
    LOGO,
    SLEEP_TIME,
    log_in_screen,
    print_logo,
    print_tasks,
    sign_in_screen,
    welcome_screen,
)
from utils import (
    clear,
    close_app,
    hash_password,
    sleep,
)

user_name = "Dear User"


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
            rprint("[yellow]Enter your password: [/yellow]")
            user_pw = input("Password: ")
            hashed_pw = hash_password(user_pw)
            add_user_to_base(user_name, hashed_pw)
            create_user_tasks_page(user_name)

        while True:
            all_tasks = show_tasks(user_name)
            clear()
            print_tasks(all_tasks)
            rprint("[yellow]Menu: [/yellow]")
            rprint(
                "[cyan]([yellow]A[/yellow])dd task[/cyan]",
                "[cyan]Show ([yellow]T[/yellow])asks[/cyan]",
                "[cyan]([yellow]E[/yellow])dit task[/cyan]",
                "[cyan]([yellow]D[/yellow])elete task[/cyan]",
                "[cyan]([yellow]Q[/yellow])uit[/cyan]",
                sep=" | ",
            )
            answer = input("Enter the letter: ")
            sleep(SLEEP_TIME)
            if answer in "qQ":
                clear()
                print(f"Bye {user_name}")
                sleep(SLEEP_TIME)
                break
            elif answer in "aA":
                clear()
                new_task = add_task_page(user_name)
                add_task(user_name, new_task)
                sleep(SLEEP_TIME)
            elif answer in "tT":
                all_tasks = show_tasks(user_name)
                clear()
                print_tasks(all_tasks)
                sleep(SLEEP_TIME)
            elif answer in "eE":
                rprint("[yellow]Enter task number: [/yellow]", end=" ")
                tsk_num = input()
                res = check_edit_enter(user_name, tsk_num)
                if res["bool"]:
                    edit_task(user_name, res["msg"])
                else:
                    rprint(f"[magenta]{res['msg']}[/magenta]")
                sleep(SLEEP_TIME)
            elif answer in "dD":
                rprint("[yellow]Enter task number: [/yellow]", end=" ")
                res = check_edit_enter(user_name, tsk_num)
                if res["bool"]:
                    delete_task(user_name, res["msg"])
                else:
                    rprint(f"[magenta]{res['msg']}[/magenta]")
                sleep(SLEEP_TIME)
            else:
                rprint("Please, enter correct letter")
                sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        clear()
        print_logo(LOGO)
        rprint(f"[orange3]Goog bye {user_name}[/orange3]")
        close_app()


if __name__ == "__main__":
    main()
