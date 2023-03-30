
# Parent class vehicle
class Vehicle:
    make = 'Dodge'
    model = 'Ram 2500'
    generation = 'Gen 3'
    color = 'Black'
    fuel_type = 'Diesel'

# instantiate print method for transportation
transportation = Vehicle()
print(transportation.make + ' ' + transportation.model + ' ' + transportation.color + ' ' + transportation.fuel_type)

# Child class car
class Car(Vehicle):
    make = 'Toyota'
    model = 'Camery'
    engine_size = 'V-6 '
    num_doors = '4 door'


# instantiate print method for car type
car = Car()
print(car.make + ' ' + car.model + ' ' + car.color + ' ' + car.engine_size + ' ' + car.num_doors)

# Child class truck
class Truck(Vehicle):
    make = 'Ford'
    model = 'Raptor'
    cab_style = 'Crew Cab'
    bed_length = '5.5 feet'




# instantiate truck type using print method
truck = Truck()
print(truck.make + ' ' + truck.generation + ' ' + truck.model + ' ' + truck.color + ' ' + truck.cab_style)

    
