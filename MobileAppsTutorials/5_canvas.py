import kivy
kivy.require("1.9.1")

from kivy.app import App

# A Widget is the base building block
# of GUI interfaces in Kivy.
# It provides a Canvas that
# can be used to draw on screen.
from kivy.uix.widget import Widget

# From graphics module we are importing
# Rectangle and Color as they are
# basic building of canvas.
from kivy.graphics import Rectangle, Color

class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Arranging Canvas
        with self.canvas:
            Color(.234, .456, .678, .8) # Set the colour

            # Setting the size and position of canvas
            self.rect = Rectangle(pos=self.center,
                                  size=(self.width/2, self.height/2))

            # Update the canvas as the screen size changes
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    # Update function, which makes canvas adjustable
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Create the App class
class CanvasApp(App):
    def build(self):
        return CanvasWidget()

if __name__ == "__main__":
    CanvasApp().run()
