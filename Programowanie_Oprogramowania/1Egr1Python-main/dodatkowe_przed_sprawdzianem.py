# zad 1
# Oblicz wspólny mianownik trzech wpisanych przez użytkownika ułamków. 
l1, m1 = map(int, input().split("/"))
l2, m2 = map(int, input().split("/"))
l3, m3 = map(int, input().split("/"))
mm1 = m1
mm2 = m2
mm3 = m3
iloczyn1 = m1 * m2
iloczyn2 = m2 * m3
while m2 > 0:
    m1, m2 = m2, m1 % m2
    nwd1 = m1
    nww1 = iloczyn1 / nwd1
while m3 > 0:
    mm2, m3 = m3, mm2 % m3
    nwd2 = mm2
    nww2 = iloczyn2 / nwd2
iloczyn_finalny = nww1 * nww2
while nww2 > 0:
    nww1, nww2 = nww2, nww1 % nww2
print(round(iloczyn_finalny / nww1))

# zad 2
def dzielniki(x):
    suma = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            suma += i
    return suma
for liczba1 in range(1, 5000):
    for liczba2 in range(1, 5000):
        if dzielniki(liczba1) == liczba2 and dzielniki(liczba2) == liczba1 and liczba1 != liczba2:
            print(liczba1, liczba2)
# zad 3
#Liczby feniczne
# n = a * b * c

def czyp(x):
    czy_p = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            czy_p = False
    if czy_p:
        return True
    else:
        return False

for liczba in range(2, 2500):
    L = []
    for j in range(2, liczba // 2 + 1):
        if liczba % j == 0 and czyp(j):
            L.append(j)
    if len(L) == 3:
        wynik = 1
        for i in L:
            wynik *= i
        if wynik == liczba:
            print(liczba)
