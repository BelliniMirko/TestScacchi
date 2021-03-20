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

        addRow = 0
        addCol = 0
        #diagonale up right
        while self.row + addRow > 0 and self.col + addCol < 7:
            addRow -= 1
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale up left
        while self.row + addRow > 0 and self.col + addCol > 0:
            addRow -= 1
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale down left
        while self.row + addRow < 7 and self.col + addCol > 0:
            addRow += 1
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale down right
        while self.row + addRow < 7 and self.col + addCol < 7:
            addRow += 1
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
    
        return moves







class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_KNIGHT
        self.black_img = B_KNIGHT

    def get_moves(self, board):
        moves = {}

        #check 2 down 1 right
        if self.row < 6 and self.col < 7:
            self.checkSpot(2, 1, board, moves)

        #check 2 down 1 left 
            self.checkSpot(2, -1, board, moves)

        #check 2 up 1 left
        if self.row > 1 and self.col > 0:
            self.checkSpot(-2, -1, board, moves)

        #check 2 up 1 right
        if self.row > 1 and self.col < 7:
            self.checkSpot(-2, 1, board, moves)

        #check 1 up 2 left
        if self.row > 0 and self.col > 1:
            self.checkSpot(-1, -2, board, moves)

        #check 1 up 2 right
        if self.row > 0 and self.col < 6:
            self.checkSpot(-1, +2, board, moves)

        #check 1 down 2 right
        if self.row < 7 and self.col < 6:
            self.checkSpot(+1, +2, board, moves)

        #check 1 down 2 left
        if self.row < 7 and self.col > 1:
            self.checkSpot(+1, -2, board, moves)

        return moves





class Rook(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_ROOK
        self.black_img = B_ROOK

    def get_moves(self, board):
        moves = {}

        addRow = 0
        addCol = 0

        #sopra
        while self.row + addRow > 0:
            addRow -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
        addRow = 0

        #sotto
        while self.row + addRow < 7:
            addRow += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0

        #sinistra
        while self.col + addCol > 0:
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
        addCol = 0

        #destra
        while self.col + addCol < 7:
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break


        return moves

            




class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.white_img = W_QUEEN
        self.black_img = B_QUEEN

    def get_moves(self, board):
        moves = {}
        addRow = 0
        addCol = 0

        #sopra
        while self.row + addRow > 0:
            addRow -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
        addRow = 0

        #sotto
        while self.row + addRow < 7:
            addRow += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0

        #sinistra
        while self.col + addCol > 0:
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
        addCol = 0

        #destra
        while self.col + addCol < 7:
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break


        addRow = 0
        addCol = 0
        #diagonale up right
        while self.row + addRow > 0 and self.col + addCol < 7:
            addRow -= 1
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale up left
        while self.row + addRow > 0 and self.col + addCol > 0:
            addRow -= 1
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale down left
        while self.row + addRow < 7 and self.col + addCol > 0:
            addRow += 1
            addCol -= 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break

        addRow = 0
        addCol = 0

        #diagonale down right
        while self.row + addRow < 7 and self.col + addCol < 7:
            addRow += 1
            addCol += 1

            flag = self.checkSpot(addRow, addCol, board, moves)
            if  flag == False or flag == "t":
                break
        
    
        return moves









