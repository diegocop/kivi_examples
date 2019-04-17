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

        # add widgets
        # on_release=	que cria evento da função
        button1 = Button(text='botao 01', font_size=30, on_release=self.increment)
        # self.label1  self torna label uma variavel da intancia da classe
        self.label1 = Label(text="1", font_size=30)

        # add o widget into layout box
        box.add_widget(button1)
        box.add_widget(self.label1)

        return box

    def increment(self, button1):
        button1.text = 'soltar'
        self.label1.text = str(int(self.label1.text) + 1)


# run method is App´s method
Test().run()		