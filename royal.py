#Start module import ===>
import os
import time
import random
try:
    from colorama import init
    from colors import red, green, blue, white, black, yellow, cyan, magenta
    init()
except ValueError:
    vl = input("ERROR: You dont have colorama package, do you want to install it? (Y/N): ")
    if vl=="y":
        try:
            os.system("pip3 install colorama")
            os.system("pip install colorama")
            os.system("cls")
            from colorama import init
            from colors import red, green, blue, white, black, yellow, cyan, magenta
            init()
        except ValueError:
            os.system("You dont have PIP installed, download it from https://pypi.python.org/")
    if vl=="Y":
        try:
            os.system("pip3 install colorama")
            os.system("pip install colorama")
            os.system("cls")
            from colorama import init
            from colors import red, green, blue, white, black, yellow, cyan, magenta
            init()
        except ValueError:
            os.system("You dont have PIP installed, download it from https://pypi.python.org/")
    elif vl=="n":
        print("Exiting...")
        exit()
    elif vl=="N":
        print("Exiting...")
        exit()
    else:
        print("WRONG OPTION")
        print("Exiting...")


try:
    import hashlib
except ValueError:
    vl = input("ERROR: You dont have hashlib package, do you want to install it? (Y/N): ")
    if vl=="y":
        try:
            os.system("pip3 install hashlib")
            os.system("pip install hashlib")
            os.system("cls")
            import hashlib
        except ValueError:
            os.system("You dont have PIP installed, download it from https://pypi.python.org/")
    if vl=="Y":
        try:
            os.system("pip3 install hashlib")
            os.system("pip install hashlib")
            os.system("cls")
            import hashlib
        except ValueError:
            os.system("You dont have PIP installed, download it from https://pypi.python.org/")
    elif vl=="n":
        print("Exiting...")
        exit()
    elif vl=="N":
        print("Exiting...")
        exit()
    else:
        print("WRONG OPTION")
        print("Exiting...")

os.system("cls")
# End module import <===
print(red("WARNING: This script is written for python 3 only, if you use python 2 the script may fail."))
print(">> Loading...")
time.sleep(3)
print("Generating an 12 characters ultra-secure password...")
from utils import password
password()
