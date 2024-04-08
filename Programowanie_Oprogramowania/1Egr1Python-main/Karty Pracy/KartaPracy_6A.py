# zad 1
#x = int(input())
#suma = 0
#k = 0
#cyfry = 0
#pocz_cyfra = int
#while k < x:
#    cyfry += 1
#    k = 10 ** cyfry
#print(f"ilosc cyfr w podanej liczbie: {cyfry}")
#while x > 0:
#    pocz_cyfra = x // (10 ** (cyfry - 1))
#    suma += pocz_cyfra
#    x -= pocz_cyfra * (10 ** (cyfry - 1))
#    cyfry -= 1
#print(f"suma cyfr tej liczby = {suma}")

#ALBO

#n = int(input())
#suma = 0
#while n>0:
#    suma += n % 10
#    n = n // 10
#print(suma)

# zad 2
#n = int(input())
#czy_p = True
#if n == 1:
#    czy_p = False
#    print("nie jest pierwsza")
#for i in range(2, int(n ** 0.5) + 1):
#    if n % i == 0:
#        print("nie jest pierwsza")
#        czy_p = False
#        exit()
#if czy_p:
#    print("Jest pierwsza")

# zad 3
#a = int(input())
#suma = 0
#for i in range(1, a // 2 + 1):
#    if a % i == 0:
#        suma += i
#if suma == a:
#    print("Liczba doskonala")
#else:
#    print("Liczba niedoskonala")

# OR THIS

#def is_perfect(number):
#    sum = 0
#    for i in range(1, number):
#        if number % i == 0:
#            sum += i
#    return sum == number
#a = int(input())
#if is_perfect(a):
#    print("liczba doskonala")
#else:
#    print("Liczba niedoskonala")

# zad 4
#a, b = map(int, input().split())
#while b > 0:
#    a, b = b, a % b
#if a == 1:
#    print("liczby wzglednie pierwsze")
#else:
#    print("liczby nie sa wzglednie pierwsze")

# zad 5
#m = int(input())
#l = []
#for i in range(10, 20):
#    a = m
#    b = i
#    while b > 0:
#        a, b = b, a % b
#    #albo w ten sposob
#    #while b > 0:
#    #    if a > b:   a -= b
#    #    if b > a:   b -= a
#    if a == 1:
#        l.append(i)
#print(l)

# zad 6
#a, b = map(int, input().split('/'))
#c = a
#d = b
#while d > 0:
#    c, d = d, c % d
#if c != 1:
#    print(f"{a}/{b} = {int(a/c)}/{int(b/c)}")

# zad 7
#a, b = map(int, input().split('/'))
#a1 = a
#czynnik = a1 // b
#a1 -= czynnik * b
#c = a1
#d = b
#while d > 0:
#    c, d = d, c % d
#if c != 1:
#    print(f"{a}/{b} = {czynnik}*({int(a1/c)}/{int(b/c)})")

# zad 8
#suma = 0
#def dzielniki(n):
#    suma = 0
#    for i in range(1, n):
#        if n % i == 0:
#            suma += i
#    return suma
#for i in range(1, 10001):
#    for j in range(1, 10001):
#        if dzielniki(i) == j and dzielniki(j) == i and i != j:
#            print(f"{i} i {j}")

# ZROBIONE, ALE POTRZEBUJE ULEPSZEN
# KOD JEST ZA CIEZKI DLA KONSOLI

# zad 9
#def czy_pierwsza(x):
#    czy_p = True
#    for i in range(2, int(x ** 0.5) + 1):
#        if x % i == 0:
#            czy_p = False
#    if czy_p:
#        return True
#    else:
#        return False

#def czy_prawp(a):
#    lista = []
#    czy_pp = False
#    for k in range(2, a // 2 + 1):
#        if a % k == 0 and czy_pierwsza(k):
#            lista.append(k)
#    for j in range(len(lista)):
#        for h in range(len(lista)):
#            if lista[j] * lista[h] == a:
#                czy_pp = True
#    if czy_pp:
#        return True
#    else:
#        return False

#res = []
#for d in range(10, 100):
#    if czy_prawp(d):
#        res.append(d)
#print(res)

# zad 10
#def czy_pierwsza(x):
#    czy_p = True
#    for i in range(2, int(x ** 0.5) + 1):
#        if x % i == 0:
#            czy_p = False
#    if czy_p:
#        return True
#    else:
#        return False
#n = int(input())
#if czy_pierwsza(n):
#    if czy_pierwsza(n - 2):
#        print(f"{n - 2} i {n}")
#    elif czy_pierwsza(n + 2):
#        print(f"{n} i {n + 2}")
#    else:
#        print("liczba nie ma blizniaka")
#else:
#    print("To nie jest liczba pierwsza")
