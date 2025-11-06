import arcade, arcade.gui

from utils.preload import *

TEXTURE_MAP = {
    ("vertical", True): vertical_connected,
    ("vertical", False): vertical_unconnected,
    
    ("horizontal", True): horizontal_connected,
    ("horizontal", False): horizontal_unconnected,

    ("left_bottom", True): left_bottom_connected,
    ("left_bottom", False): left_bottom_unconnected,
    
    ("left_top", True): left_top_connected,
    ("left_top", False): left_top_unconnected,
    
    ("right_bottom", True): right_bottom_connected,
    ("right_bottom", False): right_bottom_unconnected,
    
    ("right_top", True): right_top_connected,
    ("right_top", False): right_top_unconnected,
}

ROTATIONS =  {
    "line": ["vertical", "horizontal"],
    "corner": ["left_top", "right_top", "right_bottom", "left_bottom"]
}

NEIGHBOURS = {
    "vertical": lambda l, r, t, b: bool((b and b.connected) or (t and t.connected)),
    "horizontal": lambda l, r, t, b: bool((l and l.connected) or (r and r.connected)),
    "left_bottom": lambda l, r, t, b: bool(((l and l.connected) or (b and b.connected))),
    "right_bottom": lambda l, r, t, b: bool(((r and r.connected) or (b and b.connected))),
    "left_top": lambda l, r, t, b: bool(((l and l.connected) or (t and t.connected))),
    "right_top": lambda l, r, t, b: bool(((r and r.connected) or (t and t.connected)))
}

class PowerLine(arcade.gui.UITextureButton):
    def __init__(self, line_type, left_neighbor, top_neighbour):
        super().__init__(texture=TEXTURE_MAP[ROTATIONS[line_type][0], False])

        self.line_type = line_type
        self.rotation = ROTATIONS[line_type][0]
        self.connected = False

        self.left_neighbour, self.top_neighbour = left_neighbor, top_neighbour
        self.right_neighbour, self.bottom_neighbour = None, None

        self.on_click = lambda e: self.next_rotation()

        self.update()

    def next_rotation(self):
        current_index = ROTATIONS[self.line_type].index(self.rotation)

        if current_index + 1 == len(ROTATIONS[self.line_type]) - 1:
            self.rotation = ROTATIONS[self.line_type][0]
        else:
            self.rotation = ROTATIONS[self.line_type][current_index + 1]

        self.update()

    def update_neighbours(self):
        if self.rotation == "horizontal":
            self.left_neighbour.update() if self.left_neighbour else None
            self.right_neighbour.update() if self.right_neighbour else None
        elif self.rotation == "vertical":
            self.top_neighbour.update() if self.top_neighbour else None
            self.bottom_neighbour.update() if self.bottom_neighbour else None

    def update(self):
        if not self.connected:
            old_connected = self.connected
            self.connected = NEIGHBOURS[self.rotation](self.left_neighbour, self.right_neighbour, self.top_neighbour, self.bottom_neighbour)
            if self.connected != old_connected:
                self.update_neighbours()

        self.texture = TEXTURE_MAP[(self.rotation, self.connected)]
        self.texture_hovered = TEXTURE_MAP[(self.rotation, self.connected)]
        self._requires_render = True