# zad 1
#a, b , c = map(int, input().split())
#if c - b == b - a: print("ciag arytmetyczny", end=" ")
#if c / b == b / a: print("ciag geometryczny", end=" ")

#if a < b: print("rosnacy")
#if a > b: print("malejacy")

# zad 2
#suma = 0
#for i in range(104, 1000, 16):
#    suma += i
#print(suma)

# zad 3
#wielokr = 0
#ilosc = 0
#first = 0
#for i in range(99, 9, -1):
#    if i % 7 == 0:
#        wielokr = i
#        break
#for i in range(1000, wielokr):
#    if i % wielokr == 0:
#        first = i
#for i in range(first, 10000, wielokr):
#    ilosc += 1
#print(ilosc)

# zad 4
#ilosc = 0
#for i in range(10, 100):
#    if i // 10 >= 2 * (i % 10):
#        ilosc += 1
#print(ilosc)

# zad 5
#ilosc = 0
#suma = 0
#for i in range(100, 1000):
#    if (i % 100) * 100 > (i // 10) % 10 + (i % 10):
#        ilosc += 1
#        suma += i
#print(f"Ilosc: {ilosc}")
#print(f"Suma: {suma}")

# zad 6
#n = int(input())
#suma = 0
#i = 1
#while n > 0:
#    if i % 19 == 0:
#        suma += i
#        n -= 1
#    i = i + 1
#print(suma)

# zad 7
#n = int(input())
#suma = 0
#i = 999
#while n > 0:
#    if i % 37 == 0:
#        suma += i
#        n -= 1
#    i -= 1
#print(suma)

# zad 8
#n = int(input())
#suma = 0
#for i in range(n):
#    suma += (3 * i + 2) * ((-1) ** i)
#print(suma)

# zad 9
#n = int(input())
#iloczyn = 1
#for i in range(n):
#    iloczyn *= (2 ** i) * ((-1) ** i)
#print(iloczyn)

# zad 10
#n = int(input())
#suma = 0
#for i in range(1, n + 1):
#    element = 1
#    for j in range(1, i + 1):
#        element *= j
#    suma += element
#print(suma)

# zad 11
#n = int(input())
#suma = 0
#for i in range(n):
#    suma += (1 + i * 2) / (i + 1) ** 2
#print(suma)

#n = int(input())
#liczniki = 0
#mianownik = 1
#for i in range(1, n + 1):
#    mianownik = mianownik * i**2
#for i in range(1, i + 1):
#    liczniki += (2 * i - 1) * mianownik // (i**2)
#print(f"wynik: {liczniki}/{mianownik}")

# zad 12
#n = int(input())
#licznik = 0
#mianownik = 0
#for i in range(n):
#    licznik += 1 + i * 2
#    mianownik += (i + 1) ** 2
#print(licznik / mianownik)

# zad 13
#n = int(input())
#suma = 0
#for i in range(1, n + 1):
#    suma += (i * 2) / (i ** 3 + 2)
#print(suma)

# zad 14
#   :-/

# zad 15
#n = int(input())
#iloczyn = 1
#for i in range(1, n + 1):
#    iloczyn *= (i + 2) / (2 ** i - 1)
#print(f"{iloczyn:.20f}")
# '.20f' okresla ilosc liczb po kropce

# zad 16
#n = int(input())
#iloczyn = 1
#a = 1
#b = 2
#temp = int
#for i in range(n):
#    iloczyn *= a / (2 ** i)
#    temp = b
#    b = a + temp
#    a = temp
#print(iloczyn)
