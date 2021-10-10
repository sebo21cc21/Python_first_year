"""
@author: Sebastian Bednarski
"""
class Element:
    pass
class Lista:
    pass
def utworz_liste():
    """
    Funkcja tworzaca obiekt klasy Lista, tworzy liste

    Args:
        None
    Returns:
        Lista: utworzona lista
    """
    lista = Lista()
    lista.poczatek = None
    #lista.koniec = None
    return lista

def dopisz(lista, napis):
    """
    Funkcja tworzaca obiekt klasy Element, dopisuje na koncu listy podany napis
    
    Args:
        lista(object): utworzona lista
        napis(string): wejsciowy element wprowadzony do listy
    Returns:
        None #nastepuje dopisanie wartosci do Listy
    """
    elem = Element()
    elem.wartosc = napis
    elem.nastepny = None
    koniec = lista.poczatek
    if lista.poczatek is None:
        lista.poczatek = elem
    else:
        while koniec.nastepny is not None:
            koniec = koniec.nastepny
        koniec.nastepny = elem
        
        #lista.koniec.nastepny = elem
    #lista.koniec = elem

def nastepny_iteracja(elem, ile):
    """
    Funkcja iteracyjna umozliwiajaca odwolanie sie do wybranego elementu listy
    
    Args:
        elem(object): wprowadzony element od ktorego zaczynamy przesuwanie
        ile(int): o jaka roznice indexow elementu szukanego i wprowadzonego przesuwamy sie po liscie
    Returns:
        object: zwraca szukany element 
    """
    assert elem is not None and ile >= 0, "Niewłaściwy indeks."
    i = 0
    if ile == 0:
        return elem
    else:
        while i < ile:
            elem = elem.nastepny
            i += 1
    return elem

def nastepny(elem, ile):
    """
    Funkcja rekurencyjna umozliwiajaca do odwolania sie do wybranego elementu listy
    
    Args:
        elem(object): wprowadzony element od ktorego zaczynamy przesuwanie
        ile(int): o jaka roznice indexow elementu szukanego i wprowadzonego przesuwamy sie po liscie
    Returns:
        object: zwraca szukany element 
    """
    assert elem is not None and ile >= 0, "Niewłaściwy indeks."
    if (ile == 0):
        return elem
    return nastepny(elem.nastepny, ile - 1)

def zwroc(lista, ktory):
    """
    Funkcja, która zwraca wartość elementu

        Args:
            lista(object): lista elementow
            ktory(int): indeks szukanego elementu listy
        Returns:
            Any: zwraca zawartość elementu 

    """ 
    elem = nastepny_iteracja(lista.poczatek, ktory)
    return elem.wartosc

def zmien(lista, ktory, napis):
    """Funkcja zamieniająca elementy listy

        Args:
            lista(object): lista elementów do możliwej podmiany
            ktory(int): indeks elemntu, ktory podmieniamy
            napis(string): nadpisana wartosc elementu
        Returns:
            None #zmienia elementy, nie zwraca nic
    """
    elem = nastepny(lista.poczatek, ktory)
    elem.wartosc = napis

def wstaw(lista, ktory, napis):
    """Funkcja tworzaca obiekt o klasie Element, wstawiająca napis do listy

        Args:
            lista(object): podana lista elementów
            ktory(int): indeks elemntu- w jakie miejsce wstawiamy
            napis(string): element ktory wstawiamy
        Returns:
            None #wstawia element, nie zwraca nic        
    """
    elem = Element()
    elem.wartosc = napis
    if ktory == 0:
        elem.nastepny = lista.poczatek
        lista.poczatek = elem
    #if lista.koniec is None:
        #lista.koniec = elem
    else:
        elem_poprz = nastepny(lista.poczatek, ktory - 1)
        elem.nastepny = elem_poprz.nastepny
        elem_poprz.nastepny = elem

def usun(lista, ktory):
    """Funkcja usuwajaca element z listy

        Args:
            lista(object): podana lista elementów
            ktory(int): indeks elemntu, ktory usuwamy
        Returns:
            None #usuwa element, nie zwraca nic        
    """    
    if ktory == 0 and lista.poczatek is not None:
        lista.poczatek = lista.poczatek.nastepny
    #if lista.poczatek is None:
        #lista.koniec = None
    else:
        elem_poprz = nastepny(lista.poczatek, ktory - 1)
        elem_poprz.nastepny = elem_poprz.nastepny.nastepny
    #if elem_poprz.nastepny is None:
        #lista.koniec = elem_poprz

def dlugosc(lista):
    """
    Funkcja zwracajaca dlugosc listy jednokierunkowej

    Args:
        lista(object): podana lista do sprawdzenia dlugosci
    Returns:
        int: dlugosc listy
    """
    elem = lista.poczatek
    counter = 0
    while elem is not None:
        counter += 1
        elem = elem.nastepny
    return counter

def znajdz(lista, elem):
    """Funkcja zwracająca na ktorym miejscu w liscie wystepuje podany element
        Ars:
            lista(object): lista elementów do przeszukania
            elem(object): element szukany w liscie
        Returns:
            int: numer indeksu szukanego szczescia
            None: w przeciwynim przypadku - brak elementu w tablicy
    """
    pozycja = 0
    x = lista.poczatek
    while x is not None:
        if x.wartosc == elem:
            return pozycja
        elif x.wartosc != elem: 
            x = x.nastepny
            pozycja += 1
    return None

