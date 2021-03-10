import pygame

WID, HEI = 800, 800
ROWS, COLS = 8, 8

SQ_SIZE = WID // COLS
DIM_PIECE = SQ_SIZE - 20

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (152, 101, 50)

W_KING = pygame.transform.scale(pygame.image.load('assets/w_king.png'), (DIM_PIECE, DIM_PIECE))
W_QUEEN = pygame.transform.scale(pygame.image.load('assets/w_queen.png'), (DIM_PIECE, DIM_PIECE))
W_PAWN = pygame.transform.scale(pygame.image.load('assets/w_pawn.png'), (DIM_PIECE, DIM_PIECE))
W_BISHOP = pygame.transform.scale(pygame.image.load('assets/w_bishop.png'), (DIM_PIECE, DIM_PIECE))
W_KNIGHT = pygame.transform.scale(pygame.image.load('assets/w_knight.png'), (DIM_PIECE, DIM_PIECE))
W_ROOK = pygame.transform.scale(pygame.image.load('assets/w_rook.png'), (DIM_PIECE, DIM_PIECE))

B_KING = pygame.transform.scale(pygame.image.load('assets/b_king.png'), (DIM_PIECE, DIM_PIECE))
B_QUEEN = pygame.transform.scale(pygame.image.load('assets/b_queen.png'), (DIM_PIECE, DIM_PIECE))
B_PAWN = pygame.transform.scale(pygame.image.load('assets/b_pawn.png'), (DIM_PIECE, DIM_PIECE))
B_BISHOP = pygame.transform.scale(pygame.image.load('assets/b_bishop.png'), (DIM_PIECE, DIM_PIECE))
B_KNIGHT = pygame.transform.scale(pygame.image.load('assets/b_knight.png'), (DIM_PIECE, DIM_PIECE))
B_ROOK = pygame.transform.scale(pygame.image.load('assets/b_rook.png'), (DIM_PIECE, DIM_PIECE))


