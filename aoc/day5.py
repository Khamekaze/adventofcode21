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


def calculate_lines(coordinate_nodes):
    #Only check lines that are not diagonal
    nodes = []
    for n in coordinate_nodes:
        if n.vals[0] == n.vals[2] or n.vals[1] == n.vals[3]:
            nodes.append(n)



def create_coordinates_nodes(lines):
    coordinate_nodes = []
    for line in lines:
        vals = line.split(',')
        start_x = vals[0]
        start_y = vals[1]
        end_x = vals[2]
        end_y = vals[3]
        node = NodeLine()
        node.set_coordinates(start_x, start_y, end_x, end_y)
        coordinate_nodes.append(node)

    return coordinate_nodes


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
    calculate_lines(coordinates)
    print(lines)