from abc import ABC, abstractmethod
class Car(ABC):
    """
    Базовый класс автомобиля.

    Атрибуты:
        _brand (str): Марка автомобиля (скрыта для защиты от случайного изменения).
        _model (str): Модель автомобиля (скрыта для защиты от случайного изменения).
        year (int): Год выпуска автомобиля.
        fuel_consumption (float): Расход топлива (л/100 км).
    """

    def __init__(self, brand: str, model: str, year: int, fuel_consumption: float):
        """
        Конструктор базового класса.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param fuel_consumption: Расход топлива (л/100 км).
        """
        self._brand = brand  # Защищенный атрибут, так как марка не должна изменяться после создания
        self._model = model  # Защищенный атрибут, так как модель не должна изменяться после создания
        self.year = year
        self.fuel_consumption = fuel_consumption  # В литрах на 100 км

    @property
    def brand(self) -> str:
        """Геттер для марки автомобиля."""
        return self._brand

    @property
    def model(self) -> str:
        """Геттер для модели автомобиля."""
        return self._model

    @abstractmethod
    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Абстрактный метод для расчета стоимости топлива.

        :param distance: Дистанция в км.
        :param fuel_price: Цена топлива за литр.
        :return: Общая стоимость топлива.
        """
        pass

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year}, fuel_consumption={self.fuel_consumption})")


class PassengerCar(Car):
    """
    Класс для легковых автомобилей.

    Атрибуты:
        seats (int): Количество пассажирских мест.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_consumption: float, seats: int):
        """
        Конструктор легкового автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param fuel_consumption: Расход топлива (л/100 км).
        :param seats: Количество пассажирских мест.
        """
        super().__init__(brand, model, year, fuel_consumption)
        self.seats = seats  # Количество мест в салоне

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Расчет стоимости топлива для поездки.

        Формула: (расход * расстояние / 100) * цена топлива

        :param distance: Дистанция в км.
        :param fuel_price: Цена топлива за литр.
        :return: Общая стоимость топлива.
        """
        return (self.fuel_consumption * distance / 100) * fuel_price

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year}, fuel_consumption={self.fuel_consumption}, seats={self.seats})")
class Truck(Car):
    """
    Класс для грузовиков.

    Атрибуты:
        max_load (float): Максимальная грузоподъемность (тонны).
    """

    def __init__(self, brand: str, model: str, year: int, fuel_consumption: float, max_load: float):
        """
        Конструктор грузового автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param fuel_consumption: Расход топлива (л/100 км).
        :param max_load: Максимальная грузоподъемность (тонны).
        """
        super().__init__(brand, model, year, fuel_consumption)
        self.max_load = max_load  # В тоннах

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Расчет стоимости топлива с учетом загрузки.

        Причина перегрузки метода:
        - Грузовики потребляют больше топлива, если загружены.
        - При полной загрузке расход увеличивается на 30%.

        Формула: (расход * расстояние / 100) * цена топлива * (1 + 0.3)

        :param distance: Дистанция в км.
        :param fuel_price: Цена топлива за литр.
        :return: Общая стоимость топлива.
        """
        return (self.fuel_consumption * distance / 100) * fuel_price * 1.3

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year}, fuel_consumption={self.fuel_consumption}, max_load={self.max_load})")


if __name__ == "__main__":
    # Создаем объекты автомобилей
    passenger_car = PassengerCar(brand="Toyota", model="Camry", year=2022, fuel_consumption=8, seats=5)
    truck = Truck(brand="Volvo", model="FH16", year=2021, fuel_consumption=25, max_load=20)

    # Вывод информации о машинах
    print(passenger_car)  # Toyota Camry (2022)
    print(truck)          # Volvo FH16 (2021)

    # Расчет стоимости топлива на 100 км при цене 55 руб/л
    print(f"Легковая машина: {passenger_car.calculate_fuel_cost(100, 55)} руб")
    print(f"Грузовик: {truck.calculate_fuel_cost(100, 55)} руб")
