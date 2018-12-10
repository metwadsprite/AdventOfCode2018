from collections import deque

def p1(file):
    line = file.readline().split(' ')
    no_players = int(line[0])
    max_marble = int(line[6])

    player_scr = [0 for _ in range(no_players)]

    circle = deque([0])
    player = 0

    for marble in range(1, max_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            player_scr[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        player += 1
        if player == no_players:
            player = 0

    print(max(player_scr))


file = open('input.txt', 'r')
p1(file)
file.close()
