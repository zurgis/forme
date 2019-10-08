"""
Liskov Substitution principle
Принцип подстановки Барбары Лисков.
Необходимо, чтобы подклассы могли бы служить заменой для своих суперклассов.
Цель этого принципа заключаются в том, чтобы классы-наследники могли бы использоваться вместо родительских классов, 
от которых они образованы, не нарушая работу программы. Если оказывается, что в коде проверяется тип класса, 
значит принцип подстановки нарушается.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'

animals = [
    Lion('lion'),
    Animal('mouse')
]        

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))

animal_leg_count(animals)

"""
Чтобы заставить эту функцию следовать принципу LSP, мы будем следовать этому LSP
требования, сформулированные Стивом Фентоном:
Если у суперкласса (Animal) есть метод, который принимает тип суперкласса
(Животное) параметр. Его подкласс (голубь) должен принять в качестве аргумента
тип суперкласса (тип животного) или тип подкласса (тип голубя). Если
super-class возвращает тип суперкласса (Animal). Его подкласс должен возвращать
тип суперкласса (тип животного) или тип подкласса (голубь). 

(Они заключаются в том, что методы, принимающие или возвращающие значения с типом 
некоего суперкласса (Animal в нашем случае) должны также принимать и возвращать значения, 
типами которых являются его подклассы (Pigeon).)

Теперь мы можем повторно реализовать функцию animal_leg_count:
"""

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

"""
Функция animal_leg_count меньше заботится о типе переданного Animal, просто
вызывает метод leg_count. Все, что он знает, это то, что параметр должен быть
Тип животных, либо класс животных, либо его подкласс.
Класс Animal теперь должен реализовать / определить метод leg_count. И это
Подклассы должны реализовать метод leg_count:
"""

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass

"""
Когда он передается в функцию animal_leg_count, он возвращает количество ног, которые есть у льва.
Видите ли, animal_leg_count не нужно знать тип Animal, чтобы вернуть счетчик его ног, он просто вызывает метод 
leg_count типа Animal, потому что по контракту подкласс класса Animal должен реализовать функцию leg_count
"""