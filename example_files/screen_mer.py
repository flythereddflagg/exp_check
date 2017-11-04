from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<ListScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<AddScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class ListScreen(Screen):
    pass

class AddScreen(Screen):
    pass

# Create the screen manager

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ListScreen(name='menu'))
        sm.add_widget(AddScreen(name='settings'))
        return sm

if __name__ == '__main__':
    TestApp().run()