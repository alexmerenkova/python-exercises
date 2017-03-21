"""
Кодирование Хаффмана

По данной непустой строке s длины не более 10^4, состоящей из строчных букв
латинского алфавита, постройте оптимальный беспрефиксный код. В первой строке
выведите количество различных букв k, встречающихся в строке, и размер
получившейся закодированной строки. В следующих k строках запишите коды букв
в формате "letter: code". В последней строке выведите закодированную строку.
Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""
from collections import Counter

def coding(original_str):
    cnt_str = Counter(original_str)
    cnt = sorted(cnt_str.items(), key=lambda x: x[1])
    codes = {}
    result = {}
    
    if len(cnt_str) == 1:
       result[original_str[0]] = '0'
    else:
        while (len(cnt) > 1):
            codes[cnt[0][0]] = '0'
            codes[cnt[1][0]] = '1'
            cnt = sorted(cnt[2:] + 
                [(cnt[0][0] + cnt[1][0], cnt[0][1] + cnt[1][1])],
                key = lambda x: x[1])

        for let in cnt_str.keys():
            result[let] = ''
            let_list = []
            for elem in codes.keys():
                if let in elem:
                    let_list.append(elem)
            for code in sorted(let_list, key=lambda x: len(x), reverse=True):
                result[let] += codes[code]

    res_str = ''
    for i in original_str:
    	res_str += result[i]

    print('{} {}'.format(len(cnt_str), len(res_str)))

    for key, value in result.items():
    	print('{}: {}'.format(key, value))
    print(res_str)

def main():
    original_str = input()
    coding(original_str)


if __name__ == "__main__":
    main()



