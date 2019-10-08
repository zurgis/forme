x = 'global x' # Глобальная переменная, может использоваться везде

def test():
    global x # Объявляем глобальную переменную x, чтобы переназначить значение первого объявления
    x = '3'
    y = 'local y' # Локальная переменная, принадлежит функции
    print(x)
    print(y)

print(x) # Выводит первое объявление переменной
test()
print(x)

print('------------', end='\n\n')

def test1():
    #global x
    x = 'outer x'

    def inner():
        #nonlocal x # Делает переменную х нелокальной, изменяется также переменная на уровень выше
        x = 'inner x' # Локальная переменная
        print(x)
    
    inner()
    print(x)

test1()
print(x)

print('------------', end='\n\n')

def test2():
    #global x
    x = 'outer x'

    def inner():
        nonlocal x # Делает переменную х нелокальной, для данного уровня
        x = 'inner x' # Локальная переменная

        def t():
            #nonlocal x
            x = 1
            print(x)
        
        t()
        print(x)
    
    inner()
    global x
    x = 'outer x'
    print(x)

test2()
print(x)