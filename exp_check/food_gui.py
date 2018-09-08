#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/data_manager.py
author : Mark Redd

"""
from tkinter import Tk, Button, Entry, Listbox, OptionMenu, Label\
    , END, BOTH, N, S, E, W, StringVar,  Menu
from data_manager import DataManager
from PIL import Image, ImageTk
from tkinter.ttk import Menubutton, Style


class ExpCheckGUI(Tk):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.searching = False
        self.init_gui()
    
    
    def init_gui(self):
        self.title("exp_check")
        self.config(bg='black')
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        style = Style()
        style.configure("TMenubutton", foreground="white", background="black")
        
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
        self.delete_button = Button(text="Delete Food", **widget_options, 
                                    command=self.update_list_box)
        
        self.search_box    = Entry(insertbackground='white', **widget_options)
        self.search_box.bind("<Key>", self.search)
        self.search_box.bind("<FocusOut>", 
            lambda event: self.start_stop_search(False))

        self.data_display  = Listbox(**widget_options)
        self.d = StringVar()
        vals = self.data_manager.get_keylist()
        vals.insert(0,'name')
        menu1 = Menu(tearoff=0)
        menu1.add('radiobutton',label=vals[0], 
                command=lambda: self.update_list_box(sort_key=vals[0]))
        menu1.add('radiobutton',label=vals[1], 
                command=lambda: self.update_list_box(sort_key=vals[1]))
        menu1.add('radiobutton',label=vals[2], 
                command=lambda: self.update_list_box(sort_key=vals[2]))

        self.sort_menu = Menubutton(self, text='sort by', 
                                    menu=menu1, style="TMenubutton")        
        
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
        self.update_list_box()

        
    def generate_icon_object(self, path, size):
        image = Image.open(path)
        image.convert("RGBA")
        image.thumbnail(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    
    def update_list_box(self, event=None, sort_key='name', key_list=None):
        """
        Updates the list box with new information
        """
        if key_list is None: key_list = self.data_manager.get_keylist()
        self.data_display.delete(0, END)
        for item in self.data_manager.get_database(
                                       key_list=key_list, 
                                       sort_key=sort_key):
            
            item_str = "{} {} {}".format(*item)
            self.data_display.insert(END, item_str)
    
    def search(self, event=None):
        print(event)
        search_string = self.search_box.get()
        newchar = "" if event is None else event.char
        print(search_string + newchar)
    
    def start_stop_search(self, state):
        print("stopped")

def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("450x250+200+200")
    gui.mainloop()

if __name__ == "__main__":
    main()

