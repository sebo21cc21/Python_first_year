"""
@author: Sebastian Bednarski
"""
from struktury_dynamiczne import stos, lista2

moj_stos = stos.utworz_stos()
stos.na_stos(moj_stos, "Edek")
stos.na_stos(moj_stos, "ma")
stos.na_stos(moj_stos, "kota")
stos.ze_stosu(moj_stos)
stos.na_stos(moj_stos, "psa")
x = ""
while moj_stos.wierzch is not None:
    x = x + stos.ze_stosu(moj_stos) + " "
print(x)

moja_lista = lista2.utworz_liste()
lista2.dopisz(moja_lista, "Edek")
lista2.dopisz(moja_lista, "ma")
lista2.dopisz(moja_lista, "kota")
lista2.usun(moja_lista, 2)
lista2.dopisz(moja_lista, "psa")
x = ""
while moja_lista.poczatek is not None:
    x = x + moja_lista.poczatek.wartosc + ' '
    moja_lista.poczatek = moja_lista.poczatek.nastepny
print(x)
