#   RSA
from math import gcd    # gcd -- NWD dwuch liczb
print(gcd(20, 15))      # wyjscie : 5

# 1. Wybor duzych liczb pierwszych
p = 11
q = 13
print(p,q)

# 2. Obliczyc n = p * q oraz funkcje Eulera F = (p - 1)(q - 1)
n = p * q
F = (p - 1)* (q - 1)
print(n)
print(F)

# 3. Generowanie klucza publicznego e : NWD(F, e) = 1
for i in range(2, F):
    if gcd(i,F) == 1:
        e = i
        break
print(e, n)

# 4. Generowanie klucza prywatnego d: (e * d) % F = 1 (tzw. odrwotnosc modulo)
for j in range(2, F):
    if e * j % F == 1:
        d = j
        break
print(d, n)


# Przyklad dzialania
# m - message (wiadomosc dla zaszyfrowania)
# c = m ** e % n (cipher - szyfrogram - tekst szyfrogramy)
# t = c ** d % n (tekst jawny, czyli wiadomosc n)

m = input()
cipher = ""
for i in m:
    cipher += chr((ord(i) ** e) % n)
print(cipher)

tekst = ""
for j in cipher:
    tekst += chr((ord(j) ** d) % n)
print(tekst)
