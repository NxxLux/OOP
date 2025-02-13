from typing import Any

class Animal:
    """
    Базовый класс для описания животных.
    Содержит общие атрибуты и методы, применимые ко всем животным.
    """

    def __init__(self, name: str, age: int, habitat: str) -> None:
        """
        Инициализирует базовые параметры животного.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param habitat: Среда обитания животного.
        """
        self.name = name
        self.age = age
        self._habitat = habitat  # Непубличный атрибут, чтобы защитить данные о среде обитания.

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного для пользователя.
        """
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.
        """
        return f"Animal(name={self.name}, age={self.age}, habitat={self._habitat})"

    def speak(self) -> str:
        """
        Метод для воспроизведения звука животного.
        """
        return "Some generic animal sound"

    def get_habitat(self) -> str:
        """
        Возвращает информацию о среде обитания.
        """
        return self._habitat


class Dog(Animal):
    """
    Дочерний класс для описания собак.
    Расширяет функционал базового класса Animal.
    """

    def __init__(self, name: str, age: int, breed: str, habitat: str = "Дом") -> None:
        """
        Инициализирует параметры собаки. Расширяет базовый конструктор Animal.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        :param habitat: Среда обитания (по умолчанию "Дом").
        """
        super().__init__(name, age, habitat)
        self.breed = breed

    def __str__(self) -> str:
        """
        Переопределяет метод __str__ для более специфичного представления собаки.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def speak(self) -> str:
        """
        Переопределяет метод speak для отображения звуков, характерных для собаки.

        Причина: Собака издаёт конкретный звук, который отличается от других животных.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод, который добавляет уникальную функциональность для собаки.

        :param item: Предмет, который собака приносит.
        :return: Строка с описанием действия.
        """
        return f"{self.name} принёс(ла) {item}!"
