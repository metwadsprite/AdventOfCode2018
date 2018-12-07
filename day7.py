def p1(file):
    lines = []
    for line in file:
        lines.append(line.strip().split(' '))

    order = []
    pairs = []
    freq_l = [0 for _ in range(26)]
    freq_r = [0 for _ in range(26)]

    for line in lines:
        pair = line[1], line[7]
        pairs.append(pair)

    for pair in pairs:
        freq_l[ord(pair[0]) - 65] += 1
        freq_r[ord(pair[1]) - 65] += 1

    olen = 0

    for i in range(26):
        if freq_l[i] != 0 or freq_r[i] != 0:
            olen += 1
        if freq_l[i] != 0 and freq_r[i] == 0:
            order.append(chr(i + 65))

    while len(order) != olen:
        enabled = [1 for _ in range(26)]
        for pair in pairs:
            if pair[0] not in order:
                enabled[ord(pair[1]) - 65] = 0

        temp_min  = 'Z'
        for pair in pairs:
            if enabled[ord(pair[1]) - 65] == 1 and pair[1] not in order:
                temp_min = min(temp_min, pair[1])
        order.append(temp_min)

    print(*order, sep = '')


def p2(file):
    lines = []
    for line in file:
        lines.append(line.strip().split(' '))

    lines = [(line[1], line[7]) for line in lines]
    steps = set([line[0] for line in lines] + [line[1] for line in lines])
    wtime = 0
    workers = [0 for _ in range(5)]
    work = [None for _ in range(5)]

    while steps or any(w > 0 for w in workers):
        cand = [s for s in steps if all(b != s for (_, b) in lines)]
        cand.sort()
        cand = cand[::-1]

        for i in range(5):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    lines = [(a, b) for (a, b) in lines if a != work[i]]
                if cand:
                    n = cand.pop()
                    workers[i] = 60 + ord(n) - ord('A')
                    work[i] = n
                    steps.remove(n)
        wtime += 1
    print(wtime)


file = open('input.txt', 'r')
# p1(file)
p2(file)
file.close()
