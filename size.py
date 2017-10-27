"""from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from ls_man import ListManager


Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleGridLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

     
class Buttons(GridLayout):
    def __init__(self):
        self.init_gui()
    
    def init_gui(self):
        super(Buttons, self).__init__(cols=2)
        
        self.add_button = Button(text="ADD", font_size=14)
        self.add_button.bind(on_press=self.callback)
        self.add_widget(self.add_button)
        
        self.add_button2 = Button(text="Delete", font_size=14)
        self.add_button2.bind(on_press=self.callback)
        self.add_widget(self.add_button2)
        
    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)


class RV(RecycleView):
    def __init__(self, data, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in data]

        
class ExChGUI(GridLayout):
    def __init__(self, lm, rv, btn):
        self.lm = lm
        self.rv = rv
        self.btn = btn
        self.init_gui()
    
    def init_gui(self):
        super(ExChGUI, self).__init__(cols=1)
        
        self.add_widget(self.btn)
        self.add_widget(self.rv)


class ExpCheckApp(App):
    def build(self):
        lm = ListManager("lst.csv")
        data = lm.to_string().split('\n')
        rv = RV(data)
        btn = Buttons()
        gui = ExChGUI(lm, rv,btn)
        return gui


if __name__ == '__main__':
    ExpCheckApp().run()
    """
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView


Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()

