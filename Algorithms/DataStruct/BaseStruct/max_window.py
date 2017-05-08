"""
Максимум в скользящем окне

Найти максимум в каждом окне размера m данного массива чисел A[1 . . . n]
Наивный способ решить данную задачу — честно просканировать каждое окно
и найти в нём максимум. Время работы такого алгоритма — O(nm). 
Ваша задача — реализовать алгоритм со временем работы O(n).
Формат входа. 
Первая строка входа содержит число n, вторая — массив A[1 . . . n],
третья — число m.

Формат выхода.
n − m + 1 максимумов, разделённых пробелами

Реализовано при помощи очереди из двух стеков с поддержкой максимума

"""

def moveto (stack1, stack2, max_st):
    while stack1:
        elem = stack1.pop()
        stack2.append(elem)
        max_st.append(elem if not max_st else max(elem, max_st[-1]))


n = int(input())
origin = [int(i) for i in input().split()]
m = int(input())

q1 = origin[:m]
origin = origin[m:]
q2 = []
max_list = []
max_val = float("-Inf")
max_stack = []

moveto(q1, q2, max_stack)
while q2:
    m_val = max(max_val, max_stack.pop()) if q1 else max_stack.pop()
    q2.pop()
    max_list.append(m_val)
    if origin:
        new_elem = origin.pop(0)
        max_val = max(max_val, new_elem) if q1 else new_elem
        q1.append(new_elem)
    else:
        break
    if q1 and not q2:
        moveto(q1, q2, max_stack)

print (" ".join(map(str, max_list)))
