# ZAGADNIENIA Napisy 
# - len, for, "foreach", ord, chr
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# Algorytmy - anagram, palindom, Boyer-Moore

# Wszystkie zadania wykonujemy na 26-znakowym
# alfabecie maturalnym: od A (65) do Z (90)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Przykładowe zadania:

import math

napis = input()
# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
print("1.", napis[0], napis[-1])
print("\n")

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
L = list(napis)
print("2.", L[1:-1])
#ALBO
#print("2.", napis[1:-1])
print("\n")

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
print("3.", napis[-1:-5:-1])
print(napis[:-5:-1])
print("\n")

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
suma = 0
k = 0
for i in range(len(napis)):
    suma += ord(napis[i])
    if napis[i] == "A" or napis[i] == "a":
        k += 1
print("4.", suma)
print("\n")

# 5. Policz ile we wpisanym napisie jest liter A.
print("5.", napis.count('a'))
# ALBO TAK
print("5.", k)
print("\n")

# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.

ilosc = 0
for i in range(len(napis)):
    l = 0
    for j in range(i, len(napis)):
        if napis[i] == napis[j]:
            l += 1
        elif l > ilosc:
            ilosc = l
            literka = napis[i]
print("6.", literka)
print("\n")


# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)
# NIE ZROBIONE
wynik = ""
lmin = len(napis)
ilosc = 0
for i in range(len(napis)):
    l = 0
    for j in range(i, len(napis)):
        if napis[i] == napis[j]:
            l += 1
        elif l > ilosc:
          ilosc = l
          wynik += napis[i]
        elif l < lmin:
            lmin = l
    if l == ilosc and l > lmin:
        powt = l
        wynik += "," + napis[i]
if ilosc == lmin:
    print("7. Nie ma żadnej dominujacej litery")
else:
    print("7.", wynik)
    print("\n")

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
ile_la = napis.count('LA')
if ile_la == 3:
    print("8. TAK")
else:
    print("8. NIE")
print("\n")

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)
suma = 0
for i in range(len(napis)):
    suma += ord(napis[i])
print("9.", chr(math.floor(suma/len(napis))))
print("\n")

# 10. Wypisz literki, których nie ma w napisie
L = list()
for i in range(65, 91):
    L.append(chr(i))
print(L)
print("\n")
for j in range(len(napis)):
    if napis[j] in L:
        L.remove(napis[j])
    #ALBO W TEM SPOSOB
    #if L.__contains__(napis[j]):
    #    L.remove(napis[j])
print("10.", L)
print("\n")

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
ilosc = 0
for i in range(len(napis) - 2):
    if napis[i] == napis[i+1] == napis[i+2] or napis[i] == napis[i+2]:
        ilosc += 1
print("11.", ilosc)
