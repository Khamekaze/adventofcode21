def read_files():
    alg = ''
    with open('inputs/day20/test_algo.txt') as algo:
        lines = algo.readlines()
        lines = [line.rstrip() for line in lines]
        alg = ''.join(lines)

    with open('inputs/day20/test_image.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        image_matrix = [['' for y in range(len(lines))] for x in range(len(lines[0]))]

        x = 0
        y = 0
        for line in lines:
            for l in line:
                image_matrix[y][x] = l
                x += 1
            y += 1
            x = 0

        return alg, image_matrix


if __name__ == '__main__':
    alg, matrix = read_files()