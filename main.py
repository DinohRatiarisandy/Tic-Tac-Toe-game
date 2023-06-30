"""
    The main file for develop the game.
"""

import sys
import pygame

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe-game")

WIDTH = 450
HEIGHT = 450
SPACECING = 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
COLORS = {
    0: (31, 38, 48), # Blue grey
    1: (219, 218, 73), # Yellow
    2: (209, 43, 105), # Rose
}

grid = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
player = 1
game_over = False
game_draw = False

# ---------------
# FUNCTIONS
# ---------------
def draw_grid():
    """Draw on the SCREEN the 9 tiles"""

    for i in range(3):
        for j in range(3):
            val = grid[i][j]
            pos_x = j*WIDTH // 3 + SPACECING
            pos_y = i*HEIGHT // 3 + SPACECING
            width_rect = WIDTH // 3 - 2*SPACECING
            height_rect = HEIGHT // 3 - 2*SPACECING

            board_rect = pygame.Rect(pos_x, pos_y, width_rect, height_rect)
            border_rect = pygame.Rect(pos_x, pos_y, width_rect, height_rect)
            pygame.draw.rect(SCREEN, COLORS[val], board_rect, border_radius=4)
            pygame.draw.rect(SCREEN, (43, 52, 66), border_rect, 1, 4)

def have_winner():
    """Scan in each move who win"""

    # Horizontals
    if grid[0][0]==grid[0][1]==grid[0][2]!=0 \
        or grid[1][0]==grid[1][1]==grid[1][2]!=0 \
        or grid[2][0]==grid[2][1]==grid[2][2]!=0:
        return True

    # Verticals
    if grid[0][0]==grid[1][0]==grid[2][0]!=0 \
        or grid[0][1]==grid[1][1]==grid[2][1]!=0 \
        or grid[0][2]==grid[1][2]==grid[2][2]!=0:
        return True
    
    # Diagonals
    if grid[0][0]==grid[1][1]==grid[2][2]!=0 \
        or grid[0][2]==grid[1][1]==grid[2][0]!=0:
        return True

def is_draw():
    """Scan if the grid is full and haven't a winner"""

    return all(grid[i][j]!=0 for i in range(3) for j in range(3))

def draw_game_over(player):
    """Print Game over on the screen if player lose or print DRAW if the game is drawn"""

    font = pygame.font.Font('freesansbold.ttf', 24)
    # Create rectangle
    pygame.draw.rect(SCREEN, 'black', [50, 50, 350, 200], 0, 10)
    pygame.draw.rect(SCREEN, 'white', [50, 50, 350, 200], 2, 10)

    if game_draw==False:
        game_over_text1 = font.render(f'Player {player} Won!', True, 'white')
        game_over_text2 = font.render('Press ENTER to restart', True, 'white')
        game_over_text3 = font.render('Press ESCAPE to quit', True, 'white')
    else:
        game_over_text1 = font.render(f'Game is DRAW!', True, 'white')
        game_over_text2 = font.render('Press ENTER to restart', True, 'white')
        game_over_text3 = font.render('Press ESCAPE to quit', True, 'white')

    SCREEN.blit(game_over_text1, (130, 65))
    SCREEN.blit(game_over_text2, (95, 145))
    SCREEN.blit(game_over_text3, (95, 185))
    
# ----------------x----------------

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if game_over:
                if event.key==pygame.K_RETURN:
                    grid = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
                    game_over = False
                    game_draw = False
                    player = 1

            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and game_over==False:
            row = event.pos[1] // (WIDTH//3 - SPACECING)
            col = event.pos[0] // (HEIGHT//3 - SPACECING)
            if grid[row][col]==0:
                grid[row][col] = player
                player = player%2 + 1

            if have_winner():
                game_over = True
                continue
            if is_draw():
                game_draw = True
                game_over = True

    SCREEN.fill((26, 31, 40))
    draw_grid()

    if game_over:
        if player==2:
            draw_game_over('ONE')
        else:
            draw_game_over('TWO')

    pygame.display.update()
    CLOCK.tick(60)
