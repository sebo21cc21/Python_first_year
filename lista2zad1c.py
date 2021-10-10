"""
@author: Sebastian Bednarski
"""
x = 1 #element na sztywno wprowadzony
tab = [1,1,3,1,5,6] #tablica elementow na sztywno
licznik = 0
pozycja = 0
for pozycja in range(len(tab)): #sprawdzamy po petli wystapienia elementu
    if tab[pozycja] == x: #jesli element w tablicy na konkretnej pozycji jest rowny szukanemu elementowi
        licznik += 1 #zwiekszamy licznik wystapien o 1
print('Licznik ilości powtorzen elementu wyniesie: ' + str(licznik))