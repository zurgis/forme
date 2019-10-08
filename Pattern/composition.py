from emp_comp import PizzaRobot, Server

# Композиция и агрегация (агрегация используется для описания более слабой зависимости между контейнером и его содержимым)

class Customer: # Покупатель
    def __init__(self, name):
        self.name = name
    
    def order(self, server): # Заказ
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)

class Oven: # Печь
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat') # Встроить другие объекты
        self.chef = PizzaRobot('Bob') # Робот по имени Боб
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name) # Активизировать другие объекты
        customer.order(self.server) # Клиент делает заказ официанту
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

scene = PizzaShop() # Создать составной объект
scene.order('Homer') # Имитируем заказ клиента Homer
print('------' * 5)
scene.order('Shaggy') # Имитируем заказ клиента Shaggy
print('------' * 5)


# --------------------------------------------------------------------------

# Еще пример композиции
class Salary: # Зарплата
    def __init__(self, pay):
        self.pay = pay
    
    def getTotal(self):
        return (self.pay * 12)

class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self): # Годовой оклад (зп на 12 месяцев + бонус)
        return f'Total: {self.salary.getTotal() + self.bonus}'

emp1 = Employee(100, 10)
emp2 = Employee(1000, 50)
print(emp1.annualSalary())
print(emp2.annualSalary())
print('--------')

# Пример агрегации
class Salary1(object): # Зарплата
    def __init__(self, pay):
        self.pay = pay
    
    def getTotal(self):
        return (self.pay * 12)

class Employee1(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary1(self): # Годовой оклад (зп на 12 месяцев + бонус)
        return f'Total: {self.pay.getTotal() + self.bonus}'

salary = Salary1(100)
emp1 = Employee1(salary, 10)
print(emp1.annualSalary1())