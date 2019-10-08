import logging
import logging2

logger = logging.getLogger(__name__) # Возвращает регистратор с указанным именем
logger.setLevel(logging.DEBUG) # Устанавливает порог для этого регистратора на уровень. Регистрация сообщений, которые менее серьезны, чем уровень, будут игнорироваться. Сообщения регистрации, имеющие уровень серьезности или выше, будут отправляться любым обработчиком.

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s') # Возвращает отформатированный экземпляр класса 

file_handler = logging.FileHandler('test.log') # Указывает, что FileHandler должен быть создан с использованием указанного имени файла, а не StreamHandler
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter) # Устанавливает для Formatter, для этого обработчика значение fmt

stream_handler = logging.StreamHandler() # Возвращает сообщение в консоли
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler) # Добавляет указанный обработчик в этот регистратор
logger.addHandler(stream_handler)

#logging.basicConfig(filename='test.log', level=logging.DEBUG, # Выполняет базовую настройку ведения журнала, функции debug(), info(), warning(), error(), critical(), будут автоматически вызывать basicConfig
 #                   format='%(asctime)s:%(name)s:%(message)s')

def add(x, y):
    return x + y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        #logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result

num1 = 10
num2 = 0

add_result = add(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

div_result = divide(num1, num2)
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))