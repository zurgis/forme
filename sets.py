x = {2}
y = frozenset({4, 3, 2, 2}) # frozenset является неизменяемым множеством, когда обычное множество изменяемо
z = {4, 5}
a = (1, 2, 3)

x.add(1)

print(x)
print(y)
print(x.union(y)) # union - объединяет 2 множества
print(y.difference(x)) # difference - разница первого множества с другим
print(x.intersection(y)) # intersections - одинаковые
print(x.symmetric_difference(y)) # symmetric_diffetence - разница обоих множеств
print(x.intersection(a))