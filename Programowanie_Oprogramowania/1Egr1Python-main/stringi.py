# stringi
s = input()
L = list(s)     # list() - przetwarza slowo w liste
print(s, L)
L.sort()
print(s, L)
s = "-".join(L) # slkeje elementy listy w jeden wyraz
print(s, L)

# sprawdz czy podane slowo jest palindromem

slowo = input()
L = list(slowo)
R = list(slowo)
R.reverse()
if L == R:
    print("pallindrom")
else:
    print("nie jest")
    
    
    
#palindrom za pomoca tablicy

#sl = input()
#for i in range(len(sl) // 2):
#    if sl[i] != sl[len(sl) - i - 1]:
#        exit("NIE")
#exit("TAK")



# ANAGRAMY
# np adam dama
# burza arbuz
a, b = input(), input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
a = "".join(X)
b = "".join(Y)
if a == b:
    print("TAK")
else:
    print("NIE")




# ANAGRAM przez tablice
a, b = input(), input()
X, Y = [0] * 150, [0] * 150
#print(X)
for i in range(len(a)):
    X[ord(a[i])] += 1;
#print(X)
for i in range(len(a)):
    Y[ord(b[i])] += 1;
if X == Y:
    print("TAK")
else:
    print("NIE")
    
# ONP - Odwrotna Notacja Polska
# Obliczanie wartosci wyrarzenia ONP
# 45 + 28 * +


x = input()
wynik = ""
for literka in x:
    if x.count(literka) == 1:
        wynik += literka
print(wynik)
