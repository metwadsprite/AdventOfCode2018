from collections import deque

class Area:
    def __init__(self, x, y, x2 = None, y2 = None):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2


file = open('input2.txt', 'r')

clay = []

for line in file:
    line = line.strip().split(', ')

    if 'x' in line[0]:
        line[0] = line[0].strip('x=')
        line[1] = line[1].strip('y=').split('..')
        clay.append(Area(x=int(line[1][0]), y=int(line[0]), x2=int(line[1][1])))
    elif 'y' in line[0]:
        line[0] = line[0].strip('y=')
        line[1] = line[1].strip('x=').split('..')
        clay.append(Area(x=int(line[0]), y=int(line[1][0]), y2=int(line[1][1])))

walls = set()
for c in clay:
    if c.x2:
        for i in range(c.x, c.x2 + 1):
            walls.add((i, c.y))
    elif c.y2:
        for i in range(c.y, c.y2 + 1):
            walls.add((c.x, i))

min_depth = min(walls, key = lambda item : (item[0], item[1] * 0))[0]
depth = max(walls, key = lambda item : (item[0], item[1] * 0))[0]

print(min_depth, depth)

wat_set = set()
wat_flow = set()

queue = deque()
queue.append((0, 500))

dirqueue = deque()

# def fill(pt, direction=(1, 0))
while len(queue) > 0:
    pt = queue.pop()

    if len(dirqueue) == 0:
        direction = (1, 0)
    else:
        direction = dirqueue.pop()

    wat_flow.add(pt)

    bpt = (pt[0] + 1, pt[1])

    if bpt not in walls and bpt not in wat_flow and 1 <= bpt[1] <= depth:
        fill(bpt)

    if bpt not in walls and bpt not in wat_set:
        return False

    lpt = (pt[0], pt[1] - 1)
    rpt = (pt[0], pt[1] + 1)

    lfill = lpt in walls or lpt not in wat_flow and fill(lpt, direction=(0, -1))
    rfill = rpt in walls or rpt not in wat_flow and fill(rpt, direction=(0, 1))

    if direction == (1, 0) and lfill and rfill:
        wat_set.add(pt)

        while lpt in wat_flow:
            wat_set.add(lpt)
            lpt = (lpt[0], lpt[1] - 1)

        while rpt in wat_flow:
            wat_set.add(rpt)
            rpt = (rpt[0], rpt[1] + 1)

    return direction == (0, -1) and (lfill or lpt in wall) or \
        direction == (0, 1) and (rfill or rpt in wall)


fill((0, 500))

print('part 1:', len([pt for pt in wat_flow | wat_set if min_depth <= pt[0] <= depth]))
print('part 2:', len([pt for pt in wat_set if min_depth <= pt[0] <= depth]))
