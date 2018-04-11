import random


class Selection:
    def __init__(self):
        self.chromosome_list = []
        self.pair_list = []


    def set_chromosome_list(self, list_to_set):
        self.chromosome_list = list_to_set

    def top_down_pair(self):
        for i in range(0, 64, 2):
            temp = (self.chromosome_list[i], self.chromosome_list[i+1])
            self.pair_list.append(temp)

    def tournament_pair(self):
        index_list = list(range(0, 64))
        for i in range(0, 64, 2):
            temp = (self.chromosome_list[index_list.pop(random.randint(0, 63-i))],
                    self.chromosome_list[index_list.pop(random.randint(0, 63-i-1))])
            self.pair_list.append(temp)

    def get_pair_list(self):
        return self.pair_list
