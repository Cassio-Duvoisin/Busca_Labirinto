import random
import numpy as np

def generate_maze(width, height):
    """
    Generates a maze of given width and height using Recursive Backtracking algorithm.

    Parameters
    ----------
    width : int
        The width of the maze.
    height : int
        The height of the maze.

    Returns
    -------
    maze : list
        A 2D list representing the maze.
    start : tuple
        A tuple representing the starting position.
    end : tuple
        A tuple representing the ending position.
    """

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    def backtrack(x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = x + 2 * dx, y + 2 * dy
            if is_valid(new_x, new_y) and maze[new_x][new_y] == 1:
                maze[x + dx][y + dy] = 0
                maze[new_x][new_y] = 0
                backtrack(new_x, new_y)

    # Initialize the maze with walls
    maze = np.ones((height, width), dtype=int)

    # Start from (0, 0) and set it as the initial position
    start_x, start_y = 0, 0
    maze[0, 1] = 0
    maze[1, 0] = 0
    maze[start_x][start_y] = 2

    # Apply Recursive Backtracking
    backtrack(start_x, start_y)

    # Set a random ending position in the last row or column
    if random.random() < 0.5:
        end_x = random.randrange(0, width, 2)
        end_y = height - 1
    else:
        end_x = width - 1
        end_y = random.randrange(0, height, 2)

    maze[end_x][end_y] = 3

    return maze, (start_x, start_y), (end_x, end_y)


