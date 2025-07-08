from tkinter import *
from time import strftime

def update():
    time_string = strftime("%I:%M:%S %p")  # Current time (12-hour format with AM/PM)
    time_label.config(text=time_string)

    date_string = strftime("%d %B %Y")  # e.g., 02 July 2025
    date_label.config(text=date_string)

    day_string = strftime("%A")  # Full weekday name
    day_label.config(text=day_string)

    time_label.after(1000, update)  # update every 1000ms (1 second)

# Setup window
window = Tk()
window.title("Digital Clock")
window.geometry("300x150")
window.config(bg="black")

# Time label
time_label = Label(window, font=("Arial", 30,'bold'), fg="orange", bg="black")
time_label.pack()

# Date label
date_label = Label(window, font=("Arial", 15,'bold'), fg="white", bg="black")
date_label.pack()

# Day label
day_label = Label(window, font=("Arial", 15,'bold'), fg="lightgreen", bg="black")
day_label.pack()

# Start clock update
update()
window.mainloop()
