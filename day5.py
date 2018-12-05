import time

def p1(file):
    poly = file.readline()

    it = 0
    while it != len(poly) - 1:
        if ord(poly[it]) == ord(poly[it + 1]) + 32:
            poly = poly[:it] + poly[it + 2:]
            it -= 1
        elif ord(poly[it]) == ord(poly[it + 1]) - 32:
            poly = poly[:it] + poly[it + 2:]
            it -= 1
        else:
            it += 1

    print(len(poly) - 1)


def p2(file):
    poly = file.readline()
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    poly_main = poly
    lenghts = []

    for alph_it in range(0, len(lowercase)):
        poly = poly_main

        if lowercase[alph_it] not in poly and uppercase[alph_it] not in poly:
            continue

        it = 0
        while it != len(poly):
            if poly[it] == lowercase[alph_it] or poly[it] == uppercase[alph_it]:
                poly = poly[:it] + poly[it + 1:]
                it -= 1
            it += 1

        it = 0
        while it != len(poly) - 1:
            if ord(poly[it]) == ord(poly[it + 1]) + 32:
                poly = poly[:it] + poly[it + 2:]
                it -= 1
            elif ord(poly[it]) == ord(poly[it + 1]) - 32:
                poly = poly[:it] + poly[it + 2:]
                it -= 1
            else:
                it += 1

        lenghts.append(len(poly) - 1)
    print(min(lenghts))


file = open('input.txt', 'r')
# p1(file)
p2(file)
file.close()
