from abc import ABC
class Vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def breaks():
        print('stop it')
class Fortuner(Vehicle):
    def speed():
        print('full speed')
    def milage():
        print('340/kph')
fobj=Fortuner
fobj.speed()
fobj.milage()
fobj.breaks()