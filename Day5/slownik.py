
#mozna tez tak ale kolekcje trzeba przekazac i bedzie zmienona na ten typ
# osoby = dict()


osoby = {'Ania':'Kowalska', 2:234.4, '923232':4}

liczby = {1:2, 2:3, 3:4}

#klucz 1:2 dlatego pokazuje się 2
print(liczby[1])

#ta dwójka jest 2 element
print(osoby[2])

osoby['Joanna'] = 'policja'
print(osoby)
osoby ['Joanna'] = 'straż'
print(osoby)
#jak zmienimy na 4 to jest key erron bo nie ma 4 klucza w liczbach
print(liczby[3])


print(osoby.keys())
print(osoby.values())
#items iterator ktory w petli oddaje elementy a aw slowniku to jest para klucz:element i tylko slowniki maja ta wlasciwosc
for key, value in osoby.items():
    print(f'klucz: {key} - wartość: {value}')

