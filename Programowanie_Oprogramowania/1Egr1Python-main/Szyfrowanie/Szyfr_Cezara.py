# Szyfr Cezara

# Funkcja ord() - zwraca kod ASCII podasnego znaku
#print(ord("A"))
#print(ord("Z"))

# Funkcja chr() - zwraca znak dla podanego kodu ASCII
#print(chr(65))
#print(chr(77))

# Polanczenie w calosc:
#print(chr(ord("C")+2))

# Alfabet A - Z za pomoca FOR:
for i in range(65, 91):
    print(chr(i), end=" ")
print()

# Jak z napisu wyluskac litery
#napis = "POLSKA"
#print(len(napis))
#print(napis[1])

# Wypisz litery napisu w petli:
#napis = input()
#for i in range(len(napis)):
#    print(napis[i], end=" ")

# Wypisz kody ASCII liter
#napis = input()
#for i in range(len(napis)):
#    print(ord(napis[i]), end=" ")

# SZYFR CEZARA prosty
napis = input()
for i in range(len(napis)):
    print(chr(ord(napis[i]) + 3), end=" ")

# ZLOZONY
napis = input()
szyfr = ""
for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)

#updated
msg = input()
szyfr = ""
for i in range(len(msg)):
    if msg[i] == " ":
        szyfr += " "
    else:
        szyfr += chr(65 + (ord(msg[i]) - 65 + 4) % 26)
print(szyfr)
