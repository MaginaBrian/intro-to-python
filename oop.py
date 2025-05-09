class Vehicle:
    count = 0
    vehicle_list = []
    
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.vehicle_count()
        self.vehicle_collection(self)

    def start(self):
        print(f'{self.brand} is starting.............vooooooooo')

    @classmethod
    def vehicle_count(cls):
        cls.count +=1

    @classmethod
    def vehicle_collection(cls, new_vehicle):
        cls.vehicle_list.append(new_vehicle)




car1 = Vehicle("bmw", "M5", "2015")
car2 = Vehicle("Mazda", "CX9", "2015")
car3 = Vehicle("Audi", "r5", "2015")

print(car1.start())
print(car2.start())
print(car3.start())

print(Vehicle.count)
print(Vehicle.vehicle_list)