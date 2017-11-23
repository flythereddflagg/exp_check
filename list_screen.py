#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
list_screen.py
Code for the list screen for the exp_check app.
"""
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))



class RV(RecycleView):
    def __init__(self, data, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in data]

        
class ListScreenLayout(GridLayout):
    def __init__(self, lm, rv, root):
        self.root = root
        self.lm = lm
        self.rv = rv
        self.init_gui()
    
    def init_gui(self):
        super(ListScreenLayout, self).__init__(rows=3)
        
        self.add_button = Button(text="ADD", font_size=14,
            size_hint_y=0.1)
        self.add_button.bind(on_press=self.callback)
        self.add_widget(self.add_button)
        
        self.add_button2 = Button(text="Delete", font_size=14,
            size_hint_y=0.1)
        self.add_button2.bind(on_press=self.callback)
        self.add_widget(self.add_button2)
        
        self.add_widget(self.rv)
        
    def callback(self, instance):
        if instance.text == "ADD":
            self.root.manager.current = 'add'
        elif instance.text == "Delete":
            print("You pressed delete!")
        else:
            print('The button <%s> is being pressed' % instance.text)

            
class ListScreen(Screen):
    def __init__(self, lm, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        data = lm.to_string().split('\n')
        rv = RV(data)
        gui = ListScreenLayout(lm, rv, self)
        self.add_widget(gui)