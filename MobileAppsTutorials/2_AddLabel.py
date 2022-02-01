# Link = https://www.geeksforgeeks.org/python-add-label-to-a-kivy-window/

import kivy

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        # Label display the text on the screen
        lbl = Label(text="Label is added on the screen !!")
        return lbl

    def build(self):  # Do some styling on the Label
        l2 = Label(text="Label is added on the screen!!!\n"
                        "And it is multiline",
                   font_size="20sp",
                   color=[0.41, 0.42, 0.74, 1])
        return l2

    def build(self): # Markup the text
        l3 = Label(text="[color = #ff3333][b]'Label'[/b]' is Added '[/color]\n"
                        "[color = #3333ff]' to the '[b]'SCREEN!!!'[/b][/color]",
                   font_size="20sp",
                   markup = True)
        # markup text with different colour
        # l2 = Label(text="[color = ff3333][b]'Label'[/b] is Added [/color]\n"
        #                 "[color = 3333ff]Screen !!:):):):)[ / color]",
        #            font_size = '20sp', markup = True)
        return l3


if __name__ == "__main__":
    label = MyLabelApp()
    label.run()
