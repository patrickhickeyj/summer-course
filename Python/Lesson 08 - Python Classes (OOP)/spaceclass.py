import math

class Spacecraft():
    def __init__(self, name: str, fuel_level : float = 10 , fuel_efficiency: float = 1 ):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, newfuel):
        self.fuel_level += newfuel

    def calc_fuel_required(self, distance):
        result = distance / self.fuel_efficiency
        return result

    def fuel_available(self, distance):
        result = self.calc_fuel_required(distance)
        return result <= self.fuel_level
        # if result <= self.fuel_level:
        #     # print("Launch successful!")
        #     # self.fuel_level -= result
        # else:
        #     print("Launch failed! You're stranded")

    def launch(self, distance):
        if self.fuel_available(distance):
            self.fuel_level -= self.calc_fuel_required(distance)
            print(f'Launched {self.name} {distance} kilometers.')
        else:
            print(f'Not enough fuel, needs {self.calc_fuel_required(distance) - self.fuel_level} liters')



# voyage = Spacecraft('Voyager', 100, 10)
# print(voyage.fuel_level)
# print(voyage.fuel_efficiency)
# voyage.launch_attempt(999)
# print(voyage.fuel_level)
sp1 = Spacecraft("Vostok 1", 250, 1.5)
sp2 = Spacecraft("Voyager 1", 400, 2.0)
sp3 = Spacecraft("Apollo 11", 600, 2.5)

sp1.launch(400)
sp2.launch(200)

class Planet():
    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self):
        return f'The planet is name {self.name} and has a danger of {self.danger}'

    def __sub__(self, secondplanet):
        print(type(secondplanet))
        if not isinstance(secondplanet, Planet):
            raise TypeError("Must only subtract planets")
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = secondplanet.coordinates
        distance  = math.sqrt(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
        return distance

# Planets:
earth = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
mars = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")
jupiter = Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant")
saturn = Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant")
uranus = Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy")
neptune = Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy")
pluto = Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen")
eris = Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen")
kepler = Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like")
proxima = Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")

print(earth)
print(pluto)
print(pluto - earth)
