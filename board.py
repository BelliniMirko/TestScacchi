import pygame
from constants import HEI, WID, BLACK, WHITE, SQ_SIZE, ROWS, COLS
from piecetypes import Pawn, King, Queen, Knight, Bishop, Rook


class Board:

    def __init__(self):
        self.board = [[], [], [], [], [], [], [], []] 
        self.create_board()
        self.debug_print()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQ_SIZE, col *SQ_SIZE, SQ_SIZE, SQ_SIZE))


    def create_board(self):

        #piazzo i pezzi neri |||| per ora hard coded
        self.board[0].append(Rook(0, 0, BLACK))
        self.board[0].append(Knight(0, 1, BLACK))
        self.board[0].append(Bishop(0, 2, BLACK))
        self.board[0].append(King(0, 3, BLACK))
        self.board[0].append(Queen(0, 4, BLACK))
        self.board[0].append(Bishop(0, 5, BLACK))
        self.board[0].append(Knight(0, 6, BLACK))
        self.board[0].append(Rook(0, 7, BLACK))

        #piazzo i pedoni neri
        for col in range(COLS):
            self.board[1].append(Pawn(1, col, BLACK))

        #piazzo 0 in ogni casella libera
        for row in range(2, 6):
            for col in range(COLS):
                self.board[row].append(0)

        #piazzo i pedoni bianchi
        for col in range(COLS):
            self.board[6].append(Pawn(6, col, WHITE))
            
        #piazzo i pezzi bianchi
        self.board[7].append(Rook(7, 0, BLACK))
        self.board[7].append(Knight(7, 1, BLACK))
        self.board[7].append(Bishop(7, 2, BLACK))
        self.board[7].append(Queen(7, 3, BLACK))
        self.board[7].append(King(7, 4, BLACK))
        self.board[7].append(Bishop(7, 5, BLACK))
        self.board[7].append(Knight(7, 6, BLACK))
        self.board[7].append(Rook(7, 7, BLACK))

        
    def debug_print(self):
            print(self.board)

    # def draw(self, win):
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             if self.board[row][col]

