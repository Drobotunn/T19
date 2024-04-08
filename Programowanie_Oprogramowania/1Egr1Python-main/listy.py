L = [4, 7, 7, 3, 2, 4, 1, 4, 6, 8]
print(L)
print(len(L))       #dlugosc listy
print(L[1])
print(L[8])

print("\n")

print(L[1:6:2])
print(L[::3])       #co 3
print(L[::-3])      #co 3 odwrotnie
print(L[2:7:-2])    #nie dziala

print("\n")

for i in range(len(L)):
    print(L[i], end=" ")
print("\n")

for elem in L:
    print(elem, end=" ")
print("\n")
