class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def __str__(self):
        return f"Registration Number: {self.registration_number}, 
                 Make: {self.make}, 
                 Model: {self.model}"
class Car(Vehicle):
    def __init__(self, registration_number, make, model, seats):
        super().__init__(registration_number, make, model)
        self.seats = seats

    def __str__(self):
        return super().__str__() + f", Seats: {self.seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return super().__str__() + f", Cargo Capacity: {self.cargo_capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return super().__str__() + f", Engine Capacity: {self.engine_capacity} cc"
    
class Fleet:
    def __init__(self):
        self.vehicles = []

    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def displayVehicles(self):
        print("\nList of Vehicles in Fleet:")
        for vehicle in self.vehicles:
            print(vehicle)

    def searchVehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None
    
def main():
    fleet = Fleet()
    
    car1 = Car("KBN 001H", "Toyota", "Probox", 5)
    fleet.addVehicle(car1)
    
    truck1 = Truck("KCJ 897U", "Isuzu", "FH", 4)
    fleet.addVehicle(truck1)
    
    motorcycle1 = Motorcycle("KDNH 789", "Kawasaki", "CHRR", 600)
    fleet.addVehicle(motorcycle1)
    
    
    fleet.displayVehicles()
    
    
    regNo = "KCJ 897U"
    foundVehicle = fleet.searchVehicle(regNo)
    if foundVehicle:
        print(f"\nVehicle found - {foundVehicle}")
    else:
        print(f"\nVehicle RegNo. '{regNo}' not found.")
    
if __name__ == "__main__":
    main()