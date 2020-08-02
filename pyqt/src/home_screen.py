from constants import *
from base_screen import BaseScreen


class HomeScreen(BaseScreen):
    def __init__(self, master, parent=None):
        self.id = 'home screen'
        super().__init__(master, parent)
            
    
    def more_setup(self):
        self.widgets["data table"].setHorizontalHeaderLabels(
            ["Food Name","Date Added","Exp Date"])
        self.widgets["data table"].setEditTriggers(
            QTableWidget.NoEditTriggers)
        self.widgets["add button"].clicked.connect(
            self.add_food)
        self.widgets["delete button"].clicked.connect(
            self.delete_food)
    

    def add_food(self):
        self.master.stack.setCurrentIndex(
            self.master.add_screen_index)


    def delete_food(self):
        print("DELETED FOOD!")


