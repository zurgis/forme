"""
Intergace Segregation principle
Принцип разделения интерфейса.
Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента. 
Клиенты не должны зависеть от интерфейсов, которые они не используют.
Давайте посмотрим на интерфейс IShape ниже:
"""

# Справка:
"""
NotImplemented - В пользовательских базовых классах абстрактные методы должны вызывать это исключение, 
когда им требуется, чтобы производные классы переопределяли метод, или пока класс разрабатывается, 
чтобы указать, что реальная реализация еще должна быть добавлена.
Исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был.
"""
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

"""
Этот интерфейс рисует квадраты, круги, прямоугольники. Класс Circle, Square или Rectangle, реализующий интерфейс IShape, 
должен определять методы
draw_square (), draw_rectangle (), draw_circle ().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

"""
Довольно забавно смотреть на код выше. класс Rectangle реализует методы (draw_circle и draw_square), 
которые он не использует, также Square, реализующий draw_circle, и draw_rectangle, и 
класс Circle (draw_square, draw_rectangle).
Если мы добавим еще один метод в интерфейс IShape, например draw_triangle ()
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError

"""
Классы должны реализовывать новый метод, иначе будет выдано сообщение об ошибке.
Мы видим, что невозможно реализовать фигуру, которая может нарисовать круг, но не прямоугольник, 
квадрат или треугольник. Мы можем просто реализовать методы для выдачи ошибки, которая показывает, 
что операция не может быть выполнена.
ISP не одобряет дизайн этого интерфейса IShape. клиенты (в данном случае Rectangle, Circle и Square) 
не должны зависеть от методов, которые им не нужны или не используются. Кроме того, провайдер заявляет, 
что интерфейсы должны выполнять только одну работу (так же, как принцип SRP), любая дополнительная группа 
поведения должна быть абстрагирована к другому интерфейсу.
Здесь наш интерфейс IShape выполняет действия, которые должны обрабатываться независимо другими интерфейсами.
Чтобы интерфейс IShape соответствовал принципу ISP, мы разделяем действия между различными интерфейсами. 
Классы (Круг, Прямоугольник, Квадрат, Треугольник и т. Д.) Могут просто наследоваться от интерфейса IShape и 
реализовывать свое собственное поведение при рисовании.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

"""
Затем мы можем использовать I -интерфейсы для создания спецификаций Shape, 
таких как полукруг, прямоугольный треугольник, равносторонний треугольник, тупой прямоугольник и т. Д.
"""