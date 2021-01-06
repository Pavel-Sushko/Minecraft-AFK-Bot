import time
from Utils._Macro import macro
from win32gui import GetWindowText, GetForegroundWindow

# Gives chosen time (in seconds) to open Minecraft
time.sleep(4)

active_window_name = GetWindowText(GetForegroundWindow())

while True:
    while "Minecraft" in active_window_name:
        for x in range(100):
            if "Minecraft" in active_window_name:
                macro()

            else:
                break

    active_window_name = GetWindowText(GetForegroundWindow())


