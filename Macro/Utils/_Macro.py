# Imports of needed modules and classes
import pydirectinput
from time import sleep
from pydirectinput import press
from Utils._KeyHold import key_hold


def click(times, delay_ms):
    # Clicks 84 times
    for x in range(times):
        # X is x position of mouse, Y is y position of mouse
        pydirectinput.click()
        # Delay between clicks
        sleep(delay_ms / 1000)


def macro():
    # Holds down the "a" key for 1250 ms
    key_hold("a", 1250)

    # Delay between key presses
    sleep(0.25)

    # Presses down the "w" key until asked to release
    pydirectinput.keyDown("w")

    # Clicks 84 times
    click(times=84, delay_ms=300)

    # Releases the "w" key
    pydirectinput.keyUp("w")

    # Holds down the "a" key for 1250 ms
    key_hold("a", 1250)

    # Delay between key presses
    sleep(0.25)

    # Presses down the "s" key until asked to release
    pydirectinput.keyDown("s")

    # Clicks 84 times
    click(times=84, delay_ms=300)

    # Presses the "escape" key twice
    press("escape", 2, interval=200)

    # Delay between key presses
    sleep(0.5)

    # Releases the "s" key
    pydirectinput.keyUp("s")

    # Delay between key presses
    sleep(0.5)

    # Presses the "s" key once
    press("s")

    # Delay between key presses
    sleep(0.5)

    # Presses the "t" key once
    press("t")

    # Delay between key presses
    sleep(0.5)

    # Presses the "escape" key once
    press("escape")

    # Delay between key presses
    sleep(0.5)

    # Presses the "t" key once
    press("t")

    # Delay between key presses
    sleep(0.5)

    # Presses the "Up Arrow" key once
    press("up")

    # Delay between key presses
    sleep(0.5)

    # Presses the "escape" key once
    press("enter")

    # Delay between key presses
    sleep(0.5)

    # Presses the "t" key once
    press("t")

    # Delay between key presses
    sleep(0.5)

    # Presses the "Up Arrow" key once
    press("up", 2, interval=500)

    # Delay between key presses
    sleep(0.5)

    # Presses the "enter" key once
    press("enter")

    # Delay between key presses
    sleep(0.5)

    # Delay between key presses
    sleep(25)
