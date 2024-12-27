import inspect
class Plant:

    def __init__(self, color, eatable):
        self.color = color
        self.eatable = eatable

    def grow_plant(self):
        print("Растение подросло")

    def pull_out_the_plant(self):
        print("Растение беспощадно вырвано :(")

def introspection_info(obj):

    # Определяем тип объекта
    # Определение типа объекта: Используется type(obj).__name__, чтобы получить строковое представление типа объекта.
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    # Получение атрибутов: С помощью dir() мы получаем все атрибуты и фильтруем их, исключая методы (вызываемые функции)
    # и скрытые атрибуты (начинающиеся с "__").

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    # Получение методов: Аналогично получаем список методов, фильтруя только вызываемые функции.
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Определяем модуль, к которому принадлежит объект
    # Определение модуля: Проверяем наличие атрибута __module__, чтобы определить модуль, к которому принадлежит объект.
    module = obj.__module__ if hasattr(obj, '__module__') else 'N/A'

    # Другие интересные свойства
    #Дополнительная информация: Для коллекций (списки, словари и множества) добавляем длину коллекции в дополнительную информацию.
    additional_info = {}
    if isinstance(obj, (list, dict, set)):
        additional_info['length'] = len(obj)

        # Формируем итоговый словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        **additional_info
    }

    return info

_object = Plant("green",True)
print(introspection_info(_object))