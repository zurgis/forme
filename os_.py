import os

print(os.getcwd())

os.chdir('c:/Programming')
print(os.getcwd()) # Возвращает текущий рабочий каталог

#os.mkdir('mm') # Создает директорию
print(os.listdir()) # Возвращает список, содержащий имена записей в каталоге

#os.makedirs('mm/mm') # Создает промежуточные директории

#os.rmdir('aa') # Удаляет каталог
#os.removedirs('hello/1/2') # Последовательно удаляет каталоги

#os.rename('mm/mm', 'mm/a') # Переименовать каталог
#os.renames('mm/mm', 'aa/aa')

for dirpath, dirnames, filenames in os.walk('c:/Programming/Learnings'): # os.walk - разделяет путь на путь к каталогу, название папок, и файлы в папках
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#print(os.environ) # Выводит все переменные пользовательской среды
print(os.environ.get('HOMEPATH')) # Позволяет посмотреть отдельную переменную
print(os.environ['HOMEPATH'])

file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt') # Объединяет несколько путей присвоенным разделителем
print(file_path)

print(os.path.basename('Programming/text.txt')) # Получает имя файла
print(os.path.dirname('Programming/text.txt')) # Получает имя папки
print(os.path.split('Programming/text.txt')) # Получает кортеж имен папки и файла
print(os.path.exists('Programming/text.txt')) # Проверяет существует ли файл(путь)
print(os.path.isdir('Programming/text.txt')) # Проверяет на существование папки
print(os.path.isfile('Programming/text.txt')) # Проверяет на существование файла