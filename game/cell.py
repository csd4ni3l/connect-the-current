import arcade, arcade.gui

from utils.constants import ROTATIONS, NEIGHBOURS
from utils.preload import TEXTURE_MAP

def get_opposite(direction):
    if direction == "l":
        return "r"
    elif direction == "r":
        return "l"
    elif direction == "t":
        return "b"
    elif direction == "b":
        return "t"

class Cell(arcade.gui.UITextureButton):
    def __init__(self, cell_type, left_neighbour, top_neighbour):
        super().__init__(texture=TEXTURE_MAP[cell_type, ROTATIONS[cell_type][0], cell_type == "power_source"])

        self.rotation = ROTATIONS[cell_type][0]
        self.cell_type = cell_type
        self.powered = False
        self.left_neighbour, self.top_neighbour = left_neighbour, top_neighbour
        self.right_neighbour, self.bottom_neighbour = None, None

    def get_neighbour(self, name):
        if name == "l":
            return self.left_neighbour
        elif name == "r":
            return self.right_neighbour
        elif name == "b":
            return self.bottom_neighbour
        elif name == "t":
            return self.top_neighbour
        
    def get_connected_neighbours(self):
        return [
                self.get_neighbour(neighbour_direction) for neighbour_direction in NEIGHBOURS[self.rotation] 
                if (
                    self.get_neighbour(neighbour_direction) and 
                    get_opposite(neighbour_direction) in NEIGHBOURS[self.get_neighbour(neighbour_direction).rotation]
                )
        ]

    def update_value(self):
        self.powered = any([neighbour.powered for neighbour in self.get_connected_neighbours()])

    def update_visual(self):
        self.texture = TEXTURE_MAP[(self.cell_type, self.rotation, self.powered)]
        self.texture_hovered = TEXTURE_MAP[(self.cell_type, self.rotation, self.powered)]
        self.texture_pressed = TEXTURE_MAP[(self.cell_type, self.rotation, self.powered)]
        self._requires_render = True

    def next_rotation(self):
        current_index = ROTATIONS[self.cell_type].index(self.rotation)

        if current_index + 1 == len(ROTATIONS[self.cell_type]):
            self.rotation = ROTATIONS[self.cell_type][0]
        else:
            self.rotation = ROTATIONS[self.cell_type][current_index + 1]

        self.update_visual()