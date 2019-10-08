"""
Open Closed principle
Принцип открытости/закрытости.
Программные объекты(классы, модули, функции) должны быть открыты для расширения, а не модификации.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)


"""
Функция animal_sound не соответствует принципу открытого-закрытого
это не может быть закрыто против новых видов животных. Если мы добавим новое животное,
Снейк, мы должны изменить функцию animal_sound.
"""


animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)


"""
Как мы заставляем его (animal_sound) соответствовать OCP?
"""
print('-------')

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
"""
animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
]"""

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)

"""
У Animal теперь есть виртуальный метод make_sound. У нас каждое животное продлевает
Животный класс и реализовать виртуальный метод make_sound.
Каждое животное добавляет свою реализацию о том, как он издает звук в
make_sound. Animal_sound перебирает массив животных и просто
вызывает его метод make_sound.
Теперь, если мы добавим новое животное, animal_sound менять не нужно. Все, что нам нужно
чтобы сделать, это добавить новое животное в массив животных.
animal_sound теперь соответствует принципу OCP.
"""

"""
Другой пример:
Представим, что у вас есть магазин, и вы даете 20% скидку своему любимому
клиенты, использующие этот класс: когда вы решите предложить двойную скидку 20% на
VIP клиенты. Вы можете изменить класс следующим образом:
"""
print('------')

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4

"""
Нет, это не соответствует принципу OCP. OCP это запрещает. 
Если мы хотим дать новую процентную скидку, возможно, в diff. тип клиентов, вы увидите, 
что будет добавлена новая логика.
Чтобы заставить его следовать принципу OCP, мы добавим новый класс, который расширит скидку. 
В этом новом классе мы реализуем его новое поведение:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

"""
Если вы решили сделать скидку 80% для супер VIP-клиентов, это должно быть так:
Вы видите, расширение без изменений.
"""

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2

test = Discount('aaa', 100)
test2 = VIPDiscount('bbb', 100)
test3 = SuperVIPDiscount('ccc', 100)
print(test.get_discount(), test2.get_discount(), test3.get_discount(), sep='\n')