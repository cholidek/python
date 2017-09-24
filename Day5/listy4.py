# usuwanie elementu bez znania jego indekxu

lista = ['kwiatek', 'ziemia', 'doniczka', 'konewka']

lista.remove('ziemia')

print(lista)
#nie wiemy czy element jest na liscie ale chcemy go usunac
#trzeba najpierw sprawdzic czy jest na liscie

el_usun = 'grabki'

if el_usun in lista:
    lista.remove(el_usun)