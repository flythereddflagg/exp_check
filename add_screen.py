#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
add_screen.py
Code for the "add food" screen for the exp_check app.
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
#from KivyCalendar import DatePicker


class AddScreenLayout(GridLayout):
    def __init__(self, lm, root):
        self.root = root
        self.lm = lm
        self.init_gui()
    
    def init_gui(self):
        super(AddScreenLayout, self).__init__(cols=2)
        # add button
        add_button = Button(text="Add Food", font_size=14)#,
            #size_hint_y=0.1)
        add_button.bind(on_press=self.callback)
        # cancel button
        cancel_button = Button(text="Cancel", font_size=14)#,
            #size_hint_y=0.1)
        cancel_button.bind(on_press=self.callback)
        
        label_name = Label(text="Food Name")
        label_date = Label(text="Expiration Date")
        food_name = TextInput()
        food_name.multiline = False
        
        dt = TextInput()
        
        self.add_widget(label_date)
        self.add_widget(dt)
        
        self.add_widget(label_name)
        self.add_widget(food_name)
        
        for i in range(20):
            self.add_widget(Label())

        self.add_widget(add_button)
        self.add_widget(cancel_button)
        
        
    def callback(self, instance):
        if instance.text == "Add Food":
            print("You pressed add food!")
            
        elif instance.text == "Cancel":
            self.root.manager.current = 'list'
        else:
            print('The button <%s> is being pressed' % instance.text)


class AddScreen(Screen):
    def __init__(self, lm, **kwargs):
        self.lm = lm
        super(AddScreen, self).__init__(**kwargs)
        gui = AddScreenLayout(lm, self)
        self.add_widget(gui)