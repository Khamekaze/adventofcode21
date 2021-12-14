
def read_inputs():
    with open('inputs/day11/test_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    octopi = [[0 for x in range(12)] for y in range(12)]

    index_Y = 0
    index_X = 0
    for y in range(12):
        index_X = 0
        if y > 0 and y < 11:
            line = lines[index_Y]
            index_Y += 1
        for x in range(12):
            if x > 0 and x < 11 and y > 0 and y < 11:
                c = line[index_X]
                val = int(c)
                octopi[y][x] = val
                index_X += 1

    return octopi


def perform_step(octopi):
    #Tick
    flashes = 0

    for y in range(12):
        for x in range(12):
            if x > 0 and x < 11 and y > 0 and y < 11:
                octopi[y][x] += 1

    temp_arr = octopi

    for y in range(12):
        for x in range(12):
            if x > 0 and x < 11 and y > 0 and y < 11:
                current_val = octopi[y][x]
                add_val = get_adjescent_values(octopi, y, x)
                total_val = current_val + add_val
                temp_arr[y][x] = total_val


    return temp_arr


def print_octopi(octopi):
    for y in range(12):
        print(octopi[y])
    print()


def get_adjescent_values(octopi, y, x):
    total_val = 0
    val = octopi[y - 1][x - 1]
    if val > 9:
        total_val += 1
    val = octopi[y - 1][x]
    if val > 9:
        total_val += 1
    val = octopi[y - 1][x + 1]
    if val > 9:
        total_val += 1
    val = octopi[y][x - 1]
    if val > 9:
        total_val += 1
    val = octopi[y][x + 1]
    if val > 9:
        total_val += 1
    val = octopi[y + 1][x - 1]
    if val > 9:
        total_val += 1
    val = octopi[y + 1][x]
    if val > 9:
        total_val += 1
    val = octopi[y + 1][x + 1]
    if val > 9:
        total_val += 1

    return total_val


if __name__ == '__main__':
    octopi = read_inputs()
    flashes = 0
    for i in range(2):
        octopi = perform_step(octopi)
        print_octopi(octopi)
