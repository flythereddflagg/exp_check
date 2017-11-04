from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
#from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from ls_man import ListManager

Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '400')



class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))



class RV(RecycleView):
    def __init__(self, data, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in data]

        
class ExChGUI(GridLayout):
    def __init__(self, lm, rv):
        self.lm = lm
        self.rv = rv
        self.init_gui()
    
    def init_gui(self):
        super(ExChGUI, self).__init__(rows=3)
        
        self.add_button = Button(text="ADD", font_size=14,
            size_hint_y=0.1)
        self.add_button.bind(on_press=self.callback)
        self.add_widget(self.add_button)
        
        self.add_button2 = Button(text="Delete", font_size=14,
            size_hint_y=0.1)
        self.add_button2.bind(on_press=self.callback)
        self.add_widget(self.add_button2)
        
        self.add_widget(self.rv)
        
    def callback(self, instance):
        if instance.text == "ADD":
            do_a_thing()
        elif instance.text == "Delete":
            print("You pressed delete!")
        else:
            print('The button <%s> is being pressed' % instance.text)


class ExpCheckApp(App):
    def build(self):
        lm = ListManager("lst.csv")
        data = lm.to_string().split('\n')
        rv = RV(data)
        gui = ExChGUI(lm, rv)
        return gui


if __name__ == '__main__':
    ExpCheckApp().run()
