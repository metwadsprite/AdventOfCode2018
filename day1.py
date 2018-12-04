def p1(file):
    freq = 0

    op = []
    for line in file:
        op.append(line)

    for line in op:
        freq += int(line)

    print(freq)


def p2(file):
    freq = 0
    prev_freq = set()
    prev_freq.add(0)

    op = []
    for line in file:
        op.append(line)

    while True:
        for line in op:
            freq += int(line)

            if freq in prev_freq:
                print(freq)
                exit()

            prev_freq.add(freq)


file = open("input.txt", "r")
# p1(file)
p2(file)
file.close()
