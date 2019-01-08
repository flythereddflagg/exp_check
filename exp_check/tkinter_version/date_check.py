

"""
Date Check on Food Storage

This script checks the expiration dates from a food list then
reports via message box what foods are expired or will expire
soon.

author: Mark Redd
last modified: June, 2015
"""
from constants import food_data_path
from data_manager import DataManager
from tkinter.messagebox import showinfo
from datetime import date, timedelta

def main():
    data_manager = DataManager(food_data_path)
    message1 = data_manager.get_database()
    showinfo("Expiration Information", message1)

if __name__ == "__main__":
    main()
