# coding: utf-8

from random import randint

from config import HEIGHT, GAME_WIDTH
from engine.flappy_engine import FlappyEngine
from engine.ga_nn_flappy.ga import GaFlappy
from entities.bird import Bird


class GaNnFlappyEngine(FlappyEngine):

    def __init__(self):
        self.birds = []
        for index in range(10):
            y = HEIGHT / 2 + randint(-100, 100)
            self.birds.append(Bird(name=str(index), y=y))

        self.ga_flappy = GaFlappy(self.birds)

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
        for bird in self.birds:
            bird.dead = True

    def check_pipes_collision(self, pipes):
        for bird in self.birds:
            if not bird.dead and pipes.is_collision(bird.rect):
                bird.dead = True

    def check_floor_collision(self, floor):
        for bird in self.birds:
            if not bird.dead and (floor.rect.y < bird.rect.centery or bird.rect.centery < 0):
                bird.dead = True

    def on_finish(self, game, score_panel):
        self.ga_flappy.next_generation()

        for bird in self.birds:
            bird.dead = False
            bird.distance = 0
            bird.score = 0
            bird.rect.center = (GAME_WIDTH / 2, HEIGHT / 2 + randint(-100, 100))

        from scenes.play_scene import PlayScene
        game.change_scene(PlayScene(game, self, score_panel))
