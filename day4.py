from datetime import datetime as dt
from datetime import timedelta

def p1(file):
    max_slp = 0
    ids = []
    vals = []
    FMT = "%H:%M"

    lines = []
    for line in file:
        lines.append(line)

    lines = sorted(lines)

    g_check = False
    for line in lines:
        line = line.strip().split(" ")

        if line[2] == "Guard":
            g_check = True
            is_asleep = False
            id = line[3].strip("#")

            if int(id) not in ids:
                ids.append(int(id))
                vals.append(0)

        if line[2] == "falls" and g_check:
            slp_start = line[1].strip("]")
            is_asleep = True

        if line[2] == "wakes" and g_check:
            slp_end = line[1].strip("]")

            if is_asleep:
                slp_time = dt.strptime(slp_end, FMT) - dt.strptime(slp_start, FMT)
                slp_time_min = slp_time.seconds / 60
                vals[ids.index(int(id))] += int(slp_time_min)
                is_asleep = False

    max_val  = max(vals)
    max_id = ids[vals.index(max_val)]

    most_min = [0 for it in range(0, 60)]

    fall_check = False
    wake_check = False
    id_check = False

    for line in lines:
        line = line.strip().split(" ")

        if line[2] == "Guard":
            fall_check = False
            wake_check = False
            if int(line[3].strip("#")) == max_id:
                id_check = True
            else:
                id_check = False

        if line[2] == "falls" and id_check:
            start_min = line[1].strip("]").split(":")
            start_min = start_min[1]
            fall_check = True
            wake_check = False

        if line[2] == "wakes" and id_check:
            end_min = line[1].strip("]").split(":")
            end_min = end_min[1]
            wake_check = True

        if fall_check and wake_check:
            if start_min < end_min:
                for it in range(int(start_min), int(end_min)):
                    most_min[it] += 1
            else:
                for it in range(0, int(start_min)):
                    most_min[it] += 1
                for it in range(int(end_min), 60):
                    most_min[it] += 1

    top_freq = max(most_min)
    top_freq_id = most_min.index(top_freq)

    print(max_id * top_freq_id)

def p2(file):
    max_slp = 0
    ids = []
    vals = []
    FMT = "%H:%M"

    lines = []
    for line in file:
        lines.append(line)

    lines = sorted(lines)

    g_check = False
    for line in lines:
        line = line.strip().split(" ")

        if line[2] == "Guard":
            g_check = True
            is_asleep = False
            id = line[3].strip("#")

            if int(id) not in ids:
                ids.append(int(id))
                vals.append(0)

        if line[2] == "falls" and g_check:
            slp_start = line[1].strip("]")
            is_asleep = True

        if line[2] == "wakes" and g_check:
            slp_end = line[1].strip("]")

            if is_asleep:
                slp_time = dt.strptime(slp_end, FMT) - dt.strptime(slp_start, FMT)
                slp_time_min = slp_time.seconds / 60
                vals[ids.index(int(id))] += int(slp_time_min)
                is_asleep = False

    max_tuple = [0, 0, 0]

    for id in ids:
        most_min = [0 for it in range(0, 60)]

        fall_check = False
        wake_check = False
        id_check = False

        for line in lines:
            line = line.strip().split(" ")

            if line[2] == "Guard":
                fall_check = False
                wake_check = False
                if int(line[3].strip("#")) == id:
                    id_check = True
                else:
                    id_check = False

            if line[2] == "falls" and id_check:
                start_min = line[1].strip("]").split(":")
                start_min = start_min[1]
                fall_check = True
                wake_check = False

            if line[2] == "wakes" and id_check:
                end_min = line[1].strip("]").split(":")
                end_min = end_min[1]
                wake_check = True

            if fall_check and wake_check:
                if start_min < end_min:
                    for it in range(int(start_min), int(end_min)):
                        most_min[it] += 1
                else:
                    for it in range(0, int(start_min)):
                        most_min[it] += 1
                    for it in range(int(end_min), 60):
                        most_min[it] += 1

        top_freq = max(most_min)
        top_freq_id = most_min.index(top_freq)

        if top_freq > max_tuple[2]:
            max_tuple[0] = id
            max_tuple[1] = top_freq_id
            max_tuple[2] = top_freq
    print(max_tuple[0] * max_tuple[1])


file = open("input.txt", "r")
# p1(file)
p2(file)
file.close()
