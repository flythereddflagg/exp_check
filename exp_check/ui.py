import tkinter as tk
import tomllib

TITLE = "title"
GEOMETRY = "geometry"
CONFIG = "config"
THEME = "theme"
GRID = "grid"
WIDGET = "widgets"
TYPE = "type"
INIT = "init"
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
        "radiobutton" : tk.Radiobutton,
        "scale"       : tk.Scale,
        "scrollbar"   : tk.Scrollbar,
        "text"        : tk.Text,
        "toplevel"    : tk.Toplevel,
    }
  
    def __init__(self, layout_path):
        super().__init__()
        self.ui_config = self.dict_from_jsonfile(layout_path)
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
        
        if GRID in self.config_keys:
            for kw in self.ui_config[GRID][ROW]:
                self.rowconfigure(**kw)
            
            for kw in self.ui_config[GRID][COLUMN]:
                self.columnconfigure(**kw)  


    def init_widgets(self):
        self.widgets = {}
        for name, setup in self.ui_config[WIDGET].items():
            self.widgets[name] = self.get_widget(setup[TYPE].lower())
            self.widgets[name].config(self.theme)
            self.widgets[name].config(setup[INIT])
            self.widgets[name].grid(setup[GRID])


    def dict_from_jsonfile(self, path, **kwargs):
        with open(path, READ_BINARY) as f:
            data = tomllib.load(f, **kwargs)
        return data


    def get_widget(self, wtype):
        return self.tkwidgets[wtype](master=self)


if __name__ == '__main__':
    import pathlib
    print(pathlib.Path('.').resolve())
    UserInterface("./ui.toml").mainloop()
