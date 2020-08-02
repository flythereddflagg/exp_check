from constants import *
from base_screen import BaseScreen


class MsgScreen(BaseScreen):
    def __init__(self, master, parent=None):
        self.id = "msg screen"
        super().__init__(master, parent)

    
    def more_setup(self):
        self.widgets["ok button"].clicked.connect(
            self.okay_button_press)

    def okay_button_press(self):
        self.master.stack.setCurrentIndex(
            self.master.home_screen_index)