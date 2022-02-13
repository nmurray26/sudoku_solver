class Board:
    def __init__(self, grid_size=9):
        self.grid_size = 9
        self.empty_grid = [grid_size*[0]]*9