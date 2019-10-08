import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor: # ThreadPoolExecutor это подкласс executor, который использует пул потоков для асинхронного выполнения вызовов
    #f1 = executor.submit(do_something, 2) # Запланирует выполнение вызываемой функции и возвращает объект future, представляющий выполнение вызываемой функции
    #f2 = executor.submit(do_something, 2)

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for results in results:
        print(results)

    #results = [executor.submit(do_something, 2) for _ in range(5)]
    #results = [executor.submit(do_something, sec) for sec in secs]

    #print(f1.result())
    #print(f2.result())

    #for f in concurrent.futures.as_completed(results): # Возвращает итератор для экземпляров Future
    #    print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')