
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.app import App
# from kivy.config import Config
# from kivy.uix.textinput import TextInput
# Config.set('graphics', 'resizable', False)
#
# from kivy.core.window import Window
# Window.size = (320, 480)
#
# class Calculator(App):
#     def build(self):
#         self.title = "Калькулятор"
#         main_layout = BoxLayout(orientation="vertical")
#         screen_layout = BoxLayout(size_hint=(1,0.15) )
#         self.input_box = TextInput(multiline=False, readonly=True, halign="right", font_size=30)
#         screen_layout.add_widget(self.input_box)
#
#         keyboard_layout = GridLayout(cols=4, spacing=10, padding=10)
#         buttons = [
#             'C', '(', ')', '/',
#             '7', '8', '9', '*',
#             '4', '5', '6', '-',
#             '1', '2', '3', '+',
#             '0', '.', '='
#         ]
#
#         for button_text in buttons:
#             button = Button(text=button_text, font_size=20)
#             button.bind(on_press=self.button_press)
#             keyboard_layout.add_widget(button)
#
#         main_layout.add_widget(screen_layout)
#         main_layout.add_widget(keyboard_layout)
#         return main_layout
#
#     #логика нажатия кнопок
#     def button_press(self, instance):
#         button_text = instance.text
#
#         if button_text == '=':
#             try:
#                 result = str(eval(self.input_box.text))
#                 self.input_box.text = result
#             except:
#                 self.input_box.text = "Error"
#         elif button_text == 'C':
#             self.input_box.text = ''
#         else:
#             self.input_box.text += button_text
#
# if __name__ == "__main__":
#     Calculator().run()
# ////////////////////////////////////////////////////////////////////////////////
# from kivy.uix.gridlayout import GridLayout
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.graphics import Color, Rectangle
# from kivy.config import Config
# Config.set('graphics', 'resizable', False)
# from kivy.core.window import Window
# Window.size = (400, 400)
#
# class ChessBoard(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.size = (400, 400)
#         self.create_board()
#
#     def create_board(self):
#         with self.canvas:
#             Color(1,1,1,1)
#             Rectangle(pos=self.pos, size=self.size)
#
#             for i in range(8):
#                 for j in range(8):
#                     if (i + j) % 2 == 1:
#                         Color(0, 0, 0, 1)
#                         Rectangle(pos=[self.x + i * self.width / 8, self.y + j * self.height / 8],
#                                   size=[self.width / 8, self.height / 8])
#
# class Chess(App):
#     def build(self):
#         layout = GridLayout(cols=1, spacing=10, padding=10)
#         layout.add_widget(ChessBoard())
#         return layout
#
# if __name__ == "__main__":
#     Chess().run()

# /////////////////////////////////////

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
#
# from kivy.config import Config
# Config.set('graphics', 'resizable', False)
#
# from kivy.core.window import Window
# Window.size = (320, 480)
#
#
# class Concatenator(App):
#     def build(self):
#         self.title = "Конкатенатор"
#         main_layout = BoxLayout(orientation="vertical")
#
#         name_layout = BoxLayout(size_hint=(1, 0.15))
#         self.name_input_box = TextInput(multiline=False, readonly=False, halign="left", font_size=30)
#         name_layout.add_widget(self.name_input_box)
#
#         surname_layout = BoxLayout(size_hint=(1, 0.15))
#         self.surname_input_box = TextInput(multiline=False, readonly=False, halign="left", font_size=30)
#         surname_layout.add_widget(self.surname_input_box)
#
#         button_layout = BoxLayout(size_hint=(1, 0.15))
#         button_con = Button(text="Объединить", font_size=20)
#         button_con.bind(on_press=self.button_press)  # Связываем кнопку с функцией
#         button_clear = Button(text="Очистить", font_size=20)
#         button_clear.bind(on_press=self.button_press)  # Связываем кнопку с функцией
#         button_layout.add_widget(button_con)
#         button_layout.add_widget(button_clear)
#
#         label_layout = BoxLayout(size_hint=(1, 0.15))
#         self.label = Label(text="...", font_size=20)  # Добавляем размер шрифта
#         label_layout.add_widget(self.label)
#
#         main_layout.add_widget(name_layout)
#         main_layout.add_widget(surname_layout)
#         main_layout.add_widget(button_layout)
#         main_layout.add_widget(label_layout)
#         return main_layout
#
#     # логика нажатия кнопок
#     def button_press(self, instance):
#         button_text = instance.text
#
#         if button_text == 'Объединить':
#             result = self.name_input_box.text + " " + self.surname_input_box.text
#             self.label.text = result
#         else:
#             self.name_input_box.text = ''
#             self.surname_input_box.text = ''
#             self.label.text = '...'
#
#
# if __name__ == "__main__":
#     Concatenator().run()


#///////////////////////////////////////////

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = (320, 480)

class TaskManager(App):
    def build(self):
        self.title = "TaskManager"
        main_layout = BoxLayout(orientation="vertical")

        task_layout = BoxLayout(size_hint=(1, 0.15))
        self.task_input_box = TextInput(multiline=False, readonly=False, halign="left", font_size=30)
        task_layout.add_widget(self.task_input_box)

        button_layout = BoxLayout(size_hint=(1, 0.15))
        button_add_task = Button(text="Создать запись", font_size=20)
        button_add_task.bind(on_press=self.button_press)
        button_layout.add_widget(button_add_task)

        label_layout = BoxLayout(size_hint=(1, 0.5))
        self.label = Label(text="", font_size=20)
        label_layout.add_widget(self.label)

        main_layout.add_widget(task_layout)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(label_layout)
        return main_layout

    # логика нажатия кнопок
    def button_press(self, instance):
        task = self.task_input_box.text
        if task:
            self.label.text += f"{len(self.label.text.splitlines())+1}. {task}\n"
            self.task_input_box.text = ''
        else:
            self.label.text += f"{len(self.label.text.splitlines()) + 1}. {'Пустая запись'}\n"
            self.task_input_box.text = ''


if __name__ == "__main__":
    TaskManager().run()

