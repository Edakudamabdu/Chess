import pygame
from pygame.locals import *

from assets import load_pieces

from functions import Generate_Board
from functions import update_board
from functions import initial_setup
from functions import onClick

##initilization
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

while running:

##Adding Closing function 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x,mouse_y = event.pos
            clicked = onClick(mouse_x,mouse_y)
             
            if selected != clicked:
                selected = clicked
            else:
                selected = (-1,-1)

    if selected != (-1,-1):
        pass

    screen.fill((50,50,50))
##Begin Drawing
    Generate_Board(window_length, window_width, screen, selected)
    update_board(board, piece_assets, screen)
##End Drawing
    pygame.display.flip()

pygame.quit()