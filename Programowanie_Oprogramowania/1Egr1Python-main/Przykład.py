 ZnajdzDup(napis):
    duplikaty = []
    maxNap = 0
    for i in napis:
        spr = napis.count(i)
        if spr > 1 and i not in duplikaty:
            duplikaty.append(True)
        else:
            duplikaty.append(False)
    return duplikaty

napis = input()
napis = list(napis)
dupl = ZnajdzDup(napis)
out = []
for i in dupl:
    if dupl[i] == True:
        for j in range (i + 1, len(dupl)):
            if dupl[j] == True
