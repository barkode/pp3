# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# import only system from os
from os import name, system

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def add_task(task):
    pass


def delete_task(task_id: int):
    pass


def show_tasks():
    pass


def edit_task():
    pass


def show_ende():
    pass


def main():
    """
    Main function. Starts
    """
    clear()
    print("Please enter your name:")
    user_name = input()
    while True:
        clear()
        print("Enter your chose:")
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
