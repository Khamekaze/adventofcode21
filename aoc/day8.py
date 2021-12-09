

def read_inputs():
    with open('inputs/day8/inputs.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        outputs = [line.split(' | ') for line in lines]

        digits = []

        for i in range(len(outputs)):
            value = outputs[i][1]
            digits.append(value)

        return digits


def calulcate_all_digits(digits):
    pass


def calculate_known_digits(digits):
    sum = 0
    instances = 0
    for digit in digits:
        vals = digit.split(' ')
        for val in vals:
            if len(val) == 2:
                instances += 1
                sum += 1
            if len(val) == 3:
                instances += 1
                sum += 7
            if len(val) == 4:
                instances += 1
                sum += 4
            if len(val) == 7:
                instances += 1
                sum += 8
    return instances


if __name__ == '__main__':
    digits = read_inputs()
    print(len(digits))
    total = calculate_known_digits(digits)
    print(total)