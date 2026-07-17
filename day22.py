class Vehicle:

    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):

    def drive(self):
        print("Car is driving on the road")

class Boat(Vehicle):
    
    def drive(self):
        print("Boat is sailing on the water")

vehicles = [Car(), Boat()]
for vehicle in vehicles:
    vehicle.drive()

