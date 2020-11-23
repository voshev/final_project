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
    def __init__(self, color, coord=None, length=0, width=20):
        if coord == None:
            coord = [randint(0, screen_size[0] - self.width), randint(0, screen_size[0] - self.width), 0]
        self.coord = coord
        self.length = length
        self.width = width
        self.color = color
        self.snake_blocks = []
        pass

    def move(self):
        pass

    def draw(self):
        for coord in self.snake_blocks:
            pg.draw.rect(screen, self.color, [coord[0], coord[1], self.width, self.width])
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
    def __init__(self, coord):
        self.coord = coord

    pass


class Manager:

    def __init__(self):
        self.food = []
        self.snake = Snake1()
        self.targets = []

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

    def block_direction(self):
        n = len(self.snake.snake_blocks)
        for i in range(1, n - 2):
            if (self.snake.snake_blocks[i - 1][0] - self.snake.snake_blocks[i + 1][0] == 0):
                self.snake.snake_blocks[i][2] = 'vertical'
            elif (self.snake.snake_blocks[i - 1][1] - self.snake.snake_blocks[i + 1][1] == 0):
                self.snake.snake_blocks[i][2] = 'horizontal'
            elif ((self.snake.snake_blocks[i - 1][0] - self.snake.snake_blocks[i + 1][0]) * (
                    self.snake.snake_blocks[i - 1][1] - self.snake.snake_blocks[i + 1][1] > 0) and
                  self.snake.snake_blocks[i - 1][0] + self.snake.snake_blocks[i + 1][0] - 2 *
                  self.snake.snake_blocks[i][0] > 0):
                self.snake.snake_blocks[i][2] = 'up-right'
            elif ((self.snake.snake_blocks[i - 1][0] - self.snake.snake_blocks[i + 1][0]) * (
                    self.snake.snake_blocks[i - 1][1] - self.snake.snake_blocks[i + 1][1] > 0) and
                  self.snake.snake_blocks[i - 1][0] + self.snake.snake_blocks[i + 1][0] - 2 *
                  self.snake.snake_blocks[i][0] < 0):
                self.snake.snake_blocks[i][2] = 'down-left'
            elif ((self.snake.snake_blocks[i - 1][0] - self.snake.snake_blocks[i + 1][0]) * (
                    self.snake.snake_blocks[i - 1][1] - self.snake.snake_blocks[i + 1][1] < 0) and
                  self.snake.snake_blocks[i - 1][0] + self.snake.snake_blocks[i + 1][0] - 2 *
                  self.snake.snake_blocks[i][0] > 0):
                self.snake.snake_blocks[i][2] = 'right-down'
            elif ((self.snake.snake_blocks[i - 1][0] - self.snake.snake_blocks[i + 1][0]) * (
                    self.snake.snake_blocks[i - 1][1] - self.snake.snake_blocks[i + 1][1] < 0) and
                  self.snake.snake_blocks[i - 1][0] + self.snake.snake_blocks[i + 1][0] - 2 *
                  self.snake.snake_blocks[i][0] < 0):
                self.snake.snake_blocks[i][2] = 'left-up'

        if (self.snake.snake_blocks[0][0] - self.snake.snake_blocks[1][0] == 0 and self.snake.snake_blocks[0][1] -
                self.snake.snake_blocks[1][1] < 0):
            self.snake.snake_blocks[0][2] = 'up'
        elif (self.snake.snake_blocks[0][0] - self.snake.snake_blocks[1][0] == 0 and self.snake.snake_blocks[0][1] -
              self.snake.snake_blocks[1][1] < 0):
            self.snake.snake_blocks[0][2] = 'down'
        elif (self.snake.snake_blocks[0][0] - self.snake.snake_blocks[1][0] < 0 and self.snake.snake_blocks[0][1] -
              self.snake.snake_blocks[1][1] == 0):
            self.snake.snake_blocks[0][2] = 'left'
        elif (self.snake.snake_blocks[0][0] - self.snake.snake_blocks[1][0] > 0 and self.snake.snake_blocks[0][1] -
              self.snake.snake_blocks[1][1] == 0):
            self.snake.snake_blocks[0][2] = 'left'

        if (self.snake.snake_blocks[n - 1][0] - self.snake.snake_blocks[n - 2][0] == 0 and
                self.snake.snake_blocks[n - 1][1] - self.snake.snake_blocks[n - 2][1] < 0):
            self.snake.snake_blocks[n - 1][2] = 'up'
        elif (self.snake.snake_blocks[n - 1][0] - self.snake.snake_blocks[n - 2][0] == 0 and
              self.snake.snake_blocks[n - 1][1] - self.snake.snake_blocks[n - 2][1] < 0):
            self.snake.snake_blocks[n][2] = 'down'
        elif (self.snake.snake_blocks[n - 1][0] - self.snake.snake_blocks[n - 2][0] < 0 and
              self.snake.snake_blocks[n - 1][1] - self.snake.snake_blocks[n - 2][1] == 0):
            self.snake.snake_blocks[n - 1][2] = 'left'
        elif (self.snake.snake_blocks[n - 1][0] - self.snake.snake_blocks[n - 2][0] > 0 and
              self.snake.snake_blocks[n - 1][1] - self.snake.snake_blocks[n - 2][1] == 0):
            self.snake.snake_blocks[n - 1][2] = 'left'


done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)
    screen.fill(black)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

pg.quit()
