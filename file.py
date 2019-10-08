with open('test.txt', 'a') as f:
    aa = input('Введите текст: ')
    f.write(aa)

print('---------')

with open('test.txt') as f:
    a = f.read()
    print(a)