from pygame import Surface, Color, Rect, draw, display, time

class Grid:    
    def __init__(self, row_count: int, col_count: int, cell_width: int, cell_height: int, surface: Surface) -> None:  
        self.row_count: int
        self.col_count: int
        self.cells: list[list[int]]
        self.cell_width: int
        self.cell_height: int
        self.surface: Surface        
             
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.row_count = row_count
        self.col_count = col_count
        self.surface = surface
        self.cells = [[0 for _ in range(col_count)] for _ in range(row_count)]
    
    def set_cell(self, row_col: tuple[int, int], value: int) -> bool:
        row, col = row_col
        if row < 0 or row >= self.row_count:
            return Exception("invalid index")
        if col < 0 or col >= self.col_count:
            return Exception("invalid index")
        
        self.cells[row][col] = value
        return True
    
    def get_cell(self, row_col: tuple[int, int]) -> bool:
        row, col = row_col
        if row < 0 or row >= self.row_count:
            return Exception("invalid index")
        if col < 0 or col >= self.col_count:
            return Exception("invalid index")
        
        return self.cells[row][col]
    
    def draw_cell(self, row_col: tuple[int, int], color: Color, direction: str = "") -> None:
        row, col = row_col
        # time.delay(50)
        if direction == "TOP":
            rect = Rect((col * self.cell_width), (row * self.cell_height), self.cell_width, self.cell_height * 3)
            draw.rect(self.surface, color, rect)
            display.flip()
            return
        if direction == "BOT":
            rect = Rect((col * self.cell_width), ((row - 2) * self.cell_height), self.cell_width, self.cell_height * 3)
            draw.rect(self.surface, color, rect)
            display.flip()
            return
        if direction == "LEFT":
            rect = Rect((col * self.cell_width), (row * self.cell_height), self.cell_width * 3, self.cell_height)
            draw.rect(self.surface, color, rect)
            display.flip()
            return
        if direction == "RIGHT":
            rect = Rect(((col - 2) * self.cell_width), (row * self.cell_height), self.cell_width * 3, self.cell_height)
            draw.rect(self.surface, color, rect)
            display.flip()
            return
        rect = Rect((col * self.cell_width), (row * self.cell_height), self.cell_width, self.cell_height)
        draw.rect(self.surface, color, rect)        
        display.flip()
        
    
    def get_neighbours(self, row, col) -> list[tuple]:
        neighbours = []
        
        if row == 0 and col == 0: # Top left
            neighbours.append(((row + 2), (col)))
            neighbours.append((row, (col + 2)))
            return neighbours
        if row == (self.row_count - 2) and col == 0: # Bottom left
            neighbours.append(((row - 2), col))
            neighbours.append((row, (col + 2)))
            return neighbours
        if row == 0 and col == (self.col_count - 2): # Top right
            neighbours.append((row, (col - 2)))
            neighbours.append(((row + 2), col))
            return neighbours
        if row == (self.row_count - 2) and (self.col_count - 2): # Bottom right
            neighbours.append((row, (col - 2)))
            neighbours.append(((row - 2), col))
            return neighbours
        
        if row == 0: # Top row
            neighbours.append((row, (col - 2)))
            neighbours.append(((row + 2), col))
            neighbours.append((row, (col + 2)))
            return neighbours
        if col == 0: # Left col
            neighbours.append(((row - 2), col))
            neighbours.append((row, (col + 2)))
            neighbours.append(((row + 2), col))
            return neighbours
        if row == (self.row_count - 2): # Bottom row
            neighbours.append((row, (col - 2)))
            neighbours.append(((row - 2), col))
            neighbours.append((row, (col + 2)))
            return neighbours
        if col == (self.col_count - 2): # Right column
            neighbours.append(((row - 2), col))
            neighbours.append((row, (col - 2)))
            neighbours.append(((row + 2), col))
            return neighbours
                
        neighbours.append(((row - 2), col))
        neighbours.append((row, (col + 2)))
        neighbours.append(((row + 2), col))
        neighbours.append((row, (col - 2)))
        return neighbours    
    
        