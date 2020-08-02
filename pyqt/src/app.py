from constants import *
from home_screen import HomeScreen
from add_screen import AddScreen
from msg_screen import MsgScreen


class FoodGui():
    def __init__(self):
        self.home_screen = HomeScreen(self)
        self.add_screen = AddScreen(self)
        self.msg_screen = MsgScreen(self)
        self.home_screen_index,\
            self.add_screen_index,\
            self.msg_screen_index = range(3)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.add_screen)
        self.stack.addWidget(self.msg_screen)
        self.stack.show()


def main():
    app = QApplication([])
    gui = FoodGui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()