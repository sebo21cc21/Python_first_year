"""
@author: Sebastian Bednarski
zrodlo: zajecia/ wyklady
"""
class Stos:
    pass

class Element:
    pass

def utworz_stos():
    """
    Funkcja, ktora tworzy pusty stos, jako obiekt klasy Stos

    Args: 
        None
    Returns:
        Stos: utworzony stos
    """
    stos = Stos()
    stos.wierzch = None
    return stos

def na_stos(stos, napis):
    """
    Funkcja tworząca obiekt klasy Element, ktora kladzie na gore stosu elementy

    Args: 
        stos(Stos): utworzony funkcja utworz_stos() stos
        napis(string): element ktory umiescimy na stosie
    Returns:
        None #funkcja zmienia stosu, a nie zwraca wartosci!
    """ 
    elem = Element()
    elem.wartosc = napis
    elem.poprzedni = stos.wierzch
    stos.wierzch = elem

def ze_stosu(stos):
    """
    Funkcja, ktora zdejmuje z wierzchu stosu elementy 

    Args: 
        stos(Stos): utworzony funkcja utworz_stos() stos
    Returns:
        Any: zwraca zdjety element
    """ 
    if stos.wierzch is None:
        return None
    elem = stos.wierzch
    stos.wierzch = elem.poprzedni
    return elem.wartosc

def test_stos():
    """
    Funkcja, testujaca funkcje utworz_stos(), na_stos(stos, napis), ze_stosu(napis) 
    """ 
    mój_stos = utworz_stos()
    na_stos(mój_stos, 6)
    na_stos(mój_stos, 7)
    x = ze_stosu(mój_stos)
    assert x == 7, 'Bledna funkcja ze_stosu(napis)'
    print('Poprawnie usuniety element ze stosu')
    na_stos(mój_stos, 8)
    x = na_stos(mój_stos, 8)
    assert x == None, 'Bledna funkcja na_stos(stos, napis)'
    print('Poprawnie zmiana stosu- nalozenie elementu na stos')
    ze_stosu(mój_stos)
    ze_stosu(mój_stos)
    ze_stosu(mój_stos)

def test_stos2():
    """
    Funkcja, testujaca funkcje utworz_stos(), na_stos(stos, napis), ze_stosu(napis)- dla stringow
    """ 
    moj_stos = utworz_stos()
    na_stos(moj_stos, ".")
    na_stos(moj_stos, "kota")
    assert moj_stos.wierzch.wartosc == "kota", 'Bledna funkcja na_stos(stos, napis)'
    print('Poprawnie dzialajaca funkcja na_stos(stos, napis)')
    na_stos(moj_stos, "ma")
    na_stos(moj_stos, "Ala")
    x = ""
    while moj_stos.wierzch is not None:
        x = x + ze_stosu(moj_stos) + ' '
    assert x == "Ala ma kota . ", 'Bledna funkcja ze_stosu(napis)'
    print('Poprawnie dzialajaca funkcja ze stringami')

def test_stos3():
    """
    Funkcja, testujaca funkcje utworz_stos(), czy zadziala funkcja ze_stosu(napis) w przypadku braku elementow na stosie
    """ 
    moj_stos = utworz_stos()
    x = ze_stosu(moj_stos)
    assert x == None, 'Bledna funkcja ze_stosu(stos, napis)'
    print('Poprawnie zdjecie elementu, w przypadku braku elementow- funkcja dziala')

if __name__ == "__main__": #tylko gdy odpalamy skrypt stos ma widocznosc
    test_stos()
    test_stos2()
    test_stos3()