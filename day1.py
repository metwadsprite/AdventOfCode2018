freq = 0
prev_freq = set()
prev_freq.add(0)

file = open("input.txt", "r")
op = []
for line in file:
    op.append(line)
file.close()

while True:
    for line in op:
        freq += int(line)

        if freq in prev_freq:
            print(freq)
            exit()

        prev_freq.add(freq)
