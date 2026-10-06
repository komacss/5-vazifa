from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __new__(cls, *args, **kwargs):
        if cls is Vehicle:
            raise TypeError("Vehicle obyektini to'g'ridan-to'g'ri yaratib bo'lmaydi")
        return super().__new__(cls)

    def __init__(self, marka, model, yil, tezlik=0):
        self._marka = marka
        self._model = model
        self._yil = yil
        self._tezlik = max(tezlik, 0)

    @property
    def speed(self):
        return self._tezlik

    @speed.setter
    def speed(self, qiymat):
        self._tezlik = max(qiymat, 0)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"{self._marka} {self._model} | {self._yil} | Tezlik: {self._tezlik} km/soat"

    def __repr__(self):
        return f"{type(self).__name__}({self._marka!r}, {self._model!r}, {self._yil!r}, {self._tezlik!r})"

    def __bool__(self):
        return self._tezlik > 0

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return (self._marka, self._model, self._yil) == (other._marka, other._model, other._yil)

    def __ne__(self, other):
        natija = self.__eq__(other)
        return natija if natija is NotImplemented else not natija

    def __hash__(self):
        return hash((self._marka, self._model, self._yil))

    def __gt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self._tezlik > other._tezlik

    def __ge__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self._tezlik >= other._tezlik

    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self._tezlik < other._tezlik

    def __le__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self._tezlik <= other._tezlik


class Car(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} avtomobili kalit bilan yurgizildi")

    def move(self):
        self.speed = 90
        print(f"Avtomobil {self.speed} km/soat tezlikda ketmoqda")


class Motorcycle(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} mototsikli startyor bilan yurgizildi")

    def move(self):
        self.speed = 140
        print(f"Mototsikl {self.speed} km/soat tezlikda ketmoqda")


class Truck(Vehicle):
    def start(self):
        print(f"{self._marka} {self._model} yuk mashinasi dizel dvigatelini yurgizdi")

    def move(self):
        self.speed = 60
        print(f"Yuk mashinasi {self.speed} km/soat tezlikda yuk tashimoqda")


car = Car("Toyota", "Camry", 2022)
motorcycle = Motorcycle("Kawasaki", "Ninja", 2021)
truck = Truck("Volvo", "FH", 2019)

vehicles = [car, motorcycle, truck]

for vehicle in vehicles:
    print(vehicle)
    vehicle.start()
    vehicle.move()
    print()

print(bool(car))

print(car == motorcycle)
print(car != truck)
print(car > motorcycle)
print(truck <= car)

print(repr(car))

try:
    Vehicle("Test", "X", 2000)
except TypeError as xato:
    print(xato)