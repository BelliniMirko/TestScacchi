import pygame
from constants import HEI, WID, BLACK, WHITE, SQ_SIZE, ROWS, COLS
from piecetypes import Pawn, King, Queen, Knight, Bishop, Rook


class Board:

    def __init__(self):
        self.board = [] 

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQ_SIZE, col *SQ_SIZE, SQ_SIZE, SQ_SIZE))