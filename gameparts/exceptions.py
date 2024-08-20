class FiledIndexError(IndexError):
    def __str__(self) -> str:
        return 'Введённое значение находится за пределами размера игровго поля'


class СellOccupiedError(Exception):
    def __str__(self) -> str:
        return 'Ячейка уже занята, выберите другую клетку.'
