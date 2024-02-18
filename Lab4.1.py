class Car:
    def __init__(self, brand: str, year: int, color: str):
        """
        Конструктор базового класса "Автомобили".

        Args:
            brand (str): Марка автомобиля.
            year (int): Год выпуска автомобиля.
            color (str): Цвет автомобиля.
        """
        self.brand = brand
        self.year = year
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.brand} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта, используемое для его воссоздания.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Car(brand={self.brand}, year={self.year}, color={self.color})"


class PassengerCar(Car):
    def __init__(self, brand: str, year: int, color: str, seats: int):
        """
        Конструктор дочернего класса "Легковой автомобиль".

        Args:
            brand (str): Марка автомобиля.
            year (int): Год выпуска автомобиля.
            color (str): Цвет автомобиля.
            seats (int): Количество сидений в автомобиле.
        """
        super().__init__(brand, year, color)
        self.seats = seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.brand} ({self.year}), {self.seats} seats"


class Truck(Car):
    def __init__(self, brand: str, year: int, color: str, capacity: float):
        """
        Конструктор дочернего класса "Грузовой автомобиль".

        Args:
            brand (str): Марка автомобиля.
            year (int): Год выпуска автомобиля.
            color (str): Цвет автомобиля.
            capacity (float): Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(brand, year, color)
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.brand} ({self.year}), {self.capacity} tons"
class Fruit:
    def __init__(self, name: str, color: str):
        """
        Конструктор базового класса "Фрукты".

        Args:
            name (str): Название фрукта.
            color (str): Цвет фрукта.
        """
        self.name = name
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта, используемое для его воссоздания.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Fruit(name={self.name}, color={self.color})"


class Apple(Fruit):
    def __init__(self, name: str, color: str, variety: str):
        """
        Конструктор дочернего класса "Яблоко".

        Args:
            name (str): Название фрукта.
            color (str): Цвет фрукта.
            variety (str): Сорт яблока.
        """
        super().__init__(name, color)
        self.variety = variety

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.variety} {self.name}"


class Banana(Fruit):
    def __init__(self, name: str, color: str, length: float):
        """
        Конструктор дочернего класса "Банан".

        Args:
            name (str): Название фрукта.
            color (str): Цвет фрукта.
            length (float): Длина банана в сантиметрах.
        """
        super().__init__(name, color)
        self.length = length

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.color} {self.name}, length: {self.length} cm"
class VideoHosting:
    def __init__(self, name: str, platform: str):
        """
        Конструктор базового класса "Видеохостинги".

        Args:
            name (str): Название видеохостинга.
            platform (str): Платформа видеохостинга.
        """
        self.name = name
        self.platform = platform

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.name} ({self.platform})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта, используемое для его воссоздания.

        Returns:
            str: Строковое представление объекта.
        """
        return f"VideoHosting(name={self.name}, platform={self.platform})"


class YouTube(VideoHosting):
    def __init__(self, name: str, platform: str, subscribers: int):
        """
        Конструктор дочернего класса "YouTube".

        Args:
            name (str): Название видеохостинга.
            platform (str): Платформа видеохостинга.
            subscribers (int): Количество подписчиков на канале.
        """
        super().__init__(name, platform)
        self.subscribers = subscribers

    def get_subscribers_count(self) -> int:
        """
        Возвращает количество подписчиков на канале.

        Returns:
            int: Количество подписчиков.
        """
        return self.subscribers

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{super().__str__()}, Subscribers: {self.subscribers}"


class Twitch(VideoHosting):
    def __init__(self, name: str, platform: str, followers: int):
        """
        Конструктор дочернего класса "Twitch".

        Args:
            name (str): Название видеохостинга.
            platform (str): Платформа видеохостинга.
            followers (int): Количество подписчиков на канале.
        """
        super().__init__(name, platform)
        self.followers = followers

    def get_followers_count(self) -> int:
        """
        Возвращает количество подписчиков на канале.

        Returns:
            int: Количество подписчиков.
        """
        return self.followers

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{super().__str__()}, Followers: {self.followers}"