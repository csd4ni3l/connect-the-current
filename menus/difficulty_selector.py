import arcade, arcade.gui

from utils.preload import button_texture, button_hovered_texture
from utils.constants import big_button_style, button_style

class DifficultySelector(arcade.gui.UIView):
    def __init__(self, pypresence_client):
        super().__init__()

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout())
        self.box = self.anchor.add(arcade.gui.UIBoxLayout(space_between=10), anchor_x='center', anchor_y='center')

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state='In Menu', details='In Difficulty Selector', start=self.pypresence_client.start_time)

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        self.box.add(arcade.gui.UILabel(text="Difficulty Selector", font_size=32))

        for difficulty in ["3x3", "4x4", "5x5", "6x6", "9x9"]:
            button = self.box.add(arcade.gui.UITextureButton(text=difficulty, width=self.window.width / 2, height=self.window.height / 10, texture=button_texture, texture_hovered=button_hovered_texture, style=big_button_style))
            button.on_click = lambda e, difficulty=difficulty: self.play(difficulty)

    def play(self, difficulty):
        from game.play import Game
        self.window.show_view(Game(self.pypresence_client, difficulty))

    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))