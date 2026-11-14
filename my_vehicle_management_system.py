class vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting")

    def show_brand(self):
        print("Brand:", self.brand)


class car(vehicle):
    def drive(self):
        print("Car is driving")

class bike(vehicle):
    def ride(self):
        print("Bike is riding")


car = car("Toyota")
bike = bike("Yamaha")


print("Car information")
car.show_brand()
car.start()
car.drive()

print("\nBike Information")
bike.show_brand()
bike.start()
bike.ride()
