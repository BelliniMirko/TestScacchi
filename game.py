import pygame
from board import Board
from constants import WHITE, BLACK, GREEN, SQ_SIZE, RED


class Game:
    
    def __init__(self, win):
         self.win = win
         self.selected = None
         self.board = Board()
         self.turn = WHITE
         self.valid_moves = {}
         self.checked = None

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        if self.checked:
            pos = self.board.get_king_coords(self.checked)
            pygame.draw.circle(self.win, RED, (pos[1] * SQ_SIZE + SQ_SIZE//2, pos[0] * SQ_SIZE + SQ_SIZE//2), 15)            

        pygame.display.update()

    def select(self, row, col):

        #devo controllare se sto cercando di selezionare un pezzo, muoverlo, se lo sto muovendo in posizione valida etc..
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.valid_moves = {}
                self.selected = None
                self.select(row, col)
                return 

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece, self.turn)
            #print(self.valid_moves)  #debug mosse valide
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

            if self.board.isInCheck(self.opposite_color(self.turn)):  #controllo se è avvenuto uno scacco
                self.checked = self.opposite_color(self.turn)
            else:
                self.checked = None

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

    def opposite_color(self, turn):
        if turn == WHITE:
            return BLACK
        elif turn == BLACK:
            return WHITE
