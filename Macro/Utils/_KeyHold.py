import pydirectinput
import time


def key_hold(key, time_ms):
    pydirectinput.keyDown(key)
    recorded_time = time.monotonic()
    wait = True

    while wait:
        current_time = time.monotonic()
        if current_time - recorded_time > time_ms / 1000:
            pydirectinput.keyUp(key)
            wait = False
