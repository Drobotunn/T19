W = "TTTEEEECCCCCHHNIIKK"
# 3T4E5C2HN2I2K
print(W)
print(W[12])

ilosc = 1
H = ""
W += "."
for i in range(len(W) - 1):
    if W[i] == W[i+1]:
        ilosc += 1
    else:
        if ilosc > 1:
            H += str(ilosc)
        H += W[i]
        ilosc = 1
print(H)

# Huffman odwrotnie
huff = input()
msg = ""
for i in range(0, len(huff), 2):
    msg += int(huff[i]) * huff[i + 1]
print(msg)
