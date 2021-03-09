import pygame

WID, HEI = 800, 800
ROWS, COLS = 8, 8

SQ_SIZE = WID // COLS

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

W_KING = pygame.transform.scale(pygame.image.load('assets/w_king.png'), (SQ_SIZE, SQ_SIZE))
W_QUEEN = pygame.transform.scale(pygame.image.load('assets/w_queen.png'), (SQ_SIZE, SQ_SIZE))
W_PAWN = pygame.transform.scale(pygame.image.load('assets/w_pawn.png'), (SQ_SIZE, SQ_SIZE))
W_BISHOP = pygame.transform.scale(pygame.image.load('assets/w_bishop.png'), (SQ_SIZE, SQ_SIZE))
W_KNIGHT = pygame.transform.scale(pygame.image.load('assets/w_knight.png'), (SQ_SIZE, SQ_SIZE))
W_ROOK = pygame.transform.scale(pygame.image.load('assets/w_rook.png'), (SQ_SIZE, SQ_SIZE))

B_KING = pygame.transform.scale(pygame.image.load('assets/b_king.png'), (SQ_SIZE, SQ_SIZE))
B_QUEEN = pygame.transform.scale(pygame.image.load('assets/b_queen.png'), (SQ_SIZE, SQ_SIZE))
B_PAWN = pygame.transform.scale(pygame.image.load('assets/b_pawn.png'), (SQ_SIZE, SQ_SIZE))
B_BISHOP = pygame.transform.scale(pygame.image.load('assets/b_bishop.png'), (SQ_SIZE, SQ_SIZE))
B_KNIGHT = pygame.transform.scale(pygame.image.load('assets/b_knight.png'), (SQ_SIZE, SQ_SIZE))
B_ROOK = pygame.transform.scale(pygame.image.load('assets/b_rook.png'), (SQ_SIZE, SQ_SIZE))


