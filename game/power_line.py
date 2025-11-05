import arcade, arcade.gui

from utils.preload import vertical_connected, vertical_unconnected, horizontal_connected, horizontal_unconnected

from typing import Literal

class PowerLine(arcade.gui.UITextureButton):
    def __init__(self):
        super().__init__(texture=vertical_unconnected)

        self.rotation: Literal["vertical", "horizontal"] = "vertical"
        self.connected = False

        self.on_click = lambda e: self.next_rotation()

    def next_rotation(self):
        if self.rotation == "vertical":
            self.rotation = "horizontal"
            self.texture = horizontal_connected if self.connected else horizontal_unconnected
            self.texture_hovered = horizontal_connected if self.connected else horizontal_unconnected
        elif self.rotation == "horizontal":
            self.rotation = "vertical"
            self.texture = vertical_connected if self.connected else vertical_unconnected
            self.texture_hovered = vertical_connected if self.connected else vertical_unconnected

        self._requires_render = True