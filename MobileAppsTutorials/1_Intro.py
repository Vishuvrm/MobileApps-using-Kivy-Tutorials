# Import the kivy module
import kivy

# Below restricts the kivy version, i.e. bBelow this version of kivy, you cannot use the app or the software
kivy.require("1.10.0")

# Base class of your app inherits from the App class.
# app: always refers to the instance of your application.
from kivy.app import App

# The Label widget is for rendering text. It supports ASCII and unicode strings. The label is the text which we want
# to add to our window, give to the buttons, and so on. On labels, we can apply the styling also i.e increase text,
# size, color, and more.
from kivy.uix.button import Label


# Inherit kivy's App class which represents the window for our widgets
# HelloKivy inherits all the fields and methods from Kivy
class HelloKivy(App):

    # This returns the contents we want in our window.
    def build(self):
        """Returns the content we want in our window."""
        return Label(text="Hello Kivy!!")


hellokivy = HelloKivy()
hellokivy.run()
