class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
    
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')
    
    def __repr__(self):
        return f'Employee: name = {self.name}, salary = {self.salary}'

class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)
    
    def work(self):
        print(self.name, 'makes food')

class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(self.name, 'makes pizza')

Bob = PizzaRobot('Bob') # Создаем робото Боб
print(Bob) # Выводим методо __repr__
Bob.work() # Выполняем действие зависищее от типа
Bob.giveRaise(0.20) # Увеличиваем зп на 20% 
print(Bob, end='\n\n')

for i in Employee, Chef, Server, PizzaRobot:
    obj = i(i.__name__)
    obj.work()