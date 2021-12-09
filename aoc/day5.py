class NodeLine:

    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.vals = [0] * 4

    def __str__(self):
        return 'Start X: ' + str(self.start_x) + ' Start Y: ' + str(self.start_y) + ' End X: ' + str(self.end_x) + ' End Y: ' + str(self.end_y)

    def set_coordinates(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.vals[0] = start_x
        self.vals[1] = start_y
        self.vals[2] = end_x
        self.vals[3] = end_y

    def get_coordinates(self):
        return self.vals


def populate_grid(node_lines, grid, w, h):
    for node in node_lines:
        if node.vals[0] == node.vals[2]:
            if node.vals[1] < node.vals[3]:
                index = node.vals[3]
                while index >= node.vals[1]:
                    val = int(grid[index][node.vals[0]])
                    val += 1
                    grid[index][node.vals[0]] = val
                    index -= 1

            else:
                index = node.vals[1]
                while index <= node.vals[3]:
                    val = int(grid[index][node.vals[0]])
                    val += 1
                    grid[index][node.vals[0]] = val
                    index += 1

        elif node.vals[1] == node.vals[3]:
            if node.vals[0] < node.vals[2]:
                index = node.vals[2]
                while index >= node.vals[0]:
                    val = int(grid[node.vals[0]][index])
                    val += 1
                    grid[node.vals[0]][index] = val
                    index -= 1

            else:
                index = node.vals[0]
                while index <= node.vals[2]:
                    val = int(grid[node.vals[0][index]])
                    val += 1
                    grid[node.vals[0][index]] = val
                    index += 1


    for y in range(len(grid)):
        print(grid[y])

def calculate_lines(coordinate_nodes):
    #Only check lines that are not diagonal
    nodes = []
    for n in coordinate_nodes:
        if n.vals[0] == n.vals[2] or n.vals[1] == n.vals[3]:
            nodes.append(n)

    for node in nodes:
        print(node)
    return nodes


def create_coordinates_nodes(lines):
    coordinate_nodes = []
    for line in lines:
        vals = line.split(',')
        start_x = int(vals[0])
        start_y = int(vals[1])
        end_x = int(vals[2])
        end_y = int(vals[3])
        node = NodeLine()
        node.set_coordinates(start_x, start_y, end_x, end_y)
        coordinate_nodes.append(node)

    return coordinate_nodes


def create_grid(lines):
    max_X = 0
    max_Y = 0
    for line in lines:
        vals = line.split(',')
        val_1 = int(vals[0])
        val_2 = int(vals[1])
        max_val = max(val_1, val_2)
        max_X = max(max_X, max_val)

        val_3 = int(vals[2])
        val_4 = int(vals[3])
        max_val = max(val_3, val_4)
        max_Y = max(max_Y, max_val)

    grid = [[0 for i in range(max_Y)] for j in range(max_X)]

    return grid, max_X, max_Y


def read_input():
    lines = []
    with open('inputs/day5/test_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line.replace(">", "") for line in lines]
        lines = [line.replace("-", "") for line in lines]
        lines = [line.replace("  ", ",") for line in lines]

    return lines


if __name__ == '__main__':
    lines = read_input()
    coordinates = create_coordinates_nodes(lines)
    grid, w, h = create_grid(lines)
    line_nodes = calculate_lines(coordinates)
    populate_grid(line_nodes, grid, w, h)