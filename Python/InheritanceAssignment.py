
# class vehicle, and attributes of vehicle
class Vehicle:
    make = 'Ford'
    model = 'Raptor'
    generation = 'Gen 3'
    color = 'Black'
    fuel_type = 'Gasoline'

# Car child class of Vehicle with additional attributes
class Car(Vehicle):
    engine_size = 'V-6 '
    num_doors = '2'

# Truck child class of Vehicle with additional attributes
class Truck(Vehicle):
    cab_style = 'Crew Cab'
    bed_length = '5.5 feet'

# instantiate truck type using print method
truck = Truck()
print(truck.make + ' ' + truck.generation + ' ' + truck.model + ' ' + truck.cab_style)

    
