from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView



class Tarefas(ScrollView):
    def __init__(self, tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text='[i][color=ff3333]Hello[/color][/i][ref=world][color=0000ff]World[/color][/ref]',
    markup = True, font_size=30,size_hint_y=None,height=200))



class Test(App):
    def build(self):
        return Tarefas(['fazer compras','buscar filho','buscar filho','buscar filho','buscar filho','buscar filho'])
Test().run()
