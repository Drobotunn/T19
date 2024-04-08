# ulamki egipskie
from math import ceil, gcd
li, mi = map(int, input().split())
a, b = li, mi
L =  []
while li > 1:
    x = ceil(mi/li)
    L.append(x)
    nww = mi * x // gcd(mi, x)
    
    # li/mi - 1/x
    li *= (nww // mi)
    mi = nww
    y = nww // x
    li -= y
print(f"{a}/{b}", end =" = ")
for x in L:
    print(f"1/{x}", end=" = ")
