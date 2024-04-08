from math import gcd

# Zadanie 3
suma = 0
for i in range(11, 100, 2):
    suma += i
print(suma)

# Zadanie 4
ilosc = 0
for i in range(101, 1000, 2):
    if i % 17 == 0:
        ilosc += 1
print(ilosc)

# Zadanie 5
n = int(input())
ile = 0
for i in range(1, n + 1):
    if n % i == 0:
        ile += 1
print(ile)

# Zadanie 6
def suma_dz(x):
    suma = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            suma += i
    return suma
n = int(input())
if suma_dz(n) == n:
    print("JEST")
else:
    print("NIE JEST")

# Zadanie 7
a, b = map(int, input().split("/"))
c, d = map(int, input().split("/"))
def odejmij_ulamki(a, b, c, d):
    wynik = (f"{a}/{b} - {c}/{d} = ")
    nww = b * d // gcd(b, d)
    a, c, b = a * (nww // b), c * (nww // d), nww
    a -= c
    if gcd(a, b) > 1:
        wynik += (f"{a // gcd(a, b)}/{b // gcd(a, b)}")
    else:
        wynik += (f"{a}/{b}")
    return wynik
print(odejmij_ulamki(a, b, c, d))

# Zadanie 8
s = input()
ilee = 0
for literka in s:
    if ord(literka) % 2 == 1:
        ilee += 1
print(ilee)

# Zadanie 9
slowo1 = input()
slowo2 = input()
slowo3 = input()
iloscA = 0
for l1 in slowo1:
    if l1 == 'A':
        iloscA += 1
for l2 in slowo2:
    if l2 == 'A':
        iloscA += 1
for l3 in slowo3:
    if l3 == 'A':
        iloscA += 1
if iloscA >= 4:
    print("YES")
else:
    print("NOOO")
