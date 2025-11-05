import arcade, arcade.gui

from utils.constants import button_style
from utils.preload import button_texture, button_hovered_texture

from game.power_line import PowerLine

class Game(arcade.gui.UIView):
    def __init__(self, pypresence_client, difficulty):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state='In Game', start=self.pypresence_client.start_time)

        self.difficulty = difficulty

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.grid_size = list(map(int, difficulty.split("x")))
        self.power_grid = self.anchor.add(arcade.gui.UIGridLayout(horizontal_spacing=0, vertical_spacing=0, row_count=self.grid_size[0], column_count=self.grid_size[1]))

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                self.power_grid.add(PowerLine(), row=row, column=col)

    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))