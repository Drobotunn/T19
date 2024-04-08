# Zadanie 1
slowo = input("Podaj slowo: ")
for i in range(len(slowo) + 1):
    print(slowo[:i])

print("\n")

# Zadanie 2
napis = input()
k = 0
for i in range(len(napis) - 1):
    if napis[i] == napis[i + 1]:
        k += 1
print(f"Ilosc sytuacji, kiedy wystepuja kolo siebie dwie takie same literki: {k}")

# Zadanie 3(1)
wyraz = input()
print(len(set(wyraz)))

# Zadanie 4(2)
slowo2 = input()
wynik = ""
print("\n")
for i in range(len(slowo2) // 2):
    wynik += slowo2[i] + slowo2[-i - 1]
if len(slowo2) % 2:
    wynik += slowo2[len(slowo2)//2]
print(wynik)
