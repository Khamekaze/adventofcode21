def read_file(fileName):
    with open('inputs/day17/' + fileName + '.txt') as file:
        lines = file.readlines()
        lines = lines[0].split(' ')
        target = []
        target.append(lines[2])
        target.append(lines[3])
        vals = []
        for val in target:
            val = val.replace('=', ', ')
            val = val.replace('..', ', ')
            val = val.replace(',', ', ')
            val = val.replace(', ', '')
            val = val.split(' ')
            for v in val:
                vals.append(v)

        xVals = []
        xVals.append(int(vals[1]))
        xVals.append(int(vals[2]))
        yVals = []
        yVals.append(int(vals[4]))
        yVals.append(int(vals[5]))
        print(xVals)
        print(yVals)

        return xVals, yVals


def perform_step(xVel, yVel, xVals, yVals, maxSteps):
    #xvel -1 ->0
    #yvel -1 -> <0

    xPos = 0
    yPos = 0
    maxY = 0

    for i in range(maxSteps):
        xPos += xVel
        yPos += yVel
        xVel -= 1
        if xVel < 0:
            xVel = 0
        yVel -= 1
        if yPos > maxY:
            maxY = yPos
        if xPos >= xVals[0] and xPos <= xVals[1] and yPos >= yVals[0] and yPos <= yVals[1]:
            print('HIT!')
            return maxY, 1
    return 0, 0


if __name__ == '__main__':
    xVals, yVals = read_file('input')

    maxVal = 0
    hits = 0
    for y in range(600):
        for x in range(600):
            maxY, hit = perform_step(x, y-92, xVals, yVals, 500)
            hits += hit
            if maxY > maxVal:
                maxVal = maxY

    print(maxVal)
    print(hits)


