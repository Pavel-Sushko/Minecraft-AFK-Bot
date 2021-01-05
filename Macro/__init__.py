import time
from pydirectinput import press
from Utils._Macro import macro


def bz():
    press("/")
    press("b")
    press("z")


# Gives time to open the application that requires the inputs
time.sleep(4)

while True:
    for x in range (100):
        macro()

    bz()
