import pygame
import maze_generator as mg
import solvers
import time

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (0,255,255)
BLUE = (0, 0, 255)
RED = (220,20,60)
YELLOW = (128,0,128)
ORANGE = (238,130,238)

# Defina o tamanho da janela e do labirinto
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
MAZE_WIDTH = 13
MAZE_HEIGHT = 13



input_text = ""

def draw_maze(maze, window,CELL_SIZE):
        
        for y, row in enumerate(maze):

            for x, cell in enumerate(row):

                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if cell == 2:
                    pygame.draw.rect(window, GREEN, rect)
                elif cell == 3:
                    pygame.draw.rect(window, RED, rect)
                elif cell == 1:
                    pygame.draw.rect(window, BLACK, rect)
                else:
                    pygame.draw.rect(window, WHITE, rect)

def draw_solution(window, solution_path, visited,CELL_SIZE,delay):

    if solution_path:
        for (x, y) in visited:
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, ORANGE, rect)
            pygame.display.update()
            pygame.time.delay(delay)
                
        for (x, y) in solution_path:
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, YELLOW, rect)
            pygame.display.update()
            pygame.time.delay(delay)

def display_text(window, text, font_size, color, position,background=(0,0,0,0)):
    font = pygame.font.SysFont("couriernew", font_size)
    if(font_size>29):
        font.set_bold(True)
    text_surface = font.render(text, True, color)
    #background_color_with_alpha = background + (0,) 
    text_with_background_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
    text_rect = text_surface.get_rect(center=position)
    
    #text_with_background_surface.fill(background_color_with_alpha)
    text_with_background_surface.fill(background)

    text_with_background_surface.blit(text_surface, (0, 0))

    text_rect = text_with_background_surface.get_rect(center=position)
    window.blit(text_with_background_surface, text_rect.topleft)       


def read_integer(window):
    global input_text

    while True:
        window.fill(BLACK)
        display_text(window, "Escolha o tamanho do labirinto", 30, (255, 255, 255), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 3)))
        display_text(window, "Digite um número menor que 60", 20, (255, 255, 255), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 20)*10))
        display_text(window, "para determinar o tamanho do labirinto", 20, (255, 255, 255), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 20)*12))
        display_text(window, "depois aperte ENTER", 20, (255, 255, 255), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 20)*14))
        display_text(window, input_text, 45, ORANGE, (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 20)*16))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        number = int(input_text)
                        return number
                    except ValueError:
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        

def initialize_game():
    global input_text
    pygame.init()

    # Crie a janela
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze")


    # Variáveis para rastrear o estado do jogo
    solving = False
    solution_path = []

    # Exiba o texto de introdução
    display_text(window, "Made by Cassio and Júlia", 30, (255, 255, 255), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Aguarde 2 segundos (2000 milissegundos)
    window.fill(BLACK)

    

    pygame.event.get()
    number=read_integer(window)
    
    # Gere o labirinto
    # Tamanho de cada célula no labirinto
    #CELL_SIZE = min(WINDOW_WIDTH // number, WINDOW_HEIGHT // number)
    CELL_SIZE = max(WINDOW_WIDTH // number, WINDOW_HEIGHT // number)
    maze, start, end = mg.generate_maze(number, number)
    


    window.fill(BLACK)
    display_text(window, "Aperte D para DFS", 30, (255, 255, 255), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 3)*2))
    display_text(window, "Aperte B para BFS", 30, (255, 255, 255), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(1000)  # Aguarde 2 segundos (2000 milissegundos)



    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not solving:
                if event.type == pygame.KEYDOWN:
                    visited = []
                    if event.key == pygame.K_d:
                        solution_path = solvers.DFS(maze, start, end, visited)
                        solution_path = solution_path[::-1]
                        solving = True
                    elif event.key == pygame.K_b:
                        solution_path = solvers.BFS(maze, start, end, visited)
                        solving = True

        # Preencha a tela com a cor de fundo
        window.fill(BLACK)
       
        # Desenhe o labirinto
        draw_maze(maze, window,CELL_SIZE)
        display_text(window, "Aperte D para DFS", 30, BLACK, (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 3)*2),ORANGE+(205,))
        display_text(window, "Aperte B para BFS", 30, BLACK, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3),ORANGE+(205,))

        # Se estivermos resolvendo o labirinto, desenhe o caminho da solução
        if solving:
            draw_maze(maze, window,CELL_SIZE)
            draw_solution(window, solution_path, visited,CELL_SIZE,int(1000/number))
            solving = False

        # Atualize a janela
        pygame.display.flip()

    # Encerre o pygame
    pygame.quit()
