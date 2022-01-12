class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.status = 0

    def get_pos(self):
        pos = [self.x, self.y, self.z]
        return pos

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


def init_cube_grid():
    cubes = []
    for z in range(101):
        for y in range(101):
            for x in range(101):
                c = Cube(x - 50, y - 50, z - 50)
                cubes.append(c)

    return cubes


def read_input():
    with open('inputs/day22/test_input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


def perform_step(lines, cubes):
    for line in lines:
        current_step = line
        status = 0
        instructions = current_step.split(' ')[0]
        if instructions == 'on':
            status = 1
        values = current_step.split(' ')[1]
        values = values.split(',')
        xVals = values[0].split('=')[1]
        xVals = xVals.split('..')
        yVals = values[1].split('=')[1]
        yVals = yVals.split('..')
        zVals = values[2].split('=')[1]
        zVals = zVals.split('..')
        for i in range(len(cubes)):
            cube = cubes[i]
            if cube.x >= int(xVals[0]) and cube.x <= int(xVals[1]) and cube.y >= int(yVals[0]) and cube.y <= int(yVals[1]) and cube.z >= int(zVals[0]) and cube.z <= int(zVals[1]):
                cube.set_status(status)

        on_status = 0
        for i in range(len(cubes)):
            c = cubes[i]
            if c.status == 1:
                on_status += 1

    print(on_status)


if __name__ == '__main__':
    lines = read_input()
    cubes = init_cube_grid()
    perform_step(lines, cubes)
