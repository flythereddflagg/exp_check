#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file: exp_check/main.py
author: Mark Redd

Description:
    Runs the exp_check program and should be the entry point for any production
    version of the software.
"""
from food_gui import ExpCheckGUI
from data_manager import DataManager
from constants import food_data_path, gui_shape_pos


def main():
    data_manager = DataManager(food_data_path)
    gui = ExpCheckGUI(data_manager)
    gui.geometry(gui_shape_pos)
    gui.mainloop()


if __name__ == "__main__":
    main()