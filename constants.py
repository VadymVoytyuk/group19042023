from enum import Enum


class CarSettings(Enum):
    TANK_VOLUME: int = 18
    REMAIN_FUEL: float = 10.0
    SPEED: float = 100.0
    MILEAGE: int = 35000


class MotorcycleSettings(Enum):
    TANK_VOLUME: int = 10
    REMAIN_FUEL: float = 7.0
    SPEED: float = 150.0
    MILEAGE: int = 15000
