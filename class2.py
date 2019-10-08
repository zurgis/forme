class Employee:

    num_of_emps = 0 # Вводится классовая переменная
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        #self.email = fname + lname + '.@email.com'
        
        Employee.num_of_emps += 1 # Используется имя класса, а не self, т.к необходимо прибавлять переменную при создании экземпляра

    @property
    def email(self):
        return f'{self.fname}{self.lname}@email.com'

    @property
    def fullname(self): # @property является геттером, свойство инкапсуляции
        return f'{self.fname} {self.lname}'
    
    @fullname.setter
    def fullname(self, name): # После назначения геттера, можно использовать сеттер, чтобы изменять данные
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # self.raise_amount используется для возможности изменения у каждого экземпляра отдельно

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

dev1 = Developer('Dean', 'Winchester', 20000, 'Python')
dev2 = Developer('Merry', 'Winchester', 20000, 'Python')
print(dev1.fullname, dev1.prog_lang, dev1.email)
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print()

mgr1 = Manager('Sam', 'Winchester', 90000, [dev1])

print(mgr1.email)
mgr1.add_emp(dev2)
#mgr1.remove_emp(dev1)
mgr1.print_emps()

print(dev1)
print(dev1 + mgr1)
print()

print(dev1.email)
dev1.fullname = 'Jim Carry'
print(dev1)
del dev1.fullname
