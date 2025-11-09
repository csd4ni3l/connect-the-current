from game.cell import Cell

class House(Cell):
    def __init__(self, x, y, left_neighbour, top_neighbour):
        super().__init__("house", x, y, left_neighbour, top_neighbour)

class PowerSource(Cell):
    def __init__(self, x, y, left_neighbour, top_neighbour):
        super().__init__("power_source", x, y, left_neighbour, top_neighbour)
        self.on_click = lambda e: self.next_rotation()

class PowerLine(Cell):
    def __init__(self, cell_type, x, y, left_neighbour, top_neighbour):
        super().__init__(cell_type, x, y, left_neighbour, top_neighbour)

        if not cell_type == "cross":
            self.on_click = lambda e: self.next_rotation()