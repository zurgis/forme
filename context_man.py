import os, tempfile
from contextlib import contextmanager, suppress, closing, redirect_stdout

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, ext_type, ext_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

print(f.closed)

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample2.txt', 'w') as f1:
    f1.write('Hello world')

print(f1.closed)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('__pycache__'):
    print(os.listdir())

class Cd:
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.target)
    
    def __exit__(self, *exc_info):
        os.chdir(self.saved_cwd)
        del self.saved_cwd

print(os.getcwd())
with Cd('__pycache__'):
    print(os.listdir())
print(os.getcwd())

with suppress(FileNotFoundError): # suppress - подавляет исключения, ошибка не возникает, хотя и файла нету
    with open('notfile.txt') as f:
        text = f.read()
        print(text)

print('------' * 5)
with tempfile.TemporaryFile() as f: # TemporaryFile - создает временный файл, в менеджере сразу после работы он удалится
    path = f.name
print(path)

from urllib.request import urlopen
url = 'http://twitch.tv'
with closing(urlopen(url)) as page: # closing реализует метод close
    #server = page.getheader('Server')
    pass

#print(server)

import io
handle = io.StringIO() # StringIO() - текстовой поток в памяти
with redirect_stdout(handle): # redirect_stdout - позволяет локально перехватывать вывод в стандартный поток
    print('Hello world')
    with redirect_stdout(handle):
        print('Hello w')

print(handle.getvalue())