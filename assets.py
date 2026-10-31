import pygame

def load_pieces():
    pieces = {}

##Black pieces
    pieces["b"] = pygame.image.load("Assets/black_bishop.png").convert_alpha()
    pieces["n"] = pygame.image.load("Assets/black_knight.png").convert_alpha()
    pieces["r"] = pygame.image.load("Assets/black_rook.png").convert_alpha()
    pieces["p"] = pygame.image.load("Assets/black_pawn.png").convert_alpha()
    pieces["q"] = pygame.image.load("Assets/black_queen.png").convert_alpha()
    pieces["k"] = pygame.image.load("Assets/black_king.png").convert_alpha()


##White pieces
    pieces["B"] = pygame.image.load("Assets/white_bishop.png").convert_alpha()
    pieces["N"] = pygame.image.load("Assets/white_knight.png").convert_alpha()
    pieces["R"] = pygame.image.load("Assets/white_rook.png").convert_alpha()
    pieces["P"] = pygame.image.load("Assets/white_pawn.png").convert_alpha()
    pieces["Q"] = pygame.image.load("Assets/white_queen.png").convert_alpha()
    pieces["K"] = pygame.image.load("Assets/white_king.png").convert_alpha()

    for key in pieces:
        pieces[key] = pygame.transform.scale(pieces[key],(70,70))

    return pieces