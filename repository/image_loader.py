import json

import pygame
from utils import root_path


class ImageLoader(object):
    def __init__(self):
        with open(root_path + '/assets/metadata_sprites.json') as data_file:
            self.image = pygame.image.load(root_path + '/assets/sprites.png').convert_alpha()
            self.data = json.load(data_file)["frames"]
            self.metadata = {}
            for item in self.data:
                self.metadata[item["filename"]] = item

    def get_image(self, name):
        image = self.metadata[name]
        frame_sizes = image["frame"]
        cropped = pygame.Surface((frame_sizes["w"], frame_sizes["h"]), pygame.SRCALPHA, 32)
        cropped.blit(self.image, (0, 0), (frame_sizes["x"], frame_sizes["y"], frame_sizes["w"], frame_sizes["h"]))
        return cropped
