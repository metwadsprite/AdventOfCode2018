import time

def p1(file):
    cds = []

    for line in file:
        line = line.strip().split(', ')
        cds.append(line)

    for cd in cds:
        cd[0] = int(cd[0])
        cd[1] = int(cd[1])

    max_line = max([cd[0] for cd in cds])
    max_col = max([cd[1] for cd in cds])

    min_line = min([cd[0] for cd in cds])
    min_col = min([cd[1] for cd in cds])

    is_inf = [0 for cd in cds]

    for it in range(0, len(cds)):
        if cds[it][0] == min_line or cds[it][0] == max_line:
            is_inf[it] = 1
        if cds[it][1] == min_col or cds[it][1] == max_col:
            is_inf[it] = 1

    area = [0 for cd in cds]

    for it1 in range(min_line + 1, max_line):
        for it2 in range(min_col + 1, max_col):
            ip_dist = max_line + max_col
            op_dist = max_line + max_col
            p_id = -1

            for it3 in range(0, len(cds)):
                if is_inf[it3] == 0:
                    if ip_dist > abs(it1 - cds[it3][0]) + abs(it2 - cds[it3][1]):
                        ip_dist = abs(it1 - cds[it3][0]) + abs(it2 - cds[it3][1])
                        p_id = it3
                else:
                    op_dist = min(op_dist, abs(it1 - cds[it3][0]) + abs(it2 - cds[it3][1]))

            for it3 in range(0, len(cds)):
                if ip_dist == abs(it1 - cds[it3][0]) + abs(it2 - cds[it3][1]) and it3 != p_id:
                    ip_dist = max_line + max_col
                    break

            if ip_dist < op_dist:
                area[p_id] += 1

    print(max(area))


def p2(file):
    cds = []

    for line in file:
        line = line.strip().split(', ')
        cds.append(line)

    max_line = 0
    max_col = 0
    for cd in cds:
        cd[0] = int(cd[0])
        cd[1] = int(cd[1])
        max_line = max(max_line, cd[0])
        max_col = max(max_col, cd[1])

    max_sum = 10000
    area = 0

    for it2 in range(0, max_line + 1):
        for it3 in range(0, max_col + 1):
            point_sum = 0

            for cd in cds:
                point_sum += abs(it2 - cd[0]) + abs(it3 - cd[1])

            if point_sum < max_sum:
                area += 1

    print(area)


file = open('input.txt', 'r')
st = time.time()
# p1(file)
p2(file)
print(time.time() - st)
file.close()
