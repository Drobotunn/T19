# Palindrom - slowo, ktore sie pisze zwykle i odwrotnie tak samo
slowo = input("Podaj slowo: ")

# Funkcja sprawdza, czy slowo jest palindromem
def palindrom(slowo):
    return slowo == slowo[::-1]

print(palindrom(slowo))

# Alogoritm sprawdzenia, czy slowo jest palindromem
L = list(slowo)
R = list(slowo)
R.reverse()
if L == R:
    print("TAK")
else:
    print("NIE")





# Anagramy - slowa, z liter ktorych moga powstac inne slowa
a, b = input(), input()
A, B = list(a), list(b)
A.sort()
B.sort()
a = "".join(A)
b = "".join(B)
if a == b:
    print("Anagramy")
else:
    print("Nie anagramy")


# Funkcja sprawdzajaca czy anagramy
slowo1, slowo2 = input(), input()
def anagram(slowo1, slowo2):
    return sorted(slowo1) == sorted(slowo2)

print(anagram(slowo1, slowo2))

# Anagramy przez tablice
a, b = input(), input()
A, B = [0] * 150, [0] * 150
print(A)
for i in range(len(a)):
    A[ord(a[i])] += 1
print(A)
for i in range(len(b)):
    B[ord(b[i])] += 1
if A == B:
    print("TAK")
else:
    print("NIE")
