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
        if line[0] == "+":
            freq += int(line[1:])
        else:
            freq -= int(line[1:])

        if freq in prev_freq:
            print(freq)
            exit()

        prev_freq.add(freq)
