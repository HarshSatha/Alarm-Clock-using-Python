#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox
import datetime
import math
import winsound

def check_alarm(alarm_time):
    """Check if the current time matches the alarm time."""
    current_time = datetime.datetime.now().strftime("%H:%M")
    return current_time == alarm_time

def show_alarm_message(alarm_message):
    """Display a pop-up message with the specified alarm message."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Alarm", alarm_message)
    root.destroy()

def play_alarm_sound():
    """Play an alarm sound."""
    winsound.Beep(1000, 3000)  # Play sound (1000 Hz frequency, 1 second duration)

def update_clock():
    """Update the clock display and check for alarm trigger."""
    global clock_label  # Declare clock_label as a global variable
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)

    # Calculate angles for clock hands
    hour_angle = (datetime.datetime.now().hour % 12) * 30 + datetime.datetime.now().minute / 2
    minute_angle = datetime.datetime.now().minute * 6
    second_angle = datetime.datetime.now().second * 6

    # Update clock hands
    clock_canvas.delete("hands")
    draw_hand(hour_angle, 40, 6, "black")
    draw_hand(minute_angle, 60, 4, "black")
    draw_hand(second_angle, 70, 2, "red")

    alarm_time = alarm_time_entry.get()
    if check_alarm(alarm_time):
        if not getattr(update_clock, "alarm_triggered", False):  # Check if alarm has already been triggered
            play_alarm_sound()
            update_clock.alarm_triggered = True  # Set flag to indicate alarm has been triggered
            show_alarm_message(alarm_message_entry.get())  # Show alarm message after playing sound

    if not getattr(update_clock, "alarm_triggered", False):  # Continue updating clock if alarm has not been triggered
        clock_canvas.after(1000, update_clock)

def draw_hand(angle, length, width, color):
    """Draw a clock hand."""
    x = 150 + length * math.cos(math.radians(90 - angle))
    y = 150 - length * math.sin(math.radians(90 - angle))
    clock_canvas.create_line(150, 150, x, y, width=width, fill=color, tag="hands")

def set_alarm():
    """Set the alarm time and message."""
    alarm_time = alarm_time_entry.get()
    alarm_message = alarm_message_entry.get()
    update_clock.alarm_triggered = False  # Reset alarm trigger flag
    return alarm_time, alarm_message

def main():
    """Initialize the main GUI window."""
    root = tk.Tk()
    root.title("Alarm Clock")
    root.geometry("300x380")

    global clock_canvas
    clock_canvas = tk.Canvas(root, width=300, height=300, bg="white")
    clock_canvas.pack()

    # Draw clock face with hour numbers
    for i in range(1, 13):
        angle = math.radians(90 - i * 30)
        x = 150 + 100 * math.cos(angle)
        y = 150 - 100 * math.sin(angle)
        clock_canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))

    clock_canvas.create_oval(50, 50, 250, 250, width=2)

    global clock_label
    clock_label = tk.Label(root, font=("Arial", 24))
    clock_label.pack()
    
    global alarm_time_entry
    alarm_time_label = tk.Label(root, text="Alarm Time (HH:MM):")
    alarm_time_label.pack()
    alarm_time_entry = tk.Entry(root)
    alarm_time_entry.pack()

    global alarm_message_entry
    alarm_message_label = tk.Label(root, text="Alarm Message:")
    alarm_message_label.pack()
    alarm_message_entry = tk.Entry(root)
    alarm_message_entry.pack()

    set_alarm_button = tk.Button(root, text="Set Alarm", command=update_clock)
    set_alarm_button.pack()

    update_clock()

    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




