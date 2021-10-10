"""
@author: Sebastian Bednarski
wzorowane na kodzie z zajęć
"""
def wzor_Herona(a,b,c): #a, b, c odpowiada tu kolejnymi długościami boków
    """Funkcja oblicza pole trójkąta, wykorzystując wzór Herona.
    Args:
        a, b, c (float): długości boków #podane przykłady są jako typ int, lecz można je bez problemu zmienić na typ zmiennoprzecinkowy dodając do liczb '.x'
    Returns:
        float: pole trójkąta, jeśli podano poprawne długości boków,
        None: w przeciwnym przypadku
    """
    boki = [a, b, c] #lepiej zapisać a, b, c niż boki[0], przydatne do argumentow funkcji

    if not (max(boki) < (sum(boki) - max(boki))): #krótszy warunek spełnienia można też jak w 1a a+b>c and...
        return None

    o_pol = (a+b+c)/2 #p we wzorze Herona
    iloczyn = o_pol

    for i in range(len(boki)):
        iloczyn *= o_pol - boki[i]

    pole = iloczyn ** 0.5
    return pole

def test_wzor_Herona():
    """Funkcja testująca funkcje wzor_Herona(a,b,c)"""
    pole = wzor_Herona(3,4,5)
    assert pole == 6, 'Nieprawidlowe pole' #jeśli nieprawdziwa wartosc wyswietla AssertionError - napis 'Nieprawidlowe pole' i program sie zatrzyma
    print('Pole trojkata wynosi ' + str(pole))

    pole = wzor_Herona(3,4,10)
    assert pole is None, 'Nie sprawdzono warunku na istnienie trojkata' #jesli nieprawdziwa wartosc wyswietli napis nie sprawdzono warunku i program sie zatrzyma
    print('Nie istnieje trojkat o bokach 3, 4 i 10 ')

test_wzor_Herona()

"""Sprawdzenie poprawności funkcji wzor_Herona(a, b, c) bez tworzenia funkcji testującej"""
#pole = wzor_Herona(3,4,5)
#print('Pole trojkata wynosi: ' + str(pole))
#pole2 = wzor_Herona(3,4,10)
#print('Pole trojkata wynosi: ' + str(pole2))
 