#  blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,

karta_1 = input('Podaj kartę: ')
karta_2 = input('Podaj kartę: ')





if karta_1.isnumeric():
    karta_1 = int(karta_1)
elif karta_1 in ['K', 'J', 'Q']:
    karta_1 = 10

if karta_2.isnumeric():
    karta_2 = int(karta_2)
elif karta_2 in ['J', 'Q', 'K']:
    karta_2 = 10

if karta_2 == 'A' or karta_1 == 'A':
    if  < 11 or karta_2 <11:
        karta_as = 11
    else:
        karta_as = 1
print(karta_1 + karta_2)
