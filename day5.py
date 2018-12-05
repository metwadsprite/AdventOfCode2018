def p1(file):
    poly = file.readline()
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    it = 0
    while it != len(poly) - 1:
        if poly[it] in lowercase:
            if poly[it + 1] in uppercase:
                if ord(poly[it]) == ord(poly[it + 1]) + 32:
                    poly = poly[:it] + poly[it + 2:]
                    it -= 1
                    continue
        if poly[it] in uppercase:
            if poly[it + 1] in lowercase:
                if ord(poly[it]) == ord(poly[it + 1]) - 32:
                    poly = poly[:it] + poly[it + 2:]
                    it -= 1
                    continue
        it += 1

    print(len(poly) - 1)


def p2(file):
    poly = file.readline()
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    poly_bk = poly
    lens = []

    for lit in range(0, len(lowercase)):
        poly = poly_bk
        if lowercase[lit] not in poly and uppercase[lit] not in poly:
            continue

        pit = 0
        while pit != len(poly):
            if poly[pit] == lowercase[lit] or poly[pit] == uppercase[lit]:
                poly = poly[:pit] + poly[pit + 1:]
                pit -= 1
            pit += 1

        it = 0
        while it != len(poly) - 1:
            if poly[it] in lowercase:
                if poly[it + 1] in uppercase:
                    if ord(poly[it]) == ord(poly[it + 1]) + 32:
                        poly = poly[:it] + poly[it + 2:]
                        it -= 1
                        continue
            if poly[it] in uppercase:
                if poly[it + 1] in lowercase:
                    if ord(poly[it]) == ord(poly[it + 1]) - 32:
                        poly = poly[:it] + poly[it + 2:]
                        it -= 1
                        continue
            it += 1

        lens.append(len(poly) - 1)
    print(min(lens))


file = open("input.txt", "r")
# p1(file)
p2(file)
file.close()
