# listy

lista = ['jeden', 'dwa']

print(lista)

lista2 = [1, 'dwa', 'trzy', 5]

lista3 = list(range(2,6))

print(lista2)
print(lista3)

#lista poszczegolnych znaków
lista4 = list('kwiatek')
print(lista4)

#zamiana kawiatka slicowanego z liter na pełen wyraz z dużych liter


flower =''

for znak in lista4:
    flower += znak.upper()
print(flower)

#inny sposob na zamiane kwiatak bez for

flower2= ''.join(lista4)
print(flower2)









