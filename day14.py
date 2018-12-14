def p1(file):
    rec_no = int(file.readline())
    rec = [3, 7]

    elf1 = 0
    elf2 = 1

    while len(rec) < 2 * rec_no + 2:
        digits = str(rec[elf1] + rec[elf2])
        for digit in digits:
            rec.append(int(digit))

        elf1 += rec[elf1] + 1
        elf1 %= len(rec)
        elf2 += rec[elf2] + 1
        elf2 %= len(rec)

    print(*rec[rec_no:rec_no + 10], sep='')


def p2(file):
    rec_no = int(file.readline())
    rec_dig = [int(x) for x in str(rec_no)]
    rec = [3, 7]

    elf1 = 0
    elf2 = 1

    while True:
        digits = str(rec[elf1] + rec[elf2])
        for digit in digits:
            rec.append(int(digit))

        elf1 += rec[elf1] + 1
        elf1 %= len(rec)
        elf2 += rec[elf2] + 1
        elf2 %= len(rec)

        if rec[-len(rec_dig):] == rec_dig:
            print(len(rec) - len(rec_dig))
            break
        elif rec[-len(rec_dig) - 1:-1] == rec_dig:
            print(len(rec) - len(rec_dig) - 1)
            break


file = open('input.txt', 'r')
# p1(file)
p2(file)    # over 1 minute run time
file.close()
