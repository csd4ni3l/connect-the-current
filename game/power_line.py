import arcade, arcade.gui

from utils.preload import button_texture, button_hovered_texture
from utils.constants import button_style

from typing import Literal

ROTATIONS = ["right", "down", "left", "up"]

class PowerLine(arcade.gui.UITextureButton):
    def __init__(self):
        super().__init__(text="--->", style=button_style, texture=button_texture, texture_hovered=button_hovered_texture)

        self.rotation: Literal["right", "down", "left", "up"] = "right"

        self.on_click = lambda e: self.next_rotation()

    def next_rotation(self):
        current_index = ROTATIONS.index(self.rotation)

        if current_index + 1 == len(ROTATIONS):
            self.rotation = ROTATIONS[0]
        else:
            self.rotation = ROTATIONS[current_index + 1]

        if self.rotation == "up":
            self.text = "^"
        elif self.rotation == "down":
            self.text = "ˇ"
        elif self.rotation == "left":
            self.text = "<---"
        elif self.rotation == "right":
            self.text = "--->"