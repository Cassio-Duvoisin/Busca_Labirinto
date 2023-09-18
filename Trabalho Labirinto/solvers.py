import maze_generator as mg
import tree
from collections import deque
import functions

def BFS(maze, start, end, visited):
    root = tree.TreeNode(start)  # Crie o nó raiz com a posição de partida
    queue = deque([root])  # Crie uma fila e insira o nó raiz

    while queue:
        current_node = queue.popleft()  # Pegue o nó mais antigo da fila
        
        if current_node.data == end:  # Verifique se chegamos ao objetivo
            path = []
            while current_node:
                path.append(current_node.data)
                current_node = current_node.previous
            path.reverse()  # O caminho foi construído do objetivo para o início, então inverta-o
            return path
        
        visited.append(current_node.data)
        # Obtenha os movimentos possíveis a partir da posição atual no labirinto
        possible_moves = functions.possible_successors(maze, current_node.data)
        
        for move in possible_moves:
            new_position = (current_node.data[0] + move[0], current_node.data[1] + move[1])
            if new_position not in visited:  # Verifique se o novo nó já foi visitado
                new_node = tree.TreeNode(new_position)
                new_node.previous = current_node
                queue.append(new_node)  # Adicione o novo nó à fila
    
    return None  # Se não encontrarmos um caminho, retorne None

def DFS(maze, position, end, visited): 
    
    if position not in visited:
        visited.append(position)

    if (functions.objective(position, end)):
        return [position]

    moves = functions.possible_successors(maze, position)

    for new_position in moves:
        new_position = (position[0] + new_position[0], position[1] + new_position[1])
        if new_position not in visited:
            path = DFS(maze, new_position, end, visited)
            if path:
                return (path + [position])
            
    return None
