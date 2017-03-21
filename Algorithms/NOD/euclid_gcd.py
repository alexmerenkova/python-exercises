"""
Наибольший общий делитель

По данным двум числам 1≤a,b≤2⋅10^9 найдите их наибольший общий делитель.
"""

# Алгоритм Евклида
def gcd(a, b):
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        if a >= b:
            a = a % b
        else:
            b = b % a

def main():
    a, b = [int(i) for i in input().split()]
    print(gcd(a, b))


if __name__ == "__main__":
    main()