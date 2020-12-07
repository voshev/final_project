import pygame
import os

FPS = 8
size = screen_width, screen_height = 1440, 900
SKOBELOFF = (0, 116, 107)
BUDDHA_GOLD = (196, 184, 0)
BLACK = (255, 255, 255)

game_window = pygame.display.set_mode(size)
bg = pygame.image.load(os.path.join("images", "main_background.png"))


def text_objects(text, font, font_color):
    text_surface = font.render(text, True, font_color)
    return text_surface, text_surface.get_rect()


def button(message, x, y, button_width, button_height, active_color, font_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x < mouse[0] < x + button_width) and (y < mouse[1] < y + button_height):
        pygame.draw.rect(game_window, active_color, (x, y, button_width, button_height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(game_window, active_color, (x, y, button_width, button_height))

    small_text = pygame.font.Font(os.path.join("fonts", "slkscr.ttf"), 30)
    text_surface, text_rect = text_objects(message, small_text, font_color)
    text_rect.center = ((x + (button_width / 2)), (y + (button_height / 2)))
    game_window.blit(text_surface, text_rect)


def game_loop():
    pass


def list_stop():
    pass


def list_of_levels():
    button('2', 1110, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF, list_stop())
    button('3', 1195, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF, list_stop())


def list_of_answers(x, y):
    button('YES', x, y, 80, 50, BUDDHA_GOLD, SKOBELOFF, list_stop())


def main():
    pygame.init()
    pygame.display.set_caption("SNAKE!")

    game_window.blit(bg, (0, 0))

    button('SNAKE!', 600, 750, 250, 50, SKOBELOFF, BUDDHA_GOLD, game_loop())
    button('1', 1025, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF,  list_of_levels())
    button('NO', 1025, 494, 80, 50, BUDDHA_GOLD, SKOBELOFF, list_of_answers(1110, 494))
    button('NO', 1025, 593, 80, 50, BUDDHA_GOLD, SKOBELOFF, list_of_answers(1110, 593))

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
