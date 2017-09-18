# Narysuj piramidę Mario - jako input - wysokość piramidy

# np. piramida wysokości 3 ma wyglądać:

#

#   #

#  ###

# #####


wysokosc = input('Podaj wysokość piramidy: ')

wysokosc = int(wysokosc)

for i in range(wysokosc):

    print(" " * (wysokosc - 1 * i) + ("#") + ("#" * (1 * i)))







