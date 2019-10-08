import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[5]) # Конструктор всегда должен вызываться с ключевым аргументами. target - это вызываемый объект, который вызывается методом run()
    t.start() # Активирует поток
    threads.append(t)

for thread in threads:
    thread.join() # Ждет пока не закончится поток. Пока поток не закончится, следующие потоки не будут активированы

#t1 = threading.Thread(target=do_something)
#t2 = threading.Thread(target=do_something)

#t1.start()
#t2.start()
#t1.join()
#t2.join()

#do_something()
#do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')