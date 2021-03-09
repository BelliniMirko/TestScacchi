import pygame
from piece import Piece
from constants import W_BISHOP, W_KING, W_KNIGHT, W_PAWN, W_QUEEN, W_ROOK, B_BISHOP, B_KING, B_KNIGHT, B_QUEEN, B_PAWN, B_ROOK, WHITE, BLACK

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)


    def pawn_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_PAWN, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(B_PAWN, (self.x, self.y))



class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def king_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_KING, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(B_KING, (self.x, self.y))    

class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def bishop_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_BISHOP, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(B_BISHOP, (self.x, self.y))



class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def knight_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_KNIGHT, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(B_KNIGHT, (self.x, self.y))

class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def queen_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_QUEEN, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(W_QUEEN, (self.x, self.y))


class Rook(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def rook_mov(self):
        pass

    def draw(self, win):
        if self.color == WHITE:
            pygame.blit(W_ROOK, (self.x, self.y))
        elif self.color == BLACK:
            pygame.blit(B_ROOK, (self.x, self.y))




