import pygame
from board import Board
from constants import WHITE, BLACK, GREEN, SQ_SIZE


class Game:
    
    def __init__(self, win):
         self.win = win
         self.selected = None
         self.board = Board()
         self.turn = WHITE
         self.valid_moves = {}


    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)

        pygame.display.update()

    def select(self, row, col):

        #devo controllare se sto cercando di selezionare un pezzo, muoverlo, se lo sto muovendo in posizione valida etc..
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.valid_moves = {}
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            print(self.valid_moves)
            return True 

        return False

    def _move(self, row, col):
        #destination = self.board.get_piece(row, col):
        piece = self.board.get_piece(row, col)
        #dovrò aggiungere controllo sulla casella di destinazione

        if self.selected and (row, col) in self.valid_moves:
            if self.valid_moves[(row, col)]  == "m":
                self.board.move(self.selected, row, col)
            else:
                self.board.take(self.selected, row, col)
            self.valid_moves = {}
            self.selected = None
            self.change_turn()
        else:
            return False

        return True

    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
            
            
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQ_SIZE + SQ_SIZE//2, row * SQ_SIZE + SQ_SIZE//2), 15)
