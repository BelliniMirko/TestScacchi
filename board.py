import pygame
from constants import HEI, WID, BLACK, WHITE, SQ_SIZE, ROWS, COLS, BROWN
from piecetypes import Pawn, King, Queen, Knight, Bishop, Rook
from piece import Piece


class Board:

    def __init__(self):
        self.board = [[], [], [], [], [], [], [], []] 
        self.create_board()
        # self.draw_squares()
        # self.draw()

        
        self.debug_print()

    def draw_squares(self, win):
        win.fill(BROWN)
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
        self.board[7].append(Rook(7, 0, WHITE))
        self.board[7].append(Knight(7, 1, WHITE))
        self.board[7].append(Bishop(7, 2, WHITE))
        self.board[7].append(Queen(7, 3, WHITE))
        self.board[7].append(King(7, 4, WHITE))
        self.board[7].append(Bishop(7, 5, WHITE))
        self.board[7].append(Knight(7, 6, WHITE))
        self.board[7].append(Rook(7, 7, WHITE))

        
    def debug_print(self):
            for row in range(ROWS):
                for col in range(COLS):
                    if isinstance(self.board[row][col], Piece) and self.board[row][col].color == WHITE:
                        print("W" + type(self.board[row][col]).__name__, end='\t')
                    elif isinstance(self.board[row][col], Piece) and self.board[row][col].color == BLACK:
                        print("B" + type(self.board[row][col]).__name__, end='\t')
                    else:
                        print("0", end="\t")


                
                print("\n")


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #self.board[piece.row][piece.col].move(piece.row, piece.col) per testare swap
        piece.move(row, col)

    def take(self, piece, row, col):
        self.board[row][col] = 0
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        piece.move(row, col)


    def get_valid_moves(self, piece):
        
        moves = piece.get_moves(self.board)
        return moves

        






