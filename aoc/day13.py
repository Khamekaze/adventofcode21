
def read_inputs():
    with open('inputs/day13/test_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        values = []
        folding = []
        for line in lines:
            if any((c in 'fold') for c in line):
                folding.append(line)
            else:
                values.append(line)

        vals = list(filter(None, values))

        print(folding)
        print(vals)

    return vals, folding


def populate_matrix(values):
    matrix = [[0 for y in range(11)] for x in range(15)]
    for val in values:
        vals = val.split(',')
        for y in range(11):
            for x in range(15):
                if x == int(vals[0]) and y == int(vals[1]):
                    matrix[y][x] = 1


    return matrix



if __name__ == '__main__':
    values, folding = read_inputs()
    matrix = populate_matrix(values)