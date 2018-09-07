#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_manager.py
author : Mark Redd

"""
from tkinter import Tk, Frame, Button, Entry


class ExpCheckGUI(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.init_gui()
    
    
    def init_gui(self):
        self.parent.title("exp_check")
        self.parent.config(bg='black')
        
        options = {
            "master" : self.parent,
            "bg"     : "black",
            "fg"     : "white"
            }
            
        # setup widgets
        self.add_button    = Button(text="Add Food",    **options)
        self.delete_button = Button(text="Delete Food", **options)
        self.search_box    = Entry(insertbackground='white', **options)
        
        # place widgets
        self.add_button.grid(    row=0, column=0)
        self.delete_button.grid( row=1, column=1)
        self.search_box.grid(    row=2, column=2)
        


def main():
    root = Tk()
    gui = ExpCheckGUI(root)
    root.geometry("400x400+200+200")
    root.mainloop()

if __name__ == "__main__":
    main()

