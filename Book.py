class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = name

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть типа str")
        self._author = author

    # так как атрибуты name и author не могут изменять пишем для них только свойства getter
    @property
    def name(self) -> str:
         return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    # так как атрибут pages изменяем, то пишем свойства getter и setter, и в setter производим все необходимы проверки
    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    #перегрузим методы str и repr, чтобы выводилось также кол-во страниц
    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Кол-во страниц: {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    # так как атрибут duration изменяем, то пишем свойства getter и setter, и в setter производим все необходимы проверки
    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудио книги должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")
        self._duration = new_duration

    # перегрузим методы str и repr, чтобы выводилась также длительность
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"