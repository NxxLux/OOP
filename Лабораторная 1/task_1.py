from abc import ABC, abstractmethod


class AbstractTree(ABC):
    """
    Абстрактный класс, описывающий дерево.
    Характеристики:
    - height: float - высота дерева в метрах.
    - age: int - возраст дерева в годах.
    - type_of_tree: str - тип дерева (например, хвойное, лиственное).
    """

    def __init__(self, height: float, age: int, type_of_tree: str):
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not type_of_tree:
            raise ValueError("Type of tree cannot be empty.")

        self.height = height
        self.age = age
        self.type_of_tree = type_of_tree

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Процесс фотосинтеза дерева.
        """
        ...

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на заданное количество лет и, возможно, высоту.

        Args:
            years (int): Количество лет, на которое дерево должно вырасти.

        Raises:
            ValueError: Если передано отрицательное значение.

        >>> tree.grow(5)
        """
        ...

    @abstractmethod
    def produce_oxygen(self) -> float:
        """
        Вычисляет количество произведенного кислорода в кг за сутки.

        Returns:
            float: Количество произведенного кислорода.

        >>> tree.produce_oxygen()
        10.5
        """
        ...


class AbstractTable(ABC):
    """
    Абстрактный класс, описывающий стол.
    Характеристики:
    - material: str - материал стола (дерево, металл и т.д.).
    - length: float - длина стола в метрах.
    - width: float - ширина стола в метрах.
    """

    def __init__(self, material: str, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        if not material:
            raise ValueError("Material cannot be empty.")

        self.material = material
        self.length = length
        self.width = width

    @abstractmethod
    def support_weight(self, weight: float) -> bool:
        """
        Проверяет, может ли стол выдержать заданный вес.

        Args:
            weight (float): Вес в килограммах.

        Returns:
            bool: True, если стол выдержит, иначе False.

        >>> table.support_weight(100)
        True
        """
        ...

    @abstractmethod
    def resize(self, new_length: float, new_width: float) -> None:
        """
        Изменяет размеры стола.

        Args:
            new_length (float): Новая длина.
            new_width (float): Новая ширина.

        Raises:
            ValueError: Если переданы недопустимые размеры.

        >>> table.resize(2.0, 1.5)
        """
        ...

    @abstractmethod
    def get_area(self) -> float:
        """
        Возвращает площадь поверхности стола.

        Returns:
            float: Площадь в квадратных метрах.

        >>> table.get_area()
        3.0
        """
        ...


class AbstractSocialNetwork(ABC):
    """
    Абстрактный класс, описывающий социальную сеть.
    Характеристики:
    - name: str - название социальной сети.
    - user_count: int - количество пользователей.
    - is_active: bool - статус активности.
    """

    def __init__(self, name: str, user_count: int, is_active: bool):
        if not name:
            raise ValueError("Name cannot be empty.")
        if user_count < 0:
            raise ValueError("User count cannot be negative.")

        self.name = name
        self.user_count = user_count
        self.is_active = is_active

    @abstractmethod
    def register_user(self, username: str) -> bool:
        """
        Регистрирует нового пользователя в социальной сети.

        Args:
            username (str): Имя пользователя.

        Returns:
            bool: True, если регистрация успешна, иначе False.

        >>> network.register_user("new_user")
        True
        """
        ...

    @abstractmethod
    def post_content(self, content: str) -> None:
        """
        Публикует новый контент.

        Args:
            content (str): Содержимое поста.

        Raises:
            ValueError: Если содержимое пустое.

        >>> network.post_content("Hello, world!")
        """
        ...

    @abstractmethod
    def deactivate(self) -> None:
        """
        Деактивирует социальную сеть.

        >>> network.deactivate()
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
