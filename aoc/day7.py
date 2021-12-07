

def read_inputs():
    with open('inputs/day7/input.txt') as file:
        lines = file.readline()
        input = lines.split(',')
        input_vals = []
        for c in input:
            val = int(c, base=10)
            input_vals.append(val)

    return input_vals


def calculate_sum_of_steps(steps):
    result = int(steps * (steps + 1) / 2)
    return result


def test_new_fuel_consumption(inputs):
    max_val = max(inputs)
    results = []

    index = 0
    result = 0
    while index < max_val:
        for val in inputs:
            distance = val - index
            distance = abs(distance)
            result += calculate_sum_of_steps(distance)
        results.append(result)
        index += 1
        result = 0

    return results



def test_fuel_consumption(inputs):
    max_val = max(inputs)
    results = []

    index = 0
    result = 0
    while index < max_val:
        for val in inputs:
            distance = val - index
            distance = abs(distance)
            result += distance
        results.append(result)
        index += 1
        result = 0

    return results


def check_best_result(results):
    end_val = max(results)
    for i in results:
        if i < end_val:
            end_val = i

    print(end_val)



if __name__ == '__main__':
    inputs = read_inputs()
    #inputs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    #results = test_fuel_consumption(inputs)
    new_results = test_new_fuel_consumption(inputs)
    check_best_result(new_results)

