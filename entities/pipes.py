# coding: utf-8
from random import randint

from repository.image_loader import ImageLoader
from utils import rotate_center


class Pipes:
    visited = False

    def __init__(self, x, y, speed):
        self.image_loader = ImageLoader()
        self.lower_pipe, self.lower_rect, self.upper_pipe, self.upper_rect = self.get_sprites(x, y)
        self.speed = speed

    def get_sprites(self, width, height):
        lower_pipe = self.image_loader.get_image("pipe-green.png")
        x = width + lower_pipe.get_width()
        y = height - lower_pipe.get_height()
        y = y + randint(-100, 100)

        lower_rect = lower_pipe.get_rect()
        lower_rect.x, lower_rect.y = (x, y)
        lower_rect.inflate(-2, -2)

        upper_pipe, upper_rect = rotate_center(lower_pipe, lower_pipe.get_rect(), 180)
        upper_rect.x, upper_rect.y = (x, y - 100 - upper_pipe.get_height())
        upper_rect.inflate(-2, -2)

        return lower_pipe, lower_rect, upper_pipe, upper_rect

    def get_x(self):
        return self.lower_rect.x

    def get_y(self):
        return self.lower_rect.y

    def get_width(self):
        return self.lower_rect.width

    def draw(self, screen):
        screen.blit(self.lower_pipe, self.lower_rect)
        screen.blit(self.upper_pipe, self.upper_rect)

    def increase_x(self):
        self.lower_rect.x -= self.speed
        self.upper_rect.x -= self.speed

    def is_collision(self, rect):
        return self.lower_rect.colliderect(rect) or self.upper_rect.colliderect(rect)
