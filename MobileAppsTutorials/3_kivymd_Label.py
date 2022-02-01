# Link = https://www.geeksforgeeks.org/python-add-label-to-a-kivy-window/

# KivyMD is an extension of the Kivy framework. KivyMD is a collection of Material Design widgets for use with Kivy, a GUI framework for making mobile applications.

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

class Demo(MDApp):
    def build(self):
        # defining screen
        screen = Screen()

        # Defining 1st label
        l1 = MDLabel(text="Welcome-1",
                     pos_hint = {"center_x":0.8,
                                 "center_y": 0.8},
                     theme_text_color = "Custom",
                     text_color = (0.5,0,0.5,1),
                     font_style = "Caption")

        # defining 2nd label
        l2 = MDLabel(text="Welcome-2",
                     pos_hint = {"center_x":0.8,
                                 "center_y": 0.5},
                     theme_text_color = "Custom",
                     text_color = (0.5,0,0.5,1),
                     font_style = "H2")

        # defining 3rd Label
        l3 = MDLabel(text = "Welcome-3",
                     pos_hint = {"center_x":0.8,
                                 "center_y":0.2},
                     theme_text_color="Custom",
                     text_color=(0.5,0,0.5,1),
                     font_style = "H1")
        screen.add_widget(l1)
        screen.add_widget(l2)
        screen.add_widget(l3)

        return screen

if __name__ == "__main__":
    Demo().run()