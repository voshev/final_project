import pygame as pg
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen = pg.display.set_mode(SCREEN_SIZE)


class Snake1:
    def __init__(self):
        pass

    def move(self):
        pass

    def draw(self):
        pass


class Snake2:
    def __init__(self):
        pass

    def move(self):
        pass

    def draw(self):
        pass


class Food:
    pass


class Manager:

    def __init__(self):
        pass

    def new_food(self):
        pass

    def process(self, events, screen):
        done = self.handle_events(events)

        self.move()

        self.collide()

        self.draw(screen)

        return done

    def handle_events(self, events):
        done = False

        return done

    def draw(self, screen):
        pass

    def move(self):
        pass

    def collide(self):
        pass


done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)
    screen.fill(black)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

pg.quit()
