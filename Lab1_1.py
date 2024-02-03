# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    def __init__(self, material: str, size: float):
        self.material = material
        self.size = size

    def change_material(self, new_material: str) -> None:
        ...

    def change_size(self, new_size: float) -> None:
        if not isinstance(new_size, (int, float)):
            raise TypeError("Размер стола должен быть типа int или float")
        if new_size < 0:
            raise ValueError("Размер стола должен быть положительным числом")
        ...

    def clean(self) -> None:
        ...

    """
    Пример:
    >>> table = Table("wood", 240)
    >>> table.change_material("glass")
     """

class Tree:
    def __init__(self, age: int, height: float):
        self.age = age
        self.height = height

    def grow(self) -> None:
        ...

    def shed_leaves(self) -> None:
        ...

    def get_info(self) -> str:
        ...

    """
    Пример:
    >>> tree = Tree(100, 47)
    >>> info = tree.get_info()
     """

class Phone:
    def __init__(self, number: str, model: str,battery_capacity: int):
        self.number = number
        self.model = model
        self.battery_capacity = battery_capacity

    def make_call(self, number: str) -> None:
        """
        Метод для совершения звонка на указанный номер.

        Args:
            number (str): Номер, на который нужно совершить звонок.
        """
        print("Звонок на номер", number, "...")

    def take_photo(self) -> None:
        ...

    def check_battery_status(self, battery_capacity: int) -> int:
        ...

    """
    Пример:
    >>> phone = Phone("843665963","iPhone 14", 2800)
    >>> phone.make_call("843665963")
    """

# TODO работоспособность экземпляров класса проверить с помощью doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
