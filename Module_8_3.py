
class Car:
    def __init__(self, _model: str, _vin: int, _numbers: str):
        self._model = _model
        self._vin = _vin
        self._numbers = _numbers
        self.__is_valid_vin(_vin)
        self.__is_valid_numbers(_numbers)

    def __is_valid_vin(self, _vin_code):
        if not isinstance(_vin_code, int):
            raise IncorrectVinCode('Некорректный вин-код')
        if _vin_code < 1000000 or _vin_code > 9999999:
            raise IncorrectVinCode('Неверное кол-во цифр в вин-коде')
        else:
            return True

    def __is_valid_numbers(self, _num):
        if not isinstance(_num, str):
            raise IncorrectCarNum('Некорректный тип данных для номеров')
        if len(_num) != 6:
            raise IncorrectCarNum('Неверная кол-во знаков в номере')
        else:
            return True



class IncorrectVinCode(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNum(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinCode as exc:
    print(exc.message)
except IncorrectCarNum as exc:
    print(exc.message)
else:
    print(f'{first._model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinCode as exc:
    print(exc.message)
except IncorrectCarNum as exc:
    print(exc.message)
else:
    print(f'{second._model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinCode as exc:
    print(exc.message)
except IncorrectCarNum as exc:
    print(exc.message)
else:
    print(f'{third._model} успешно создан')