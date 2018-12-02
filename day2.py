def p1(file):
    alph = 'abcdefghijklmnopqrstuvwxyz'

    no_two = 0
    no_three = 0

    for line in file:
        add_two = False
        add_three = False

        for char in alph:
            if line.count(char) == 2 and not add_two:
                no_two += 1
                add_two = True
            elif line.count(char) == 3 and not add_three:
                no_three += 1
                add_three = True

    print(no_two * no_three)
    return


def p2(file):
    lines = []

    for line in file:
        lines.append(line.strip())

    dif_list = []

    for line1 in lines:
        for line2 in lines:
            dif_no = 0

            for it in range(0, len(line1)):
                if line1[it] != line2[it]:
                    dif_no += 1
                    dif_it = it

            if dif_no == 1:
                for it in range(0, len(line1)):
                    if it != dif_it:
                        dif_list.append(line1[it])

                print(*dif_list, sep="")
                return


file = open("input.txt", "r")
# p1(file)
p2(file)
file.close()
