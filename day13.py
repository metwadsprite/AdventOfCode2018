def p1(file):
    lines = []
    for line in file:
        lines.append(line.strip('\n'))

    carts = []
    for i, line in enumerate(lines):
        for j, chr in enumerate(line):
            if chr == '<':
                carts.append([i, j, 'l', 'lt', False])
            if chr == '>':
                carts.append([i, j, 'r', 'lt', False])
            if chr == '^':
                carts.append([i, j, 'u', 'lt', False])
            if chr == 'v':
                carts.append([i, j, 'd', 'lt', False])

    for cart in carts:
        if cart[2] == 'r' or cart[2] == 'l':
            lines[cart[0]] = lines[cart[0]][:cart[1]] + '-' + lines[cart[0]][cart[1] + 1:]
        if cart[2] == 'u' or cart[2] == 'd':
            lines[cart[0]] = lines[cart[0]][:cart[1]] + '|' + lines[cart[0]][cart[1] + 1:]

    while len(carts) > 1:
        carts.sort()
        for cart in carts:
            if cart[2] == 'u':
                cart[0] -= 1

            elif cart[2] == 'd':
                cart[0] += 1

            elif cart[2] == 'l':
                cart[1] -= 1

            elif cart[2] == 'r':
                cart[1] += 1

            for cart2 in carts:
                if cart != cart2 and cart[0] == cart2[0] and cart[1] == cart2[1] and not cart2[4]:
                    cart[4] = True
                    cart2[4] = True
                    break

            if cart[4]:
                continue

            if lines[cart[0]][cart[1]] == '/':
                if cart[2] == 'u':
                    cart[2] = 'r'
                elif cart[2] == 'r':
                    cart[2] = 'u'
                elif cart[2] == 'l':
                    cart[2] = 'd'
                elif cart[2] == 'd':
                    cart[2] = 'l'
            elif lines[cart[0]][cart[1]] == '\\':
                if cart[2] == 'u':
                    cart[2] = 'l'
                elif cart[2] == 'l':
                    cart[2] = 'u'
                elif cart[2] == 'r':
                    cart[2] = 'd'
                elif cart[2] == 'd':
                    cart[2] = 'r'
            elif lines[cart[0]][cart[1]] == '+':
                if cart[3] == 'lt':
                    if cart[2] == 'u':
                        cart[2] = 'l'
                    elif cart[2] == 'l':
                        cart[2] = 'd'
                    elif cart[2] == 'd':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[2] = 'u'
                    cart[3] = 'fwd'
                elif cart[3] == 'fwd':
                    cart[3] = 'rt'
                elif cart[3] == 'rt':
                    if cart[2] == 'u':
                        cart[2] = 'r'
                    elif cart[2] == 'r':
                        cart[2] = 'd'
                    elif cart[2] == 'd':
                        cart[2] = 'l'
                    elif cart[2] == 'l':
                        cart[2] = 'u'
                    cart[3] = 'lt'

        carts = [c for c in carts if not c[4]]
    print(carts[0][1], carts[0][0], sep=',')


file = open('input.txt', 'r')
p1(file)
file.close()
