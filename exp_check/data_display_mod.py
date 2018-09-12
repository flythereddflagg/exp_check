#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_display_mod.py
author : Mark Redd

"""
from tkinter import Frame, Listbox, N, S, E, W

class DataDisplay(Frame):
    def __init__(self, widget_options):
        super().__init__()
        self.widget_options = widget_options
        self.init_gui()
        
    def init_gui(self):
        self.names      = Listbox(self, **self.widget_options)
        self.date_added = Listbox(self, **self.widget_options)
        self.expdate    = Listbox(self, **self.widget_options)
        
        self.names.grid(     row=0, column=0, sticky=N+S+E+W)
        self.date_added.grid(row=0, column=1, sticky=N+S+E+W)
        self.expdate.grid(   row=0, column=2, sticky=N+S+E+W)
    
    def delete(self, *args):
        self.names.delete(*args)
        self.date_added.delete(*args)
        self.expdate.delete(*args)
    
    def insert(self, where, item):
        self.names.insert(where, item[0])
        self.date_added.insert(where, item[1])
        self.expdate.insert(where, item[2])
    
    def get(self, *args):
        item = (
            self.names.get(*args),
            self.date_added.get(*args),
            self.expdate.get(*args))
        return "{} {} {}".format(*item)

