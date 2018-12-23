import networkx as nx

file = open('input.txt', 'r')
regex = file.readline().strip().strip('^').strip('$')

map = nx.Graph()

direction = {'N': -1, 'S': 1, 'E': -1j, 'W': 1j}
stack = []
path_start = {0}
path_end = set()
pos = {0}

for i in regex:
    if i == '|':
        path_end.update(pos)
        pos = path_start
    elif i in 'NSEW':
        map.add_edges_from((p, p + direction[i]) for p in pos)
        pos = {p + direction[i] for p in pos}
    elif i == '(':
        stack.append((path_start, path_end))
        path_start = pos
        path_end = set()
    elif i == ')':
        path_start, path_end = stack.pop()
        path_end.update(pos)

len = nx.algorithms.shortest_path_length(map, source=0)
print(max(len.values()))

count = 0
for room in len.values():
    if room >= 1000:
        count += 1
print(count)
