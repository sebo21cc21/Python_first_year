"""
@author: Sebastian Bednarski
"""
def zamiana_rna(kod):
   """ Funckja do zamiana sekwencji DNA na nić matrycową
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty

    Returns: 
        list: tablica posortowanych elementów
    """
   for i in range(len(kod)):
      if (kod[i] == 'A'): #sprawdzanie kolejno czy wystepuje dana zasada i zamiana A z U, a T z A oraz C z G
         kod[i] = 'U' #Uracyl w rna
      elif(kod[i] == 'T'):
         kod[i] = 'A'
      elif(kod[i] == 'G'):
         kod[i] = 'C'
      elif(kod[i] == 'C'):
         kod[i] = 'G'
      else:
         return False #przypadek gdy podano bledna sekwencje
   return kod

def test_zamiana_rna():
   """Funkcja testujaca funkcje zamiana_rna"""
    
   matrycowa = zamiana_rna(['A', 'G', 'C']) 
   assert matrycowa == ['U', 'C', 'G'], 'Blednie przypisane zasady'
   print('RNA: ' + str(matrycowa))

   matrycowa = zamiana_rna(['C', 'T', 'A', 'T', 'T', 'G']) 
   assert matrycowa == ['G', 'A', 'U', 'A', 'A', 'C'], 'Blednie przypisane zasady'
   print('RNA: ' + str(matrycowa))

   matrycowa = zamiana_rna(['A', 'T', 'A', 'A', 'A', 'B', 'G', 'C', 'G'])  #wystepuje B, błąd
   assert matrycowa == False, 'Blednie przypisane zasady'
   print('Blad w sekwencji wpisanego DNA')

test_zamiana_rna()
