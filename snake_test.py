import pygame as pg
import time
import numpy as np
from random import randint, gauss
import os

pg.init()

horizontal = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
vertical = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
up_right = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
right_down = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
down_left = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
left_up = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))

head_right = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
head_down = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
head_left = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
head_up = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))

tail_right = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
tail_down = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
tail_left = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))
tail_up = pg.image.load(os.path.join("images", "Snake Images", "Snake_main.jpg"))

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
    def __init__(self, color, lives=1, start_coord=None, length=1, width=20, move_direction=0):
        self.lives = lives
        self.move_direction = move_direction
        self.color = color
        self.length = length
        self.width = width
        if start_coord == None:
            start_coord = [randint(0, int(screen_size[0] / self.width) - 1) * self.width,
                     randint(0, int(screen_size[1] / self.width) - 1) * self.width, 'right']
        self.start_coord = start_coord
        self.snake_blocks = [self.start_coord]
        pass

    def move_x(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0] + self.width, self.snake_blocks[0][1], 'right'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0] - self.width, self.snake_blocks[0][1], 'left'])
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def move_y(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] + self.width, 'down'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] - self.width, 'up'])
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def draw(self):
        for block in self.snake_blocks:
            pg.draw.rect(screen, self.color, [block[0], block[1], self.width, self.width])

            # рисует хвост
            if self.length >= 2:
                if block == self.snake_blocks[self.length-1]:
                    if block[2] == 'up':
                        block_coord = [block[0], block[1]]
                        screen.blit(tail_up, tail_up.get_rect(topleft=block_coord))
                    elif block[2] == 'right':
                        block_coord = [block[0], block[1]]
                        screen.blit(tail_right, tail_right.get_rect(topleft=block_coord))
                    elif block[2] == 'down':
                        block_coord = [block[0], block[1]]
                        screen.blit(tail_down, tail_down.get_rect(topleft=block_coord))
                    elif block[2] == 'left':
                        block_coord = [block[0], block[1]]
                        screen.blit(tail_left, tail_left.get_rect(topleft=block_coord))

            # рисует голову
            elif block == self.snake_blocks[0]:
                if block[2] == 'right':
                    block_coord = [block[0], block[1]]
                    screen.blit(head_right, head_right.get_rect(topleft=block_coord))
                elif block[2] == 'down':
                    block_coord = [block[0], block[1]]
                    screen.blit(head_down, head_down.get_rect(topleft=block_coord))
                elif block[2] == 'left':
                    block_coord = [block[0], block[1]]
                    screen.blit(head_left, head_left.get_rect(topleft=block_coord))
                elif block[2] == 'up':
                    block_coord = [block[0], block[1]]
                    screen.blit(head_up, head_up.get_rect(topleft=block_coord))

            # рисует туловищу
            if block[2] == 'horizontal':
                block_coord = [block[0], block[1]]
                screen.blit(horizontal, horizontal.get_rect(topleft=block_coord))
            elif block[2] == 'vertical':
                block_coord = [block[0], block[1]]
                screen.blit(vertical, vertical.get_rect(topleft=block_coord))
            elif block[2] == 'up_right':
                block_coord = [block[0], block[1]]
                screen.blit(up_right, up_right.get_rect(topleft=block_coord))
            elif block[2] == 'right_down':
                block_coord = [block[0], block[1]]
                screen.blit(right_down, right_down.get_rect(topleft=block_coord))
            elif block[2] == 'down_left':
                block_coord = [block[0], block[1]]
                screen.blit(down_left, down_left.get_rect(topleft=block_coord))
            elif block[2] == 'left_up':
                block_coord = [block[0], block[1]]
                screen.blit(left_up, left_up.get_rect(topleft=block_coord))


    def grow(self):
        self.length += 1


