import pygame

##Generating Board
cell_size = 70 

black = (0,0,0)
white = (238, 238, 210)
green = (118, 150, 86)
white_tint = (243, 214, 127)
black_tint = (181, 179, 88)

def draw_cell(screen, color, dimension):
    pygame.draw.rect(screen, color, dimension)
    

def Generate_Board(w_l,w_w, screen, selected):
    current_pos = {'x': (w_l-8*cell_size)/2, 'y': (w_w-8*cell_size)/2}
    current_color = white
    for i in range(8):
        if i != 0:
            if current_color == white:
                current_color = green
            else:
                current_color = white

            current_pos['y'] += cell_size
            current_pos['x'] = (w_l-8*cell_size)/2
        for v in range(8):
            if (v,i) == selected:

                if current_color == green:
                    draw_cell(screen, black_tint,(current_pos['x'], current_pos['y'],cell_size,cell_size))
                elif current_color == white:
                    draw_cell(screen, white_tint,(current_pos['x'], current_pos['y'],cell_size,cell_size))
            else:
                draw_cell(screen, current_color,(current_pos['x'], current_pos['y'],cell_size,cell_size))
                
            if current_color == white:
                current_color = green
            else:
                current_color = white

            current_pos['x']+= cell_size



w_l = 800
w_w = 600

start_x = (w_l - (8*cell_size))/2
start_y = (w_w - (8*cell_size))/2

def cell_pos(p_1,p_2):

    pos = ((start_x + cell_size*p_1),(start_y + cell_size*p_2))

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
           
                

def initial_setup(board):

    b_backrow = ["r","n","b","q","k","b","n","r"]
    w_backrow = ["R","N","B","Q","K","B","N","R"]

    for i in range(8):
        board[i][0] = b_backrow[i]
        board[i][7] = w_backrow[i]

        board[i][1] = "p"
        board[i][6] = "P"


##inputs 

def onClick(mouse_x, mouse_y):

    if (start_x <= mouse_x < start_x + 8*cell_size and
        start_y <= mouse_y < start_y + 8*cell_size):

        mouse_pos = (
            (mouse_x - start_x) // cell_size,
            (mouse_y - start_y) // cell_size
        )

        return mouse_pos

    return (-1,-1)