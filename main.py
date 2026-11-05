import pygame
from pygame.locals import *

from assets import load_pieces

from functions import Generate_Board
from functions import update_board
from functions import initial_setup
from functions import onClick
from functions import choices
from functions import draw_choices

#initilization
pygame.init()

window_length = 800
window_width = 600

screen = pygame.display.set_mode((window_length, window_width))
pygame.display.set_caption("Chess")

running = True

##board
piece_assets = load_pieces()

board = []
selected = (-1,-1)

for i in range(8):
    board_line = [0,0,0,0,0,0,0,0]
    board.append(board_line)

initial_setup(board)

board[5][4] = "k"

while running:

#Adding Closing function 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x,mouse_y = event.pos
            clicked = onClick(mouse_x,mouse_y)

            x_pos, y_pos = clicked
            current_piece = board[int(x_pos)][int(y_pos)]
             
            if selected != clicked and current_piece != 0:
                selected = clicked
            else:
                selected = (-1,-1)

    can_move = []
    
    if selected != (-1,-1):
        can_move = choices(board, selected)

    screen.fill((50,50,50))
#Begin Drawing
    Generate_Board(window_length, window_width, screen, selected)
    update_board(board, piece_assets, screen)

    if can_move != []:
        for i in range(len(can_move)):
            cell_x, cell_y = can_move[i]
            draw_choices(screen, cell_x, cell_y)
#End Drawing
    pygame.display.flip()

pygame.quit()