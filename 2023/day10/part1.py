with open('2023\day10\input.txt', 'r') as input:
    data = input.read().splitlines()
    d4 = [(0,1),(1,0),(0,-1),(-1,0)]
    pipes = {
        "|":((0,1),(0,-1)),
        "-":((1,0),(-1,0)),
        "L":((0,-1),(1,0)),
        "J":((0,-1),(-1,0)),
        "7":((0,1),(-1,0)),
        "F":((0,1),(1,0))
    }
        
    def solve(pos, start):
        prev = start
        value = 1
        while pos != start:
            for vec in pipes[data[pos[1]][pos[0]]]:
                newPos = (pos[0] + vec[0], pos[1] + vec[1])
                if newPos != prev:
                    prev = pos
                    pos = newPos
                    value += 1
                    break
        return value / 2


    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                for k in range(4):
                    
                    x, y = j - d4[k][0], i - d4[k][1]
                    if data[y][x] in pipes and d4[k] in pipes[data[y][x]]:
                        print(solve((x, y), (j, i)))
                        break