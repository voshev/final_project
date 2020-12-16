import pygame
import os
from snake_test import Snake1, Food, Manager
from snake_colors import *

#set fps
FPS = 18

#set screen size
size = screen_width, screen_height = 1440, 900


game_window = pygame.display.set_mode(size)
bg = pygame.image.load(os.path.join("images", "main_background.png"))


def text_objects(text, font, font_color):
    text_surface = font.render(text, True, font_color)
    return text_surface, text_surface.get_rect()


def button(message, x, y, button_width, button_height, active_color, font_color, action=None):
    '''
    Draws button
    :param message: text that programm draws
           x,y: coordinates of rectangle with text
           button_width, button_height: size of button
           active_color: color of buttons background
           font_color: color of font
    '''
    pygame.draw.rect(game_window, active_color, (x, y, button_width, button_height))

    small_text = pygame.font.Font(os.path.join("fonts", "slkscr.ttf"), 30)
    text_surface, text_rect = text_objects(message, small_text, font_color)
    text_rect.center = ((x + (button_width / 2)), (y + (button_height / 2)))
    game_window.blit(text_surface, text_rect)


def game_loop(Snake_FPS):
    '''
    The main programm loop wich draws snake window
    '''
    done = False
    clock = pygame.time.Clock()
    small_text = pygame.font.Font(os.path.join("fonts", "slkscr.ttf"), 30)
    big_text = pygame.font.Font(os.path.join("fonts", "slkscr.ttf"), 60)
    mgr = Manager()

    screen_size = [800, 600]
   

    screen = pygame.display.set_mode(screen_size)
    while not done:
        clock.tick(Snake_FPS)
        screen.fill(WHITE)
        n = mgr.snake1.length 
        s = "WASD Snake:" + str(n-1)
        text1 = small_text.render(s, False, BLACK)
        game_over_message = "GAME OVER" 
        game_over_text = big_text.render(game_over_message, False, RED)
        score_message = "SCORE:" + str(n-1)
        score_text = big_text.render(score_message, False, BLACK)
        
        if mgr.snake1.lives == 1:
            done = mgr.process(pygame.event.get(), screen)
            screen.blit(text1, (0,0))
        if mgr.snake1.lives < 1:
            screen.fill(WHITE)
            screen.blit(game_over_text, (200,150))
            screen.blit(score_text, (250,200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
        pygame.display.update()

    pygame.quit()


def main():		
    '''
    Function that draws main Menu with options of choose the level and starting the game
    '''
    Snake_FPS = 18
    
    pygame.init()
    pygame.display.set_caption("SNAKE!")

    game_window.blit(bg, (0, 0))

    button('SNAKE!', 600, 750, 250, 50, SKOBELOFF, BUDDHA_GOLD)
    button('1', 1025, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF)
    button('NO', 1025, 494, 80, 50, BUDDHA_GOLD, SKOBELOFF)
    button('NO', 1025, 593, 80, 50, BUDDHA_GOLD, SKOBELOFF)

    clock = pygame.time.Clock()	
    finished = False
    number = 0
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (1025 < event.pos[0] < 1105) and (395 < event.pos[1] < 445):
                    if event.button == 1:
                        number += 1
                        Snake_FPS += 5
                        button(str(number), 1025, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF)
                        if number >= 5:
                            number = 0
                    if event.button == 3:
                        number -= 1
                        if number <= 0:
                            number = 1
                        else:
                            button(str(number), 1025, 395, 80, 50, BUDDHA_GOLD, SKOBELOFF)

                if (1025 < event.pos[0] < 1105) and (494 < event.pos[1] < 544):
                    if event.button == 1:
                        message_text = 'YES'
                        button(message_text, 1025, 494, 80, 50, BUDDHA_GOLD, SKOBELOFF)
                    if event.button == 3:
                        message_text = 'NO'
                        button(message_text, 1025, 494, 80, 50, BUDDHA_GOLD, SKOBELOFF)
                if (600 < event.pos[0] < 850) and (750 < event.pos[1] < 800):
                    game_loop(Snake_FPS)

        pygame.init()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
