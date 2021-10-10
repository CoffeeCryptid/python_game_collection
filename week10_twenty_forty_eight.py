"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    new = slide(line)
            
    for index in range(1, len(line)):
        if new[index] == new[index-1]:
            new[index-1] = new[index-1] + new[index]
            new[index] = 0
    
    merged = slide(new)
    
    return merged

def slide(line):
    """
    Helper function for merge:
    slide all non-zero numbers left
    """
    new = [0] * len(line)
    index = 0
    for num in line:
        if num != 0:
            new[index] = num
            index += 1
    return new


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._initial_tiles = {
            UP: [(0, index) for index in range(grid_width)],
            DOWN: [(grid_height-1, index) for index in range(grid_width)],
            LEFT: [(index, 0) for index in range(grid_height)],
            RIGHT: [(index, grid_width-1) for index in range(grid_height)]
        }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0] * self._width for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = [" ".join([str(num) for num in row]) for row in self._grid]
        return "\n".join(result)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        offset = OFFSETS[direction]
        if direction in [UP, DOWN]:
            step_num = self._height
        elif direction in [LEFT, RIGHT]:
            step_num = self._width
        
        for tile in self._initial_tiles[direction]:
            row = self.get_row(tile, offset, step_num)
            
            merged = merge(row)
            if row != merged:
                moved = True
            
            self.set_row(tile, offset, merged)
        
        if moved:
            self.new_tile()
            
    def get_row(self, init, offset, step_num):
        """
        Helper method: retrieve an entire row or column
        """
        cur_tile = init
        row = list()
        for index in range(step_num):
            tile = self.get_tile(cur_tile[0], cur_tile[1])
            row.append(tile)
            cur_tile = [num + offset[index] for index, num in enumerate(cur_tile)]
        
        return row
    
    def set_row(self, init, offset, nums):
        """
        Helper method: set an entire row or column
        to values in a list
        """
        cur_tile = init
        for tile in nums:
            self.set_tile(cur_tile[0], cur_tile[1], tile)
            cur_tile = [num + offset[index] for index, num in enumerate(cur_tile)]

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        value = random.choice([2] * 9 + [4])
        locs = list()
        for i_row, n_row in enumerate(self._grid):
            for i_col, n_col in enumerate(n_row):
                if n_col == 0:
                    locs.append((i_row, i_col))
        location = random.choice(locs)
        self.set_tile(location[0], location[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
