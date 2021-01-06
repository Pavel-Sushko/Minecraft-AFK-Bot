try:
    import tkinter
    from tkinter import messagebox
    import time
    from Utils._Macro import macro
    from win32gui import GetWindowText, GetForegroundWindow

    # Gives time to open the application that requires the inputs
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


except ModuleNotFoundError:
    parent = tkinter.Tk()  # Create the object
    parent.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
    parent.withdraw()  # Hide the window as we do not want to see this one

    messagebox.showerror("Error", "Make sure that you have installed all required modules. For more information refer "
                                  "to https://github.com/Pavel-Sushko/Minecraft-AFK-Bot", parent=parent)
