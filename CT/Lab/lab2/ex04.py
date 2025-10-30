class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed           
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passengers):
        super().__init__(max_speed, mileage)
        self.passengers = passengers
    def get_info(self):
        return f"Bus - Max speed: {self.max_speed}, Mileage: {self.mileage}, Passengers: {self.passengers}"

bus1 = Bus(120, 15000, 45)
bus2 = Bus(200, 12000, 60)
print(bus1.get_info())
print(bus2.get_info())