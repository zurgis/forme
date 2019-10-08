"""
Dependency Inversion principle
Принцип инверсии зависимости.
Объектом зависимости должна быть абстракция, а не что-то конкретное.
Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
"""

class XMLHttpService(XMLHttpRequestService):
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

"""
Здесь класс Http представляет собой высокоуровневый компонент, а XMLHttpService — низкоуровневый. 
Такая архитектура нарушает пункт A принципа инверсии зависимостей: «Модули верхних уровней не должны зависеть 
от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций».
Класс Http вынужденно зависит от класса XMLHttpService. Если мы решим изменить механизм, используемый классом Http 
для взаимодействия с сетью — скажем, это будет Node.js-сервис или, например, сервис-заглушка, применяемый для целей 
тестирования, нам придётся отредактировать все экземпляры класса Http, изменив соответствующий код. Это нарушает 
принцип открытости-закрытости.
Класс Http не должен знать о том, что именно используется для организации сетевого соединения. Поэтому мы создадим 
интерфейс Connection:
"""

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

"""
Интерфейс подключения имеет метод запроса. После этого мы передаем аргумент типа Connection нашему классу Http:
"""

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

"""
Так что теперь, независимо от типа службы соединения Http, переданной в Http, она может легко подключаться к сети, 
не заботясь о типе сетевого соединения.
Теперь мы можем повторно реализовать наш класс XMLHttpService для реализации интерфейса Connection:
"""

class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()

"""
Мы можем создать много типов соединений Http и передать их нашему классу Http без суеты об ошибках.
"""

class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

"""
Теперь мы видим, что как модули высокого уровня, так и модули низкого уровня зависят от абстракций. 
Класс Http (модуль высокого уровня) зависит от интерфейса соединения (абстракция), а типы сервиса Http
(модули низкого уровня), в свою очередь, зависят от интерфейса соединения (абстракция).
Кроме того, этот DIP заставит нас не нарушать принцип замещения Лискова:
Типы соединения Node-XML-MockHttpService могут заменять родительский тип Connection.
"""