# Пример использования BoxLayout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.properties import ObjectProperty
# class MyBoxLayout(BoxLayout):
#     button1 = ObjectProperty()
#     button2 = ObjectProperty()
#     def on_button_click(self, button1):
#         if self.textinput.text=="":
#             self.textinput.text = "Hello, Kivy!"
#         else:
#             self.textinput.text = ""
#     def off_button_click(self, button2):
#         self.textinput.text = ""
#
# class MyApp(App):
#     def build(self):
#         layout = MyBoxLayout()
#         button1 = Button(text="Click me!")
#         button1.bind(on_press=layout.on_button_click)
#         layout.add_widget(button1)
#         layout.textinput = TextInput()
#         layout.add_widget(layout.textinput)
#         button2 = Button(text="None")
#         button2.bind(on_press=layout.off_button_click)
#         layout.add_widget(button2)
#         return layout
#
# if __name__ == "__main__":
#     MyApp().run()

#Пример использования GridLayout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# ROWS = COLS = 10
# class GridApp(App):
#     def build(self):
#         root = GridLayout(rows=ROWS, cols=COLS)
#         for i in range(ROWS):
#             for j in range(COLS):
#                 root.add_widget(Button(text=str(i)+str(j)))
#         return root
#
# GridApp().run()

# Пример использования StackLayout:
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.button import Button
# from kivy.app import App
#
# class StackApp(App):
#     def build(self):
#         layout = StackLayout(orientation="lr-tb")
#         for i in range(25):
#             btn = Button(text=str(i), width=40 + i*6,
#                          size_hint=(None, 0.15))
#             layout.add_widget(btn)
#         return layout
#
# StackApp().run()

# В слои также можно добавлять другие слои с помощью метода
# add_widget(). Это позволяет комбинировать разные варианты разметки в
# случае, если возможностей одного слоя недостаточно:

#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
from kivy.uix.textinput import TextInput
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = (320, 480)

class Calculator(App):
    def build(self):
        self.title = "Калькулятор"
        
        main_layout = GridLayout(cols=4, spacing=10, padding=10)
        self.input_box = TextInput(multiline=False, readonly=True, halign="right", font_size=30)
        main_layout.add_widget(self.input_box)
        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=20)
            button.bind(on_press=self.button_press)
            main_layout.add_widget(button)
        
        return main_layout
        
    #логика нажатия кнопок
    def button_press(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(self.input_box.text))
                self.input_box.text = result
            except:
                self.input_box.text = "Error"
        elif button_text == 'C':
            self.input_box.text = ''
        else:
            self.input_box.text += button_text
            
if __name__ == "__main__":
    Calculator().run()
