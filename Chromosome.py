class Chromosome:

    def __init__(self):
        self.path = []
        self.fitness = 0

    def set_path(self, path_to_set):
        for node in path_to_set:
            self.path.append(node)

    def get_path(self):
        return self.path

    def set_fitness(self, matrix):
        for i in range(0, 8):
            self.fitness += matrix[self.path[i%8]][self.path[(i+1)%8]]

    def get_fitness(self):
        return self.fitness
