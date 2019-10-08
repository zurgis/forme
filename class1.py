class Employee:

    num_of_emps = 0 # Вводится классовая переменная
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + lname + '.@email.com'
        
        Employee.num_of_emps += 1 # Используется имя класса, а не self, т.к необходимо прибавлять переменную при создании экземпляра

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # self.raise_amount используется для возможности изменения у каждого экземпляра отдельно

    @classmethod
    def set_raise_amount(cls, amount): # @classmethod используется для определения классового метода, получает класс первым аргументом, таким образом можно неявно использовать класс
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day): # @staticmethod преобразует метод в статический, используется для решения прямых задачы
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp1 = Employee('Jhon', 'Lennon', 30000)
emp2 = Employee('Ilon', 'Mask', 100000)

print(emp1.email)
print(emp1.fullname())
print(Employee.fullname(emp1))
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

#Employee.raise_amount = 1.05
#emp2.raise_amount = 1.05

print()
print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)
print(emp2.__dict__)
print(Employee.num_of_emps)
print()

Employee.set_raise_amount(1.05)
#emp1.set_raise_amount(1.05)
print(emp2.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print()
emp_str1 = 'John-Lennon-30000'
new_emp1 = Employee.from_string(emp_str1)
print(new_emp1.email)
print()

import datetime
my_date = datetime.date(2019, 9, 14)
print(Employee.is_workday(my_date))

#print(emp1.is_workday(my_date))
#print(emp1.__dict__)
