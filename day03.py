def p1(file):
    mat = [[0 for it in range(0, 1000)] for it in range (0, 1000)]

    for line in file:
        line = line.strip().split(" ")
        start_col, start_line = line[2].strip(":").split(",")
        area_col, area_line = line[3].split("x")
        start_col = int(start_col)
        start_line = int(start_line)
        area_col = int(area_col)
        area_line = int(area_line)

        for it1 in range(start_line - 1, start_line + area_line - 1):
            for it2 in range(start_col - 1, start_col + area_col - 1):
                mat[it1][it2] += 1

    sqr_in = 0
    for it1 in range(0, 1000):
        for it2 in range(0, 1000):
            if mat[it1][it2] >= 2:
                sqr_in += 1

    print(sqr_in)
    return


def p2(file):
    mat = [[0 for it in range(0, 1000)] for it in range (0, 1000)]
    lines = []

    for line in file:
        lines.append(line)

    for line in lines:
        line = line.strip().split(" ")
        start_col, start_line = line[2].strip(":").split(",")
        area_col, area_line = line[3].split("x")
        start_col = int(start_col)
        start_line = int(start_line)
        area_col = int(area_col)
        area_line = int(area_line)

        for it1 in range(start_line - 1, start_line + area_line - 1):
            for it2 in range(start_col - 1, start_col + area_col - 1):
                mat[it1][it2] += 1

    for line in lines:
        line = line.strip().split(" ")
        start_col, start_line = line[2].strip(":").split(",")
        area_col, area_line = line[3].split("x")
        start_col = int(start_col)
        start_line = int(start_line)
        area_col = int(area_col)
        area_line = int(area_line)

        no_overlap = True

        for it1 in range(start_line - 1, start_line + area_line - 1):
            for it2 in range(start_col - 1, start_col + area_col - 1):
                if mat[it1][it2] >= 2:
                    no_overlap = False

        if no_overlap:
            print(line[0])
    return


file = open("input.txt", "r")
# p1(file)
p2(file)
file.close()
