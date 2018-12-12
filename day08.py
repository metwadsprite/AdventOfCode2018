class Node():
    def __init__(self):
        self.meta = []
        self.child = []


def make_node(line, p):
    global pos
    pos = p
    node = Node()

    no_child = int(line[pos])
    no_meta = int(line[pos + 1])
    pos += 2

    for _ in range(no_child):
        node.child.append(make_node(line, pos))
    for _ in range(no_meta):
        node.meta.append(int(line[pos]))
        pos += 1

    return node


def value(root):
    if not root.child:
        return sum(root.meta)
    return sum([value(root.child[m - 1]) for m in root.meta if m - 1 < len(root.child)])


def p1(file):
    line = file.readline().strip().split(' ')
    root = make_node(line, 0)

    val = 0

    stack = []
    stack.append(root)

    while stack:
        current = stack.pop()
        val += sum(current.meta)

        for c in current.child:
            stack.append(c)

    print(val)


def p2(file):
    line = file.readline().strip().split(' ')
    root = make_node(line, 0)

    print(value(root))


file = open('input.txt', 'r')
# p1(file)
p2(file)
file.close()
