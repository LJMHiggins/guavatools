## Code to monitor guava easycyte connection ##
import os
from datetime import datetime
from argparse import ArgumentParser, Namespace
import tkinter as tk
from tkinter import ttk
import sys
# Pop up
def popupmsg(msg):
    NORM_FONT = ("Helvetica", 10)
    popup = tk.Tk()
    popup.wm_title("Attention!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def monitor_guava_connection(raw_string_data_dir):
    # Changing the current working directory
    os.chdir(raw_string_data_dir)
    # Loop through files and get latest created fcs file
    most_recent_file = None
    most_recent_time = 0
    for entry in os.scandir(raw_string_data_dir):
        if entry.is_file() and "FCS" in entry.name:
            file_i = entry.name
            time_created = os.path.getctime(file_i)
            if time_created > most_recent_time:
                most_recent_file = file_i
                most_recent_time = most_recent_time

    status_check = True
    while status_check == True:
        modification_timestamp = os.path.getmtime(most_recent_file)
        mod_time = datetime.fromtimestamp(modification_timestamp)
        now = datetime.now()
        time_passed = now - mod_time
        minutes_passed = time_passed.seconds / 60
        if minutes_passed > 7:
            popupmsg(msg = "Check EasyCyte machine.")
            break
            
    sys.exit()
