# 1. Algorytm sprawdzajacy czy liczba jest pierwsza
# liczba pierwsza dzieli sie tylko przez 1 i sama siebie
# 2, 3, 5, 7, 11, 13, 17, 19 itd...
# liczba x ma swoj dzielnik (o ile go ma) w przedziale [2, sqrt(x)]
# dzielnik wlasciwy - dzielnik liczby oprocz 1 i niej samej

#n = int(input())
#for i in range(2,int(n**0.5)+1):
#    if n % i == 0:
#        print("liczba nie jest pierwsza")
#        exit(0)
#print("liczba jest pierwsza")


# 2. Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]

# [10, 15] - 11 i 13
# [20, 22] - brak liczb pierwszych

#l = "angole to wory".split()
#print(l)
#l = list(map(int, "880-055-535-35".split("-")))
#print(l)

#p, q = map(int, input().split())
#for i in range(p,q+1):
#    flaga = True
#    for j in range(2,int(i**0.5)+1):
#        if i%j==0:
#            flaga = False
#            break
#    if flaga:
#        print(i, end=" ")

#3 Generator liczb pierwszych - poczatkowe k liczb pierwszych

#n = int(input())
#x = 2
#while 1:
#    flaga = True
#    for i in range(2, x):
#        if x % i == 0:
#            flaga = False
#            break

#    if flaga:
#        print(x, end=" ")
#        n = n - 1
#        if n == 0:
#            break
#    x += 1

# inny sposob (zmiana w 'while' i brak ostatniego 'if')
#n = int(input())
#x = 2
#while n > 0:
#    flaga = True
#    for i in range(2, x):
#        if x % i == 0:
#            flaga = False
#            break

#    if flaga:
#        print(x, end=" ")
#        n = n - 1
#    x += 1

# NWD liczb (Najwiekszy wspolny dzielnik)
#a, b = map(int, input().split())
#while a != b:
#    if a > b:
#        a -= b
#    if b > a:
#        b -= a
#print(a)

# Modulo %
#a, b = map(int, input().split())
#while b != 0:
#    print(f"{a}\t\t{b}\t\t{a%b}")
#    a, b = b, a % b
#print(a)

# NWW - Najmniejsza Wspolna Wielokrotnosc
#a, b = map(int, input().split())
#iloczyn = a * b
#while a != b:
#    if a > b:
#        a -= b
#    if b > a:
#        b -= a
#print("NWD: ", a)
#nww = iloczyn // a
#print("NWW:", nww)

a, b = map(int, input().split())
iloczyn = a * b
while b > 0:
    a, b = b, a % b
print("NWD: ", a)
print("NWW: ", iloczyn // a)
