

def read_inputs():
    with open('inputs/day9/inputs.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


def create_matrix(lines):
    x = len(lines[0])
    y = len(lines)
    matrix = [[0 for i in range(x)] for j in range(y)]

    for i in range(y):
        for j in range(x):
            val = lines[i][j]
            matrix[i][j] = int(val)

    return matrix


def calculate_low_points(matrix):
    low_points = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            current_val = matrix[y][x]
            val_1 = 999
            val_2 = 999
            val_3 = 999
            val_4 = 999

            if 0 < y < (len(matrix) - 1) and 0 < x < (len(matrix[0]) - 1):
                val_1 = matrix[y][x - 1]
                val_2 = matrix[y + 1][x]
                val_3 = matrix[y][x + 1]
                val_4 = matrix[y - 1][x]
                if current_val < val_1 and current_val < val_2 and current_val < val_3 and current_val < val_4:
                    low_points.append(current_val)

            elif y == 0:
                if x == 0:
                    val_1 = matrix[y + 1][x]
                    val_2 = matrix[y][x + 1]
                    if current_val < val_1 and current_val < val_2:
                        low_points.append(current_val)

                if x == len(matrix[0]) - 1:
                    val_1 = matrix[y][x - 1]
                    val_2 = matrix[y + 1][x]
                    if current_val < val_1 and current_val < val_2:
                        low_points.append(current_val)

                else:
                    val_1 = matrix[y][x - 1]
                    val_2 = matrix[y + 1][x]
                    val_3 = matrix[y][x + 1]
                    if current_val < val_1 and current_val < val_2 and current_val < val_3:
                        low_points.append(current_val)

            elif y == len(matrix) - 1:
                if x == 0:
                    val_1 = matrix[y - 1][x]
                    val_2 = matrix[y][x + 1]
                    if current_val < val_1 and current_val < val_2:
                        low_points.append(current_val)

                if x == len(matrix[0]) - 1:
                    val_1 = matrix[y][x - 1]
                    val_2 = matrix[y - 1][x]
                    if current_val < val_1 and current_val < val_2:
                        low_points.append(current_val)

                else:
                    val_1 = matrix[y][x - 1]
                    val_2 = matrix[y - 1][x]
                    val_3 = matrix[y][x + 1]
                    if current_val < val_1 and current_val < val_2 and current_val < val_3:
                        low_points.append(current_val)

            elif x == 0 and y != 0 and y != len(matrix) - 1:
                val_1 = matrix[y - 1][x]
                val_2 = matrix[y][x + 1]
                val_3 = matrix[y + 1][x]
                if current_val < val_1 and current_val < val_2 and current_val < val_3:
                    low_points.append(current_val)

            elif x == len(matrix[0]) - 1 and y != 0 and y != len(matrix) - 1:
                val_1 = matrix[y - 1][x]
                val_2 = matrix[y][x - 1]
                val_3 = matrix[y + 1][x]
                if current_val < val_1 and current_val < val_2 and current_val < val_3:
                    low_points.append(current_val)

    return low_points


def calculate_risk_level(low_points):
    sum = 0
    for point in low_points:
        val = 1 + point
        sum += val

    print(sum)


if __name__ == '__main__':
    lines = read_inputs()
    matrix = create_matrix(lines)
    low_points = calculate_low_points(matrix)
    calculate_risk_level(low_points)