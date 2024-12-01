import tkinter as tk
import yaml

TITLE = "window title"
GEOMETRY = "window geometry"
CONFIG = "ui config"
THEME = "theme config"
GRID_CONFIG = "grid config"
GRID_LOCATION = "grid location"
WIDGET = "widgets"
TYPE = "type"
INIT = "init"
ROW = "row"
COLUMN = "column"
READ_BINARY = 'rb'


class UserInterface(tk.Tk):
    tkwidgets = {
        "button"      : tk.Button,
        "canvas"      : tk.Canvas,
        "checkbutton" : tk.Checkbutton,
        "entry"       : tk.Entry,
        "frame"       : tk.Frame,
        "label"       : tk.Label,
        "listbox"     : tk.Listbox,
        "menu"        : tk.Menu,
        "menubutton"  : tk.Menubutton,
        "message"     : tk.Message,
        "optionmenu"  : tk.OptionMenu,
        "radiobutton" : tk.Radiobutton,
        "scale"       : tk.Scale,
        "scrollbar"   : tk.Scrollbar,
        "text"        : tk.Text,
        "toplevel"    : tk.Toplevel,
    }
  
    def __init__(self, layout_path):
        super().__init__()
        self.ui_config = self.dict_from_conf(layout_path)
        self.config_keys = self.ui_config.keys()
        self.theme = {} \
            if THEME not in self.config_keys \
            else self.ui_config[THEME]
        self.init_ui()
        self.init_widgets()


    def init_ui(self):
        if TITLE in self.config_keys:
            self.title(self.ui_config[TITLE])
        
        if GEOMETRY in self.config_keys:
            self.geometry(self.ui_config[GEOMETRY])
        
        if CONFIG in self.config_keys:
            self.config(self.ui_config[CONFIG])
        
        if GRID_CONFIG in self.config_keys:
            grid_weights = self.ui_config[GRID_CONFIG]
            for index_, weight in enumerate(grid_weights[ROW]):
                self.rowconfigure(index=index_, weight=weight) 
            
            for index_, weight in enumerate(grid_weights[COLUMN]):
                self.columnconfigure(index=index_, weight=weight) 


    def init_widgets(self):
        self.widgets = {}
        for name, setup in self.ui_config[WIDGET].items():
            self.widgets[name] = self.get_widget(setup[TYPE].lower())
            self.widgets[name].config(self.theme)
            self.widgets[name].config(setup[INIT])
            self.widgets[name].grid(setup[GRID_LOCATION])


    def dict_from_conf(self, path, **kwargs):
        with open(path) as f:
            data = yaml.safe_load(f)
        return data


    def get_widget(self, wtype):
        return self.tkwidgets[wtype](master=self)


if __name__ == '__main__':
    import pathlib
    print(pathlib.Path('.').resolve())
    # UserInterface("./data/tada_ui.json").mainloop()
    UserInterface("./out.yaml").mainloop()
