from z3 import *


class Bot:
    def __init__(self, pos, rad):
        self.pos = pos
        self.rad = rad


file = open('input.txt', 'r')

bots = []
max_rad = 0

for line in file:
    line = line.strip().split('>, ')
    pos = line[0].strip('pos=<').split(',')
    pos = [int(i) for i in pos]
    rad = int(line[1].strip('r='))

    b = Bot(pos, rad)
    if rad > max_rad:
        max_rad = rad
        max_bot = b

    bots.append(b)
file.close()


def dist(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1]) + abs(p0[2] - p1[2])


count = 0
for bot in bots:
    if dist(bot.pos, max_bot.pos) <= max_rad:
        count += 1
print(count)


def z3_abs(x):
    return If(x >= 0,x,-x)


def z3_dist(x, y):
    return z3_abs(x[0] - y[0]) + z3_abs(x[1] - y[1]) + z3_abs(x[2] - y[2])


x = Int('x')
y = Int('y')
z = Int('z')

orig = (x, y, z)
expr = x * 0

for bot in bots:
    expr += If(z3_dist(orig, bot.pos) <= bot.rad, 1, 0)

opt = Optimize()
opt.maximize(expr)
opt.minimize(z3_dist((0, 0, 0), (x, y, z)))
opt.check()
model = opt.model()
print(model)
print(dist((0, 0, 0), (model[x].as_long(), model[y].as_long(), model[z].as_long())))
