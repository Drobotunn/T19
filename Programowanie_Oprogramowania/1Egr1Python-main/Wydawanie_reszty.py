# ALGORYTM WYDAWANIA RESZTY
N = [500, 200, 100, 50, 20, 10, 5, 2, 1]
kwota = int(input())
while kwota > 0:
    for nominal in N:
        ilosc = kwota // nominal
        kwota -= nominal * ilosc
        if ilosc > 0:
            print(f"{nominal} -- {ilosc}")
            print()

# FUNKCJA WYDAJACA RESZTE
def reszta(kwota):
    N = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    reszta = []
    for nominal in N:
        while kwota > nominal:
            kwota -= nominal
            reszta.append(nominal)
    return reszta

# FUNKCJA WYPISUJACA NOMINALY Z ILOSCIA
def reszta_il(kwota):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    reszta = []
    while kwota > 0:
        for nominal in nominaly:
            ilosc = kwota // nominal
            if ilosc > 0:
                kwota -= nominal * ilosc
                reszta.append(f"{nominal} -- {ilosc}")
    return reszta
