try:
    # Import tkinter for easier error displaying
    from tkinter import *
    from tkinter import messagebox

    # Time imported for delay when starting program
    import time
    # Exterior class imported for better organizing of functions
    from Utils._Macro import macro
    # Imported to verify the active window before running the script
    from win32gui import GetWindowText, GetForegroundWindow

    # Gives time to open the application that requires the inputs
    time.sleep(4)

    # Gets and stores the name of the current foreground window
    active_window_name = GetWindowText(GetForegroundWindow())

    # Looped to run forever
    while True:
        # Only runs when the input goes to the Minecraft window
        while "Minecraft" in active_window_name:
            # Runs 100 times for later integration of the sell function
            for x in range(100):
                # Checks if Minecraft is the active window receiving the inputs
                if "Minecraft" in active_window_name:
                    macro()

                else:
                    break

                # Re-verifies if Minecraft is still the foreground window
                active_window_name = GetWindowText(GetForegroundWindow())

        # Re-verifies if Minecraft is still the foreground window
        active_window_name = GetWindowText(GetForegroundWindow())

# Displays the module errors with a simple, yet effective UI
except ModuleNotFoundError as e:
    parent = Tk()  # Creates the window object
    parent.overrideredirect(1)  # Stops the window object from appearing and then disappearing quickly
    parent.withdraw()  # Hides the window so that it runs in the background

    # Opens a message box, displaying the error
    messagebox.showerror("Error", str(e) + "\n\nMake sure that you have installed all required modules.\nFor more "
                                           "information refer to: https://github.com/Pavel-Sushko/Minecraft-AFK-Bot",
                         parent=parent)

    # Closes the program once the "Ok" button is pressed
    parent.quit()
