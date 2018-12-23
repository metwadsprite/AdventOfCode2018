import copy

opcode = [None for _ in range(16)]
opcode_id = [set() for _ in range(16)]
lines = []


def instruction(start_reg, i, arg1, arg2, arg3):
    reg = copy.deepcopy(start_reg)

    if i == 0:      #addr
        reg[arg3] = reg[arg1] + reg[arg2]
    elif i == 1:    #addi
        reg[arg3] = reg[arg1] + arg2
    elif i == 2:    #mulr
        reg[arg3] = reg[arg1] * reg[arg2]
    elif i == 3:    #muli
        reg[arg3] = reg[arg1] * arg2
    elif i == 4:    #banr
        reg[arg3] = reg[arg1] & reg[arg2]
    elif i == 5:    #bani
        reg[arg3] = reg[arg1] & arg2
    elif i == 6:    #borr
        reg[arg3] = reg[arg1] | reg[arg2]
    elif i == 7:    #bori
        reg[arg3] = reg[arg1] | arg2
    elif i == 8:    #setr
        reg[arg3] = reg[arg1]
    elif i == 9:    #seti
        reg[arg3] = arg1
    elif i == 10:   #gtir
        if arg1 > reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 11:   #gtri
        if reg[arg1] > arg2:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 12:   #gtrr
        if reg[arg1] > reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 13:   #eqir
        if arg1 == reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 14:   #eqri
        if reg[arg1] == arg2:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 15:   #eqrr
        if reg[arg1] == reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0

    return reg


def p1(file):
    for line in file:
        if line[:6] == 'Before':
            lines.append(line.strip().strip('Before: [').strip(']'))
        elif line[:5] == 'After':
            lines.append(line.strip().strip('After: [').strip(']'))
        elif line == '\n':
            continue
        else:
            lines.append(line.strip())

    reg1 = []
    ins = []
    reg2 = []
    count = 0

    i = 0
    while i < len(lines):
        no_op = 0

        reg1 = lines[i].split(', ')
        reg1 = [int(j) for j in reg1]

        ins = lines[i + 1].split(' ')
        ins = [int(j) for j in ins]

        reg2 = lines[i + 2].split(', ')
        reg2 = [int(j) for j in reg2]

        i += 3

        new_set = set()
        for x in range(16):
            if reg2 == instruction(reg1, x, ins[1], ins[2], ins[3]):
                no_op += 1
                new_set.add(x)
        if len(opcode_id[ins[0]]) < 1:
            opcode_id[ins[0]] = new_set
        else:
            opcode_id[ins[0]] = opcode_id[ins[0]] & new_set

        if no_op >= 3:
            count += 1

    print(count)


def p2(file):
    max_i = 0
    max_len = 0
    for i, s in enumerate(opcode_id):
        if len(s) > max_len:
            max_i = i
            max_len = len(s)

    while len(opcode_id[max_i]) > 1:
        for i, s in enumerate(opcode_id):
            if len(s) == 1:
                k = s.pop()
                opcode[i] = k
                for sk in opcode_id:
                    if k in sk:
                        sk.remove(k)

    reg = [0, 0, 0, 0]

    for line in file:
        ins = line.strip().split(' ')
        ins = [int(i) for i in ins]

        reg = instruction(reg, opcode[ins[0]], ins[1], ins[2], ins[3])

    print(reg[0])


file = open('input.txt', 'r')
p1(file)
p2(open('input2.txt', 'r'))
file.close()
