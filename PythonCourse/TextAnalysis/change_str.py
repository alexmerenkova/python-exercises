"""
Вашей программе на вход подаются три строки s, a, b,
состоящие из строчных латинских букв.

За одну операцию вы можете заменить все вхождения
строки a в строку s на строку b.
Необходимо узнать, после какого минимального количества операций
в строке s не останется вхождений строки a, либо же определить,
что это невозможно.

Выведите одно число – минимальное число операций, после применения
которых в строке s не останется вхождений строки a.
Если после применения любого числа операций в строке s останутся
вхождения строки a, выведите Impossible.

Sample Input 1:
ababa
a
b

Sample Output 1:
1

Sample Input 3:
ababa
c
c

Sample Output 3:
0

Sample Input 4:
ababac
c
c

Sample Output 4:
Impossible
"""
def change_str():
    s, a, b = [input() for i in range(3)]
    res = 0
    if (a in s) and (a in b):
        return "Impossible"
    
    while a in s:
        s = s.replace(a,b)
        res +=1 
    return res

if __name__ == "__main__":
    print(change_str())



