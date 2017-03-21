"""
Различные слагаемые

По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n
можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4

Sample Output 1:
2
1 3 

Sample Input 2:
6

Sample Output 2:
3
1 2 3
"""

def summand(n):
    result = []
    if n == 1:
        result.append(1)
    for i in range(1,n):
        s = n - i 
        if s > n - s:
            result.append(i)
            n -= i
        else:
            result.append(n)
            break
    return result


def main():
    n = int(input())
    result = summand(n)
    print(len(result))
    for i in result:
        print(i, end = ' ')

if __name__ == "__main__":
    main()