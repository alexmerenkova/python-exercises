"""
Вам дано описание наследования классов в формате JSON. 
Описание представляет из себя массив JSON-объектов,
которые соответствуют классам. У каждого JSON-объекта
есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов
он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2
"""
import json
from collections import defaultdict

hier = defaultdict(list)
result = defaultdict(set)

def find_parent(par, child):
    if child not in hier:
        return False
    if par in hier[child] or par == child:
        result[par].add(child)
        return True
    else:
        for n in hier[child]:
            if find_parent(par, n):
                result[par].add(child)
                return True
        return False

def main():
    jdata = input()
    pdata = json.loads(jdata)

    all_elements = set()
    for elem in pdata:
        for i in elem['parents']:
            hier[elem['name']].append(i)
            all_elements.add(i)
        if not elem['parents']:
            hier[elem['name']] = []
        all_elements.add(elem['name'])

    for one in all_elements:
        for two in all_elements:
            find_parent(one, two)

    for key, val in sorted(result.items()):
        print('{} : {}'.format(key, len(val)))

if __name__ == "__main__":
    main()
