from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine is starting in car")

    def stop_engine(self):
        print("Engine is stopped here in car class")

car=Car()
car.start_engine()
car.stop_engine()