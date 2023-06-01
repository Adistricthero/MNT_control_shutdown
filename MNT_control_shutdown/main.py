import pickle

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MainWindow(Screen):
    def __init__(self):
        super().__init__()
        self.load_file()

    def load_file(self):
        load_data = load_data_from_db()

        self.ids.box.height = dp(len(load_data) * 150 + 20)

        for child in self.children:
            if 'grl' in child.ids.keys():
                self.clear_widgets(children=child)

        for i, row_dict in enumerate(load_data):
            gl = GridLayout_Table(ids={'grl': i})
            for child in gl.walk():
                if 'Label' in str(child.__class__) or 'TextInput' in str(child.__class__):

                    if child.text == 'Дата':
                        child.text = str(row_dict.get('date'))
                    if child.text == 'Производство':
                        child.text = str(row_dict.get('prd'))
                    if child.text == 'Комментарий':
                        child.text = str(row_dict.get('comment'))

            self.ids.box.add_widget(gl)
            for child in self.children:
                if 'grl' in child.ids.keys():
                    cur = child
                    cur.text = child.ids.get('grl')




class GridLayout_Table(GridLayout):
    # def __init__(self):
    #     super().__init__()

    def view_wr(self):
        print(self.ids.get('grl'))

class AddWindow(Screen):



    def input_inform(self):
        records_db.update({'date': self.ids.txt_date.text})
        records_db.update({'prd': self.ids.txt_prd.text})
        records_db.update({'comment': self.ids.txt_comment.text})
        print(records_db)

    def save_data(self):
        with open('data.db', 'ba+') as f:
            obj = pickle.dumps(records_db)
            f.write(obj)
            print(obj)
            print(records_db)




records_db = {'date': '',
              'prd': '',
              'comment': ''}

#kv = Builder.load_file('mnt.kv')


class MntApp(App):
    def build(self):
        sm = ScreenManager()
        main = MainWindow()
        sm.add_widget(main)

        sm.add_widget(AddWindow())
        return sm


def load_data_from_db():
    list_records_db = []
    with open('data.db', 'br+') as f:
        while True:
            try:
                list_records_db.append(pickle.load(f))

            except EOFError:
                break

    return list_records_db

if __name__ == '__main__':
    MntApp().run()



