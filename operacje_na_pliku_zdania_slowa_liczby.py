
'''
@author: Sebastian Bednarski
'''


with open('tekst.txt') as file:
    for line in file:
        print(line)


def statystyka(filepath):

    """ Funkcja przyjmująca ścieżkę pliku i zwracająca liczbę zdań, slow, znakow w tekscie z pliku
    Args:
        filepath: ścieżka dostepu do pliku 
    Returns:
        list: [0]ilość zdań w pliku, [1]ilosc slow w pliku, [2]ilosc znakow w pliku
    """
    lista = list()
    counter = 0
    file = open(filepath)
    tekst = file.read()
    slowa_bez_spacji = tekst.split()
    #zdania
    for zdania in tekst:
        if zdania.endswith("."):
            counter+=1
        if zdania.endswith("?"):
            counter+=1
        if zdania.endswith("!"):
            counter+=1
    lista.append('Liczenie zdan: ' +str(counter))
    
    #slowa
    licz_slowa= len(slowa_bez_spacji)
    lista.append('Liczenie slow: ' +str(licz_slowa))

    #znaki
    """
    for zdania in tekst:
        for char in zdania:
            if char != 0:
                counter+=1
    lista.append(counter)
    """
    licz_znaki= len(tekst)
    lista.append('Liczenie znakow: ' + str(licz_znaki))
    return(lista)
    

print(statystyka('tekst.txt'))
