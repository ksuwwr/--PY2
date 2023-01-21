# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
class House:
    def __int__(self, capacity: int, free_space: int):
        """
        Объект Дом: создание и подготовка к работе
        :param capacity: Вместимость дома
        :param free_space: Свободное место в доме
        """

        if not isinstance(capacity, int):
            raise TypeError("Вместимость должна быть в формате int")
        if capacity < 0:
            raise ValueError("Вместимость не должна быть отрицательной")
        self.capacity = capacity

        if not isinstance(free_space, int):
            raise TypeError("Свободное  место должно быть в формате int")
        if free_space < 0:
            raise ValueError("Свободное место не может быть отрицательным")
        self.free_space = free_space

    def is_room_empty(self) -> bool:
        """
        Проверка, есть ли люди в доме.
        :return: Есть ли люди в доме
        """
    def invite_someone(self, person: float) -> None:
        """
        "Добавление" в дом людей.
        :param person: Пришедшие люди
        :return: ValueError: ошибка, если пришедших людей больше, чем вместимость дома
        """
    def expel_someone(self, person_expelled: float) -> None:
        """
        Удаление из дома людей.
        :param person_expelled: Количество человек, удаленных из дома
        :raise ValueError: ошибка, если пытаются удалить больше людей, чем есть в доме
        :return: Сколько людей удалены
        """


class User(object):
    """
    Объект Пользователь: создание и подготовка к работе
    :param username: имя пользователя, str
    :param age: возраст, int
    :param country: страна, str
    """
    def __init__(self, username: str, age: int, country: str):
        """Валидация артибутов объекта Пользователь"""
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должго содержать только буквы")
        if len(username) < 2:
            raise ValueError("Имя пользователя должно состоять не более чем из 2 букв.")
        self.username = username

        if not isinstance(age, int):
            raise TypeError("Укажите возраст пользователя в формате целого числа")
        if age <= 0:
            raise ValueError("Возраст пользователя не может быть менее года")
        self.age = age

        if not isinstance(country, str):
            raise TypeError("Укажите корректное название страны в формате string.")
        self.country = country

    def create_account(self) -> dict:
        """Создание аккаунта пользователя"""
        pass

    def account_info(self) -> str:
        """Возвращает информацию экземпляра пользователя"""
        return  f"The user is {self.username}, {self.age} y.o., from {self.country}"

    def delete_account(self):
        """Удаление существующего аккаунта"""
        pass

    @staticmethod
    def calculate_age(year: int, month: int, day: int) -> int:
        """
        Рассчет текущего возраста
        :param year: год, int
        :param month: месяц, int
        :param day: день, int
        """
if __name__ == "__main__":
    doctest.testmod()

class City:
    def __init__(self, population, area):
        """
        Объект Город: создание и подготовка к работе
        :param population: население города
        :param area: площадь города (км^2)
        Примеры:
        >>> samara = City(3173000, 542) #PEP8 противоречит, что города пишутся с большой буквы
        """
        if not isinstance(population, int):
            raise TypeError("Population должна быть int")
        if population <= 0:
            raise ValueError("Population должна быть положительным числом")
        if not isinstance(area, (int, float)):
            raise TypeError("Area должна быть float или int!")
        if area <= 0:
            raise ValueError("Area должна быть положительным числом")
        
    def population_census(self):
        """
        Метод проводит перепись населения
        :return: возвращает новое число населения
        Примеры:
        >>> samara = City(3173000, 542)
        >>> samara.population_census()
        """
        ...
    
    def city_expand(self, additional_area):
        """
        Метод увеличивает площадь города на additional_area
        :param additional_area: дополнительная площадь города
        :raise TypeError: вызывает ошибку, если тип additional_area не int и не float
        :return: возвращает новую площадь города
        Примеры:
        >>> samara = City(3173000, 542)
        >>> samara.city_expand(10)
        """
        ...
