# coding: utf-8
import copy
import random

import numpy as np

from engine.ga_nn_flappy.nn import NN


class GaFlappy:

    def __init__(self, birds):
        self.population = []
        self.epoch = 1
        self.mutate_rate = 0.1

        self.best_score = 0
        self.best_fitness = 0
        self.initialize_population(birds)

        self.generations = 0

    def initialize_population(self, birds):
        for bird in birds:
            population = {"bird": bird, "nn": NN(2, 20, 1, int(bird.name) * 10)}
            self.population.append(population)

    def update(self, next_pipe_x, next_pipe_y):
        for population in self.population:
            bird_x, bird_y = population["bird"].rect.center
            next_pipe_distance_x = bird_x - next_pipe_x
            next_pipe_distance_y = bird_y - next_pipe_y

            probability = population["nn"].predict(next_pipe_distance_x, next_pipe_distance_y)
            if probability > 0.5:
                population['bird'].jump()

    def next_generation(self):
        n_parents = 4
        n_offspring = len(self.population) - n_parents

        parents = self.select_mating_pool(self.population, n_parents)
        offspring = self.crossover_parents(parents, n_offspring)
        next_generation = self.mutation(offspring)

        for i in range(n_parents):
            self.population[i].update(nn=parents[i])

        for i in range(n_parents, len(self.population)):
            self.population[i].update(nn=next_generation[i - n_parents])

        self.generations += 1

    @staticmethod
    def select_mating_pool(population, n_parents):
        p = sorted(population, key=lambda k: k['bird'].distance, reverse=True)
        return [d['nn'] for d in p[:n_parents]]

    def crossover_parents(self, parents, n_offspring):
        if len(parents) == 1:
            return parents

        offspring = []
        for x, y in zip(*[iter(parents)] * 2):
            child = self.crossover(x, y)
            offspring.append(child)

        for i in range(n_offspring - len(offspring)):
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            child = self.crossover(p1, p2)
            offspring.append(child)

        return offspring

    @staticmethod
    def crossover(parent_nn_1, parent_nn_2):
        cut_point = np.random.randint(1, len(parent_nn_1.b1[0]))

        child = NN(2, 20, 1)
        child.b1 = copy.deepcopy(parent_nn_1.b1)

        for i in range(cut_point, len(parent_nn_1.b1[0])):
            child.b1[0][i] = parent_nn_2.b1[0][i]

        if np.random.randint(2):
            child.b2 = copy.deepcopy(parent_nn_1.b2)
            child.w1 = copy.deepcopy(parent_nn_1.w1)
            child.w2 = copy.deepcopy(parent_nn_1.w2)
        else:
            child.b2 = copy.deepcopy(parent_nn_2.b2)
            child.w1 = copy.deepcopy(parent_nn_2.w1)
            child.w2 = copy.deepcopy(parent_nn_2.w2)

        return child

    def mutation(self, offspring):
        for child in offspring:
            for i in range(len(child.b1[0])):
                child.b1[0][i] = self.mutate(child.b1[0][i])

            child.b2[0][0] = self.mutate(child.b2[0][0])

            for i in range(child.w1.shape[0]):
                for j in range(child.w1.shape[1]):
                    child.w1[i][j] = self.mutate(child.w1[i][j])

            for i in range(child.w2.shape[0]):
                for j in range(child.w2.shape[1]):
                    child.w2[i][j] = self.mutate(child.w2[i][j])

        return offspring

    def mutate(self, gene):
        if np.random.rand() < self.mutate_rate:
            mutate_factor = 1 + ((np.random.rand() - 0.5) * 3 + (np.random.rand() - 0.5))
            gene *= mutate_factor

        return gene
