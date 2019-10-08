"""
Single Responsibility principle
Принцип единственной ответственности.
Каждый класс должен иметь одну и только одну причину для изменений.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass



"""
Здесь класс нарушает принцип, потому что управляем свойствами животного, когда метод save() управляет в базе данных.
Чтобы исправить это, добавим еще 1 класс, который будет отвечать за хранение в БД
"""

class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

"""
При разработке наших классов мы должны стремиться соединить связанные функции, поэтому
всякий раз, когда они имеют тенденцию меняться, они меняются по той же причине. И мы должны попробовать
разделить функции, если они изменятся по разным причинам. - Стив Фентон
"""
"""
Недостатком этого решения является то, что клиенты этого кода должны иметь дело
с двумя классами. Распространенным решением этой дилеммы является применение Фасада
шаблон. Животный класс будет Фасадом для управления базами данных животных и
управление свойствами животных.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)

"""
Самые важные методы хранятся в классе Animal и используются как Facade для
меньшие функции.
"""