# zamień stringa na listę wyrazów, bez przecinka
zdanie = 'Ala ma kota, kot ma ale'

# uzycie replace zamiana przecinka na nicosc bo po spacji to nam wypisze przecinek, jak po przecinku to nam zrobi 2 elementy ktore sa odzienone przecinkiem
zdanie = zdanie.replace(',', '')
print(zdanie)

zdanie2 = zdanie.split(' ')
print(zdanie2)

