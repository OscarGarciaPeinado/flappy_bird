# coding: utf-8
from ml_engine.ga_ann_flappy_engine.perceptron import Perceptron


class GaFlappy:
    def __init__(self, birds):
        self.epoch = 1
        self.mutate_rate = 1

        self.best_score = 0
        self.best_fitness = 0
        self.initialize_population(birds)

    def initialize_population(self, birds):
        self.population = []
        for bird in birds:
            population = {"bird": bird, "perceptron": Perceptron()}
            self.population.append(population)

    def update(self, x, y):
        for population in self.population:
            bird_x, bird_y = population["bird"].rect.center
            distance_x = bird_x - x
            distance_y = bird_y - y
            print(str(distance_x) + " - " + str(distance_y))
            print(population["perceptron"].predict(distance_x, distance_y))
        pass

    def evolve(self):
        winners = self.select_the_best_population()
        if self.mutate_rate and winners[0]["fitness"] < 0:
            pass
        else:
            self.mutate_rate = 0.2

    def mutate(self):
        pass

    def get_random_unit(self):
        pass

    def select_the_best_population(self):
        pass
