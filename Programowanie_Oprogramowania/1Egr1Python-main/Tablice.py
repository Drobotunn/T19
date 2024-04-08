#Wygeneruj tablice n losowych liczb:
from random import randint
L = [randint(1,20) for i in range(20)]
print(f"{L}")
print(f"Max value: {max(L)}")
print(f"Min value: {min(L)}")
print(f"Ilosc Maksow: {L.count(max(L))}")
print(f"Ilosc Minow: {L.count(min(L))}")
print(f"Rozpientosc: {max(L) - min(L)}")
print(f"Suma elementow: {sum(L)}")
print(f"Srednia: {round(sum(L)/len(L), 1)}")
x = 0
for i in range(len(L)):
    if L[i] % 2 == 0:
        x += 1
    else:
        x -= 1
if x > 0:
    print("Wiecej parzystych")
elif x == 0:
    print("Rowna ilosc parzystych i nieparzystych")
else:
    print("Wiecej nieparzystych")


for i in range(L.count(max(L))):
    L.pop(L.index(max(L)))
print(F"V-ce Maks: {max(L)}")

# ALBO W TEN SPOSOB
#print(L)
#print(list(set(L)))
#S = list(set(L))
#print(S[len(S) - 2])
