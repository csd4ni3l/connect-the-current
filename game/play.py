import arcade, arcade.gui, random

from utils.constants import button_style
from utils.preload import button_texture, button_hovered_texture

from collections import deque

from game.power_line import PowerLine

class Game(arcade.gui.UIView):
    def __init__(self, pypresence_client, difficulty):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state='In Game', start=self.pypresence_client.start_time)

        self.difficulty = difficulty
        self.power_lines = []
        self.power_sources = []

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.grid_size = list(map(int, difficulty.split("x")))
        self.power_grid = self.anchor.add(arcade.gui.UIGridLayout(horizontal_spacing=0, vertical_spacing=0, row_count=self.grid_size[0], column_count=self.grid_size[1]))

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        for row in range(self.grid_size[0]):
            self.power_lines.append([])
            for col in range(self.grid_size[1]):
                left_neighbour = self.power_lines[row][col - 1] if col > 0 else None
                top_neighbour = self.power_lines[row - 1][col] if row > 0 else None

                line_type = random.choice(["line", "corner", "power_source"])
                power_line = PowerLine(line_type, left_neighbour, top_neighbour)

                if line_type == "power_source":
                    self.power_sources.append(power_line)

                self.power_grid.add(power_line, row=row, column=col)
                self.power_lines[row].append(power_line)

                if left_neighbour:
                    left_neighbour.right_neighbour = power_line
                if top_neighbour:
                    top_neighbour.bottom_neighbour = power_line

        arcade.schedule(self.update_grid, 1 / 10)

    def update_grid(self, _):
        for row in self.power_lines:
            for power_line in row:
                if power_line.line_type != "power_source":
                    power_line.powered = False

        queue = deque(self.power_sources)
        visited = set()
        
        while queue:
            current = queue.popleft()
            
            if id(current) in visited:
                continue

            visited.add(id(current))
            
            current.powered = True
            
            for connected_neighbour in current.get_connected_neighbours():
                if id(connected_neighbour) not in visited:
                    queue.append(connected_neighbour)

        for row in self.power_lines:
            for power_line in row:
                power_line.update_visual()

    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))