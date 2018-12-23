import os

clear = lambda: os.system('cls')

class State:
    def __init__(self):
        self.open = set()
        self.tree = set()
        self.lumb = set()


def bound_check(i, j, list):
    adj_check = 0

    if (i - 1, j - 1) in list:
        adj_check += 1
    if (i - 1, j) in list:
        adj_check += 1
    if (i - 1, j + 1) in list:
        adj_check += 1
    if (i, j - 1) in list:
        adj_check += 1
    if (i, j + 1) in list:
        adj_check += 1
    if (i + 1, j - 1) in list:
        adj_check += 1
    if (i + 1, j) in list:
        adj_check += 1
    if (i + 1, j + 1) in list:
        adj_check += 1

    return adj_check



file = open('input.txt', 'r')

init_state = State()

for i, line in enumerate(file):
    for j, ch in enumerate(line):
        if ch == '.':
            init_state.open.add((i, j))
        elif ch == '|':
            init_state.tree.add((i, j))
        elif ch == '#':
            init_state.lumb.add((i, j))

step = (1000000000 - 460) % 28
for _ in range(460 + step):
    new_state = State()

    for i in range(51):
        for j in range(51):
            if (i, j) in init_state.open:
                if bound_check(i, j, init_state.tree) >= 3:
                    new_state.tree.add((i, j))
                else:
                    new_state.open.add((i, j))

            elif (i, j) in init_state.tree:
                if bound_check(i, j, init_state.lumb) >= 3:
                    new_state.lumb.add((i, j))
                else:
                    new_state.tree.add((i, j))

            elif (i, j) in init_state.lumb:
                if bound_check(i, j, init_state.lumb) >= 1 and bound_check(i, j, init_state.tree) >= 1:
                    new_state.lumb.add((i, j))
                else:
                    new_state.open.add((i, j))

    init_state = new_state
    # clear()
    # print(_)
    # for i in range(51):
    #     for j in range(51):
    #         if (i, j) in init_state.open:
    #             print(' ', end='')
    #         elif (i, j) in init_state.tree:
    #             print('|', end='')
    #         elif (i, j) in init_state.lumb:
    #             print('#', end='')
    #     print()

print(len(init_state.tree) * len(init_state.lumb))
