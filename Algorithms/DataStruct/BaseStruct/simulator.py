"""
Обработка сетевых пакетов

Реализовать обработчик сетевых пакетов

Формат входа.
Первая строка входа содержит размера буфера size
и число пакетов n. Каждая из следующих n строк содержит
два числа: время arrival i прибытия i-го пакета и время
duration i, необходимое на его обработку. Гарантируется,
что arrival 1 <= arrival 2 <= .. <= arrival n. При этом 
может оказаться, что arrival i-1 = arrival i. В таком случае
считаем, что пакет i-1 поступил раньше пакета i.

Формата выхода.
Для каждого из n пакетов выведите время, когда процессор
начал его обрабатывать, или -1, если пакет был отброшен
"""

def process_pack(size, n):
    buff = []
    for _ in range(n):
        arr, dur = [int(i) for i in input().split()]
        #выкидываем из буфера обработанные к этому времени пакеты
        if buff and arr >= buff[0][1]:
            buff.pop(0)
        #если есть место
        if len(buff) < size:
            #время начала обработки
            start = max(buff[-1][1], arr) if len(buff) else arr
            #время конца обработки
            stop =  start + dur if len(buff) else arr + dur
            buff.append((start, stop))
            print(start)
        else:
            print(-1)

if __name__ == "__main__":
    size, n = [int(i) for i in input().split()]
    process_pack(size, n)