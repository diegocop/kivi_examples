# import app maneger the windows with containers
from kivy.app import App
# import layout
from kivy.uix.boxlayout import BoxLayout


class incrementador(BoxLayout):
    pass


# the class herence from APP
class Teste(App):
    # build method buld all widgets
    def build(self):
        return incrementador()


# run method is App´s method
Teste().run()