"""
Вашей программе на вход подаются две строки s и t,
состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa﻿

Sample Input 1:
abababa
aba

Sample Output 1:
3
"""

def find_str():
	s, t = input(), input()
	result = 0
	res = s.find(t)
	while  res != -1:
		res = s.find(t, res+1)
		result += 1
	return result

if __name__ == "__main__":
    print(find_str())