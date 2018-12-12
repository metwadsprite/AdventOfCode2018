def p1(file):
    new_state = file.readline().strip('initial state: ').strip()
    file.readline()

    spread = []

    for line in file:
        spread.append(line.strip().split(' => '))

    start = 0
    for gen in range(1, 21):

        state = new_state

        if '#' in state[:4]:
            state = '....' + state
            start -= 4
        if '#' in state[len(state) - 5:]:
            state += '....'

        new_state = ''
        for _ in range(len(state)):
            new_state += '.'

        for i in range(2, len(state) - 3):
            for s in spread:
                if state[i - 2:i + 3] == s[0]:
                    new_state = new_state[:i] + s[1] + new_state[i + 1:]
        # print(new_state)

    sum = 0
    j = start
    for i in range(len(new_state)):
        if new_state[i] == '#':
            sum += j
        j += 1
    print(sum)


def p2(file):
    new_state = file.readline().strip('initial state: ').strip()
    file.readline()

    spread = []

    for line in file:
        spread.append(line.strip().split(' => '))

    start = 0
    for gen in range(1, 151):
        state = new_state

        if '#' in state[:4]:
            state = '....' + state
            start -= 4
        if '#' in state[len(state) - 5:]:
            state += '....'

        new_state = ''
        for _ in range(len(state)):
            new_state += '.'

        for i in range(2, len(state) - 3):
            for s in spread:
                if state[i - 2:i + 3] == s[0]:
                    new_state = new_state[:i] + s[1] + new_state[i + 1:]
    glider = 0
    sum = 0
    j = start
    for i in range(len(new_state)):
        if new_state[i] == '#':
            sum += j
            glider += 1
        j += 1

    print(sum + (50000000000 - 150) * glider)


file = open('input.txt', 'r')
# p1(file)
p2(file)
file.close()
