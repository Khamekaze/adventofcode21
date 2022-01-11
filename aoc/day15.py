def read_input():
    with open('inputs/day15/test_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        matrix = [[0 for y in range(len(lines))] for x in range(len(lines[0]))]
        x = 0
        y = 0
        for line in lines:
            for l in line:
                matrix[x][y] = int(l)
                x += 1
            y += 1

        print(matrix)


if __name__ == '__main__':
    read_input()

