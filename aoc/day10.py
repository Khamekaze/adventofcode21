
def read_inputs():
    with open('inputs/day10/test_inputs.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


def count_chunks(lines, chars):
    pass


if __name__ == '__main__':
    chars = ['(', '[', '{', '<', ')', ']', '}', '>']
    inputs = read_inputs()
    count_chunks(lines=inputs, chars=chars)