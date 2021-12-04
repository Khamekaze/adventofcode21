
def find_oxygen_gen_rating(lines):
    index = 0
    new_list = list(lines)
    while index < len(lines[0]):
        sum_val = 0
        for line in new_list:
            if line[index] == '1':
                sum_val += 1

        compare_val = len(new_list) / 2
        for line in list(new_list):
            if sum_val >= compare_val:
                if line[index] == '0':
                    new_list.remove(line)
            elif sum_val < compare_val:
                if line[index] == '1':
                    new_list.remove(line)

        if len(new_list) == 1:
            break

        index += 1

    return int(new_list[0], 2)


def find_c02_rating(lines):
    index = 0
    new_list = list(lines)
    while index < len(lines[0]):
        sum_val = 0
        for line in new_list:
            if line[index] == '1':
                sum_val += 1

        compare_val = len(new_list) / 2
        for line in list(new_list):
            if sum_val >= compare_val:
                if line[index] == '1':
                    new_list.remove(line)
            elif sum_val < compare_val:
                if line[index] == '0':
                    new_list.remove(line)

        if len(new_list) == 1:
            break

        index += 1

    return int(new_list[0], 2)



def calculate_gamma(lines):
    length = len(lines[0])
    num_arr = [0] * length
    for line in lines:
        for c in range(len(line)):
            num = int(line[c], base=10)
            arr_num = num_arr[c]
            sum = num + arr_num
            num_arr[c] = sum

    binary_str = ''
    for i in range(len(num_arr)):
        if num_arr[i] >= len(lines) / 2:
            binary_str += str(1)
        else:
            binary_str += str(0)
    return binary_str


def calculate_epsilon(gamma):
    epsilon = ''
    for c in gamma:
        if c == '1':
            epsilon += '0'
        else:
            epsilon += '1'

    return epsilon


def calculate_power(gamma, epsilon):
    gamma_val = int(gamma, 2)
    epsilon_val = int(epsilon, 2)

    return gamma_val * epsilon_val


def diagnostics():
    with open('inputs/day3/day3_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    gamma = calculate_gamma(lines)
    epsilon = calculate_epsilon(gamma)

    power = calculate_power(gamma, epsilon)

    oxygen_rating = find_oxygen_gen_rating(lines)
    print(oxygen_rating)
    c02_rating = find_c02_rating(lines)
    print(c02_rating)

    print(oxygen_rating * c02_rating)


if __name__ == '__main__':
    diagnostics()
