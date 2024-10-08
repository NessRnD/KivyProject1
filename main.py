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

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = (320, 480)

class Calculator(App):
    def build(self):
        superBox = BoxLayout(orientation='vertical')

        # окно вывода информации калькулятора
        screen = Label(text="0", size_hint=(1,0.1))

        num_buttons = GridLayout(rows=6, cols=5)
        btn1 = Button(text="MR")
        btn2 = Button(text="MC")
        btn3 = Button(text="MS")
        btn4 = Button(text="M+")
        btn5 = Button(text="M-")

        btn6 = Button(text='<-')
        btn7 = Button(text='CE')
        btn8 = Button(text='C')
        btn9 = Button(text=chr(177))
        btn10 = Button(text='V')

        btn11 = Button(text='7')
        btn12 = Button(text='8')
        btn13 = Button(text='9')
        btn14 = Button(text='/')
        btn15 = Button(text='%')

        btn16 = Button(text='4')
        btn17 = Button(text='5')
        btn18 = Button(text='6')
        btn19 = Button(text='*')
        btn20 = Button(text='1/x')

        num_buttons.add_widget(btn1)
        num_buttons.add_widget(btn2)
        num_buttons.add_widget(btn3)
        num_buttons.add_widget(btn4)
        num_buttons.add_widget(btn5)
        num_buttons.add_widget(btn6)
        num_buttons.add_widget(btn7)
        num_buttons.add_widget(btn8)
        num_buttons.add_widget(btn9)
        num_buttons.add_widget(btn10)

        superBox.add_widget(screen)
        superBox.add_widget(num_buttons)
        return superBox

Calculator().run()