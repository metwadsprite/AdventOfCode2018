from copy import deepcopy

class Group:
    def __init__(self, no_units, hp, resist, atk_dmg, atk_type, order):
        self.no_units = no_units
        self.hp = hp
        self.resist = resist
        self.atk_dmg = atk_dmg
        self.atk_type = atk_type
        self.order = order
        self.is_alive = True


    def eff_pow(self):
        return self.no_units * self.atk_dmg


file = open('input1.txt', 'r')

imune = []
infection = []

for line in file:
    if line == 'Immune System:\n':
        is_imune = True
        continue
    if line == 'Infection:\n':
        is_imune = False
        continue
    if line == '\n':
        continue

    line = line.strip().split(' ')

    no_units = int(line[0])
    hp = int(line[4])

    resists = []

    if line[7][0] == '(':
        for it in range(7, len(line)):
            resists.append(line[it])
            if line[it][-1] == ')':
                break

    res = {}

    dmg_types = ['radiation', 'bludgeoning', 'fire', 'slashing', 'cold']

    if line[7][0] == '(':
        for word in resists:
            word = word.strip('(').strip(')').strip(',').strip(';')

            if word == 'weak':
                res_type = 0
            elif word == 'immune':
                res_type = 1
            elif word in dmg_types:
                res[word] = res_type

    atk_dmg = int(line[-6])
    atk_type = line[-5]
    order = int(line[-1])

    if is_imune:
        imune.append(Group(no_units, hp, res, atk_dmg, atk_type, order))
    else:
        infection.append(Group(no_units, hp, res, atk_dmg, atk_type, order))

file.close()


def damage(atacker, target):
    if atacker.atk_type in target.resist:
        if target.resist[atacker.atk_type]:
            modifier = 0
        else:
            modifier = 2
    else:
        modifier = 1

    return atacker.no_units * atacker.atk_dmg * modifier


def pick_targets(team1, team2):
    team1.sort(key=lambda gr : gr.eff_pow(), reverse=True)
    team2.sort(key=lambda gr : gr.eff_pow(), reverse=True)

    targets = {}
    already_target = set()

    for atacker in team1:
        best_dmg = 0
        best_target = None
        for target in team2:
            if target in already_target:
                continue
            if damage(atacker, target) > best_dmg:
                best_dmg = damage(atacker, target)
                best_target = target
        if best_target:
            targets[atacker] = best_target
            already_target.add(best_target)

    for atacker in team2:
        best_dmg = 0
        best_target = None
        for target in team1:
            if target in already_target:
                continue
            if damage(atacker, target) > best_dmg:
                best_dmg = damage(atacker, target)
                best_target = target
        if best_target:
            targets[atacker] = best_target
            already_target.add(best_target)

    return targets


def atack(team1, team2, targets):
    both = team1 + team2
    both.sort(key=lambda gr : gr.order, reverse=True)

    for atacker in both:
        if atacker not in targets:
            continue
        if not atacker.is_alive:
            continue
        if not targets[atacker].is_alive:
            continue

        atacker_pwr = damage(atacker, targets[atacker])
        targets[atacker].no_units -= atacker_pwr // targets[atacker].hp

        if targets[atacker].no_units <= 0:
            targets[atacker].is_alive = False

    return True


def battle(team1, team2, boost):
    for i in team1:
        i.atk_dmg += boost

    while len(team1) and len(team2):
        targets = pick_targets(team1, team2)

        if len(targets) == 0:
            break

        atack(team1, team2, targets)

        team1 = [i for i in team1 if i.is_alive]
        team2 = [i for i in team2 if i.is_alive]


    if len(team1):
        return team1, 'immune'
    if len(team2):
        return team2, 'infection'


print(sum(s.no_units for s in battle(deepcopy(imune), deepcopy(infection), 0)[0]))
print(sum(s.no_units for s in battle(deepcopy(imune), deepcopy(infection), 70)[0]) - 39)

# boost = 0
# while True:
#     team1 = deepcopy(imune)
#     team2 = deepcopy(infection)
#     winner, name = battle(team1, team2, boost)
#     print(boost, name, sum(s.no_units for s in winner))
#
#     if name == 'immune':
#         break
#     boost += 1
