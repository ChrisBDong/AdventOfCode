d4x = [0, 1, 1, 1, 0, -1, -1, -1]
d4y = [1, 1, 0, -1, -1, -1, 0, 1]

with open('2023\day3\input.txt', 'r') as input:
    n = input.readline()
    data = []
    output = 0

    while n:
        data.append(n.strip('\n'))
        n = input.readline()
        
    cols = len(data[0])
    rows = len(data)
    adjacency = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            char = data[i][j]
            if char.isdigit() or char == '.':
                continue
            for k in range(8):
                x = j + d4x[k]
                y = i + d4y[k]
                if 0 <= x and x < cols and 0 <= y and y < rows:
                    adjacency[y][x] = 1

    temp = ''
    part = False
    number = False
    for i in range(rows):
        for j in range(cols):
            char = data[i][j]
            if number:
                if char.isdigit():
                    temp += char
                    if adjacency[i][j]: part = True
                else:   
                    if part:
                        output += int(temp)
                    part = False
                    number = False
                    temp = ''        
                    
            else:
                if char.isdigit():
                    number = True
                    temp += char
                    if adjacency[i][j]: part = True
    print(output)