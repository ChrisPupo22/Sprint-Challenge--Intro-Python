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

#Are we saying that Flight Vehicle and Starships are subclasses of Vehicle????? Very unclear...

#Base class of Car and Motorcycle
class Vehicle: 
    def __init__(self):
        pass

class Car(Vehicle):
    def __init__(self):
                    pass

class Motorcycle(Vehicle):
    def __init__(self):
                    pass

#Base class of Airplane
class FlightVehicle:
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass

#This is a Base class as well
class Starship: 
    def __init__(self):
        pass

