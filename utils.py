import math
import os

import pygame

root_path = os.path.dirname(os.path.abspath(__file__))


def get_repeated_surface(image, width):
    number_of_image = math.ceil(width / image.get_width()) + 1

    cropped = pygame.Surface(
        (image.get_width() * number_of_image, image.get_height()),
        pygame.SRCALPHA, 32)
    x = 0
    for base in range(number_of_image):
        cropped.blit(image, (x, 0))
        x += image.get_width()
    return cropped


def rotate_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect
