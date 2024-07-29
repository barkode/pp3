# To hash password
import hashlib

# To create timestamp
import sys
import time

# import only system from os
from os import name, system

import maskpass


def sleep(seconds: float):
    """Adds delay in seconds"""
    time.sleep(seconds)


def clear():
    """Clear screen"""
    system("cls") if name == "nt" else system("clear")


def hash_password(password: str) -> str:
    """Hash user password and return hashed password"""
    # Hash the password
    pw = hashlib.sha256(password.encode("utf-8"))
    return pw.hexdigest()


def gen_task_id():
    """Generate a timestamp-based ID"""
    gen_id = str(int(time.time()))
    return gen_id


def time_stamp():
    time_now = time.localtime()
    return time.strftime("%Y-%m-%d", time_now)


def close_app():
    """Terminates the app with a system call"""
    sys.exit(0)


def hide_user_pass():
    """Hide user password when"""
    pwd = maskpass.askpass(prompt="Password: ", mask="#")
    return pwd
