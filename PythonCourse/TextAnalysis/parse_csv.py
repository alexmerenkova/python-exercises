"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
"""
import csv
from collections import Counter

def parse_csv():
    crimes = []
    with open('Crimes.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            year, _ = row['Date'].split(' ', 1)
            if year.endswith('2015'):
                crimes.append(row['Primary Type'])
        cnt = Counter(crimes)
        result = sorted(cnt.items(), key = lambda x: x[1], reverse=True)
        print(result[0][0])

if __name__ == "__main__":
    parse_csv()
