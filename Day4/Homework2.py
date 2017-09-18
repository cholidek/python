# program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

i = 0
x = 0
y = 1
print(x)
print(y)
wynik = 0

while True:
    wynik = x + y
    if wynik > 100:
        break
    x =  y
    y = wynik
    print(wynik)





