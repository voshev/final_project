import pygame as pg
import time
import numpy as np
from random import randint, gauss

pg.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen_size = [1440, 900]

screen = pg.display.set_mode(screen_size)


class Snake1:
    def __init__(self, color, coord=None, length=0, width=10):
        if coord == None:
            coord = [randint(0, screen_size[0] - self.width), randint(0, screen_size[0] - self.width)]
        self.coord = coord
        self.length = length
        self.width = width
        self.color = color
        self.snake_blocks_coord = []

        pass

    def move(self):
        pass

    def draw(self):
        for coord in self.snake_blocks_coord:
            pg.draw.rect(screen, self.color, [coord, self.width, self.width])
        pass

    def eat(self):
        self.length += 1


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
        self.food = []

        self.snake = Snake1()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_static_targets = n_static_targets
        self.n_moving_targets = n_moving_targets
        self.new_mission()

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
