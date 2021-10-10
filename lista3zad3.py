"""
@author: Sebastian Bednarski
"""
def zamiana_nic_matrycowa(kod):
   """ Funckja do zamiana sekwencji DNA na nić matrycową
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty

    Returns: 
        list: tablica posortowanych elementów
    """
   for i in range(len(kod)):
      if (kod[i] == 'A'): #sprawdzanie kolejno czy wystepuje dana zasada i zamiana A z T oraz C z G
         kod[i] = 'T'
      elif(kod[i] == 'T'):
         kod[i] = 'A'
      elif(kod[i] == 'G'):
         kod[i] = 'C'
      elif(kod[i] == 'C'):
         kod[i] = 'G'
      else:
         return False #przypadek gdy podano bledna sekwencje
   return kod

def test_zamiana_nic_matrycowa():
   """Funkcja testujaca funkcje zamiana_nic_matrycowa"""
    
   matrycowa = zamiana_nic_matrycowa(['A', 'G', 'C', 'T']) 
   assert matrycowa == ['T', 'C', 'G', 'A'], 'Blednie przypisane zasady'
   print('Nic matrycowa: ' + str(matrycowa))

   matrycowa = zamiana_nic_matrycowa(['C', 'T', 'G', 'A', 'C', 'G']) 
   assert matrycowa == ['G', 'A', 'C', 'T', 'G', 'C'], 'Blednie przypisane zasady'
   print('Nic matrycowa: ' + str(matrycowa))

   matrycowa = zamiana_nic_matrycowa(['A', 'T', 'A', 'A', 'A', 'B', 'G', 'C', 'G', 'G']) #wystepuje B, ktorego nie ma w sekwencji DNA
   assert matrycowa == False, 'Blednie przypisane zasady'
   print('Blad w sekwencji wpisanego DNA')

test_zamiana_nic_matrycowa()
