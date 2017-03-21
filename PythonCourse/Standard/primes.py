"""
Реализуйте функцию-генератор primes,

которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""
def primes():
    x = 1
    while True:
        x += 1
        simp = 0
        for i in range(2, x+1):
            simp += 1 if not x % i else 0
        if simp == 1:
            yield x