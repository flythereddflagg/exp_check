#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_manager.py
author : Mark Redd

"""
from tkinter import Tk, Button, Entry, Listbox, OptionMenu, Label\
    , END, BOTH, N, S, E, W, StringVar
from data_manager import DataManager
from PIL import Image, ImageTk


class ExpCheckGUI(Tk):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.init_gui()
    
    
    def init_gui(self):
        self.title("exp_check")
        self.config(bg='black')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        widget_options = {
            "master" : self,
            "bg"     : "black",
            "fg"     : "white"
            }
         
        grid_options = {
            "padx" : 3,
            "pady" : 3
            }
            
        # setup widgets
        self.add_button    = Button(text="Add Food",    **widget_options)
        self.delete_button = Button(text="Delete Food", **widget_options)
        self.search_box    = Entry(insertbackground='white', **widget_options)
        #self.search_box.insert(0,"Search")
        self.data_display  = Listbox(**widget_options)
        self.d = StringVar()
        vals = self.data_manager.get_keylist()
        vals.insert(0,'name')
        self.sort_menu = OptionMenu(self, self.d, *vals)
        self.sort_menu.config(bg = 'black', fg = 'white')
        
        search_icon = self.generate_icon_object("search_icon.png", (20,20))
        self.search_label = Label(image=search_icon, **widget_options)
        self.search_label.image = search_icon
        
        
        
        # place widgets
        self.add_button.grid(    row=0, column=0, **grid_options)
        self.delete_button.grid( row=0, column=1, **grid_options)
        
        self.data_display.grid(  row=3, column=0, **grid_options,
                                 columnspan=6, sticky=N+S+E+W)
        
        self.search_label.grid(row=0, column=3)
        self.search_box.grid(    row=0, column=4, **grid_options)
        self.sort_menu.grid(row=0, column=5, **grid_options)
       
        for item in self.data_manager.get_database(
                                       key_list=self.data_manager.get_keylist(), 
                                       sort_key='name'):
            
            item_str = "{:^40}\t {:^10}\t {:^10}".format(*item)
            self.data_display.insert(END, item_str)
        
        
    def generate_icon_object(self, path, size):
        image = Image.open(path)
        image.convert("RGBA")
        image.thumbnail(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("450x250+200+200")
    gui.mainloop()

if __name__ == "__main__":
    main()

