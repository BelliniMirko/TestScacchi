import pygame
from board import Board
from constants import WHITE


class Game:
    
    def __init__(self, win):
         self.win = win
         self.selected = None
         self.board = Board()
         self.turn = WHITE
         self.valid_moves = {}


    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col):

        #devo controllare se sto cercando di selezionare un pezzo, muoverlo, se lo sto muovendo in posizione valida etc..
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            #self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        #destination = self.board.get_piece(row, col):
        if self.selected:  #dovrò aggiungere controllo sulla casella di destinazione
            self.board.move(self.selected, row, col)
        else:
            return False

        return True
            
            

