
class Ant(object):
    """
    init --> (key of place, value of place so places that are connect to this
    place, (x, y))
    """
    phero_weight = 0.1
    data = tuple()
    init_data = tuple()
    places_traveled = []  # (pos, phero_weight)

    def __init__(self, *args, **kwargs):
        self.places_traveled = []
        if 'data' in kwargs:
            self.data = kwargs['data']
            self.init_data = kwargs['data']
            self.places_traveled.append((self.data[0], self.phero_weight))

    def localized(self):
        return self.data[2]

    def value_place(self):
        return self.data[0]

    def print_ant(self):
        print "%s: %s, (%s, %s)" % (
            str(self.data[0]), str(self.data[1]),
            str(self.data[2][0]), str(self.data[2][1]))

    def if_was_visited(self, place):
        just_places_traveled = [i[0] for i in self.places_traveled]
        return True if place in just_places_traveled else False

    def set_data(self, data):
        self.data = data
        if not self.if_was_visited(data[0]):
            self.places_traveled.append((self.data[0], self.phero_weight))

    def del_places_traveled(self):
        self.places_traveled = []
