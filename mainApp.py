from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from db import database
db = database('notes.db')

from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = (1240, 480)

class TaskManager(App):
    def build(self):
        self.title = "TaskManager"
        main_layout = BoxLayout(orientation="vertical")

        task_layout = BoxLayout(size_hint=(1, 0.25))
        self.task_input_box = TextInput(multiline=False, readonly=False, halign="left", font_size=30)
        task_layout.add_widget(self.task_input_box)

        button_layout = BoxLayout(size_hint=(1, 0.25))
        button_add_task = Button(text="Создать запись", font_size=20, size_hint=(1,1))
        button_add_task.bind(on_press=self.button_press)
        button_layout.add_widget(button_add_task)

        label_layout = BoxLayout(orientation="vertical",size_hint=(1, 0.5))
        notes = db.read_notes()
        self.label = Label(text=notes, font_size=20)
        label_layout.add_widget(self.label)

        clear_button = Button(text="Очистить БД",size_hint=(1, 1))
        clear_button.bind(on_press=self.clear_table)
        label_layout.add_widget(clear_button)

        main_layout.add_widget(task_layout)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(label_layout)
        return main_layout

    # логика нажатия кнопок
    def button_press(self, instance):
        task = self.task_input_box.text
        if task:
            db.create_note(task)
            notes = db.read_notes()
            self.label.text = notes
            self.task_input_box.text = ''

    def clear_table(self, instance):
        db.delete_all_notes()
        self.label.text=''
        self.task_input_box.text = ''



if __name__ == "__main__":
    TaskManager().run()

