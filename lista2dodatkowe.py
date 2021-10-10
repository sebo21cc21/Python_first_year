"""
@author: Sebastian Bednarski
"""
def Ciag(c0, N):
    """ Funkcja zwracajaca ciag 
    Args:
        c0 (int) pierwszy element tablicy
        N (int) liczba elementow tablicy
    Returns:
        list: zwraca ciag elementow
        None: w przeciwnym przypadku
    """
    if N > 0 and c0 >= 0:
        c = [c0]
        i = 0
        for i in range(N-1):
            if(c[i]%2 == 0): #wartunek parzystosci
                c.append(0.5 * c[i]) #przy spelnieniu kolejny element wynosi
            else:
                c.append(3 * c[i] + 1) #gdy nieparzysty kolejny element wyniesie
        return c
    else:
        return None

def test_Ciag():
    """ Funkcja testujaca funkcje Ciag(c0, N) """
    c = Ciag(8,8)
    assert c == [8, 4.0, 2.0, 1.0, 4.0, 2.0, 1.0, 4.0], 'Blad funkcji- niepoprawna wartosc'
    print('Ciag sklada sie z: ' + str(c)) #w parzystej max wartosc wynosi c[0], dlugosc nieskonczona

    c = Ciag(0,8) #sprawdzenie jesli 0 jest liczba naturalna 
    assert c == [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Blad funkcji- niepoprawna wartosc'
    print('Ciag sklada sie z: ' + str(c))

    c = Ciag(17,14)
    assert c == [17, 52, 26.0, 13.0, 40.0, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0, 4.0], 'Blad funkcji- niepoprawna wartosc'
    print('Ciag sklada sie z: ' + str(c)) #max wartosci to 3*c[0]+1, dlugosc nieskonczona

#w podanych przypadkach na końcu powtarza sie 4,2,1 jeśli traktować 0 jako liczbe naturalna nie występuje przypadek!

test_Ciag()
"""
#Sprawdzenie ciagow
ciag=Ciag(8,8)
print(str(ciag))
"""