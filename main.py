import pygame 
from constants import WID, HEI, SQ_SIZE
from game import Game

FPS = 60

WIN = pygame.display.set_mode((WID, HEI))
pygame.display.set_caption('SCACCHI')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQ_SIZE
        col = x // SQ_SIZE
        return row, col
    

    while run:
        clock.tick(FPS)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                game.board.debug_print()

        



        game.update()

        

main()