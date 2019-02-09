import pygame

from config import HEIGHT, WIDTH
from repository.image_loader import ImageLoader
from utils import root_path


class OptionMenu(pygame.Surface):
    white = (255, 255, 255)

    def __init__(self, name, x, y):
        self.image_loader = ImageLoader()
        font = pygame.font.Font(root_path + '/assets/flappy_bird_font.ttf', 80)
        surface = font.render(name, True, self.white)
        pygame.Surface.__init__(self, (surface.get_width(), surface.get_height()), pygame.SRCALPHA, 32)

        self.x, self.y = (x - (surface.get_width() / 2)), (y + (surface.get_height() / 2))

        self.blit(surface, (0, 0), (0, 0, surface.get_width(), surface.get_height()))
        self.name = name

    def text_objects(self, name):
        textSurface = self.font.render(name, True, self.white)
        return textSurface, textSurface.get_rect()
