"""
Покрыть отрезки точками

По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк
содержит по два числа 0≤l≤r≤10^9, задающих начало и конец отрезка. Выведите
оптимальное число m точек и сами m точек. Если таких множеств точек несколько,
выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3 
Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 
"""

def opt_dots(n):
    tmp_list = []
    result = []
    for i in range(n):
        tmp_list.append(tuple([int(i) for i in input().split()]))
    
    #сортировка по правым концам отрезков
    tmp_list.sort(key = lambda x: x[1])
    
    for left, right in tmp_list:
        if not result:
            result.append(right)
            continue
        if left <= result[-1] and right >= result[-1]:
            continue
        result.append(right)
    return result

def main():
    n = int(input())
    result = opt_dots(n)
    print(len(result))
    for i in result:
        print(i, end = ' ')

if __name__ == "__main__":
    main()