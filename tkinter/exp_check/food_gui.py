#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
file   : exp_check/food_gui.py
author : Mark Redd

Description:
    The main class implementing the UI for the exp check program 
"""
from tkinter import Tk, Frame, Button, Entry, OptionMenu, Label, END, BOTH,\
                    N, S, E, W, Menu, ACTIVE
from PIL import Image, ImageTk
from tkinter.ttk import Menubutton, Style
from string import printable
from exp_check.data_display_mod import DataDisplay
#from data_manager import DataManager # uncomment for testing
from exp_check.add_food_gui import AddFoodGUI
from exp_check.constants import widget_options, format_string, search_icon_path


class ExpCheckGUI(Tk):
    def __init__(self, data_manager, program_root):
        super().__init__()
        self.program_root = program_root
        self.data_manager = data_manager
        self.searching = False
        self.good_chars = printable[:-5] + '\x08'
        self.add_gui = AddFoodGUI(self)
        self.init_gui()
    
    
    def init_gui(self):
        """
        Initializes all widgets for the main screen and calls grid_widgets()
        to place them
        """
        self.title("exp_check")
        self.config(bg='black')
        
        style = Style()
        style.configure("TMenubutton", foreground="white", background="black")
        # setup widgets
        self.add_button    = Button(self, text="Add Food",    **widget_options,
                                    command=self.add_food)
        self.delete_button = Button(self, text="Delete Food", **widget_options, 
                                    command=self.delete_food)
        
        self.search_box    = Entry(self,  **widget_options,
                                    insertbackground='white')
        self.search_box.bind("<Key>", self.search)

        self.data_display  = DataDisplay(widget_options)
        vals = self.data_manager.get_keylist()
        vals.insert(0,'name')
        menu1 = Menu(tearoff=0)
        menu1.add('radiobutton',label=vals[0], 
                command=lambda: self.update_data_display(sort_key=vals[0]))
        menu1.add('radiobutton',label=vals[1], 
                command=lambda: self.update_data_display(sort_key=vals[1]))
        menu1.add('radiobutton',label=vals[2], 
                command=lambda: self.update_data_display(sort_key=vals[2]))

        self.sort_menu = Menubutton(self, text='sort by', 
                                    menu=menu1, style="TMenubutton")        
        
        search_icon = self.generate_icon_object(
            self.program_root+search_icon_path, 
            (20,20)
        )
        self.search_label = Label(image=search_icon, **widget_options)
        self.search_label.image = search_icon
        # setup message box dialog
        self.message = Label(self, text='', **widget_options)
        self.okay_button = Button(self, text="   OK   ", 
                    **widget_options, 
                    command=lambda: self.okay_button_press(self.cur_instance))
        
        self.grid_widgets()

        
    def grid_widgets(self):
        """
        Places initialized widgets on screen
        """
        self.title("exp_check")
        self.cur_instance = self
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        grid_options = {
            "padx" : 3,
            "pady" : 3
            }
        self.add_button.grid(    row=0, column=0, **grid_options)
        self.delete_button.grid( row=0, column=1, **grid_options)
        self.data_display.grid(  row=2, column=0, **grid_options,
                                 columnspan=6, sticky=N+S+E+W)
        self.search_label.grid(row=0, column=3)
        self.search_box.grid(    row=0, column=4, **grid_options)
        self.sort_menu.grid(row=0, column=5, **grid_options)
        self.update_data_display()

        
    def generate_icon_object(self, path, size):
        """
        Initializes the an icon with @param path so it is ready to be placed
            inside a label widget to be placed on screen
        """
        image = Image.open(path)
        image.convert("RGBA")
        image.thumbnail(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    
    
    def update_data_display(self, event=None, sort_key='name',
                            key_list=None, search_string=None):
        """
        Synchronizes the data display with the database from the data manager
        """
        if key_list is None: key_list = self.data_manager.get_keylist()
        self.data_display.delete(0, END)
        for item in self.data_manager.get_database(
                                       key_list=key_list, 
                                       sort_key=sort_key):
            
            item_str = "{} {} {}".format(*item)
            if  search_string is None or\
                search_string in item_str.lower():
                    item[1] = format_string.format(item[1])
                    item[2] = format_string.format(item[2])
                    self.data_display.insert(END, item)

    
    def search(self, event=None):
        """
        Updates the data display with whatever is in the search box. Will run
        any time a key is pressed while focused on the search box.
        """
        search_string = self.search_box.get()
        if event is None or event.char not in self.good_chars:
            newchar = ""
        elif event.char == '\x08':
            search_string = search_string[:-1]
            newchar = ""
        else:
            newchar = event.char

        search_string += newchar
        search_string = search_string.lower()

        self.update_data_display(search_string=search_string)

        
    def un_grid_widgets(self, event=None):
        """
        Removes all the current widgets
        """
        self.add_button.grid_forget()
        self.delete_button.grid_forget()
        self.data_display.grid_forget()                        
        self.search_label.grid_forget()
        self.search_box.grid_forget()
        self.sort_menu.grid_forget()
    

    def add_food(self, event=None):
        """
        Removes all the current widgets and draws draws the add_food_gui widgets
        on the window.
        """
        self.un_grid_widgets()
        self.add_gui.grid_widgets()


    def delete_food(self, event=None):
        """
        Selects and deletes a food from the database by calling the data manager
        """
        selection = self.data_display.get(ACTIVE).split()
        if not selection: return
        name = ' '.join(selection[0:-2]) if len(selection) > 3 else selection[0]
        msg = self.data_manager.delete_entry(name)
        if msg is not None: 
            self.msg_box_init(self, msg)
            return
        self.update_data_display()
    
    
    def msg_box_init(self, instance, msg='a message'):
        """
        Creates a message box after deleting all removing all widgets from 
            the screen
        """
        instance.un_grid_widgets()
        self.message['text'] = msg
        self.message.grid(row=0, column=0)
        self.okay_button.grid(row=1, column=0)
    
    
    def okay_button_press(self, instance, event=None):
        """
        On pressing the okay button, replaces all changed widgets
        """
        self.message.grid_forget()
        self.okay_button.grid_forget()
        instance.grid_widgets()    



def main():
    data_manager = DataManager("./data.json")
    gui = ExpCheckGUI(data_manager)
    gui.geometry("475x250+200+200") # adjust here
    gui.mainloop()


if __name__ == "__main__":
    main()
