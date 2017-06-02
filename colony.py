import time
import random

from ant import Ant


class Colony(object):
    world = object
    list_init_places = [0]  # wich places the ant is goint to start
    list_init_ants = []
    how_many_places_init = 1  # in how many places the ant is going to start
    black_list = []  # list of places to not travel

    def __init__(self, *args, **kwargs):
        if 'world' in kwargs:
            self.world = kwargs['world']

    def init_colony(self, how_many_places_init=1):
        if how_many_places_init > len(self.world.graph):
            print "how_many_places have be less than len of world.graph"
            return False

        self.how_many_places_init = how_many_places_init
        self.list_init_places = random.sample(
            xrange(0, len(self.world.graph) - 1), self.how_many_places_init)

        self.list_init_ants = [Ant(data=(
            place, self.world.graph[place], self.world.pair_points[place]
        )) for place in self.list_init_places]

    def choice_next_place(self, ant):
        # print "ant.value_place(): ", ant.value_place()
        paths = self.world.graph[ant.value_place()]
        # print "paths; ", paths
        path_pos = random.randint(0, len(paths) - 1)
        # print "path_pos: ", path_pos
        return paths[path_pos]

    def nose(self, ant):
        print "places traveled: ", ant.places_traveled
        next_place = self.choice_next_place(ant)
        if not ant.if_was_visited(next_place):
            ant.set_data(data=(
                next_place, self.world.graph[next_place],
                self.world.pair_points[next_place]))
            print "ant next: ", ant.print_ant()
            time.sleep(0.5)
            return ant
        return False

    def forwarding(self):
        for ant in self.list_init_ants:
            # print "places traveled: ", ant.places_traveled
            # next_place = self.choice_next_place(ant)
            # if not ant.if_was_visited(next_place):
            #     ant.set_new_data(data=(
            #         next_place, self.world.graph[next_place],
            #         self.world.pair_points[next_place]))
            # print "ant next: ", ant.print_ant()
            while True:
                print "ant.init_data: ", ant.init_data
                time.sleep(0.5)
                print "new ant in same possssss"
                ant.set_data(data=ant.init_data)
                antt = self.nose(ant)
                while antt:
                    antt = self.nose(ant)
                ant.del_places_traveled()
