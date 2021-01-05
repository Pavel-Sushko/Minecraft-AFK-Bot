import time
from Utils._Macro import macro
from win32gui import GetWindowText, GetForegroundWindow

# Gives time to open the application that requires the inputs
time.sleep(4)

active_window_name = GetWindowText(GetForegroundWindow())

while True:
    while "Notepad" in active_window_name:
        for x in range(100):
            if "Notepad" in active_window_name:
                macro()

            else:
                break

    active_window_name = GetWindowText(GetForegroundWindow())


