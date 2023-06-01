from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Загрузка файла kv design language
Builder.load_file('box.kv')


class MyLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
