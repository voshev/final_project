import pygame
from pygame.draw import *
import os

FPS = 8
size = screen_width, screen_height = 1440, 900
SKOBELOFF = (0, 116, 107)
BUDDHA_GOLD = (196, 184, 0)

bg = pygame.image.load(os.path.join("images", "main_background.png"))


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SNAKE!")

    screen.blit(bg, (0, 0))

    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
