class Vehicle:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_difference):
        self.speed += abs(speed_difference)
        self.speed = min(self.speed, self.max_speed)

    def slow_down(self, speed_difference):
        self.speed -= abs(speed_difference)
        self.speed = max(self.speed, -5)


class Bus(Vehicle):
    def slow_down(self, speed_difference):
        super().slow_down(speed_difference)
        self.speed = max(self.speed, 0)


class Car(Vehicle):
    pass


car = Car("Alto", 4)
car.accelerate(4)
print("Max Speed Car ", car.max_speed)
print("Max Speed Model ", car.model)
print("Max Speed Speed ", car.speed)
bus = Bus("TATA", 3)
bus.accelerate(3)
print("Max Speed Bus ", bus.max_speed)
print("Max Speed Model ", bus.model)
print("Max Speed Speed ", bus.speed)
