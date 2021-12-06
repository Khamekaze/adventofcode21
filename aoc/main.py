def read_depths():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    i = 0
    val_counter = 0
    while i < len(lines):
        val_prev = lines[i - 1]
        val_current = lines[i]
        if val_current > val_prev:
            val_counter += 1
        i += 1
    print(val_counter)

    i = 0
    val_counter = 0
    while i < len(lines):
        if (i + 4) > len(lines):
            break

        val_a_1 = int(lines[i], base=10)
        val_a_2 = int(lines[i + 1], base=10)
        val_a_3 = int(lines[i + 2], base=10)

        val_b_1 = int(lines[i + 1], base=10)
        val_b_2 = int(lines[i + 2], base=10)
        val_b_3 = int(lines[i + 3], base=10)

        val_counter_a = val_a_1 + val_a_2 + val_a_3
        val_counter_b = val_b_1 + val_b_2 + val_b_3
        if val_counter_b > val_counter_a:
            print(val_counter_b)
            val_counter += 1
        i += 1
    print(val_counter)


def read_directions():
    hor_val = 0
    vert_val = 0
    with open('directions.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for line in lines:
        split_line = line.split()
        current_val = split_line[1]
        current_dir = split_line[0]
        if "f" in current_dir:
            hor_val += int(current_val, base=10)
        if "u" in current_dir:
            vert_val -= int(current_val, base=10)
        if "n" in current_dir:
            vert_val += int(current_val, base=10)

    final_pos = hor_val * vert_val

    print("Hor_Val: " + str(hor_val))
    print("Vert_Val: " + str(vert_val))
    print("Final pos: " + str(final_pos))


def read_directions_2():
    hor_val = 0
    vert_val = 0
    aim = 0
    with open('directions.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for line in lines:
        split_line = line.split()
        current_val = split_line[1]
        current_dir = split_line[0]
        if "f" in current_dir:
            hor_val += int(current_val, base=10)
            vert_delta = int(current_val, base=10) * aim
            vert_val += vert_delta
        if "u" in current_dir:
            aim -= int(current_val, base=10)
        if "n" in current_dir:
            aim += int(current_val, base=10)

    final_pos = hor_val * vert_val

    print("Hor_Val: " + str(hor_val))
    print("Vert_Val: " + str(vert_val))
    print("Final pos: " + str(final_pos))

def main():
    #read_depths()
    #read_directions()
    read_directions_2()


if __name__ == '__main__':
    main()