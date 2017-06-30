import time
import random

from ant import Ant


class Colony(object):
    world = object
    list_init_places = [0]  # wich places the ant is goint to start
    list_init_ants = []
    how_many_places_init = 1  # in how many places the ant is going to start
    black_list = [[]]  # list of places to not travel
    how_many_places = 1

    def __init__(self, *args, **kwargs):
        if 'world' in kwargs:
            self.world = kwargs['world']
            self.how_many_places = len(self.world.graph) 

    def init_colony(self, how_many_places_init=1):
        if how_many_places_init > len(self.world.graph):
            print "how_many_places have be less than len of world.graph"
            return False

        self.how_many_places_init = how_many_places_init
        self.list_init_places = random.sample(
            xrange(0, len(self.world.places) - 1), self.how_many_places_init)

        # self.list_init_ants = [Ant(data=(
        #     place,
        #     self.world.places[place].neighbors,
        #     self.world.places[place].position
        # )) for place in self.list_init_places]

        self.list_init_ants = [Ant(
            data=self.world.places[place]
        ) for place in self.list_init_places]

    def choice_next_place(self, ant):
        paths = self.world.graph[ant.value_place()]
        print "paths; ", paths
        major = 0
        path_pos = None
        for i, place in enumerate(paths):
            buff = self.world.places[place].value_pheromone
            if buff > major:
                major = buff
                path_pos = i
        print "major; ", major
        if not path_pos:
            path_pos = random.randint(0, len(paths) - 1)

        print "path_pos: ", path_pos
        return paths[path_pos]

    def each_ant(self, ant):
        print "places traveled: ", ant.places_traveled
        next_place = self.choice_next_place(ant)
        if not ant.if_was_visited(next_place):
            # ant.set_data(data=(
            #     next_place,
            #     self.world.graph[next_place],
            #     self.world.places[next_place]
            # ))
            ant.set_data(data=self.world.places[next_place])
            # new place visited and puttin phero in that place
            self.world.places[next_place].set_value_pheromone(0.1, ant.data)
            print "ant next: ", ant.print_ant()
            time.sleep(0.7)
            print "ant.data.value: ", ant.data.value
            print "ant.init_data.value: ", ant.init_data.value
            if ant.data.value == ant.init_data.value:
                    print "endedddddddddddddddddddddddddddddddddddddddd"
                    raise "asdasds"
            return ant
        else:
            self.world.places[next_place].evaporate()
        return False

    def forwarding(self):
        for ant in self.list_init_ants:

            while len(ant.places_traveled) != self.how_many_places - 1:
                time.sleep(0.5)
                print "new ant in same position"
                ant.set_data(data=ant.init_data)
                antt = self.each_ant(ant)
                while antt:
                    antt = self.each_ant(ant)
                ant.del_places_traveled()

                for place in self.world.places:
                    place.print_place()
