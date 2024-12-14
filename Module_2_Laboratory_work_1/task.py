import doctest
class Car:
    def __init__(self, color: str, speed: float):
        """
               Создание и подготовка к работе объекта "Машина"

               :param color: Цвет машины
               :param speed: Скорость движения

               Примеры:
               >>> car = Car("Blue", 120.0)  # инициализация экземпляра класса
               """
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть строкой")
        if not color.strip():
            raise ValueError("Цвет машины не может быть пустым")
        self.color = color

        if not isinstance(speed, (int, float)):
            raise TypeError("Cкорость должна быть числом")
        if speed <= 0:
            raise ValueError("Cкорость должна быть положительным числом")
        self.max_speed = speed
    def is_fast(self) -> bool:
        """
        Проверяет, нарушает ли машина правила (нарушает, если скорость > 150 км/ч)

        :return: True, если машина быстрая, иначе False

        Примеры:
        >>> car = Car("Blue", 180.0)
        >>> car.is_fast()
        True
        >>> car = Car("Green", 120.0)
        >>> car.is_fast()
        False
        """
        return self.max_speed > 150

    def repaint(self, new_color: str) -> None:
        """
        Меняет цвет машины.

        :param new_color: Новый цвет машины

        :raise ValueError: Если цвет пустой или не является строкой

        Примеры:
        >>> car = Car("Red", 200.0)
        >>> car.repaint("Blue")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        if not new_color.strip():
            raise ValueError("Новый цвет не может быть пустым")
        self.color = new_color

class Bus:
    def __init__(self, color: str, seats: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param color: Цвет автобуса
        :param seats: Количество сидений в автобусе (должно быть больше 0)

        Примеры:
        >>> bus = Bus("yellow", 40)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет автобуса должен быть строкой")
        if not color.strip():
            raise ValueError("Цвет автобуса не может быть пустым")
        self.color = color

        if not isinstance(seats, int):
            raise TypeError("Количество сидений должно быть целым числом")
        if seats <= 0:
            raise ValueError("Количество сидений должно быть больше 0")
        self.seats = seats

    def is_full(self, passengers: int) -> bool:
        """
        Проверяет, заполнен ли автобус полностью.

        :param passengers: Количество пассажиров
        :return: True, если пассажиров больше или равно количеству сидений, иначе False

        Примеры:
        >>> bus = Bus("red", 50)
        >>> bus.is_full(50)
        True
        >>> bus.is_full(40)
        False
        """
        if not isinstance(passengers, int):
            raise TypeError("Количество пассажиров должно быть целым числом")
        if passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        return passengers >= self.seats

    def repaint(self, new_color: str) -> None:
        """
        Меняет цвет автобуса.

        :param new_color: Новый цвет автобуса

        :raise ValueError: Если цвет пустой или не является строкой

        Примеры:
        >>> bus = Bus("yellow", 40)
        >>> bus.repaint("green")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        if not new_color.strip():
            raise ValueError("Новый цвет не может быть пустым")
        self.color = new_color

    def available_seats(self, passengers: int) -> int:
        """
        Рассчитывает количество доступных сидений в автобусе.

        :param passengers: Количество пассажиров
        :return: Количество доступных сидений (может быть отрицательным, если пассажиров больше, чем сидений)

        Примеры:
        >>> bus = Bus("blue", 30)
        >>> bus.available_seats(20)
        10
        >>> bus.available_seats(35)
        -5
        """
        if not isinstance(passengers, int):
            raise TypeError("Количество пассажиров должно быть целым числом")
        if passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        return self.seats - passengers

class Truck:
    def __init__(self, color: str, capacity: float):
        """
        Создание и подготовка к работе объекта "Грузовик"

        :param color: Цвет грузовика
        :param capacity: Грузоподъемность грузовика (в тоннах, должна быть больше 0)

        Примеры:
        >>> truck = Truck("blue", 10.5)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет грузовика должен быть строкой")
        if not color.strip():
            raise ValueError("Цвет грузовика не может быть пустым")
        self.color = color

        if not isinstance(capacity, (int, float)):
            raise TypeError("Грузоподъемность должна быть числом")
        if capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом")
        self.capacity = capacity

    def is_overloaded(self, load_weight: float) -> bool:
        """
        Проверяет, перегружен ли грузовик.

        :param load_weight: Вес груза (в тоннах)
        :return: True, если вес груза превышает грузоподъемность, иначе False

        Примеры:
        >>> truck = Truck("red", 8.0)
        >>> truck.is_overloaded(9.0)
        True
        >>> truck.is_overloaded(7.5)
        False
        """
        if not isinstance(load_weight, (int, float)):
            raise TypeError("Вес груза должен быть числом")
        if load_weight < 0:
            raise ValueError("Вес груза не может быть отрицательным")
        return load_weight > self.capacity

    def repaint(self, new_color: str) -> None:
        """
        Меняет цвет грузовика.

        :param new_color: Новый цвет грузовика

        :raise ValueError: Если цвет пустой или не является строкой

        Примеры:
        >>> truck = Truck("blue", 10.0)
        >>> truck.repaint("green")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        if not new_color.strip():
            raise ValueError("Новый цвет не может быть пустым")
        self.color = new_color

    def remaining_capacity(self, load_weight: float) -> float:
        """
        Рассчитывает оставшуюся грузоподъемность грузовика.

        :param load_weight: Вес груза (в тоннах)
        :return: Оставшаяся грузоподъемность (может быть отрицательной, если грузовик перегружен)

        Примеры:
        >>> truck = Truck("yellow", 12.0)
        >>> truck.remaining_capacity(8.0)
        4.0
        >>> truck.remaining_capacity(15.0)
        -3.0
        """
        if not isinstance(load_weight, (int, float)):
            raise TypeError("Вес груза должен быть числом")
        if load_weight < 0:
            raise ValueError("Вес груза не может быть отрицательным")
        return self.capacity - load_weight

if __name__ == "__main__":
    doctest.testmod()
