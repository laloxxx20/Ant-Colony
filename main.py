from draw import Draw
from mapp import Map
from colony import Colony


window = Draw(title="Ants Colony")

world = Map(max_of_distance=600)
for point in world.pair_points:
    window.draw_point(point[0], point[1])

for i, node in world.graph.iteritems():
    for j in node:
        window.draw_line(
            world.pair_points[i][0],
            world.pair_points[i][1],
            world.pair_points[j][0],
            world.pair_points[j][1],
        )

a = Colony(world=world)
# a.init_colony(how_many_places_init=len(world.graph) - 5)
a.init_colony(1)
window.changecolor_point("green")
window.changecolor_radio(5)
for ant in a.list_init_ants:
    point = window.draw_point(ant.localized()[0], ant.localized()[1])
a.forwarding()
