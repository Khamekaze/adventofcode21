
class PufferFish():

    def __init__(self):
        self.timer = 0

    def set_timer(self, timer):
        self.timer = timer

    def get_timer(self):
        return self.timer

    def update_timer(self):
        self.timer -= 1

    def birth_fish(self):
        self.timer = 6

def update_fish2(fish):
    for i in range(80):
        fish_list = list(fish)
        for f in range(len(fish_list)):
            fish[f] = fish[f] - 1
            if fish[f] == -1:
                fish.append(8)
                fish[f] = 6

    print(len(fish))


def update_fish(fish):
    for i in range(80):
        fishList = []
        for f in range(len(fish)):
            fish[f].update_timer()
            currentTimer = fish[f].get_timer()
            if currentTimer == -1:
                newFish = PufferFish()
                newFish.set_timer(8)
                fishList.append(newFish)
                fish[f].birth_fish()
            fishList.append(fish[f])

        fish = fishList
    print(len(fishList))


def read_inputs():
    with open('inputs/day6/input.txt') as file:
        lines = file.readline()
        input = lines.split(',')
        input_vals = []
        for c in input:
            val = int(c, base=10)
            input_vals.append(val)

    return input_vals



if __name__ == '__main__':

    inputs = read_inputs()
    #Too slow :(
    update_fish2(inputs)
    # inputs = read_inputs()
    # fish = []
    # for i in range(len(inputs)):
    #     newFish = PufferFish()
    #     inputTime = int(inputs[i], base=10)
    #     newFish.set_timer(inputTime)
    #     fish.append(newFish)
    #
    # update_fish(fish)

