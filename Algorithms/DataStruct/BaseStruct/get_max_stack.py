"""
Стек с поддержкой максимума

Реализовать стек с поддержкой операций push,pop и max.

Формата входа.
Первая строка содержит число запросов q. 
Каждая из последующих q строк задаёт запрос в одном из
следующихформатов: push v, pop, or max. 

Формат выхода. 
Для каждого запроса max выведите (в отдельнойстроке)
текущий максимум на стеке.
"""

def get_max():
    num_req = int(input())
    max_stack = []
    for _ in range(num_req):
        cmd = input().split()
        if cmd[0] == 'push':
            elem = int(cmd[1])
            if not max_stack:
                max_stack.append(elem)
            else:
                old_elem = max_stack[-1]
                max_stack.append(max(elem, old_elem))
        elif cmd[0] == 'pop':
            max_stack.pop()
        else:
            print(max_stack[-1])


if __name__ == "__main__":
    get_max()