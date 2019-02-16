# coding: utf-8
import pygame

from engine.flappy_engine import FlappyEngine
from entities.bird import Bird


class ManualFlappyEngine(FlappyEngine):

    def __init__(self):
        self.birds = [Bird(name="Manual")]

    def get_birds(self):
        return self.birds

    def on_update(self, next_pipe_x, next_pipe_y):
        for bird in self.birds:
            bird.refresh()

    def draw(self, screen):
        for bird in self.birds:
            if not bird.dead:
                screen.blit(bird.image, bird.rect)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            for bird in self.birds:
                bird.jump()

    def check_pipes_collision(self, pipes):
        for bird in self.birds:
            if pipes.is_collision(bird.rect):
                bird.dead = True

    def check_floor_collision(self, floor):
        for bird in self.birds:
            if floor.rect.y < bird.rect.centery:
                bird.dead = True

    def on_finish(self, game, score_panel):
        from scenes.home_scene import HomeScene
        game.change_scene(HomeScene(game))
