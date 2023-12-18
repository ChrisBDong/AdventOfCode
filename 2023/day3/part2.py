d4x = [0, 1, 1, 1, 0, -1, -1, -1]
d4y = [1, 1, 0, -1, -1, -1, 0, 1]

with open('2023\day3\input.txt', 'r') as input:
    data = input.read().splitlines()
    output = 0
        
    cols = len(data[0])
    rows = len(data)
    adjacency = [[-1 for i in range(cols)] for j in range(rows)]
    gears = []
    gearcount = -1

    for i in range(rows):
        for j in range(cols):
            char = data[i][j]
            if char == '*':
                gearcount += 1
                gears.append([])
                for k in range(8):
                    x = j + d4x[k]
                    y = i + d4y[k]
                    if 0 <= x and x < cols and 0 <= y and y < rows:
                        adjacency[y][x] = gearcount

    temp = ''
    part = -1
    number = False
    for i in range(rows):
        for j in range(cols):
            char = data[i][j]
            if number:
                if char.isdigit():
                    temp += char
                    if adjacency[i][j] != -1: part = adjacency[i][j]
                else:   
                    if part != -1:
                        gears[part].append(int(temp))
                    part = -1
                    number = False
                    temp = ''

            else:
                if char.isdigit():
                    number = True
                    temp += char
                    if adjacency[i][j] != -1: part = adjacency[i][j]

    for gear in gears:
        if len(gear) == 2:
            output += gear[0] * gear[1]
    print(output)