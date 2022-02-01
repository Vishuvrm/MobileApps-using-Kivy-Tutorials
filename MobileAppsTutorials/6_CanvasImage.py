# link = https://www.geeksforgeeks.org/python-canvas-in-kivy/

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Arranging canvas
        with self.canvas:
            Color(1,0,0,1)
            self.rect = Rectangle(source=".\\Images\\image1.jpg",
                                  pos=self.pos,
                                  size=self.size)
            # Update the canvas as the screen size change
            # if not use this next 5 line the
            # code will run but not cover the full screen
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class CanvasApp(App):
    def build(self):
        return CanvasWidget()

if __name__ == "__main__":
    CanvasApp().run()