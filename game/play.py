import arcade, arcade.gui, random

from utils.constants import button_style
from utils.preload import button_texture, button_hovered_texture

from collections import deque

from game.level_generator import generate_map
from game.cells import *

class Game(arcade.gui.UIView):
    def __init__(self, pypresence_client, difficulty):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state='In Game', start=self.pypresence_client.start_time)

        self.difficulty = difficulty
        self.cells = []
        self.power_sources = []
        self.houses = []

        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.grid_size = int(difficulty.split("x")[0])
        self.grid = generate_map(self.grid_size, int((self.grid_size * self.grid_size) / 10), int((self.grid_size * self.grid_size) / 5))

        self.power_grid = self.anchor.add(arcade.gui.UIGridLayout(horizontal_spacing=0, vertical_spacing=0, row_count=self.grid_size, column_count=self.grid_size))

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        for row in range(self.grid_size):
            self.cells.append([])
            for col in range(self.grid_size):
                left_neighbour = self.cells[row][col - 1] if col > 0 else None
                top_neighbour = self.cells[row - 1][col] if row > 0 else None

                cell_type = self.grid[row][col]

                if cell_type in ["line", "corner", "t_junction", "cross"]:
                    cell = PowerLine(cell_type, left_neighbour, top_neighbour)
                elif cell_type == "power_source":
                    cell = PowerSource(left_neighbour, top_neighbour)
                    self.power_sources.append(cell)
                elif cell_type == "house":
                    cell = House(left_neighbour, top_neighbour)
                    self.houses.append(cell)

                self.power_grid.add(cell, row=row, column=col)
                self.cells[row].append(cell)

                if left_neighbour:
                    left_neighbour.right_neighbour = cell
                if top_neighbour:
                    top_neighbour.bottom_neighbour = cell

        arcade.schedule(self.update_grid, 1 / 8)

    def update_grid(self, _):
        for row in self.cells:
            for power_line in row:
                if power_line.cell_type != "power_source":
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

        for row in self.cells:
            for cell in row:
                cell.update_visual()


    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))