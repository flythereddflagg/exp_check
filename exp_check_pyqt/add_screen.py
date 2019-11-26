from constants import *


class AddScreen(QWidget):
    def __init__(self, master, parent=None):
        super().__init__(parent)
        self.master = master
        self.widgets = {}
        self.grid_places = {}
        self.setup_widgets()


    def setup_widgets(self):
        self.main_layout = QGridLayout()
        self.init_widgets()
        self.grid_widgets()
        self.more_setup()
        self.setLayout(self.main_layout)
    
    
    def init_widgets(self):
        layout_info = LAYOUT_INFO["add screen"]

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
            self.cancel_add_food)
    

    def add_food(self):
        self.cancel_add_food()


    def cancel_add_food(self):
        self.master.stack.setCurrentIndex(0)
        