def test_lista1():
    """
    Funkcja testujaca funkcje utworz_liste(), dopisz(lista, napis), nastepny_iteracja(elem, ile), zwroc(lista, ktory), 
    zmien(lista, ktory, napis), wstaw(lista, ktory, napis), usun(lista, ktory) - lista jako miniprogram :)
    """
    moja_lista = utworz_liste()
    dopisz(moja_lista, "Ala") #trzy testy funkcji dopisz(lista,napis)
    dopisz(moja_lista, "ma")
    dopisz(moja_lista, "kota.")
    elem = moja_lista.poczatek
    x = ''
    while elem is not None:
        x = x + elem.wartosc + ' '
        elem = elem.nastepny
    assert x == 'Ala ma kota. ', 'Bledna funkcja'
    print(x, 'Poprawne dopisywanie elementow')


    x = zwroc(moja_lista, 0) #jesli dziala dobrze zwroc, to funkcja nastepny_iteracja(elem, ile) tez musi! Dwa testy w jednym :)
    assert x == "Ala", 'Bledna funkcja'
    print(x, 'poprawny zwrot elementu')
    x = zwroc(moja_lista, 1)
    assert x == "ma", 'Bledna funkcja'
    print(x, 'poprawny zwrot elementu')
    x = zwroc(moja_lista, 2)
    assert x == "kota.", 'Bledna funkcja'
    print(x, 'poprawny zwrot elementu')


    zmien(moja_lista, 0, "Bella")
    zmien(moja_lista, 0, "Gryzelda")
    zmien(moja_lista, 0, "Ela")
    elem = moja_lista.poczatek
    x = ''
    while elem is not None:
        x = x + elem.wartosc + ' '
        elem = elem.nastepny
    assert x == 'Ela ma kota. ', 'Bledna funkcja'
    print(x, 'Poprawna zamiana elementow')


    usun(moja_lista, 1) #usuwanie elementu 1 test
    elem = moja_lista.poczatek
    x = ''
    while elem is not None:
        x = x + elem.wartosc + ' '
        elem = elem.nastepny
    assert x == 'Ela kota. ', 'Bledna funkcja'
    print(x, 'Poprawne usuniecie elementu o numerze indeksu 1')

    wstaw(moja_lista, 1, "goni") #wstawianie elemntu 1 test
    elem = moja_lista.poczatek
    x = ''
    while elem is not None:
        x = x + elem.wartosc + ' '
        elem = elem.nastepny
    assert x == 'Ela goni kota. ', 'Bledna funkcja'
    print(x, 'Poprawne wstawienie elementu o numerze indeksu 1')   
    
    usun(moja_lista, 2) #miniprogram ciag dalszy test 2,3 funkcji wstaw(lista, ktory, napis), usun(lista, ktory)
    wstaw(moja_lista, 2, "psa.")
    wstaw(moja_lista, 0, "Kaczka")
    elem = moja_lista.poczatek
    x = ''
    while elem is not None:
        x = x + elem.wartosc + ' '
        elem = elem.nastepny
    assert x == 'Kaczka Ela goni psa. ', 'Bledna funkcja'
    print(x, 'Poprawne dzialanie funkcji wstaw i usun')

def test_dlugosc():
    """ Funkcja testujaca funkcje dlugosc(lista) """
    moja_lista = utworz_liste()

    dopisz(moja_lista, "Ala")
    x = dlugosc(moja_lista)
    assert x == 1, 'Bledna funkcja, sprawdz poprawnosc zapisu funkcji dlugosc(lista)'
    print('Dlugosc wprowadzonej listy jednokierunkowej wynosi:', x)

    dopisz(moja_lista, "ma")
    x = dlugosc(moja_lista)
    assert x == 2, 'Bledna funkcja, sprawdz poprawnosc zapisu funkcji dlugosc(lista)'
    print('Dlugosc wprowadzonej listy jednokierunkowej wynosi:', x)

    dopisz(moja_lista, "kota.")
    x = dlugosc(moja_lista)
    assert x == 3, 'Bledna funkcja, sprawdz poprawnosc zapisu funkcji dlugosc(lista)'
    print('Dlugosc wprowadzonej listy jednokierunkowej wynosi:', x)

def test_znajdz():
    """Funkcja testujaca funkcje znajdz(lista, elem)"""
    moja_lista = utworz_liste()
    for i in range(10):
        dopisz(moja_lista, i)

    x = znajdz(moja_lista, 4)
    assert x == 4, 'Bledna funkcja znajdywania'
    print('Znaleziony element jest na', x, 'indeksie')

    x = znajdz(moja_lista, 9)
    assert x == 9, 'Bledna funkcja znajdywania'
    print('Znaleziony element jest na', x, 'indeksie')

    x = znajdz(moja_lista, 10)
    assert x == None, 'Bledna funkcja znajdywania'
    print('Znaleziony element poza tablica, wartosc', x)

if __name__ == "__main__":
    test_lista1()
    test_dlugosc()
    test_znajdz()