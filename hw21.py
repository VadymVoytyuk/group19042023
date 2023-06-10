
import datetime


class Car:
    def __init__(self, maker: str, series: str, fuel_consumption: float, color: str, year: int = 2020) -> None:
        self.__year = year
        self._maker = maker
        self._series = series
        self.km_run = 0
        self.fuel_consumption = fuel_consumption
        self.color = color

    def __str__(self):
        return f'CAR DETAILS:Year of release : {self.__year} , Maker: {self._maker}, Type: {self._series}, Mileage: {self.km_run}, Consumption: {self.fuel_consumption} ltrs , Age: {self.age_of_car} years'

    @property
    def age_of_car(self):
        return datetime.datetime.today().year - self.__year


car1 = Car(maker='Hyundai', series='Accent', fuel_consumption=4.5, color='White')
car2 = Car(maker='Toyota', series='Land Cruiser 150', fuel_consumption= 8.3, color='Black')

print(car1)
print(car2)
