from game.cell import Cell

class House(Cell):
    def __init__(self, left_neighbour, top_neighbour):
        super().__init__("house", left_neighbour, top_neighbour)

class PowerSource(Cell):
    def __init__(self, left_neighbour, top_neighbour):
        super().__init__("power_source", left_neighbour, top_neighbour)
        self.on_click = lambda e: self.next_rotation()

class PowerLine(Cell):
    def __init__(self, cell_type, left_neighbour, top_neighbour):
        super().__init__(cell_type, left_neighbour, top_neighbour)

        if not cell_type == "cross":
            self.on_click = lambda e: self.next_rotation()