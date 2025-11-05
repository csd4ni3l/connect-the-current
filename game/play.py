import arcade, arcade.gui, pyglet

from utils.constants import button_style
from utils.preload import button_texture, button_hovered_texture
from game.power_line import PowerLine

class Game(arcade.gui.UIView):
    def __init__(self, pypresence_client, difficulty):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state="In Game")

        self.difficulty = difficulty

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.grid_size = list(map(int, difficulty.split("x")))
        self.power_grid = self.anchor.add(arcade.gui.UIGridLayout(horizontal_spacing=0, vertical_spacing=0, row_count=self.grid_size[0], column_count=self.grid_size[1]))


    def on_show_view(self):
        super().on_show_view()

        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                self.power_grid.add(PowerLine(), row=row, column=col)
