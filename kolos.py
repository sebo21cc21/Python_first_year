class Stos:
    pass

class Element:
    pass

def utworz_stos():
    stos = Stos()
    stos.wierzch = None
    return stos

def na_stos(stos, napis):
    elem = Element()
    elem.wartosc = napis
    elem.poprzedni = stos.wierzch
    stos.wierzch = elem

def ze_stosu(stos):
    if stos.wierzch is None:
        return None
    elem = stos.wierzch
    stos.wierzch = elem.poprzedni
    return elem.wartosc

mój_stos = utworz_stos()
na_stos(mój_stos, 6)
na_stos(mój_stos, 7)
print(ze_stosu(mój_stos))
na_stos(mój_stos, 8)
na_stos(mój_stos, 8)
print(ze_stosu(mój_stos))
print(ze_stosu(mój_stos))
print(ze_stosu(mój_stos))

