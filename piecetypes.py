import pygame
from piece import Piece
from constants import W_BISHOP, W_KING, W_KNIGHT, W_PAWN, W_QUEEN, W_ROOK, B_BISHOP, B_KING, B_KNIGHT, B_QUEEN, B_PAWN, B_ROOK, WHITE, BLACK, DIM_PIECE, SQ_SIZE

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_PAWN
        self.black_img = B_PAWN
        if self.color == WHITE:
            self.direction = -1
        else:
            self.direction = 1


    def get_moves(self, board):
        moves = {}

        #check double step in black side
        if self.row == 1 and self.color == BLACK:
             if board[self.row + self.direction*2][self.col] == 0:
                    moves[(self.row + self.direction*2, self.col)] = "m"
                    #moves.append((self.row + self.direction*2, self.col))

        #check double step in white side
        if self.row == 6 and self.color == WHITE:
             if board[self.row + self.direction*2][self.col] == 0:
                    #moves.append((self.row + self.direction*2, self.col))            
                    moves[(self.row + self.direction*2, self.col)] = "m"

        #check single step 
        if board[self.row + self.direction][self.col] == 0:
            #moves.append((self.row + self.direction, self.col))
            moves[(self.row + self.direction, self.col)] = "m"

        #check take on the left side
        if self.col > 0:
            if board[self.row + self.direction][self.col - 1] != 0 and board[self.row + self.direction][self.col - 1].color != self.color:
                #moves.append((self.row + self.direction, self.col - 1))
                moves[(self.row + self.direction, self.col - 1)] = "t"

        #check take on the right side
        if self.col < 7:
            if board[self.row + self.direction][self.col + 1] != 0 and board[self.row + self.direction][self.col + 1].color != self.color:
                #moves.append((self.row + self.direction, self.col + 1))
                moves[(self.row + self.direction, self.col + 1)] = "t"

        return moves




class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_KING
        self.black_img = B_KING       

    def get_moves(self, board):
        moves = {}

        #controlli verticali tranne ultima riga
        if self.row < 7:

            if board[self.row + 1][self.col] == 0:
                moves[(self.row + 1, self.col)] = "m"
            elif board[self.row + 1][self.col].color != self.color:
                moves[(self.row + 1, self.col)] = "t"
            
            if self.col < 7:
                if board[self.row + 1][self.col+1] == 0:
                    moves[(self.row + 1, self.col+1)] = "m"
                elif board[self.row + 1][self.col+1].color != self.color:
                    moves[(self.row + 1, self.col+1)] = "t" 

            if self.col > 0:
                if board[self.row + 1][self.col-1] == 0:
                    moves[(self.row + 1, self.col-1)] = "m"
                elif board[self.row + 1][self.col-1].color != self.color:
                    moves[(self.row + 1, self.col-1)] = "t"    

        #controlli verticali tranne prima riga
        if self.row > 0:

            if board[self.row - 1][self.col] == 0:
                moves[(self.row - 1, self.col)] = "m"
            elif board[self.row - 1][self.col].color != self.color:
                moves[(self.row - 1, self.col)] = "t"

            if self.col < 7:
                if board[self.row - 1][self.col+1] == 0:
                    moves[(self.row - 1, self.col+1)] = "m"
                elif board[self.row - 1][self.col+1].color != self.color:
                    moves[(self.row - 1, self.col+1)] = "t"

            if self.col > 0:
                if board[self.row - 1][self.col-1] == 0:
                    moves[(self.row - 1, self.col-1)] = "m"
                elif board[self.row - 1][self.col-1].color != self.color:
                    moves[(self.row - 1, self.col-1)] = "t"    

        if self.col < 7:

            if board[self.row][self.col + 1] == 0:
                moves[(self.row, self.col + 1)] = "m"
            elif board[self.row][self.col + 1].color != self.color:
                moves[(self.row, self.col + 1)] = "t"

        if self.col > 0:

            if board[self.row][self.col - 1] == 0:
                moves[(self.row, self.col - 1)] = "m"
            elif board[self.row][self.col - 1].color != self.color:
                moves[(self.row, self.col - 1)] = "t"

        return moves


                           




class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_BISHOP
        self.black_img = B_BISHOP

    def get_moves(self, board):
        moves = {}
        srow = self.row 
        scol = self.col

        #diagonale up right
        while srow > 0 and scol < 7:
            srow -= 1
            scol += 1

            if board[srow][scol] == 0:
                moves[(srow, scol)] = "m"
            elif board[srow][scol].color != self.color:
                moves[(srow, scol)] = "t"
                break
            else:
                break

        srow = self.row 
        scol = self.col

        #diagonale up left
        while srow > 0 and scol > 0:
            srow -= 1
            scol -= 1

            if board[srow][scol] == 0:
                moves[(srow, scol)] = "m"
            elif board[srow][scol].color != self.color:
                moves[(srow, scol)] = "t"
                break
            else:
                break

        srow = self.row 
        scol = self.col

        #diagonale down left
        while srow < 7 and scol > 0:
            srow += 1
            scol -= 1

            if board[srow][scol] == 0:
                moves[(srow, scol)] = "m"
            elif board[srow][scol].color != self.color:
                moves[(srow, scol)] = "t"
                break
            else:
                break

        srow = self.row 
        scol = self.col

        #diagonale down right
        while srow < 7 and scol < 7:
            srow += 1
            scol += 1

            if board[srow][scol] == 0:
                moves[(srow, scol)] = "m"
            elif board[srow][scol].color != self.color:
                moves[(srow, scol)] = "t"
                break
            else:
                break
        
        

        

        

        return moves







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





