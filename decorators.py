from functools import wraps

def prefix_decorator(prefix): # НЕОБЯЗАТЕЛЬНАЯ ФУНКЦИЯ, ПРОСТО ДЛЯ ПРИМЕРА, СОЗДАЕТ ПРЕФИКС
    def decorator_function(original_functions): # Функция декоратор, ОСНОВНАЯ ФУНКЦИЯ ДЕКОРАТОР
        @wraps(original_functions) # @wraps игнориет другие названия, кроме оригинальной функции
        def wrapper_function(*args, **kwargs):
            print(prefix, 'wrapper executed this before {}'.format(original_functions.__name__))
            return original_functions(*args, **kwargs)
        return wrapper_function
    return decorator_function

class decorator_class(object): # Создаем класс - декоратор
    
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@prefix_decorator('TEST:')
def display():
    print('display function ran')

@decorator_class
@prefix_decorator('1')
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))

#decorated_display = decorator_function(display)
#decorated_display()

display()
print()
display_info('John', 25)