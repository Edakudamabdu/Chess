import pygame

##Generating Board
cell_size = 70 

def draw_cell(lib, screen, color, dimension):
    lib.draw.rect(screen, color, dimension)
    

def Generate_Board(lib,w_l,w_w, screen):
    current_pos = {'x': (w_l-8*cell_size)/2, 'y': (w_w-8*cell_size)/2}
    current_color = (255,255,255)
    for i in range(8):
        if i != 0:
            if current_color == (255,255,255):
                current_color = (0,0,0)
            else:
                current_color = (255,255,255)

            current_pos['y'] += 70
            current_pos['x'] = (w_l-8*cell_size)/2
        for v in range(8):
            draw_cell(lib, screen, current_color,(current_pos['x'], current_pos['y'],cell_size,cell_size) )
            if current_color == (255,255,255):
                current_color = (0,0,0)
            else:
                current_color = (255,255,255)

            current_pos['x']+= 70



w_l = 800
w_w = 600

def cell_pos(p_1,p_2):
    x = (w_l - (8*cell_size))/2
    y = (w_w - (8*cell_size))/2

    pos = ((x + cell_size*p_1),(y + cell_size*p_2))

    return pos

def draw_piece(screen, piece, pos):
    screen.blit(piece, pos)


def update_board(board, pieces, screen):
    for i in range(8):
        for j in range(8):
            piece_key = board[i][j]
            if piece_key != 0:
                if isinstance(pieces[piece_key], pygame.Surface):
                    draw_piece(screen, pieces[piece_key], cell_pos(i,j))
           
                
