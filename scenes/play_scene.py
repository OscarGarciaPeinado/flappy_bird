import pygame

from config import WIDTH, HEIGHT, GAME_WIDTH, MAP_SPEED
from entities.bird import Bird
from entities.floor import Floor
from entities.pipes import Pipes
from entities.score import Score
from repository.image_loader import ImageLoader
from scenes.scene import Scene


class PlayScene(Scene):
    add_pipes = True
    distance = 0

    def __init__(self, game, flappy_engine):
        Scene.__init__(self, game)
        self.flappy_engine = flappy_engine
        self.image_loader = ImageLoader()
        self.initialize_bg(game.screen)
        self.initialize_pipes()
        self.initialize_pipes()
        self.initialize_score()

    def initialize_score(self):
        self.score = Score(GAME_WIDTH, WIDTH - GAME_WIDTH, self.flappy_engine.get_birds())

    def initialize_pipes(self):
        self.pipes = []
        pipes = Pipes(GAME_WIDTH, HEIGHT, MAP_SPEED)
        self.pipes.append(pipes)

    def initialize_bg(self, screen):
        self.floor = Floor(MAP_SPEED, GAME_WIDTH)
        screen.fill((0, 153, 204))

    def on_update(self, time):
        self.game.screen.fill((0, 153, 204))
        self.floor.refresh()
        next_pipe = next(pipes for pipes in self.pipes if not pipes.visited)
        self.flappy_engine.on_update(next_pipe.get_x(), next_pipe.get_y())
        self.refresh_pipes()
        self.check_collision()
        self.refresh_birds_score()
        self.check_if_all_birds_are_dead()
        self.distance += MAP_SPEED * int(time * 0.1)

    def on_event(self, event):
        self.flappy_engine.on_event(event)

    def on_draw(self, screen):
        for pipes in self.pipes:
            pipes.draw(screen)

        screen.blit(self.floor.image, self.floor.rect)
        self.flappy_engine.draw(screen)
        self.score.draw(screen)

    def refresh_pipes(self):
        if GAME_WIDTH - self.pipes[-1].get_x() > 170:
            pipes = Pipes(GAME_WIDTH, HEIGHT, MAP_SPEED)
            self.pipes.append(pipes)
        for pipes in self.pipes:
            pipes.increase_x()

        self.pipes = [pipes for pipes in self.pipes if pipes.get_x() + pipes.get_width() > 0]

    def check_collision(self):
        first_not_visited_pipe = next(pipes for pipes in self.pipes if not pipes.visited)
        self.flappy_engine.check_pipes_collision(first_not_visited_pipe)
        self.flappy_engine.check_floor_collision(self.floor)

    def check_if_all_birds_are_dead(self):
        from scenes.home_scene import HomeScene
        if all(bird.dead for bird in self.flappy_engine.get_birds()):
            self.game.change_scene(HomeScene(self.game))

    def refresh_birds_score(self):
        first_not_visited_pipe = next(pipes for pipes in self.pipes if not pipes.visited)
        not_dead_birds = [bird for bird in self.flappy_engine.get_birds() if not bird.dead]
        if first_not_visited_pipe.get_x() + first_not_visited_pipe.get_width() < GAME_WIDTH / 2:
            for pipes in self.pipes:
                if not pipes.visited:
                    pipes.visited = True
                    break
            for bird in not_dead_birds:
                bird.score += 1
        for bird in not_dead_birds:
            bird.distance = self.distance
