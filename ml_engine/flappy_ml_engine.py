# coding: utf-8

class FlappyMlEngine:
    def get_birds(self):
        raise NotImplementedError

    def on_update(self, next_pipe_x, next_pipe_y):
        raise NotImplementedError

    def check_pipes_collision(self, pipes):
        raise NotImplementedError

    def check_floor_collision(self, floor):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError

    def on_event(self, event):
        raise NotImplementedError
