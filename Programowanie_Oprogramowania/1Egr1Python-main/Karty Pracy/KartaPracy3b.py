## zad 1
#for i in range(30):
#    print(i+1, end=" ")

## zad 2
#for i in range(10):
#    if i%2==1:
#        print(i**2, end=" ")

## zad 3
#for i in range(1000, 10000):
#    if i%379==0:
#        print(i, end=" ")

## zad 4
#for i in range(100, 1000):
#    if i%5==0 and i%6==0 or i%11==0:
#        print(i)

## zad 5
#n = int(input("Ile liczb:"))
#suma = 0
#for i in range(n):
#    suma = suma + int(input())
#print("Suma:",suma)

## zad 6
#k = int(input("Ilosc liczb:"))
#suma = 0
#for i in range(1, k*2+1):
#    if i%2==0:
#        suma += i
#print("Suma:",suma)

## zad 7
#m = int(input("Ilosc liczb: "))
#suma = 0
#for i in range(11, (m*2)+11, 2):
#    if i<100:
#      suma += i
#print("Suma:", suma)

## zad 8
#w0 = int(input("Podaj kwote wejsciowa:"))
#l = int(input("Ilosc lat:"))
#kap = 0
#wartosc = w0
#for i in range(1, l+1):
#    kap = wartosc * 0.06
#    wartosc = wartosc + kap
#print("Wartosc:", round(wartosc, 2))

## zad 9
#n = int(input("Ilosc liczb: "))
#temp = 0
#suma = 0
#for i in range(n):
#    temp = i*100+21
#    suma += temp
#print("Suma:", suma)

# zad 10
for i in range(1,1001):
    if i%10==(i**0.5) or i%100==(i**0.5):
        print(i, end=" ")
