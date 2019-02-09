import pygame

from repository.image_loader import ImageLoader
from config import WIDTH, HEIGHT
from utils import get_repeated_surface


class Floor(pygame.sprite.Sprite):
    def __init__(self, x_speed, width=WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.x_speed = x_speed
        self.base = ImageLoader().get_image("base.png")

        self.image = get_repeated_surface(self.base, width)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - self.base.get_height()

    def refresh(self):
        self.rect.x = -((-self.rect.x + self.x_speed) % self.base.get_width())
