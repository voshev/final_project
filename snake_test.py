import pygame as pg
import time
import numpy as np
from random import randint, gauss
import os



pg.init()

apfel = pg.image.load(os.path.join("images", "Food_apple.jpg"))
apfel.set_colorkey((28, 248, 18))

#load game textures
horizontal = pg.image.load(os.path.join("images", "Snake_main_horizontal.jpg"))
vertical =   pg.image.load(os.path.join("images", "Snake_main_vertical.jpg"))
up_right =   pg.image.load(os.path.join("images", "Snake_main.jpg"))
right_down = pg.image.load(os.path.join("images", "Snake_main.jpg"))
down_left =  pg.image.load(os.path.join("images", "Snake_main.jpg"))
left_up =    pg.image.load(os.path.join("images", "Snake_main.jpg"))

head_right = pg.image.load(os.path.join("images", "Snake_head_right.jpg"))
head_down =  pg.image.load(os.path.join("images", "Snake_head_down.jpg"))
head_left =  pg.image.load(os.path.join("images", "Snake_head_left.jpg"))
head_up =    pg.image.load(os.path.join("images", "Snake_head_up.jpg"))

tail_right = pg.image.load(os.path.join("images", "Snake_tail_left.jpg"))
tail_down =  pg.image.load(os.path.join("images", "Snake_tail_up.jpg"))
tail_left =  pg.image.load(os.path.join("images", "Snake_tail_right.jpg"))
tail_up =    pg.image.load(os.path.join("images", "Snake_tail_down.jpg"))

brick_wall = pg.image.load(os.path.join("images", "Brick_wall.png"))

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen_size = [800, 600]

screen = pg.display.set_mode(screen_size)



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
    #food class
    def __init__(self, color, coord=None, width=20):
        self.color = color
        self.width = width
        if coord == None:
            coord = [randint(0, int(screen_size[0] / self.width) - 1) * self.width,
                     randint(0, int(screen_size[1] / self.width) - 1) * self.width]
        self.coord = coord

    def draw(self):
        # draw food
        pg.draw.rect(screen, self.color, [self.coord[0], self.coord[1], self.width, self.width])

        block_coord = [self.coord[0], self.coord[1]]
        screen.blit(apfel, apfel.get_rect(topleft=block_coord))

    pass

from snake_module import Snake1

class Manager:
    """
    class hendeling main game pcocces
    """
    def __init__(self):
        self.walls = []
        self.food = [Food(green)]
        self.snake1 = Snake1(red)
        # self.snake2 = Snake2(blue)
        # self.snakes = [self.snake1, self.snake2]
        self.snakes = [self.snake1]

    def new_food(self):
        """
        create new food
        """
        self.food.insert(0, Food(green))

    def process(self, events, screen):
        """
        main game processes
        """
        done = self.handle_events(events)

        self.move()

        self.walls_update()

        self.block_direction()

        self.pass_through_screen_edge()

        self.draw()

        self.collide()


        return done

    def handle_events(self, events):
        """
        work with comands got from user
        """
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
        """
        activate objekts draw funktions
        """
        for food in self.food:
            food.draw()
        for snake in self.snakes:
            snake.draw()

    def move(self):
        """
        activate objekts moove funktions
        """
        for snake in self.snakes:
            if snake.move_direction == 'right':
                snake.move_x(1)
            if snake.move_direction == 'left':
                snake.move_x(-1)
            if snake.move_direction == 'down':
                snake.move_y(1)
            if snake.move_direction == 'up':
                snake.move_y(-1)

    def pass_through_screen_edge(self):
        """
        allow snake to pass throght screan edges apearin on the opposite side
        """
        for snake in self.snakes:
            for block in snake.snake_blocks:
                if block[0] >= screen_size[0]:
                    block[0] = 0
                elif block[0] <= -snake.width:
                    block[0] = screen_size[0]-snake.width
                if block[1] >= screen_size[1]:
                    block[1] = 0
                elif block[1] <= -snake.width:
                    block[1] = screen_size[1]-snake.width






    def walls_update(self):
        """
        add and update objects snake couldn't pass throught
        """
        self.walls = [[160,100],[160,120],[160,140],[160,160],[160,180],[160,200],[160,220],[160,240],[160,260],[160,280],[160,300],
        [220,120],[240,120],[260,120],[280,120],[300,120],[320,120],[340,120],[360,120],[380,120],[400,120]]
        self.blocks = []
        for wall in self.walls:
            screen.blit(brick_wall, brick_wall.get_rect(topleft=wall))
        for snake in self.snakes:
            for e in range(1, snake.length - 1):
                self.blocks.append([snake.snake_blocks[e][0], snake.snake_blocks[e][1]])
 

    def collide(self):
        """
        hendle snake collisions with walls and food
        """
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
                for block in self.blocks:
                    if [snake.snake_blocks[i][0], snake.snake_blocks[i][1]] == block:
                        snake.move_direction = 0
                        snake.lives -= 1                    
        for i in range(len(self.food)):
            for wall in self.snakes:
                if wall == self.food[i].coord:
                    self.food.pop(i)
                    self.new_food()
                    
                    
    def block_direction(self):
        """
        update snake blocks textures
        """
        for snake in self.snakes:
            
            #updqate body
            n = snake.length
            for i in range(1, n-1):
                if (snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0] == 0):
                    snake.snake_blocks[i][2] = 'vertical'
                elif (snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] == 0):
                    snake.snake_blocks[i][2] = 'horizontal'
                # elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                #         snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] > 0) and
                #       snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                #       snake.snake_blocks[i][0] > 0):
                #     snake.snake_blocks[i][2] = 'up-right'
                # elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                #         snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] > 0) and
                #       snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                #       snake.snake_blocks[i][0] < 0):
                #     snake.snake_blocks[i][2] = 'down-left'
                # elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                #         snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] < 0) and
                #       snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                #       snake.snake_blocks[i][0] > 0):
                #     snake.snake_blocks[i][2] = 'right-down'
                # elif ((snake.snake_blocks[i - 1][0] - snake.snake_blocks[i + 1][0]) * (
                #         snake.snake_blocks[i - 1][1] - snake.snake_blocks[i + 1][1] < 0) and
                #       snake.snake_blocks[i - 1][0] + snake.snake_blocks[i + 1][0] - 2 *
                #       snake.snake_blocks[i][0] < 0):
                #     snake.snake_blocks[i][2] = 'left-up'

            #update head
            snake.snake_blocks[0][2] = snake.move_direction

            #update tail
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
