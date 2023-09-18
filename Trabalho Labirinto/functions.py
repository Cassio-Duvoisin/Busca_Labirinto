def possible_successors(maze, position):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    

    possible_moves = []

    for dx, dy in directions:
    
        new_x = position[0] + dx
        new_y = position[1] + dy
       
        if 0 <= new_x < maze.shape[1] and 0 <= new_y < maze.shape[0] and (maze[new_x][new_y] != 1):
            possible_moves.append((dx, dy))

    return possible_moves


def objective(position, end):
 
    if (position == end):
        return True
    else:
        return False
