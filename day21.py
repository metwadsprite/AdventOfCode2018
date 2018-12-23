file = open('input.txt', 'r')
bound_ip = int(file.readline().strip('#ip '))
ins = []
for line in file:
    line = line.strip().split(' ')
    ins.append(line)

file.close()


def instruction(reg, i, arg1, arg2, arg3):

    if i == 'addr':      #addr
        reg[arg3] = reg[arg1] + reg[arg2]
    elif i == 'addi':    #addi
        reg[arg3] = reg[arg1] + arg2
    elif i == 'mulr':    #mulr
        reg[arg3] = reg[arg1] * reg[arg2]
    elif i == 'muli':    #muli
        reg[arg3] = reg[arg1] * arg2
    elif i == 'banr':    #banr
        reg[arg3] = reg[arg1] & reg[arg2]
    elif i == 'bani':    #bani
        reg[arg3] = reg[arg1] & arg2
    elif i == 'borr':    #borr
        reg[arg3] = reg[arg1] | reg[arg2]
    elif i == 'bori':    #bori
        reg[arg3] = reg[arg1] | arg2
    elif i == 'setr':    #setr
        reg[arg3] = reg[arg1]
    elif i == 'seti':    #seti
        reg[arg3] = arg1
    elif i == 'gtir':   #gtir
        if arg1 > reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 'gtri':   #gtri
        if reg[arg1] > arg2:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 'gtrr':   #gtrr
        if reg[arg1] > reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 'eqir':   #eqir
        if arg1 == reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 'eqri':   #eqri
        if reg[arg1] == arg2:
            reg[arg3] = 1
        else:
            reg[arg3] = 0
    elif i == 'eqrr':   #eqrr
        if reg[arg1] == reg[arg2]:
            reg[arg3] = 1
        else:
            reg[arg3] = 0


reg = [0, 0, 0, 0, 0, 0]
ip = 0

prev_reg = 0

prev = set()

iter2 = 0
iter = 0
while True:
    i = ins[ip][0]
    arg1 = int(ins[ip][1])
    arg2 = int(ins[ip][2])
    arg3 = int(ins[ip][3])

    reg[bound_ip] = ip
    instruction(reg, i, arg1, arg2, arg3)
    ip = reg[bound_ip] + 1
    iter2 += 1

    if ip == 28:
        if reg[4] in prev:
            print(iter)
            print(prev_reg)
            break
        else:
            prev.add(reg[4])
            prev_reg = reg[4]
        if iter == 0:
            print(prev_reg)
        iter += 1
