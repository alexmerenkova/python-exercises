"""
Вам дано описание наследования классов исключений в следующем формате. 

<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.
try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить,
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются
от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет
определять обработку каких исключений можно удалить из кода.

Формат входных данных:
В первой строке входных данных содержится целое число n - число классов исключений.
В следующих n строках содержится описание наследования классов. В i-й строке указано
от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого
не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных:
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода,
не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они
идут во входных данных.

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError
"""

from collections import defaultdict
hier_d = defaultdict(list)

def find_parent(par, child):
    if child not in hier_d:
        return False
    if par in hier_d[child] or par == child:
        return True
    else:
        for n in hier_d[child]:
            if find_parent(par, n):
                return True
        return False

def hierarhy():
    num = int(input())
    for _ in range(num):
        inp = input().split(' ')
        hier_d[inp[0]].extend([]) if len(inp) == 1 else hier_d[inp[0]].extend(inp[2:])
    stack = []
    notused = []
    num = int(input())
    for _ in range(num):
        newcmd = input()
        if newcmd in stack:
            if newcmd not in notused:
                notused.append(newcmd)
        else:
            for i in stack:
                if find_parent(i, newcmd):
                    notused.append(newcmd)
                    break
            stack.append(newcmd)
    for elem in notused:
        print(elem)

if __name__ == "__main__":
    hierarhy();