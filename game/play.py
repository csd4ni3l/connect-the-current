import arcade, arcade.gui, json, time, os

from utils.constants import button_style, NEIGHBOURS
from utils.preload import button_texture, button_hovered_texture

from collections import deque

from game.level_generator import generate_map
from game.cells import *

class Game(arcade.gui.UIView):
    def __init__(self, pypresence_client, grid_size, source_count=None, house_count=None):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.pypresence_client.update(state='In Game', start=self.pypresence_client.start_time)

        self.grid_size = grid_size
        self.source_count = source_count
        self.house_count = house_count

        self.start = time.perf_counter()
        self.wire_rotations = 0
        self.won = False
    
        self.cells = []
        self.power_sources = []
        self.houses = []
        
        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.map = generate_map(self.grid_size, int((self.grid_size * self.grid_size) / 10) if not source_count else source_count, int((self.grid_size * self.grid_size) / 5) if not house_count else house_count)

        self.spritelist = arcade.SpriteList()

        with open("settings.json", "r") as file:
            self.settings = json.load(file)

        self.first_time = False
        self.custom = False
        
        if source_count is None:
            if os.path.exists("data.json"):
                with open("data.json") as file:
                    self.data = json.load(file)
            else:
                self.data = {}

            if self.data.get(f"best_time_{self.grid_size}", None) == None:
                self.best_time = self.data[f"best_time_{self.grid_size}"] = 99999
                self.first_time = True
            else:
                self.best_time = self.data[f"best_time_{self.grid_size}"]
        else:
            self.custom = True
            self.best_time = None

    def on_show_view(self):
        super().on_show_view()

        self.back_button = arcade.gui.UITextureButton(texture=button_texture, texture_hovered=button_hovered_texture, text='<--', style=button_style, width=100, height=50)
        self.back_button.on_click = lambda event: self.main_exit()
        self.anchor.add(self.back_button, anchor_x="left", anchor_y="top", align_x=5, align_y=-5)

        self.won_label = self.anchor.add(arcade.gui.UILabel(text="You won!", font_size=48), anchor_x="center", anchor_y="center")
        self.won_label.visible = False

        if not self.custom:
            self.info_label = self.anchor.add(arcade.gui.UILabel(f"Time spent: 0s Best time: {self.best_time}s Wire Rotations: 0", font_size=24), anchor_x="center", anchor_y="top")
        else:
            self.info_label = self.anchor.add(arcade.gui.UILabel(f"Time spent: 0s Wire Rotations: 0", font_size=24), anchor_x="center", anchor_y="top")

        x = (self.window.width / 2) - (self.grid_size * 32) 
        y = (self.window.height / 2) + (self.grid_size * 32) - 32 # extra 32 needed because the first iteration will not be higher by 32

        for row in range(self.grid_size):
            self.cells.append([])
            
            for col in range(self.grid_size):
                left_neighbour = self.cells[row][col - 1] if col > 0 else None
                top_neighbour = self.cells[row - 1][col] if row > 0 else None

                cell_type = self.map[row][col]

                if cell_type in ["line", "corner", "t_junction", "cross"]:
                    cell = PowerLine(cell_type, x, y, left_neighbour, top_neighbour)
                elif cell_type == "power_source":
                    cell = PowerSource(x, y, left_neighbour, top_neighbour)
                    self.power_sources.append(cell)
                elif cell_type == "house":
                    cell = House(x, y, left_neighbour, top_neighbour)
                    self.houses.append(cell)

                self.spritelist.append(cell)
                self.cells[row].append(cell)

                if left_neighbour:
                    left_neighbour.right_neighbour = cell
                if top_neighbour:
                    top_neighbour.bottom_neighbour = cell
                
                x += 64

            x = (self.window.width / 2) - (self.grid_size * 64) / 2
            y -= 64

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

        self.check_win()

    def check_win(self):
        for row in self.cells:
            for cell in row:
                if cell.cell_type == "power_source":
                    continue
                elif cell.cell_type == "house":
                    if not len(cell.get_connected_neighbours()) >= 1:
                        return
                    else:
                        continue

                if len(cell.get_connected_neighbours(True)) != len(NEIGHBOURS[cell.rotation]):
                    return

        self.won_label.visible = True
        self.spritelist.visible = False
        self.won = True

        if not self.custom and int(time.perf_counter() - self.start) < self.best_time:
            self.data[f"best_time_{self.grid_size}"] = self.best_time = int(time.perf_counter() - self.start)
            self.info_label.text = f"Time left: {int(time.perf_counter() - self.start)}s Best time: {self.best_time}s Wire Rotations: {self.wire_rotations}"

            with open("data.json", "w") as file:
                file.write(json.dumps(self.data, indent=4))

        arcade.unschedule(self.update_grid)

    def on_mouse_press(self, x, y, button, modifiers):
        for row in self.cells:
            for cell in row:
                if cell.cell_type in ["house", "power_source"]:
                    continue

                if cell.rect.point_in_rect((x, y)):
                    self.wire_rotations += 1
                    cell.next_rotation(self.settings["sfx"], self.settings.get("sfx_volume", 50))        

    def on_draw(self):
        super().on_draw()
        self.spritelist.draw()

    def on_update(self, delta_time):
        if self.won:
            return
        
        if self.first_time:
            self.best_time = int(time.perf_counter() - self.start)

        if not self.custom:
            self.info_label.text = f"Time left: {int(time.perf_counter() - self.start)}s Best time: {self.best_time}s Wire Rotations: {self.wire_rotations}"
        else:
            self.info_label.text = f"Time left: {int(time.perf_counter() - self.start)}s Wire Rotations: {self.wire_rotations}"

    def main_exit(self):
        from menus.main import Main
        self.window.show_view(Main(self.pypresence_client))