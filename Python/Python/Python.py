class Car():
    pass

class Yugo:
    pass

class Car():
    def excalaim(self):
        print("I'm a car")

class Yugo(Car):
    def excalaim(self):
        print("I'm not a car")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.excalaim()

give_me_a_yugo.excalaim()