class Snake2:
    # предпологается, что snake1 на стрелочках snake2 на awsd в остальном они одинаковы
    def __init__(self, color, lives=1, coord=None, length=1, width=20, move_direction=0):
        self.lives = lives
        self.move_direction = move_direction
        self.color = color
        self.length = length
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0] / self.width) - 1) * self.width,
                     randint(0, int(screen_size[1] / self.width) - 1) * self.width, 'right']
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
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def move_y(self, dir):
        if dir == 1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] + self.width, 'down'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] - self.width, 'up'])
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def draw(self):
        for coord in self.snake_blocks:
            pg.draw.rect(screen, self.color, [coord[0], coord[1], self.width, self.width])
        pass

    def grow(self):
        self.length += 1


class Food:
    def __init__(self, color, coord=None, width=20):
        self.color = color
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0] / self.width) - 1) * self.width,
                     randint(0, int(screen_size[1] / self.width) - 1) * self.width]
        self.coord = coord

    def draw(self):
        pg.draw.rect(screen, self.color, [self.coord[0], self.coord[1], self.width, self.width])

    pass


class Manager:

    def __init__(self):
        self.walls = []
        self.food = [Food(green)]
        self.snake1 = Snake1(red)
        self.snake2 = Snake2(blue)
        self.snakes = [self.snake1, self.snake2]

    def new_food(self):
        self.food.insert(0, Food(green))

    def process(self, events, screen):
        done = self.handle_events(events)

        self.move()

        self.walls_update()

        self.block_direction()

        self.draw()

        self.collide()


        return done

    def handle_events(self, events):
        done = False
        for snake in self.snakes:
            if snake.lives <= 0:
                done = True
        for event in events:
            if event.type == pg.QUIT:
                done = True

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.snakes[0].move_direction = 'up'
                elif event.key == pg.K_DOWN:
                    self.snakes[0].move_direction = 'down'
                elif event.key == pg.K_RIGHT:
                    self.snakes[0].move_direction = 'right'
                elif event.key == pg.K_LEFT:
                    self.snakes[0].move_direction = 'left'
                elif event.key == pg.K_w:
                    self.snakes[1].move_direction = 'up'
                elif event.key == pg.K_s:
                    self.snakes[1].move_direction = 'down'
                elif event.key == pg.K_d:
                    self.snakes[1].move_direction = 'right'
                elif event.key == pg.K_a:
                    self.snakes[1].move_direction = 'left'

        return done

    def draw(self):
        for food in self.food:
            food.draw()
        for snake in self.snakes:
            snake.draw()

    def move(self):
        for snake in self.snakes:
            if snake.move_direction == 'right':
                snake.move_x(1)
            if snake.move_direction == 'left':
                snake.move_x(-1)
            if snake.move_direction == 'down':
                snake.move_y(1)
            if snake.move_direction == 'up':
                snake.move_y(-1)

    def walls_update(self):
        self.walls = []
        for snake in self.snakes:
            for t in range(int(screen_size[0] / snake.width)):
                self.walls.append([t * snake.width, -snake.width])
                self.walls.append([t * snake.width, screen_size[1]])
            for y in range(int(screen_size[1] / snake.width)):
                self.walls.append([-snake.width, y * snake.width])
                self.walls.append([screen_size[0], y * snake.width])
        for snake in self.snakes:
            for e in range(1, snake.length - 1):
                self.walls.append([snake.snake_blocks[e][0], snake.snake_blocks[e][1]])

    def collide(self):
        for snake in self.snakes:
            for i in range(snake.length):
                for i in range(len(self.food)):
                    if [snake.snake_blocks[i][0], snake.snake_blocks[i][1]] == self.food[i].coord:
                        snake.grow()
                        self.food.pop(i)
                        self.new_food()
                for wall in self.walls:
                    if [snake.snake_blocks[i][0], snake.snake_blocks[i][1]] == wall:
                        snake.move_direction = 0
                        snake.lives -= 1

    def block_direction(self):
        for snake in self.snakes:
            n = snake.length
            for i in range(1, n-1):
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

            if n >= 2:
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
                    snake.snake_blocks[n - 1][2] = 'right'


done = False
done1 = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(18)
    screen.fill(black)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

pg.quit()
