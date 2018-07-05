class Car:
    '''def __init__(self):
        print("I am fron Zero Peram Cons")'''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I am fron Zero Peram Cons")

    def dataPrint(self):
        print(self.x, ", ", self.y)


#car1 = Car()

car2 = Car(5, 6)
car3 = Car(1, 2)
car4 = Car(3,4)
print("Values from Obj Car2 ", car2.x, car2.y)
print("Values from Obj Car3 ", car3.x, car3.y)
print("Values from Obj Car4 ", car4.x, car4.y)
print(car2.dataPrint())
print(car3.dataPrint())
print(car4.dataPrint())
