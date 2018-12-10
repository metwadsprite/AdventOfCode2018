from copy import deepcopy

def p1(file):
    pos = []
    vel = []

    for line in file:
        line = line.strip('position=<').strip().strip('>').split('velocity=<')
        pair = line[0].strip().strip('>').split(',')
        pair[0] = int(pair[0])
        pair[1] = int(pair[1].strip())
        pos.append(pair)
        pair = line[1].strip().split(',')
        pair[0] = int(pair[0])
        pair[1] = int(pair[1].strip())
        vel.append(pair)

    max_line = pos[0][1]
    max_col = pos[0][0]
    min_line = pos[0][1]
    min_col = pos[0][0]
    for pair in pos:
        max_col = max(max_col, pair[0])
        max_line = max(max_line, pair[1])
        min_col = min(min_col, pair[0])
        min_line = min(min_line, pair[1])

    no_lines = max_line - min_line
    step_pos = deepcopy(pos)
    step = 10000
    while True:
        for i in range(len(pos)):
            step_pos[i][0] = pos[i][0] + vel[i][0] * step
            step_pos[i][1] = pos[i][1] + vel[i][1] * step

        max_line = step_pos[0][1]
        max_col = step_pos[0][0]
        min_line = step_pos[0][1]
        min_col = step_pos[0][0]
        for pair in step_pos:
            max_col = max(max_col, pair[0])
            max_line = max(max_line, pair[1])
            min_col = min(min_col, pair[0])
            min_line = min(min_line, pair[1])

        if max_line - min_line > no_lines:
            step -= 1
            break
        no_lines = max_line - min_line
        step += 1

    for i in range(len(pos)):
        pos[i][0] += vel[i][0] * (step)
        pos[i][1] += vel[i][1] * (step)

    max_line = pos[0][1]
    max_col = pos[0][0]
    min_line = pos[0][1]
    min_col = pos[0][0]
    for pair in pos:
        max_col = max(max_col, pair[0])
        max_line = max(max_line, pair[1])
        min_col = min(min_col, pair[0])
        min_line = min(min_line, pair[1])

    for i in range(min_line, max_line + 1):
        for j in range(min_col, max_col + 1):
            if [j, i] in pos:
                print('X', end='')
            else:
                print(' ', end='')
        print()
    print(step)


file = open('input.txt', 'r')
p1(file)
file.close()
