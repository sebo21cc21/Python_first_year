"""
@author: Sebastian Bednarski
"""

def zamiana_mrna(kod):
   """ Funckja do zamiana sekwencji DNA na nić matrycową
    Args:
        tab (list): tablica podanych elementow #moga byc typu float argumenty

    Returns: 
        list: tablica posortowanych elementów
    """
   for i in range(len(kod)):
      if (kod[i] == 'UUU'): #sprawdzanie kolejno czy wystepuje dana zasada i zamiana na kodon
         kod[i] = 'Phe'
      elif(kod[0] == 'AUG'): #warunek startu
         kod[0] = 'START'
      elif(kod[i] == 'UUC'):
         kod[i] = 'Phe'
      elif(kod[i] == 'UUA'):
         kod[i] = 'Leu'
      elif(kod[i] == 'UUg'):
         kod[i] = 'Leu'
      elif(kod[i] == 'CUU'):
         kod[i] = 'Leu'
      elif(kod[i] == 'CUC'):
         kod[i] = 'Leu'
      elif(kod[i] == 'CUA'):
         kod[i] = 'Leu'
      elif(kod[i] == 'CUG'):
         kod[i] = 'Leu'
      elif(kod[i] == 'AUU'):
         kod[i] = 'Ile'
      elif(kod[i] == 'AUC'):
         kod[i] = 'Ile'
      elif(kod[i] == 'AUA'):
         kod[i] = 'Ile'
      elif(kod[i] == 'AUG'):
         kod[i] = 'Met'
      elif(kod[i] == 'GUU'):
         kod[i] = 'Val'
      elif(kod[i] == 'GUC'):
         kod[i] = 'Val'
      elif(kod[i] == 'GUA'):
         kod[i] = 'Val'
      elif(kod[i] == 'GUG'):
         kod[i] = 'Val'
      elif(kod[i] == 'UCU'):
         kod[i] = 'Ser'
      elif(kod[i] == 'UCC'):
         kod[i] = 'Ser'
      elif(kod[i] == 'UCA'):
         kod[i] = 'Ser'
      elif(kod[i] == 'UCG'):
         kod[i] = 'Ser'
      elif(kod[i] == 'CCU'):
         kod[i] = 'Pro'
      elif(kod[i] == 'CCC'):
         kod[i] = 'Pro'
      elif(kod[i] == 'CCA'):
         kod[i] = 'Pro'
      elif(kod[i] == 'CCG'):
         kod[i] = 'Pro'
      elif(kod[i] == 'ACU'):
         kod[i] = 'Thr'
      elif(kod[i] == 'ACC'):
         kod[i] = 'Thr'
      elif(kod[i] == 'ACA'):
         kod[i] = 'Thr'
      elif(kod[i] == 'ACG'):
         kod[i] = 'Thr'
      elif(kod[i] == 'GCU'):
         kod[i] = 'Ala'
      elif(kod[i] == 'GCC'):
         kod[i] = 'Ala'
      elif(kod[i] == 'GCA'):
         kod[i] = 'Ala'  
      elif(kod[i] == 'GCG'):
         kod[i] = 'Ala'  
      elif(kod[i] == 'UAU'):
         kod[i] = 'Tyr'
      elif(kod[i] == 'UAC'):
         kod[i] = 'Tyr'
      elif(kod[i] == 'UAA'):
         kod[i] = 'Stop'
      elif(kod[i] == 'UAG'):
         kod[i] = 'Stop'
      elif(kod[i] == 'CAU'):
         kod[i] = 'His'
      elif(kod[i] == 'CAC'):
         kod[i] = 'His'
      elif(kod[i] == 'CAA'):
         kod[i] = 'Gin'
      elif(kod[i] == 'CAG'):
         kod[i] = 'Gin'
      elif(kod[i] == 'AAU'):
         kod[i] = 'Asn'
      elif(kod[i] == 'AAC'):
         kod[i] = 'Asn'
      elif(kod[i] == 'AAA'):
         kod[i] = 'Lys'
      elif(kod[i] == 'AAG'):
         kod[i] = 'Lys'
      elif(kod[i] == 'GAU'):
         kod[i] = 'Asp'
      elif(kod[i] == 'GAC'):
         kod[i] = 'Asp'
      elif(kod[i] == 'GAA'):
         kod[i] = 'Glu' 
      elif(kod[i] == 'GAG'):
         kod[i] = 'Glu'    
      elif(kod[i] == 'UGU'):
         kod[i] = 'Cys'  
      elif(kod[i] == 'UGC'):
         kod[i] = 'Cys'
      elif(kod[i] == 'UGA'):
         kod[i] = 'Stop'
      elif(kod[i] == 'UGG'):
         kod[i] = 'Typ'
      elif(kod[i] == 'CGU'):
         kod[i] = 'Arg'
      elif(kod[i] == 'CGC'):
         kod[i] = 'Arg'
      elif(kod[i] == 'CGA'):
         kod[i] = 'Arg'
      elif(kod[i] == 'CGG'):
         kod[i] = 'Arg'
      elif(kod[i] == 'AGU'):
         kod[i] = 'Ser'
      elif(kod[i] == 'AGC'):
         kod[i] = 'Ser'
      elif(kod[i] == 'AGA'):
         kod[i] = 'Arg'
      elif(kod[i] == 'AGG'):
         kod[i] = 'Arg'
      elif(kod[i] == 'GGU'):
         kod[i] = 'Gly'
      elif(kod[i] == 'GGC'):
         kod[i] = 'Gly'
      elif(kod[i] == 'GGA'):
         kod[i] = 'Gly'
      elif(kod[i] == 'GGG'):
         kod[i] = 'Gly'                                                         
      else:
         return False #przypadek, gdy podano bledna sekwencje
   return kod
def test_zamiana_mrna():
   """Funkcja testujaca funkcje zamiana_rna"""

   mrna = zamiana_mrna(['AUG', 'UUC', 'AUG', 'UGA']) #AUG 2 role
   assert mrna == ['START', 'Phe', 'Met', 'Stop'], 'Blad kodonow, bledna funkcja'
   print(mrna)

   mrna = zamiana_mrna(['AUG', 'AGC', 'GGA', 'GGG', 'UAA']) 
   assert mrna == ['START', 'Ser', 'Gly', 'Gly', 'Stop'], 'Blad kodonow, bledna funkcja'
   print(mrna)

   mrna = zamiana_mrna(['AUG', 'CGC', 'GBA', 'GCG', 'UAA']) #bledne sekwencje
   assert mrna == False, 'Blad kodonow, bledna funkcja'
   print('Nie wystepuje taka sekwencja w kodonach')

test_zamiana_mrna()
