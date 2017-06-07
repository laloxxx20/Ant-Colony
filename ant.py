
class Ant(object):
    """
    init --> (key of place, value of place so places that are connect to this
    place, (x, y))
    """
    phero_weight = 0.1
    # data = tuple()
    data = object  # Place()
    # init_data = tuple()
    init_data = object
    places_traveled = []  # (pos, phero_weight)

    def __init__(self, *args, **kwargs):
        self.places_traveled = []
        if 'data' in kwargs:
            self.data = kwargs['data']
            self.init_data = kwargs['data']
            self.places_traveled.append((self.data.value, self.phero_weight))

    def localized(self):
        # return self.data[2]
        return self.data.position

    def value_place(self):
        # return self.data[0]
        return self.data.value

    def print_ant(self):
        # print "%s: %s, (%s, %s)" % (
        #     str(self.data[0]), str(self.data[1]),
        #     str(self.data[2].position[0]), str(self.data[2].position[1]))
        print "%s: %s, (%s, %s)" % (
            str(self.data.value), str(self.data.neighbors),
            str(self.data.position[0]), str(self.data.position[1]))

    def if_was_visited(self, place):
        if place == self.data.value:
            return False
        just_places_traveled = [i[0] for i in self.places_traveled]
        return True if place in just_places_traveled else False

    def set_data(self, data):
        self.data = data
        if not self.if_was_visited(data.value):
            self.places_traveled.append((self.data.value, self.phero_weight))

    def del_places_traveled(self):
        self.places_traveled = []
