#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/add_food_gui.py
author : Mark Redd

"""
from tkinter import Button
from data_manager import DataManager



class AddFoodGUI():
    def __init__(self, parent):
        self.parent = parent
        self.init_gui()
    
    
    def init_gui(self):
        
        widget_options = {
            "bg"     : "black",
            "fg"     : "white"
            }           
        # setup widgets
        self.add_button    = Button(self.parent, text="Add Food", **widget_options,
                                    command=self.add_food)
        self.cancel_button = Button(self.parent, text="Cancel", **widget_options, 
                                    command=self.cancel)
    
    def grid_widgets(self):
        # place widgets
        self.parent.title("exp_check: add food")
        grid_options = {
            "padx" : 3,
            "pady" : 3
            }
        self.add_button.grid(    row=0, column=0, **grid_options)
        self.cancel_button.grid( row=0, column=1, **grid_options)

    
    def add_food(self, event=None):
        pass
        
    
    def cancel(self, event=None):
        self.add_button.grid_forget()
        self.cancel_button.grid_forget()
        
        self.parent.grid_widgets()
        


def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("450x250+200+200")
    gui.mainloop()

if __name__ == "__main__":
    main()

