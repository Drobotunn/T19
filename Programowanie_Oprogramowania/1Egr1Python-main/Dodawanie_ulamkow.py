a1, b1 = map(int, input().split("/"))
a2, b2 = map(int, input().split("/"))
a = a1
b = a2
c = b1
d = b2
if b1 != b2:
    iloczyn = b1 * b2
    while b2 > 0:
        b1, b2 = b2, b1 % b2
    nww = (iloczyn / b1)
a1 = a1 * (nww / c)
a2 = a2 * (nww / d)
p = a1 + a2
print(f"{a}/{c} + {b}/{d} = {round(a1)}/{round(nww)} + {round(a2)}/{round(nww)} = {round(p)}/{round(nww)}")
