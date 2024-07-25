# To hash password
import hashlib

# To create timestamp
import sys
import time

# import only system from os
from os import name, system


# import sleep to show output for some time period
def sleep(sec):
    time.sleep(sec)


def clear():
    """Clear screen"""
    system("cls") if name == "nt" else system("clear")


def hash_password(password: str) -> str:
    """
    Function hash user password and return hashed password
    """
    # Hash the password
    pw = hashlib.sha256(password.encode("utf-8"))
    return pw.hexdigest()


def gen_task_id():
    # Generate a timestamp-based ID
    gen_id = str(int(time.time()))
    return gen_id


def time_stamp():
    time_now = time.localtime()
    return time.strftime("%Y-%m-%d", time_now)


def close_app(msg: str):
    sys.exit(msg)
