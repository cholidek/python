#wydrukuje liczbe od 0 do 100 jezeli liczba jest podzielna przez 3 to wypisz Fizz, jeżeli podzielana przez 5 to wypisz Buzz, jeżeli przez 3 i 5 to FizzBuzz
#dzielimy przez 15 bo optymalizacja 3*5
#pozbyć się jednego if fizz i buzz + dodać Homework zoptymalizuj kod


# for i in range(101):
#     if i % 15 ==0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

for i in range(101):
    normal_print = True
    if i % 3 == 0:
        print('Fizz', end='')
        normal_print = False
    if i % 5 == 0:
        print('Buzz', end='')
        normal_print = False
    if normal_print:
        print(i, end='')
    print('')
