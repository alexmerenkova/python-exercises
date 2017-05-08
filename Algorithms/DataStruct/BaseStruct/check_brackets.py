"""
Скобки в коде

Проверить, правильно ли расставлены скобки в данном коде.
Формат входа. Строка s[1: : : n], состоящая из заглавных
и прописных букв латинского алфавита, цифр, знаков препинания
и скобок из множества []{}().
Формат выхода.Если скобки в s расставлены правильно, выведите
строку “Success". В противном случае выведите индекс (используя
индексацию с единицы) первой закрывающей скобки, для которой нет
соответствующей открывающей. Если такой нет, выведите индекс первой
открывающей скобки, для которой нет соответствующей закрывающей.
"""
def check_brackets(check_str):
    bracket_dict = {'(':')', '{':'}', '[':']'}
    check_stack = []
    
    for ind, element in enumerate(check_str, 1):
        #открывающая скобка
        if element in bracket_dict:
            check_stack.append((ind, element))
        #закрывающая скобка
        elif element in bracket_dict.values():
            if len(check_stack) == 0:
                return ind
            _, top_elem = check_stack.pop()
            if bracket_dict[top_elem] != element:
                return ind
    if len(check_stack):
        i, _ = check_stack.pop(0)
        return i
    return "Success"

if __name__ == "__main__":
    print(check_brackets(input()))






