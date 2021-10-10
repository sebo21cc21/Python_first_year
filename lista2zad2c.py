"""
@author: Sebastian Bednarski
"""
def liczenie_elementow(tab, x):
    """ Funckja do liczenia wystapien elementow w tablicy
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty
        x (float): sprawdzany element

    Returns: 
        int: ilosc powtorzen elementu x w tablicy tab  #tu jest typu int, gdyż nie będzie powtarzalo sie coś 0.5 raza
    """

    licznik = 0
    for pozycja in range(len(tab)): #sprawdzamy po petli wystapienia elementu
        if tab[pozycja] == x: #jesli element w tablicy na konkretnej pozycji jest rowny szukanemu elementowi
            licznik += 1 #zwiekszamy licznik wystapien o 1
    return licznik

def test_liczenie_elementow():
    """Funkcja testująca dla funkcji liczenie_elementow(tab, x)"""
    licznik = liczenie_elementow([1],1)
    assert licznik == 1, 'Bledna funkcja wyliczania powtarzalnych elementow' #jesli program sie zatrzyma i wystapi AssertionError wystapil blad w funkcji wyliczania
    print('Element x wystapi w tablicy tab : ' + str(licznik))

    licznik = liczenie_elementow([1,2],1)
    assert licznik == 1, 'Bledna funkcja wyliczania powtarzalnych elementow' #jesli program sie zatrzyma i wystapi AssertionError wystapil blad w funkcji wyliczania
    print('Element x wystapi w tablicy tab : ' + str(licznik))

    licznik = liczenie_elementow([1,2,3],1)
    assert licznik == 1, 'Bledna funkcja wyliczania powtarzalnych elementow' #jesli program sie zatrzyma i wystapi AssertionError wystapil blad w funkcji wyliczania
    print('Element x wystapi w tablicy tab : ' + str(licznik))
    
    licznik = liczenie_elementow([1,1,1,1],1)
    assert licznik == 4, 'Bledna funkcja wyliczania powtarzalnych elementow' #jesli program sie zatrzyma i wystapi AssertionError wystapil blad w funkcji wyliczania
    print('Element x wystapi w tablicy tab : ' + str(licznik))

    licznik = liczenie_elementow([1.5,-1,3,1],1.5)
    assert licznik == 1, 'Bledna funkcja wyliczania powtarzalnych elementow' #jesli program sie zatrzyma i wystapi AssertionError wystapil blad w funkcji wyliczania
    print('Element x wystapi w tablicy tab : ' + str(licznik))

test_liczenie_elementow()