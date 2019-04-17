# import app maneger the windows with containers
from kivy.app import App
# import widgets like button
from kivy.uix.button import Button
from kivy.uix.label import Label
# import layout
from kivy.uix.boxlayout import BoxLayout


# the class herence from APP
class Test(App):
    # build method buld all widgets
    def build(self):
        # add layout
        box = BoxLayout(orientation='vertical')
        box2 = BoxLayout(orientation='vertical')
        # add widgets
        button1 = Button(text='botao 01')
        button2 = Button(text='botao 02')

        label1 = Label(text="label1")
        label2 = Label(text="label2")
        # add o widget into layout box
        box.add_widget(button1)
        box.add_widget(button2)
        box2.add_widget(label1)
        box2.add_widget(label2)
        box.add_widget(box2)
        return box


# run method is App´s method
Test().run()		