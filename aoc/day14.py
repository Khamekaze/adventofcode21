
def read_input():
    with open('inputs/day14/input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        input = lines[0]
        lines.remove(input)
        lines.remove('')

        legend = {}
        for line in lines:
            vals = line.split(' -> ')
            legend[vals[0]] = vals[1]

        return input, legend

def compare_values(input, legend):
    #Too slow for 40 iterations :(
    modified_input = ''
    for i in range(len(input)):
        if i < len(input) - 1:
            a = input[i]
            b = input[i + 1]
            ab = a + b
            for x, y in legend.items():
                if x == ab:
                    modified_input += a + y
        else:
            a = input[i]
            modified_input += a

    return modified_input


def get_final_quantity(legend, input):
    values = []
    for x in legend.values():
        if x not in values:
            values.append(x)

    new_dict = {}
    for v in values:
        new_dict[v] = 0

    for c in input:
        val = new_dict[c]
        val = int(val) + 1
        new_dict[c] = val

    key_max = max(new_dict.keys(), key=(lambda k: new_dict[k]))
    key_min = min(new_dict.keys(), key=(lambda k: new_dict[k]))

    final_value = int(new_dict[key_max]) - int(new_dict[key_min])

    print(final_value)


if __name__ == '__main__':
    start_input, legend = read_input()
    for i in range(10):
        print(i)
        start_input = compare_values(start_input, legend)

    get_final_quantity(legend, start_input)
