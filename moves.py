def pawn(piece, x, y):
    moves = []

    if piece == "P":
        moves.append((x, y - 1))
        if y == 6:
            moves.append((x, y - 2))

    if piece == "p":
        moves.append((x, y + 1))
        if y == 1:
            moves.append((x, y + 2))

    return moves
    

def rook():
    pass

def knight():
    pass

def bishop():
    pass

def queen():
    pass

def king():
    pass