import pygame 
from constants import WID, HEI
from board import Board

FPS = 60

WIN = pygame.display.set_mode((WID, HEI))
pygame.display.set_caption('SCACCHI')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        board.draw_squares(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

        

main()