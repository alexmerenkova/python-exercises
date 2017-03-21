"""
Вам дана последовательность строк. 
"""
import sys
import re

def re_1():
    """Выведите строки, содержащие "cat" в качестве слова."""
    pat = r'\bcat\b'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pat, line):
            print(line)

def re_2():
    """Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа."""
    pat = r'z.{3}z'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pat, line):
            print(line)
def re_3():
    """Выведите строки, содержащие обратный слеш "\﻿"."""
    pat = r'\\'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pat, line):
            print(line)

def re_4():
    """Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)."""
    pat = r'\b(\w+)\1\b'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pat, line):
            print(line)

def re_5():
    """В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ 
    и выведите полученные строки."""
    pat = r'human'
    for line in sys.stdin:
        line = line.rstrip()
        print (re.sub(pat, 'computer', line))

def re_6():
    """В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" 
    (регистр не важен), на слово "argh"."""
    pat = r'\b[aA]+\b'
    for line in sys.stdin:
        line = line.rstrip()
        print (re.sub(pat, 'argh', line, count=1))

def re_7():
    """В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
    Буквой считается символ из группы \w﻿."""
    pat = r'(\w{1})(\w{1})(\w*)'
    for line in sys.stdin:
        line = line.rstrip()
        print (re.sub(pat, r'\2\1\3', line))

def re_8():
    """В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
    Буквой считается символ из группы \w."""
    pat = r'(\w)(\1+)'
    for line in sys.stdin:
        line = line.rstrip()
        print (re.sub(pat, r'\1', line))
    