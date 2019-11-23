import sys
import json
from PyQt5.QtWidgets import (QApplication, QLabel, QGridLayout, QDialog,
    QTableWidget, QPushButton, QWidget)

LAYOUT_JSON = "layout.json"
WIDGET_DICT = {
    "label"  : QLabel,
    "table"  : QTableWidget,
    "button" : QPushButton
}

class AddGui(QWidget):
    def __init__(self, friend, parent=None):
        super().__init__(parent)
        self.friend = friend
        self.widgets = {}
        self.grid_places = {}
        self.setup_widgets()
        self.show()


    def setup_widgets(self):
        self.main_layout = QGridLayout()
        self.init_widgets()
        self.grid_widgets()
        self.more_setup()
        self.setLayout(self.main_layout)
    
    
    def init_widgets(self):
        with open(LAYOUT_JSON, 'r') as f:
            layout_info = json.load(f)["add"]

        for key, val in layout_info.items():
            self.widgets[key] = WIDGET_DICT[val['type']](*val['init'])
            self.grid_places[key] = val['grid']
    

    def grid_widgets(self):
        for key, val in self.grid_places.items():
            self.main_layout.addWidget(self.widgets[key], *val)
    
    
    def more_setup(self):
        self.widgets["add button"].clicked.connect(
            self.add_food)
        self.widgets["delete button"].clicked.connect(
            self.delete_food)
    

    def add_food(self):
        self.friend.stack.setCurrentIndex(0)


    def delete_food(self):
        print("DELETED FOOD!")
        




if __name__ == '__main__':
    app = FoodGui()
    sys.exit(app.exec_())