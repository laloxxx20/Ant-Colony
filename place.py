
class Place(object):
    value = 0
    position = (0, 0)
    neighbors = []
    value_pheromone = 0
    prev_neighbor = None  # Place object
    value_to_up_phero = 0.1

    def __init__(self, pos, value, neighbors):
        self.position = pos
        self.value = value
        self.neighbors = neighbors

    def set_position(self, x, y):
        self.position = (x, y)

    def set_value(self, value):
        self.value = value

    def add_neighbor(self, value):
        self.neighbors.append(value)

    def set_value_pheromone(self, value, prev_neighbor):
        self.value_pheromone += value
        if self.prev_neighbor:
            self.prev_neighbor = prev_neighbor
            self.prev_neighbor.value_pheromone += value

    def evaporate(self):
        self.value_pheromone -= self.value_to_up_phero
        if self.prev_neighbor:
            self.prev_neighbor.value_pheromone -= self.value_to_up_phero

    def print_place(self):
        print "%s: [%s] -- %s. PHE: %s" % (
            self.value,
            ', '.join(str(n) for n in self.neighbors),
            str(self.position),
            str(self.value_pheromone),
        )
