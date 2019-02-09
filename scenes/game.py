import pygame
import sys

from config import *
from scenes.play_scene import PlayScene


class Game():
    def __init__(self):
        pygame.display.set_caption(GAME_NAME)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((255, 255, 255))
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def on_exit(self):
        pygame.quit()
        sys.exit()

    def loop(self):
        while not self.quit_flag:
            time = self.clock.tick(FPS)
            # self.scene.time = time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    else:
                        self.scene.on_event(event)

            self.scene.on_update(time)

            self.scene.on_draw(self.screen)

            pygame.display.flip()

    def change_scene(self, scene):
        self.scene = scene

    def quit(self):
        self.quit_flag = True
