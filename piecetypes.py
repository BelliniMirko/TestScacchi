import pygame
from piece import Piece
from constants import W_BISHOP, W_KING, W_KNIGHT, W_PAWN, W_QUEEN, W_ROOK, B_BISHOP, B_KING, B_KNIGHT, B_QUEEN, B_PAWN, B_ROOK, WHITE, BLACK, DIM_PIECE, SQ_SIZE

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_PAWN
        self.black_img = B_PAWN


    def pawn_mov(self):
        pass




class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_KING
        self.black_img = B_KING       

    def king_mov(self):
        pass


class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_BISHOP
        self.black_img = B_BISHOP

    def bishop_mov(self):
        pass





class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_KNIGHT
        self.black_img = B_KNIGHT

    def knight_mov(self):
        pass


class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_QUEEN
        self.black_img = B_QUEEN

    def queen_mov(self):
        pass


class Rook(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_ROOK
        self.black_img = B_ROOK

    def rook_mov(self):
        pass





