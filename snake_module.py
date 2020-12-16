from snake_test import*


class Snake1:
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
        #provides movement along the X axis
        if dir == 1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0] + self.width, self.snake_blocks[0][1], 'right'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0] - self.width, self.snake_blocks[0][1], 'left'])
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def move_y(self, dir):
        # provides movement along the X axis
        if dir == 1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] + self.width, 'down'])
        elif dir == -1:
            self.snake_blocks.insert(0,
                                     [self.snake_blocks[0][0], self.snake_blocks[0][1] - self.width, 'up'])
        if self.length + 1 == len(self.snake_blocks):
            self.snake_blocks.pop(self.length)

    def draw(self):
        # draw snake blocks
        for block in self.snake_blocks:
            pg.draw.rect(screen, self.color, [block[0], block[1], self.width, self.width])



            # draw head
            if block == self.snake_blocks[0]:
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


            # draw tail
            if self.length >= 2:
                if block == self.snake_blocks[self.length - 1]:
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


            # draw boody
            if block[2] == 'horizontal':
                block_coord = [block[0], block[1]]
                screen.blit(horizontal, horizontal.get_rect(topleft=block_coord))
            elif block[2] == 'vertical':
                block_coord = [block[0], block[1]]
                screen.blit(vertical, vertical.get_rect(topleft=block_coord))
            # elif block[2] == 'up_right':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(up_right, up_right.get_rect(topleft=block_coord))
            # elif block[2] == 'right_down':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(right_down, right_down.get_rect(topleft=block_coord))
            # elif block[2] == 'down_left':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(down_left, down_left.get_rect(topleft=block_coord))
            # elif block[2] == 'left_up':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(left_up, left_up.get_rect(topleft=block_coord))

            # if block[2] == 'right':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(head_right, head_right.get_rect(topleft=block_coord))
            # elif block[2] == 'down':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(head_down, head_down.get_rect(topleft=block_coord))
            # elif block[2] == 'left':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(head_left, head_left.get_rect(topleft=block_coord))
            # elif block[2] == 'up':
            #     block_coord = [block[0], block[1]]
            #     screen.blit(head_up, head_up.get_rect(topleft=block_coord))


    def grow(self):
        self.length += 1

