from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from ls_man import ListManager

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')


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

            
class Buttons(BoxLayout):
    def __init__(self):
        self.init_gui()
    
    def init_gui(self):
        super(Buttons, self).__init__(orientation='horizontal')
        
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

        
class ExChGUI(BoxLayout):
    def __init__(self, lm, rv, btn):
        self.lm = lm
        self.rv = rv
        self.btn = btn
        self.init_gui()
    
    def init_gui(self):
        super(ExChGUI, self).__init__(orientation='vertical')
        
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