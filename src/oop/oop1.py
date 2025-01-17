# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    # Base class
    pass

class FlightVehicle(Vehicle):
    # Child
    pass

class Starship(FlightVehicle):
    #GrandChild
    pass

class Airplane(FlightVehicle):
    #grand child
    pass

class GroundVehicle(Vehicle):
    #child
    pass

class Car(GroundVehicle):
    #grandchild
    pass

class Motorcycle(GroundVehicle):
    #grand child
    pass