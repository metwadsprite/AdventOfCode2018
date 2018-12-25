file = open('input1.txt', 'r')

points = []

for line in file:
    line = line.strip().split(',')
    line = tuple(int(i) for i in line)
    points.append(line)


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])


cons = [set()]
cons[0].add(points.pop(0))

for point in points:
    added = False

    for c in cons:
        for point2 in c:
            if distance(point, point2) <= 3:
                if not added:
                    c.add(point)
                    added = True
                    last_add = cons.index(c)
                    break
                else:
                    cons[last_add] |= c
                    cons.remove(c)
                    break
    if not added:
        cons.append(set())
        cons[-1].add(point)

print(len(cons))
