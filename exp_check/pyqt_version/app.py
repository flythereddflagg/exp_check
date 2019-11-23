import sys
import json
from add_screen import AddGui
from PyQt5.QtWidgets import (QApplication, QLabel, QGridLayout, QDialog,
    QTableWidget, QPushButton, QWidget, QStackedWidget)

LAYOUT_JSON = "layout.json"
WIDGET_DICT = {
    "label"  : QLabel,
    "table"  : QTableWidget,
    "button" : QPushButton
}

class FoodGui():
    def __init__(self):
        self.widgets = {}
        self.grid_places = {}
        self.home = QWidget()
        self.setup_widgets()
        self.add_screen = AddGui(self)
        self.stack = QStackedWidget()
        self.stack.addWidget(self.home)
        self.stack.addWidget(self.add_screen)
        self.stack.show()


    def setup_widgets(self):
        self.main_layout = QGridLayout()
        self.init_widgets()
        self.grid_widgets()
        self.more_setup()
        self.home.setLayout(self.main_layout)
    
    
    def init_widgets(self):
        with open(LAYOUT_JSON, 'r') as f:
            layout_info = json.load(f)['home']

        for key, val in layout_info.items():
            self.widgets[key] = WIDGET_DICT[val['type']](*val['init'])
            self.grid_places[key] = val['grid']
    

    def grid_widgets(self):
        for key, val in self.grid_places.items():
            self.main_layout.addWidget(self.widgets[key], *val)
    
    
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
        self.stack.setCurrentIndex(1)


    def delete_food(self):
        print("DELETED FOOD!")
        




if __name__ == '__main__':
    app = QApplication([])
    gui = FoodGui()
    sys.exit(app.exec_())