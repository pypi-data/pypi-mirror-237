from pydantic import BaseModel

# pypi-AgEIcHlwaS5vcmcCJDllZjhkN2I0LTgzNzctNGJkZS1hNzk3LWRhYmFjN2Q3YTE4OAACKlszLCIzNzNiNGI0Yy01NzE0LTRkODQtYTk2OC1kMzdlYjI5MmYxYjIiXQAABiCe6rs_EYAilA8jd5vBIsoBggA3Qe2ILmIQGZCawXfiBA


class Item(BaseModel):
    """
    Вещи

    :param name: название
    :type name: obj:`str`

    :param description: описание
    :type description: obj:`str`

    :param price: цена
    :type price: obj:`float`

    :param tax: налог
    :type tax: obj:`float`
    """
    name: str
    """Имя"""
    description: str | None = None
    """Описание"""
    price: float
    """Цена"""
    tax: float | None = None
    """Налог"""

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.balance = 100

    def get_price(self):
        return Item.price