#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
add_screen.py
Code for the "add food" screen for the exp_check app.
"""
from kivy.uix.screenmanager import Screen

class AddScreen(Screen):
    def __init__(self, lm, **kwargs):
        self.lm = lm
        super(AddScreen, self).__init__(**kwargs)