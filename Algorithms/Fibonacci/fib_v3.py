"""
Огромное число Фибоначчи по модулю

Даны целые числа 1≤n≤10^18 и 2≤m≤10^5,
необходимо найти остаток от деления n-го числа Фибоначчи на m.
"""
    
def fib(n, m):
    # для решения воспользуемся периодом Пизано
    period = [0, 1, 1]
    # key = m, value = количество элементов в периоде
    pisano_dict = {1: 1, 2: 3, 3: 8, 4: 6, 5: 20}
    per_pisano = 0
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if m in pisano_dict:
        per_pisano = pisano_dict[m]
        for i in range(3, per_pisano):
            period.append((period[i-2] + period[i-1]) % m)
    else:
        #Pisano(m) < 6m
        for i in range(3, 6*m+1):
            period.append((period[i-2] + period[i-1]) % m)
           if period[:4] == period[-4:]:
                per_pisano = len(period) - 4
                break
    return period[n%per_pisano]


def main():
    n, m = [int(i) for i in input().split()]
    print(fib(n, m))

if __name__ == "__main__":
    main()

