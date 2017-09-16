#if
#
# if True:
#     pass

# input zczytuje liczbe, wszystkie inputy sa stringiem, nawet jak podaje liczbe, dlatego dopisalismy int przed inputem aby string zamienic na int,
# inptu trzeba zawsze przypisac do czegos

x = 5
# y = int(input('podaj liczbę całkowitą: '))
#
# print(y)
# print(type(y))

y = input('podaj liczbę całkowitą: ')

if y.isnumeric():
    print('To jest liczba')


if x < int(y):
    print(f'{x} jest mniejszy od Twojej liczy')

    if int(y) > 10:
        print('Twoja liczba jest większa od 10')

print('koniec programu')

