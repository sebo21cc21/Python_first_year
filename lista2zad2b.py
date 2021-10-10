"""
@author: Sebastian Bednarski
"""
def algorytm_odcinki(Ap, Ak, Bp, Bk):
    """ Funkcja do wyliczenia części wspólnej dwóch odcinków o początkach Ap, Bp oraz końcach Ak, Bk
    Args:
        Ap, Ak (float): punkty pierwszego odcinka, czyli A 
        Bp, Bk (float): punkty drugiego odcinka, czyli B
    Returns:
        float: dlugosc czesci wspolnej, jesli podano poprawne dlugosci
        None: w przeciwnym wypadku
    """
    if not (Ap < Ak and Bp < Bk):
        return None
    else:
        if Ap <= Bp and Ak >= Bp:
            if Ak >= Bk:
                C = Bk - Bp 
            else: 
                C = Ak - Bp 
        else: 
            if Ap <= Bk and Ak >= Bk:
                C = Bk - Ap 
            elif Ap > Bp and Ak < Bk:
                C = Ak - Ap
            else:
                C = 0 
    return C

def test_algorytm_odcinki():
    """ Funkcja testująca funkcje algorytm_odcinki(Ap, Ak, Bp, Bk) """
    "a"
    C = algorytm_odcinki(1,5,1,5) #przypisujemy do C dlugosc czesci wspolnej, wyliczonej z funkcji
    assert C == 4, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna wynosi ' + str(C)) # wyswietla napis z wartoscia
    "b"
    C = algorytm_odcinki(2,5,1,5)
    assert C == 3, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna wynosi ' + str(C))
    "c"
    C = algorytm_odcinki(1,5,2,5)
    assert C == 3, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna wynosi ' + str(C))
    "d"
    C = algorytm_odcinki(1,3,2,4)
    assert C == 1, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna wynosi ' + str(C))
    "e"
    C = algorytm_odcinki(1,3,3,4)
    assert C == 0, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna wynosi ' + str(C))
    "f"
    C = algorytm_odcinki(1,2,3,4)
    assert C == 0, 'Nieprawidlowa czesc wspolna' #sprawdza warunek, jeśli niespelniony zatrzymuje program i wyswietla napis
    print('Czesc wspolna nie istnieje') 

test_algorytm_odcinki()