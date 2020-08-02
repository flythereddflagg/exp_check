from constants import *
from base_screen import BaseScreen


class AddScreen(BaseScreen):
    def __init__(self, master, parent=None):
        self.id = "add screen"
        super().__init__(master, parent)

    
    def more_setup(self):
        self.widgets["add button"].clicked.connect(
            self.add_food)
        self.widgets["delete button"].clicked.connect(
            self.cancel_add_food)
    

    def add_food(self):
        if self.widgets['food name'].text() == "":
            self.master.stack.setCurrentIndex(
                self.master.msg_screen_index)
            return
        self.cancel_add_food()


    def cancel_add_food(self):
        self.master.stack.setCurrentIndex(
            self.master.home_screen_index)
        
