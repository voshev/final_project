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
    # предпологается, что snake1 на стрелочках snake2 на awsd в остальном они одинаковы
    def __init__(self, color, coord=None, length=1, width=20):
        self.color = color
        self.length = length
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0]/self.width)-1) * self.width, randint(0, int(screen_size[1]/self.width)-1) * self.width, 'right']
        self.coord = coord
        self.snake_blocks = [self.coord]
        pass

    def move_x(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0] + self.width, self.snake_blocks[0][1], 'right'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0] - self.width, self.snake_blocks[0][1], 'left'])
        self.snake_blocks.pop(self.length)

    def move_y(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0], self.snake_blocks[0][1] + self.width, 'down'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0], self.snake_blocks[0][1] - self.width, 'up'])
        self.snake_blocks.pop(self.length)

    def draw(self):
        for coord in self.snake_blocks:
            pg.draw.rect(screen, self.color, [coord[0], coord[1], self.width, self.width])
        pass

    def eat(self):
        self.length += 1


class Snake2:
    # предпологается, что snake1 на стрелочках snake2 на awsd в остальном они одинаковы
    def __init__(self, color, coord=None, length=1, width=20):
        self.color = color
        self.length = length
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0]/self.width)-1) * self.width, randint(0, int(screen_size[1]/self.width)-1) * self.width, 'right']
        self.coord = coord
        self.snake_blocks = []
        pass

    def move_x(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0] + self.width, self.snake_blocks[0][1], 'right'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0] - self.width, self.snake_blocks[0][1], 'left'])

        self.snake_blocks.pop(self.length)

    def move_y(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0], self.snake_blocks[0][1] + self.width, 'down'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                [self.snake_blocks[0][0], self.snake_blocks[0][1] - self.width, 'up'])
        self.snake_blocks.pop(self.length)

    def draw(self):
        for coord in self.snake_blocks:
            pg.draw.rect(screen, self.color, [coord[0], coord[1], self.width, self.width])
        pass

    def eat(self):
        self.length += 1


class Food:
    def __init__(self, color, coord = None, width=20):
        self.color = color
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0]/self.width)-1) * self.width, randint(0, int(screen_size[1]/self.width)-1) * self.width]
        self.coord = coord
    def draw(self):
        pg.draw.rect(screen, self.color, [self.coord[0], self.coord[1], self.width, self.width])
    pass


class Manager:

    def __init__(self):
        self.food = []
        self.snake1 = Snake1(red)
        self.snake2 = Snake2(blue)
        self.snakes = [self.snake1, self.snake2]

        pass

    def new_food(self):
        self.food.insert(0,Food(green))
        pass

    def process(self, events, screen):
        done = self.handle_events(events)

        self.move()

        self.block_direction()

        self.collide()

        self.draw(screen)

        return done

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.snake1.move_y(-1)
                elif event.key == pg.K_DOWN:
                    self.snake1.move_y(1)
                elif event.key == pg.K_RIGHT:
                    self.snake1.move_x(1)
                elif event.key == pg.K_LEFT:
                    self.snake1.move_x(-1)
                elif event.key == pg.K_UP:
                    self.snake2.move_y(-1)
                elif event.key == pg.K_DOWN:
                    self.snake2.move_y(1)
                elif event.key == pg.K_RIGHT:
                    self.snake2.move_x(1)
                elif event.key == pg.K_LEFT:
                    self.snake2.move_x(-1)

        return done

    def draw(self,screen):
        for food in self.food:
            food.draw()
        for snake in self.snakes:
            snake.draw()

        pass

    def move(self):
        pass

    def collide(self):
        pass

    def block_direction(self):
        for snake in self.snakes:
            n = snake.length
            for i in range(1, n - 2):
                if (snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0] == 0):
                    snake.snake_blocks[i][2] = 'vertical'
                elif (snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] == 0):
                    snake.snake_blocks[i][2] = 'horizontal'
                elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                        snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] > 0) and
                      snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                      snake.snake_blocks[i][0] > 0):
                    snake.snake_blocks[i][2] = 'up-right'
                elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                        snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] > 0) and
                      snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                      snake.snake_blocks[i][0] < 0):
                    snake.snake_blocks[i][2] = 'down-left'
                elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                        snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] < 0) and
                      snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                      snake.snake_blocks[i][0] > 0):
                    snake.snake_blocks[i][2] = 'right-down'
                elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                        snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] < 0) and
                      snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                      snake.snake_blocks[i][0] < 0):
                    snake.snake_blocks[i][2] = 'left-up'
            if n > 1:
                if (snake.snake_blocks[0][0] - snake.snake_blocks[1][0] == 0 and snake.snake_blocks[0][1] -
                        snake.snake_blocks[1][1] < 0):
                    snake.snake_blocks[0][2] = 'up'
                elif (snake.snake_blocks[0][0] - snake.snake_blocks[1][0] == 0 and snake.snake_blocks[0][1] -
                      snake.snake_blocks[1][1] < 0):
                    snake.snake_blocks[0][2] = 'down'
                elif (snake.snake_blocks[0][0] - snake.snake_blocks[1][0] < 0 and snake.snake_blocks[0][1] -
                      snake.snake_blocks[1][1] == 0):
                    snake.snake_blocks[0][2] = 'left'
                elif (snake.snake_blocks[0][0] - snake.snake_blocks[1][0] > 0 and snake.snake_blocks[0][1] -
                      snake.snake_blocks[1][1] == 0):
                    snake.snake_blocks[0][2] = 'left'

                if (snake.snake_blocks[n - 1][0] - snake.snake_blocks[n - 2][0] == 0 and
                        snake.snake_blocks[n - 1][1] - snake.snake_blocks[n - 2][1] < 0):
                    snake.snake_blocks[n - 1][2] = 'up'
                elif (snake.snake_blocks[n - 1][0] - snake.snake_blocks[n - 2][0] == 0 and
                      snake.snake_blocks[n - 1][1] - snake.snake_blocks[n - 2][1] < 0):
                    snake.snake_blocks[n][2] = 'down'
                elif (snake.snake_blocks[n - 1][0] - snake.snake_blocks[n - 2][0] < 0 and
                      snake.snake_blocks[n - 1][1] - snake.snake_blocks[n - 2][1] == 0):
                    snake.snake_blocks[n - 1][2] = 'left'
                elif (snake.snake_blocks[n - 1][0] - snake.snake_blocks[n - 2][0] > 0 and
                      snake.snake_blocks[n - 1][1] - snake.snake_blocks[n - 2][1] == 0):
                    snake.snake_blocks[n - 1][2] = 'left'


done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)
    screen.fill(black)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

pg.quit()

