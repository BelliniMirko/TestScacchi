import pygame
from board import Board
from constants import WHITE, BLACK


class Game:
    
    def __init__(self, win):
         self.win = win
         self.selected = None
         self.board = Board()
         self.turn = WHITE
         self.valid_moves = []


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
            self.valid_moves = self.board.get_valid_moves(piece)
            print(self.valid_moves)
            return True 

        return False

    def _move(self, row, col):
        #destination = self.board.get_piece(row, col):
        piece = self.board.get_piece(row, col)
        #dovrò aggiungere controllo sulla casella di destinazione

        if self.selected and (row, col) in self.valid_moves:  
            self.board.move(self.selected, row, col)
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
            
            

