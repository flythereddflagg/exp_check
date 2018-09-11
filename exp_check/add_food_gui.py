#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/add_food_gui.py
author : Mark Redd

"""
from tkinter import Button, Entry, Label, END, N, W, E
from data_manager import DataManager
from ttkcalendar import Calendar


class AddFoodGUI():
    def __init__(self, parent):
        self.parent = parent
        self.init_gui()
    
    
    def init_gui(self):
        
        widget_options = {
            "background"     : "black",
            "foreground"     : "white"
            }           
        # setup widgets
        self.add_button    = Button(self.parent, text="Add Food", 
                                    **widget_options, command=self.add_food)
        self.cancel_button = Button(self.parent, text="Cancel", 
                                    **widget_options, command=self.cancel)
        self.name_box      = Entry(self.parent, insertbackground='white',
                                    **widget_options)
        self.name_label    = Label(self.parent, text="Food Name",
                                    **widget_options)
        self.expdate_label = Label(self.parent, text="Expiration Date", 
                                    **widget_options)
        self.date_picker   = Calendar(self.parent)
    
    
    def grid_widgets(self):
        # place widgets
        self.parent.title("exp_check: add food")
        self.parent.cur_instance = self
        grid_options = {
            "padx" : 3,
            "pady" : 3
            }
        self.add_button.grid(   row=0, column=2, **grid_options)
        self.cancel_button.grid(row=1, column=2, **grid_options, sticky=N)
        self.name_box.grid(     row=0, column=1, **grid_options, sticky=W)
        self.expdate_label.grid(row=1, column=0, columnspan=2, **grid_options)
        self.date_picker.grid(  row=2, column=0, columnspan=2, **grid_options)
        self.name_label.grid(   row=0, column=0, **grid_options, sticky=E)
    
    
    def un_grid_widgets(self):
        self.add_button.grid_forget()
        self.cancel_button.grid_forget()
        self.name_box.grid_forget()
        self.date_picker.grid_forget()
        self.name_label.grid_forget()
        self.expdate_label.grid_forget()
    
    
    def add_food(self, event=None):
        name = self.name_box.get().strip()
        
        date_obj = self.date_picker.selection
        if name == "" or date_obj is None:
            self.parent.msg_box_init(self,"Please Select a name and a date")
            return
        
        self.name_box.delete(0,END)
        date = "".join((str(date_obj).split()[0][2:]).split('-'))
        msg = self.parent.data_manager.add_entry(name, date)
        if msg is not None: 
            self.parent.msg_box_init(self, msg)
            return
        self.parent.update_data_display()
        self.cancel()

        
    def cancel(self, event=None):
        self.un_grid_widgets()
        self.parent.grid_widgets()

    
def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("450x250+200+200")
    gui.mainloop()

if __name__ == "__main__":
    main()

