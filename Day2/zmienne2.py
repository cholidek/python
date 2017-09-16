print('Hello world!')


#pierwsza zmienna

imie = 'Lidia'
nazwisko='kowalska'




#print(nazwisko) nie jest wypisane bo jak nawet jest funkcja zakomentowana to jej nie wywola

#print(3 * imie)
#print(imie +' '+ nazwisko.capitalize())

#print('{} {}'.format(imie, nazwisko.capitalize())) dwie klamerki oznaczają 2 wartości imię i naziwsko jakie będzie umieszczał inne wywołanie powyższego bez dodwania spacji z plusikami

print('{1} {0}'.format(imie, nazwisko))
print('{0} {1}'.format(imie, nazwisko))
print('{0} {0}'.format(imie, nazwisko))
#zmiana kolejności przy wypisaniu

#przypisywanie zmiennych
nazwisko_duze = nazwisko.capitalize()
print('Nazwisko z dużej: ', nazwisko_duze)
print('Nazwisko oryginalne: ', nazwisko)

# pythontutor.com mozna obejrzec








