#Ankieta
# p = int(input())
# q = int(input())
# if q > 1.3*p:
#     print("TAK")
# else:
#     print("NIE")

# for i in range(10,22):
#     print(i, end=" ")
#
# for i in range(15,31,2):
#     print(i, end=" ")
#
# for i in range(99, 9, -1):
#     print(i, end=" ")
#
# for i in range(10,100):
#     print(109-i, end=" ")
#
# for i in range(100,1000,20):
#         print(i)

#zad 4
# s = 0
# for i in range(10,99):
#     s = s+i
# print(s)

#zad 5
# n = int(input("Podaj ilość liczb: "))
# s = n*(n+1)/2
# for i in range(n-1):
#     x = int(input())
#     s = s - x
# print(s)

#zad 6
# n = int(input())
# a=1
# b=2
# print(a, b, end=" ")
# for i in range(n-2):
#     a,b=b, a+b
#     print(b, end=" ")

#zad 7 silnia iteracyjna
n = int(input())
silnia = 1
for i in range(1,n+1):
    silnia = silnia * i
print(silnia)
