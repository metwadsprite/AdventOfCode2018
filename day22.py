import heapq

file = open('input.txt', 'r')
depth = int(file.readline().split(' ')[1])
target = file.readline().strip().split(' ')[1].split(',')
file.close()

target = (int(target[0]), int(target[1]))
start = (0, 0)

erosion = {}
type = {}
risk = 0

xbound = target[0] + 1000
ybound = target[1] + 1000

for x in range(xbound):
    for y in range(ybound):
        if (x, y) == start or (x, y) == target:
            geo_id = 0
        elif y == 0:
            geo_id = x * 16807
        elif x == 0:
            geo_id = y * 48271
        else:
            geo_id = erosion[(x - 1, y)] * erosion[(x, y - 1)]

        erosion[(x, y)] = (geo_id + depth) % 20183
        type[(x, y)] = erosion[(x, y)] % 3

print(sum(type[(x, y)] for x in range(target[0] + 1) for y in range(target[1] + 1)))

queue = [(0, 0, 0, 1)]
best = {}

target = (target[0], target[1], 1)

while queue:
    minutes, x, y, cant = heapq.heappop(queue)
    best_key = (x, y, cant)

    if best_key in best and best[best_key] <= minutes:
        continue

    best[best_key] = minutes

    if best_key == target:
        print(minutes)
        break

    for i in range(3):
        if i != cant and i != type[(x, y)]:
            heapq.heappush(queue, (minutes + 7, x, y, i))

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newx = x + dx
        newy = y + dy

        if newx < 0 or newx > xbound:
            continue
        if newy < 0 or newy > ybound:
            continue
        if type[(newx, newy)] == cant:
            continue

        heapq.heappush(queue, (minutes + 1, newx, newy, cant))
