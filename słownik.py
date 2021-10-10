"""
def translacja_dna(sekwencja):
    kod_genetyczny = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                 'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
                 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
                 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
                 }
    #słownik - wykorzystana struktura danych
    #indeks pierwszego kodonu
    kodon_start = sekwencja.find('AUG')#szuka kodonu start

    #nukleotyd startowy i reszta sekwecji
    start_sekwencji = sekwencja[int(kodon_start):]
    #wybieramy pierwszy nukleotyd w danych kodonie, zaczynając od 0, wybieramy wielokrotności liczby 3 ( kodon to 3 nukleotydy)
    # n to wielokrotności liczby 3, ale zaczynając od 0
    for n in (0, len(start_sekwencji), 3):
        if start_sekwencji[n:n+3] in kod_genetyczny:
            sekwencja_białka += kod_genetyczny[start_sekwencji[n:n+3]]
        if d.get(sekwencja[i:i+3])=='Stop':        
    x = 1
    return x

sequence = 'AUGGUUGAU'
for i in range(len(sequence)):
    test=translacja_dna(sequence)

print(test)
"""

