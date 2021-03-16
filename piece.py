import pygame
from constants import *

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.white_img = None
        self.black_img = None

    def calc_pos(self):
        self.x = SQ_SIZE * self.col
        self.y = SQ_SIZE * self.row

    def draw(self, win):
        if self.color == WHITE:
            win.blit(self.white_img, (self.x + (SQ_SIZE - DIM_PIECE)//2, self.y + (SQ_SIZE - DIM_PIECE)//2))
        elif self.color == BLACK:
            win.blit(self.black_img, (self.x + (SQ_SIZE - DIM_PIECE)//2, self.y + (SQ_SIZE - DIM_PIECE)//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    