from constants import *

class BaseScreen(QWidget):
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
        layout_info = LAYOUT_INFO[self.id]

        for key, val in layout_info.items():
            self.widgets[key] = WIDGET_DICT[val['type']](*val['init'])
            self.grid_places[key] = val['grid']
    

    def grid_widgets(self):
        for key, val in self.grid_places.items():
            self.main_layout.addWidget(self.widgets[key], *val)
    
    
    def more_setup(self):
        pass

