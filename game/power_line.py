import arcade, arcade.gui

from utils.preload import *

TEXTURE_MAP = {
    ("line", "vertical", True): vertical_powered,
    ("line", "vertical", False): vertical_unpowered,
    
    ("line", "horizontal", True): horizontal_powered,
    ("line", "horizontal", False): horizontal_unpowered,

    ("corner", "left_bottom", True): left_bottom_powered,
    ("corner", "left_bottom", False): left_bottom_unpowered,
    
    ("corner", "left_top", True): left_top_powered,
    ("corner", "left_top", False): left_top_unpowered,
    
    ("corner", "right_bottom", True): right_bottom_powered,
    ("corner", "right_bottom", False): right_bottom_unpowered,
    
    ("corner", "right_top", True): right_top_powered,
    ("corner", "right_top", False): right_top_unpowered,

    ("power_source", "all", True): power_source,
}

ROTATIONS =  {
    "line": ["vertical", "horizontal"],
    "corner": ["right_bottom", "left_bottom", "left_top", "right_top"],
    "power_source": ["all"]
}

NEIGHBOURS = {
    "vertical": ["b", "t"],
    "horizontal": ["l", "r"],
    "left_bottom": ["l", "b"],
    "right_bottom": ["r", "b"],
    "left_top": ["l", "t"],
    "right_top": ["r", "t"],
    "all": ["l", "r", "t", "b"]
}

def get_opposite(direction):
    if direction == "l":
        return "r"
    elif direction == "r":
        return "l"
    elif direction == "t":
        return "b"
    elif direction == "b":
        return "t"

class PowerLine(arcade.gui.UITextureButton):
    def __init__(self, line_type, left_neighbour, top_neighbour):
        super().__init__(texture=TEXTURE_MAP[line_type, ROTATIONS[line_type][0], line_type == "power_source"])

        self.line_type = line_type
        self.rotation = ROTATIONS[line_type][0]
        self.powered = self.line_type == "power_source"

        self.left_neighbour, self.top_neighbour = left_neighbour, top_neighbour
        self.right_neighbour, self.bottom_neighbour = None, None

        self.on_click = lambda e: self.next_rotation()

        self.update_visual()

    def next_rotation(self):
        current_index = ROTATIONS[self.line_type].index(self.rotation)

        if current_index + 1 == len(ROTATIONS[self.line_type]):
            self.rotation = ROTATIONS[self.line_type][0]
        else:
            self.rotation = ROTATIONS[self.line_type][current_index + 1]

        self.update_visual()

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
        self.texture = TEXTURE_MAP[(self.line_type, self.rotation, self.powered)]
        self.texture_hovered = TEXTURE_MAP[(self.line_type, self.rotation, self.powered)]
        self._requires_render = True