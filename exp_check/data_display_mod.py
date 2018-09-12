#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_display_mod.py
author : Mark Redd

"""
from tkinter import Frame, Listbox, N, S, E, W, END, Label

class DataDisplay(Frame):
    def __init__(self, widget_options):
        super().__init__()
        self.widget_options = widget_options
        self.init_gui()
        
    def init_gui(self):
        self.names      = Listbox(self, **self.widget_options)
        self.date_added = Listbox(self, **self.widget_options)
        self.expdate    = Listbox(self, **self.widget_options)
        self.names.bind("<ButtonRelease-1>", self.select_fields)
        self.date_added.bind("<ButtonRelease-1>", self.select_fields)
        self.expdate.bind("<ButtonRelease-1>", self.select_fields)
        
        self.name_label  = Label(self, text="Food Name" ,
                                **self.widget_options)
        self.added_label = Label(self, text="Date Added" ,
                                **self.widget_options)
        self.exp_label   = Label(self, text="Expiration Date",
                                **self.widget_options)
        
        self.name_label.grid( row=0, column=0, sticky=N+S+E+W)
        self.added_label.grid(row=0, column=1, sticky=N+S+E+W)
        self.exp_label.grid(  row=0, column=2, sticky=N+S+E+W)
        self.names.grid(     row=1, column=0, sticky=N+S+E+W)
        self.date_added.grid(row=1, column=1, sticky=N+S+E+W)
        self.expdate.grid(   row=1, column=2, sticky=N+S+E+W)
    
    def delete(self, *args):
        self.names.delete(*args)
        self.date_added.delete(*args)
        self.expdate.delete(*args)
    
    def insert(self, where, item):
        self.names.insert(where, item[0])
        self.date_added.insert(where, item[1])
        self.expdate.insert(where, item[2])
    
    def get(self, *args):
        name_select = self.names.curselection()
        date_added_select = self.date_added.curselection()
        expdate_select = self.expdate.curselection()
        
        item = (
            self.names.get(*args),
            self.date_added.get(*args),
            self.expdate.get(*args))
        return "{} {} {}".format(*item)
    
    
    def select_fields(self, event=None):
        instance = event.widget
        sel_ind = instance.curselection()[0] if instance.curselection() else 0
        self.names.selection_clear(0, END) 
        self.date_added.selection_clear(0, END) 
        self.expdate.selection_clear(0, END) 
        
        self.date_added.selection_set(sel_ind)
        self.expdate.selection_set(sel_ind)
        self.names.selection_set(sel_ind)
        