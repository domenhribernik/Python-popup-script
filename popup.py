import tkinter as tk
import keyboard
import time
import os
import signal

def create_popup(text):
    def close_popup():
        popup.destroy()

    popup = tk.Tk()
    popup.title("Popup")
    popup.geometry("300x100")
    popup.resizable(False, False)
    popup.overrideredirect(True) # Remove the nav bar
    popup.wm_attributes("-topmost", 1) # Set the popup to stay on top
    popup.configure(bg="#333333")
    popup.config(bd=5, relief=tk.RAISED, highlightbackground="#FFD700", highlightthickness=3)

    # Position the popup at the bottom right of the screen
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup.update_idletasks()
    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()
    x_pos = screen_width - popup_width - 10
    y_pos = screen_height - popup_height - 70
    popup.geometry(f"+{x_pos}+{y_pos}")

    label = tk.Label(popup, text=text, fg="white", bg="#333333", font=("Arial", 14, "normal"))
    label.pack(padx=10, pady=10)
    cancel_button = tk.Button(popup, text="Cancel", command=close_popup, bg="#555555", fg="white", font=("Arial", 12, "bold"))
    cancel_button.pack(pady=5)
    popup.mainloop()

popup_interval = 3600
text_to_display = "It's time stretch!"

def terminate_program():
    keyboard.unhook_all()  # Unhook the keyboard listener   
    create_popup("Program terminated.")
    time.sleep(2)  # Give time for the popup to display
    os.kill(os.getpid(), signal.SIGTERM) # Terminate the program

if __name__ == "__main__":
    keyboard.add_hotkey("ctrl+left+right", terminate_program)

    while True:
        create_popup(text_to_display)
        time.sleep(popup_interval)