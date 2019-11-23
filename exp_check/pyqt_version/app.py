from constants import *
from home_screen import HomeScreen
from add_screen import AddScreen

class FoodGui():
    def __init__(self):
        self.home = HomeScreen(self)
        self.add_screen = AddScreen(self)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(self.home)
        self.stack.addWidget(self.add_screen)
        self.stack.show()


if __name__ == '__main__':
    app = QApplication([])
    gui = FoodGui()
    sys.exit(app.exec_())