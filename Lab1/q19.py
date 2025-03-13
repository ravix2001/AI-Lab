# Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and methods start() and stop(). The Car class should have instances of Engine and Wheel classes as attributes. Implement a method start_car() in the Car class which starts the engine and prints "Car started".

import os 

os.system('cls')

class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} engine started.")

    def stop(self):
        print(f"{self.type} engine stopped.")


class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} wheel started rolling.")

    def stop(self):
        print(f"{self.type} wheel stopped rolling.")


class Car:
    def __init__(self, engine, wheel):
        self.engine = engine  # Instance of Engine class
        self.wheel = wheel    # Instance of Wheel class

    def start_car(self):
        self.engine.start()
        print("Car started.")

    def stop_car(self):
        self.wheel.stop()
        print("Car stopped.")


engine = Engine("V8")
wheel = Wheel("Alloy")

car = Car(engine, wheel)

car.start_car()
car.stop_car()
