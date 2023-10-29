from pydantic import BaseModel



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

class User(Item):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.balance = 100