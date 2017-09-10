# Zamień string wejściowy "Ala ma kota, kot ma 4 nogi." na "Arek lubi psy, a najbardziej boksery!"

str_wejsciowy = "Ala ma kota, kot ma 4 nogi."

# wyliczenie kody ASCII od literki t małej
kod = ord((str_wejsciowy[9]))

r = chr(kod-2)
e = chr(kod-15)
u = chr(kod+1)
b = chr(kod-18)
p = chr(kod-4)
s = chr(kod-1)
y = chr(kod+5)
j = chr(kod-10)
d = chr(kod-16)
z = chr(kod+6)
wykrzyknik = chr(kod-83)

#indeksowanie liter ze str_wejsciowego
A = str_wejsciowy[0]
k = str_wejsciowy[7]
l = str_wejsciowy[1]
i = str_wejsciowy[25]
przecinek = str_wejsciowy[11]
a = str_wejsciowy[2]
spacja =str_wejsciowy[3]
n = str_wejsciowy[22]
i = str_wejsciowy[25]
o = str_wejsciowy[8]
k = str_wejsciowy[7]



wyraz1 = A + r + e + k
wyraz2 = l + u + b + i
wyraz3 = p + s + y + przecinek + spacja + a
wyraz4 = n + a + j + b + a + r + d +z + i + e + j
wyraz5 = b + o + k + s + e + r + y + wykrzyknik


print(wyraz1, wyraz2, wyraz3, wyraz4, wyraz5)

