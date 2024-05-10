from Grid import Grid

class Algo:
    def __init__(self, name: str, grid: Grid) -> None:
        self.name: str        
        self.grid: Grid
        
        self.name = name
        self.grid = grid