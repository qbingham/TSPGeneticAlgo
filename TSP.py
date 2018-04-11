import numpy
from Chromosome import Chromosome
import random
from Selection import Selection
from Mate import Mate
from copy import deepcopy

cost_requirement = 6400


class TSP:
    def __init__(self):
        self.matrix = numpy.zeros((8, 8))
        self.filename = "data.txt"
        self.sample_space = []
        self.used_space = []
        self.sample_size = 128
        self.pruned_size = 64

    def get_matrix(self):
        return self.matrix

    def read_file(self):
        file = open(self.filename, "r")

        for i in range(0, 8):
            for j in range(0, 8):
                self.matrix[i][j] = int(file.readline())

    def set_sample_space(self):
        for i in range(0, self.sample_size):
            chromosome = Chromosome()
            self.sample_space.append(chromosome)
            path_to_set = [0, 0]
            node_list = [1, 2, 3, 4, 5, 6, 7]
            for j in range(1, 8):
                path_to_set.insert(1, node_list.pop(random.randint(0, 7-j)))
            self.sample_space[i].set_path(path_to_set)
            self.sample_space[i].set_fitness(self.matrix)

    def sort_sample_space(self):
        fitness_list = []
        for chromosome in self.sample_space:
            fitness_list.append(chromosome.get_fitness())
        fitness_list.sort()
        chromosome_list = []
        for fitness in fitness_list:
            for chromosome in self.sample_space:
                if fitness == chromosome.get_fitness():
                    chromosome_list.append(chromosome)
        self.sample_space = chromosome_list

    def prune_space(self):
        for i in range(0, self.pruned_size):
            self.used_space.append(self.sample_space[i])

    def get_pruned_space(self):
        return self.used_space


def runGA(tsp, selections, lowest_cost_child, children_list, cost, generation):
    selections.set_chromosome_list(children_list)

    selections.top_down_pair()

    pair_list = selections.get_pair_list()

    mating = Mate(tsp.get_matrix())
    mating.set_parent_chromosomes(pair_list)
    #mating.single_point_crossover()
    mating.double_point_crossover()

    children_list = mating.get_children_chromosomes()

    print("     ", cost, "      ", generation)
    for child in children_list:
        if child.get_fitness() < cost:
            cost = child.get_fitness()
            lowest_cost_child = deepcopy(child)

    child_path = lowest_cost_child.get_path()
    #print(child_path)
    print("     ", cost, "      ", generation)





def main():
    tsp = TSP()
    tsp.read_file()
    tsp.set_sample_space()
    tsp.prune_space()

    selections = Selection()
    lowest_cost_child = Chromosome()
    children_list = tsp.get_pruned_space()

    generation = 0

    cost = 10000
    while cost > 6400:
        #runGA(tsp, selections, lowest_cost_child, children_list, cost, generation)
        #generation += 1
        selections.set_chromosome_list(children_list)

        selections.tournament_pair()

        pair_list = selections.get_pair_list()

        mating = Mate(tsp.get_matrix())
        mating.set_parent_chromosomes(pair_list)
        mating.single_point_crossover()

        children_list = mating.get_children_chromosomes()

        for child in children_list:
            if child.get_fitness() < cost:
                cost = child.get_fitness()
                lowest_cost_child = deepcopy(child)

        child_path = lowest_cost_child.get_path()
        # print(child_path)
        print("     ", cost, "      ", generation)

        generation += 1

    print("Number of generations:   ", generation)
    child_path = lowest_cost_child.get_path()
    print("Circuit produced:        ", child_path)
    print("Cost of circuit:         ", cost)


main()
