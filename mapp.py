import random
from place import Place


class Map:
    graph = dict()
    # pair_points = []
    places = []  # list of Places()
    max_of_distance = 30  # always major than len(graph)

    def __init__(self, *args, **kwargs):
        if kwargs['max_of_distance']:
            self.max_of_distance = kwargs['max_of_distance']

        # self.graph = {
        #     0: [1, 4, 5],
        #     1: [0, 7, 3],
        #     2: [1, 9, 3],
        #     3: [2, 11, 4],
        #     4: [3, 13, 0],
        #     5: [0, 14, 6],
        #     6: [5, 16, 7],
        #     7: [6, 8, 1],
        #     8: [7, 17, 9],
        #     9: [8, 10, 2],
        #     10: [9, 18, 11],
        #     11: [10, 3, 12],
        #     12: [11, 19, 13],
        #     13: [12, 14, 4],
        #     14: [13, 15, 5],
        #     15: [14, 16, 19],
        #     16: [6, 17, 15],
        #     17: [16, 8, 18],
        #     18: [10, 19, 17],
        #     19: [18, 12, 15]
        # }

        self.graph = {
            0: [1, 2, 3, 4],
            1: [0, 2],
            2: [0, 1, 3],
            3: [0, 2, 4],
            4: [0, 3],
        }

        len_graph = len(self.graph)
        pair_points_x = random.sample(
            xrange(0, self.max_of_distance), len_graph)
        pair_points_y = random.sample(
            xrange(0, self.max_of_distance), len_graph)

        # for i in xrange(len_graph):
        #     self.pair_points.append(
        #         (pair_points_x[i], pair_points_y[i]))

        for i in xrange(len_graph):
            self.places.append(Place(
                (pair_points_x[i], pair_points_y[i]),
                i, self.graph[i],
            ))

        # for p in self.places:
        #     p.print_place()
