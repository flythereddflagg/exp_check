#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/add_food_gui.py
author : Mark Redd

"""
from tkinter import Button, Entry, Label, END
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
        self.name_label    = Label(self.parent, text="Food Name", **widget_options)
        self.date_picker   = Calendar(self.parent)
        self.message = Label(self.parent, text='', **widget_options)
        self.okay_button = Button(self.parent, text="   OK   ", 
                                    **widget_options, command=self.okay_button)
    
    
    def grid_widgets(self):
        # place widgets
        self.parent.title("exp_check: add food")
        grid_options = {
            "padx" : 3,
            "pady" : 3
            }
        self.add_button.grid(   row=0, column=2, **grid_options)
        self.cancel_button.grid(row=1, column=2, **grid_options)
        self.name_box.grid(     row=0, column=1, **grid_options)
        self.date_picker.grid(  row=1, column=0, columnspan=2, **grid_options)
        self.name_label.grid(   row=0, column=0, **grid_options)
    
    
    def un_grid_widgets(self):
        self.add_button.grid_forget()
        self.cancel_button.grid_forget()
        self.name_box.grid_forget()
        self.date_picker.grid_forget()
        self.name_label.grid_forget()
    
    
    def add_food(self, event=None):
        name = self.name_box.get().strip()
        
        date_obj = self.date_picker.selection
        if name == "" or date_obj is None:
            self.un_grid_widgets()
            self.msg_box_init("Please Select a name and a date")
            return
        
        self.name_box.delete(0,END)
        date = str(date_obj).split()[0][2:]
        date = "".join(date.split('-'))
        print(date, name)
        self.parent.data_manager.add_entry(name, date)
        self.parent.update_data_display()
        self.cancel()

        
    def cancel(self, event=None):
        self.un_grid_widgets()
        self.parent.grid_widgets()
     
     
    def msg_box_init(self, msg='a message'):
        self.un_grid_widgets()
        self.message['text'] = msg
        self.message.grid(row=0, column=0)
        self.okay_button.grid(row=1, column=0)
    
    
    def okay_button(self, event=None):
        self.message.grid_forget()
        self.okay_button.grid_forget()
        self.grid_widgets()
    
def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("450x250+200+200")
    gui.mainloop()

if __name__ == "__main__":
    main()

