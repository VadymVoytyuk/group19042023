from abc import ABC, abstractmethod

import constants


class Vehicle(ABC):
    def __init__(self, model: str, tank_volume: int, remain_fuel: int, speed: float, mileage: int, ):
        self.model = model
        self.tank_volume = tank_volume
        self.remain_fuel = remain_fuel
        self.speed = speed
        self.mileage = mileage

    def refuel_from_vehicle(self, other, wanted_value):
        if other.remain_fuel:
            possible_other_value = wanted_value if other.remain_fuel >= wanted_value else other.remain_fuel
            possible_self_value = self.tank_volume - self.remain_fuel
            final_value = min([possible_self_value, possible_other_value])
            self.remain_fuel += final_value
            other.remain_fuel -= final_value

    def refuel_from_station(self):
        self.remain_fuel = self.tank_volume

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, other):
        return self.tank_volume == other.tank_volume

    def __gt__(self, other):
        return self.tank_volume > other.tank_volume

    def __ge__(self, other):
        return self.tank_volume >= other.tank_volume

    def __lt__(self, other):
        return self.tank_volume < other.tank_volume


class Car(Vehicle):

    def __init__(self, model: str, passengers: int, airbag: True or False):
        super().__init__(model=model, tank_volume=constants.CarSettings.TANK_VOLUME.value,
                         remain_fuel=constants.CarSettings.REMAIN_FUEL.value, speed=constants.CarSettings.SPEED.value,
                         mileage=constants.CarSettings.MILEAGE.value)
        self.passengers = passengers
        self.airbag = airbag

    def __str__(self):
        return f'I am a car, my sit number is {self.passengers}'


class Motorcycle(Vehicle):

    def __init__(self, model: str, sidecar=True or False):
        super().__init__(model=model, tank_volume=constants.MotorcycleSettings.TANK_VOLUME.value,
                         remain_fuel=constants.MotorcycleSettings.REMAIN_FUEL.value,
                         speed=constants.MotorcycleSettings.SPEED.value,
                         mileage=constants.MotorcycleSettings.MILEAGE.value)
        self.sidecar = sidecar

    def __str__(self):
        return f'I am a moto, my sidecar is {self.sidecar}'


car1 = Car(model='Hyundai', passengers=5, airbag=True)
motorcycle1 = Motorcycle(model='Honda', sidecar=False)

print(car1.__dict__)
car1.refuel_from_vehicle(motorcycle1, 5)
print(car1.__dict__)
print(motorcycle1.__dict__)
motorcycle1.refuel_from_vehicle(car1, 5)
print(motorcycle1.__dict__)
car1.refuel_from_station()
print(car1.__dict__)
motorcycle1.refuel_from_station()
print(motorcycle1.__dict__)