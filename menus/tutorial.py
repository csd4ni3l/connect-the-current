import arcade, arcade.gui

from utils.preload import button_texture, button_hovered_texture
from utils.constants import button_style

TUTORIAL_TEXT = """
In Connect the Current, you have to rotate power lines so power reaches to all of the houses.
- Every line has to be connected on all of it's sides.
- Every power source and house must have at least one connection
- Houses dont share electricity, like power lines.
- When needed, you might have to create loops of power or branches with no house linked to them. 
(This is also because it's randomly generated and i couldn't find a way to generate maps with no meaningless branches)
- To rotate a line, just click on it and it will change its rotation.
- Maps are randomly generated, difficulty(size, source count, house count) depends on what you pick and grows exponentially.
"""

class Tutorial(arcade.gui.UIView):
    def __init__(self, pypresence_client):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state="Checking Tutorial")

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.box = self.anchor.add(arcade.gui.UIBoxLayout(space_between=20), anchor_x="center", anchor_y="top")

    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        self.box.add(arcade.gui.UILabel(text="CTC Tutorial", font_size=40))
        self.box.add(arcade.gui.UILabel(text=TUTORIAL_TEXT, font_size=20, multiline=True))