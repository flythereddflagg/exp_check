#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/constants.py
author : Mark Redd

Description:
    A file for holding all constants used by exp_check
"""

food_data_path = "./food_data.json"
icon_path = "./exp_check.ico"

gui_shape_pos  = "475x250+200+200"

widget_options = {
    "background"     : "black",
    "foreground"     : "white"
    } 

format_string = "{0[2]}{0[3]}/{0[4]}{0[5]}/{0[0]}{0[1]}"

empty_database = {
    "_warning": "DO NOT MODIFY THIS FILE",
    "food data": {},
    "key list": [
        "date added",
        "expiration date"
    ],
    "last read date/time" : "1801010000",
    "last write date/time": "1801010000"
}
