#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.py
The main program and builder for the exp_check app.
"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from add_screen import AddScreen
from list_screen import ListScreen
from list_manager import ListManager

Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '400')

class ExpCheckApp(App):
    def build(self):
        sm = ScreenManager()
        lm = ListManager("lst.csv")
        sm.add_widget(ListScreen(lm, name='list'))
        sm.add_widget(AddScreen(lm, name='add'))
        return sm

if __name__ == '__main__':
    ExpCheckApp().run()
