#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Date Check on Food Storage

This script checks the expiration dates from a food list then
reports via message box what foods are expired or will expire
soon.

author: Mark Redd
last modified: 190111
"""
from exp_check.constants import food_data_path
from exp_check.data_manager import DataManager
import tkinter as tk
from tkinter.messagebox import showinfo
from datetime import date, timedelta


def calc_delta_date(future_time, current_time):
    """
    Calculates the number of days between
    @param current_time and @param future_time
    and @returns a negative number of days if current_time
    is after future_time.
    """
    f_date = date(  int(future_time[:2]), 
                    int(future_time[2:4]),
                    int(future_time[4:]))
    
    c_date = date(  int(current_time[:2]), 
                    int(current_time[2:4]),
                    int(current_time[4:]))
    
    seconds = (f_date-c_date).total_seconds()
    
    return int(seconds/86400)
    

def main():
    data_manager = DataManager(food_data_path)
    database = data_manager.get_database()
    current_date = data_manager.get_current_datetime()[:-4]
    
    expired     = []
    exp_30_days = []
    
    for entry in database:
        delta_date = calc_delta_date(entry[2], current_date)
        if delta_date < 0:
            expired.append([entry[0], abs(delta_date)])
        elif delta_date < 30:
            exp_30_days.append([entry[0], delta_date])
    
    
    if expired:
        exp_text  = "\n\nThe following items are expired:\n\n"
        exp_text += "{:^40} {:^10}\n".format("Food Name", "Expired")
        exp_text += "-"*60 + "\n"
        
        for datum in expired:
            exp_text += f"{datum[0]:^40} {datum[1]:>10} day(s) ago\n"
    else:
        exp_text = ""
    
    
    if exp_30_days:
        warn_30  = "\n\nThe following items will expire "\
                   "in less than 30 days:\n\n"
        warn_30 += "{:^40} {:^10}\n".format("Food Name", "Expires in")
        warn_30 += "-"*60+"\n"
        
        for datum in exp_30_days:
            warn_30 += f"{datum[0]:^40} {datum[1]:>10} day(s)\n"
    else:
        warn_30 = ""
    
    exp_message = f"{exp_text}{warn_30}"
    
    if exp_message:
        tk.Tk().withdraw()
        showinfo("Expiration Information", exp_message)
    
    
if __name__ == "__main__":
    main()
