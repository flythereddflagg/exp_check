from exp_check.ui import UserInterface

class MainWindow(UserInterface):
    def __init__(self, toml_path):
        super().__init__(toml_path)
        self.widgets["add_button"].configure(command=self.add_button_pressed)

    def add_button_pressed(self, event=None):
        print("you pressed the add button!")


if __name__ == "__main__":
    my_window = MainWindow("./ui.toml")
    my_window.mainloop()

