"""
Непрерывный рюкзак

Первая строка содержит количество предметов 1≤n≤10^3
и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6
и объём 0<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа). 
Выведите максимальную стоимость частей предметов (от каждого предмета
можно отделить любую часть, стоимость и объём при этом пропорционально
уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000
"""

def backpack():
    n, w_backpack = [int(i) for i in input().split()]
    tmp_list = []
    for i in range(n):
        ci, wi = [int(i) for i in input().split()]
        tmp_list.append((ci, wi, ci/wi))
    tmp_list.sort(key=lambda x: x[2], reverse=True)
    result = 0.0
    for ci, wi, ci_wi in tmp_list:
        if wi <= w_backpack:
            result += ci
            w_backpack -= wi
        else:
            result += (ci_wi * w_backpack)
            break
    print('{0:.3f}'.format(result))


if __name__ == "__main__":
    backpack()
