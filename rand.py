import random

print(random.random()) # Выводит рандомно число с плавающей запяток от 0.0 до 1.0
print(random.uniform(1, 10)) # Выводит рандомно число с плавающей запятов в диапазоне
print(random.randint(-11, 0)) # Выводит рандомное целое число в диапазоне

a = [1, 2, 3, 4, 5]
print(random.choice(a)) # Возвращает рандомный элемент из последовательности
print(random.choices(a, k=10)) # Возвращает рандомный элемент из последовательности, k - задает кол-во раз
print(a)
random.shuffle(a) # Перемешивает последовательность
print(a)
print(random.sample(a, k=5)) # Возвращает новый список, содержащий элементы из совокупности, оставляя исходную совокупность без изменений.

b = 'abcdefg'
print(random.sample(b, k=6))