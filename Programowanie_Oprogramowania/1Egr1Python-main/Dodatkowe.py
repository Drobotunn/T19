def czy_pierwsza(x):
    czy_p = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            czy_p = False
    if czy_p:
        return True
    else:
        return False
x = int(input())
czy = False
for j in range(2, x // 2 + 1):
    if czy_pierwsza(j) and czy_pierwsza(x - j):
        czy = True
        print(j, x - j)
if czy:
    print("Tak")
else:
    print("Nie")
