import pygame
from pygame.locals import *

from assets import load_pieces

from functions import Generate_Board
from functions import update_board



##initilization
pygame.init()

window_length = 800
window_width = 600

screen = pygame.display.set_mode((window_length, window_width))
pygame.display.set_caption("Chess")

running = True

##board

piece_assets = load_pieces()

board_line = [0,0,0,0,0,0,0,0]
board = []

for i in range(8):
    board.append(board_line)
board[1][1] = "p"

while running:

##Adding Closing function 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,150,0))
##Begin Drawing
    Generate_Board(pygame, window_length, window_width, screen)
    ##screen.blit(piece_assets['p'],cell_pos(0,1))
    update_board(board, piece_assets, screen)
##End Drawing
    pygame.display.flip()

pygame.quit()