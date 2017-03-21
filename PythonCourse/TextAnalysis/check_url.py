"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B,
т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
Yes

Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:
No
"""

import re
import requests

def getlist(url):
    pat = r'<a href="(.+)">.+</a>'
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        return re.findall(pat, res.text)
    return []


def check():
    url1, url2  = input(), input()
    linklist = getlist(url1)
    for lnk in linklist:
        lst = getlist(lnk)
        if url2 in lst:
            return 'Yes'
    return 'No'

if __name__ == "__main__":
    print(check())