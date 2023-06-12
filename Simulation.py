from Franchise import *

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        location_1 = Franchise("1")
        location_2 = Franchise("2")
        location_3 = Franchise("3")

        location_1.place_order()
        input("Press enter to continue")
        location_2.place_order()
        input("Press enter to continue")
        location_3.place_order()
        input("Press enter to continue")
        location_2.place_order()
        input("Press enter to continue")
        location_3.place_order()
        input("Press enter to continue")
        location_1.place_order()
        input("Press enter to continue")
