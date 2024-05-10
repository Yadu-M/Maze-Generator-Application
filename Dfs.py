from Grid import Grid
from algo import Algo
from pygame import Color
import random

class DFS(Algo):
    def __init__(self, grid: Grid) -> None:
        super().__init__("DFS", grid)
        self.path: list[tuple[int, int]]
        self.path = []        
               
    def update_path(self, row_col: tuple[int, int], color: Color, direction: str = "") -> bool:
        self.path.append(row_col)
        self.grid.set_cell(row_col, 1)
        self.grid.draw_cell(row_col, color, direction)
        
    
    def get_univisted_neighbour(self, color: Color = (255, 255, 255)) -> tuple[int, int]:            
        if len(self.path) == 0:
            return None
        curr_row, curr_col = self.path[len(self.path) - 1]
        neighbours = self.grid.get_neighbours(curr_row, curr_col)
        unvisited_neighbours: list[tuple[int, int]]
        unvisited_neighbours = []
        for row, col in neighbours:
            if self.grid.cells[row][col] != 1:
                unvisited_neighbours.append((row, col))
        
        if len(unvisited_neighbours) <= 1:        
            if len(unvisited_neighbours) == 0:
                self.path.pop()
                return self.get_univisted_neighbour(color=(0, 153, 255))
            else:       
                new_row, new_col = unvisited_neighbours[0]
                direction = ""
                if new_row == curr_row:
                    if new_col < curr_col:
                        direction = "LEFT"
                    else:
                        direction = "RIGHT"
                else:
                    if new_col == curr_col:
                        if new_row < curr_row:
                            direction = "TOP"
                        else:
                            direction = "BOT"
                self.update_path(unvisited_neighbours[0], (255,255,255), direction)
                return unvisited_neighbours[0]
            
        else:
            random_index = random.randint(0, len(unvisited_neighbours) - 1)
            new_row, new_col = unvisited_neighbours[random_index]
            direction = ""
            if new_row == curr_row:
                if new_col < curr_col:
                    direction = "LEFT"
                else:
                    direction = "RIGHT"
            else:
                if new_col == curr_col:
                    if new_row < curr_row:
                        direction = "TOP"
                    else:
                        direction = "BOT"
            self.update_path(unvisited_neighbours[random_index], color, direction)
            return unvisited_neighbours[random_index]
        
    
        
        
            
        
            
        
    