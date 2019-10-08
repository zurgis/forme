name = ['James', 'aaa', 'ssss', 'a', 'b', 'c']
l_n = [0, 1, 2, 3, 4]

a = {n: name for n, name in zip(range(1, len(name) + 1), name)} # zip - функция которая объединяет элементы из 2 разных списков
print(len(name))
print(a)

b = {n: name for n in range(len(name)) for nam in name}
print(b)

c = {l_n : name for l_n, name in zip(l_n, name)}
print(c)

d = {len(i): i for i in name}
print(d)

from itertools import count
x = {n: name for n, name in zip(count(start=1), name)} # zip - функция которая объединяет элементы из 2 разных списков
print(x)