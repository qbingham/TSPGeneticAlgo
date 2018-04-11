from Chromosome import Chromosome
import random


def mutate(path):
    for gene in range(1, 7):
        if 1 == random.randint(0, 4):
            path[gene], path[gene + 1] = path[gene + 1], path[gene]
    return path

class Mate:
    def __init__(self, matrix_to_set):
        self.parent_chromosomes = []
        self.child_chromosomes = []
        self.matrix = matrix_to_set

    def set_parent_chromosomes(self, list_to_set):
        self.parent_chromosomes = list_to_set

    def get_children_chromosomes(self):
        return self.child_chromosomes



    def single_point_crossover(self):
        for i in range (0, 32):
            temp = self.parent_chromosomes[i]
            p0 = temp[0]
            p1 = temp[1]
            p0_path = p0.get_path()
            p1_path = p1.get_path()
            c0 = Chromosome()
            c1 = Chromosome()
            c0_path = []
            c1_path = []
            for j in range(0, 4):
                c0_path.append(p0_path[j])
                c1_path.append(p1_path[j])
            for j in range(4, 9):
                c0_path.append(p1_path[j])
                c1_path.append(p0_path[j])

            c0_duplicates = []
            c1_duplicates = []
            for j in range(1, 9):
                for k in range(j+1, 9):
                    if c0_path[j] == c0_path[k]:
                        c0_duplicates.append(c0_path[k])
                    if c1_path[j] == c1_path[k]:
                        c1_duplicates.append(c1_path[k])

            for j in range(1, 9):
                for k in range(j + 1, 9):
                    if c0_path[j] == c0_path[k]:
                        c0_path[j] = c1_duplicates[-1]
                        c1_duplicates.pop(-1)
                    if c1_path[j] == c1_path[k]:
                        c1_path[j] = c0_duplicates[-1]
                        c0_duplicates.pop(-1)

            c0_path = mutate(c0_path)
            c1_path = mutate(c1_path)

            c0.set_path(c0_path)
            c1.set_path(c1_path)



            c0.set_fitness(self.matrix)
            c1.set_fitness(self.matrix)
            self.child_chromosomes.append(c0)
            self.child_chromosomes.append(c1)


    def double_point_crossover(self):
        for i in range (0, 32):
            temp = self.parent_chromosomes[i]
            p0 = temp[0]
            p1 = temp[1]
            p0_path = p0.get_path()
            p1_path = p1.get_path()
            c0 = Chromosome()
            c1 = Chromosome()
            c0_path = []
            c1_path = []
            for j in range(0, 3):
                c0_path.append(p0_path[j])
                c1_path.append(p1_path[j])
            for j in range(3, 6):
                c0_path.append(p1_path[j])
                c1_path.append(p0_path[j])
            for j in range(6, 9):
                c0_path.append(p1_path[j])
                c1_path.append(p0_path[j])


            c0_duplicates = []
            c1_duplicates = []
            for j in range(1, 9):
                for k in range(j+1, 9):
                    if c0_path[j] == c0_path[k]:
                        c0_duplicates.append(c0_path[k])
                    if c1_path[j] == c1_path[k]:
                        c1_duplicates.append(c1_path[k])

            for j in range(1, 9):
                for k in range(j + 1, 9):
                    if c0_path[j] == c0_path[k]:
                        c0_path[j] = c1_duplicates[-1]
                        c1_duplicates.pop(-1)
                    if c1_path[j] == c1_path[k]:
                        c1_path[j] = c0_duplicates[-1]
                        c0_duplicates.pop(-1)


            for gene in range(1,7):
                if 1 == random.randint(0, 4):
                    c0_path[gene], c0_path[gene + 1] = c0_path[gene + 1], c0_path[gene]

            for gene in range(1, 7):
                if 1 == random.randint(0, 4):
                    c1_path[gene], c1_path[gene + 1] = c1_path[gene + 1], c1_path[gene]

            c0.set_path(c0_path)
            c1.set_path(c1_path)

            c0.set_fitness(self.matrix)
            c1.set_fitness(self.matrix)
            self.child_chromosomes.append(c0)
            self.child_chromosomes.append(c1)
