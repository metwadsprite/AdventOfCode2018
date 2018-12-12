def p1(file):
    SN = int(file.readline())

    rack_id = 0
    maxs = 0
    maxs_x = 0
    maxs_y = 0

    rack = [[0 for _ in range(300)] for _ in range(300)]

    for x in range(300):
        for y in range(300):
            rack_id = x + 11
            rack[x][y] = rack_id * (y + 1)
            rack[x][y] += SN
            rack[x][y] *= rack_id
            rack[x][y] = (rack[x][y] // 100) % 10
            rack[x][y] -= 5

    maxsize = 0

    for size in range(10, 21):
        for x in range(300 - size + 1):
            for y in range(300 - size + 1):
                sum = 0
                for p in range(x, size + x):
                    for q in range(y, size + y):
                        sum += rack[p][q]
                if sum > maxs:
                    maxs = sum
                    maxs_x = x
                    maxs_y = y
                    maxsize = size

    print(maxs_x + 1, maxs_y + 1, maxsize, sep=',')


file = open('input.txt', 'r')
p1(file)
file.close()
