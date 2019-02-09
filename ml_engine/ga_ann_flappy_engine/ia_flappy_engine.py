# coding: utf-8
import pygame

from config import HEIGHT
from entities.bird import Bird
from ml_engine.flappy_ml_engine import FlappyMlEngine
from random import randint

from ml_engine.ga_ann_flappy_engine.ga_flappy import GaFlappy


class IaFlappyEngine(FlappyMlEngine):
    def __init__(self):
        self.birds = []
        self.initialize_birds()
        self.initialize_gap()

    def get_birds(self):
        return self.birds

    def on_update(self, next_pipe_x, next_pipe_y):
        for bird in self.birds:
            bird.refresh()
            self.ga_flappy.update(next_pipe_x, next_pipe_y)

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

    def initialize_birds(self):
        for index in range(5):
            y = HEIGHT / 2 + randint(-100, 100)
            self.birds.append(Bird(name=str(index), y=y))

    def initialize_gap(self):
        self.ga_flappy = GaFlappy(self.get_birds())
