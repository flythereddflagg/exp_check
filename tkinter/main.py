#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file: exp_check/main.py
author: Mark Redd

Description:
    Runs the exp_check program and should be the entry point for any production
    version of the software.
"""
import os
from sys import argv

PROGRAM_ROOT = os.path.dirname(os.path.abspath(__file__))

from exp_check.date_check import main as date_check
from exp_check.food_gui import ExpCheckGUI
from exp_check.data_manager import DataManager
from exp_check.constants import food_data_path, gui_shape_pos, icon_path


def main():
    if len(argv) > 1 and argv[1] == "-chk":
        date_check(PROGRAM_ROOT)
    else:
        data_manager = DataManager(PROGRAM_ROOT+food_data_path)
        gui = ExpCheckGUI(data_manager, PROGRAM_ROOT)
        gui.geometry(gui_shape_pos)
        gui.iconbitmap(PROGRAM_ROOT+icon_path)
        gui.mainloop()


if __name__ == "__main__":
    main()