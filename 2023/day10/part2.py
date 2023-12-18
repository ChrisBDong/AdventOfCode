with open('2023\day10\input.txt', 'r') as input:
    data = input.read().splitlines()
    tiles = [['.' for i in range(2 * len(data[0]) + 1)] for j in range(2 * len(data) + 1)]
    d4 = [(0,1),(1,0),(0,-1),(-1,0)]
    d8 = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
    pipes = {
        "|":((0,1),(0,-1)),
        "-":((1,0),(-1,0)),
        "L":((0,-1),(1,0)),
        "J":((0,-1),(-1,0)),
        "7":((0,1),(-1,0)),
        "F":((0,1),(1,0))
    }
        
    def solve(pos, start, vec):
        prev = start
        tiles[2 * start[1] + 1][2 * start[0] + 1] = '#'
        tiles[2 * start[1] + 1 - vec[1]][2 * start[0] + 1 - vec[0]] = '#'
        while pos != start:
            for vec in pipes[data[pos[1]][pos[0]]]:
                newPos = (pos[0] + vec[0], pos[1] + vec[1])
                if newPos != prev:
                    tiles[2 * pos[1] + 1][2 * pos[0] + 1] = '#'
                    tiles[2 * pos[1] + 1 + vec[1]][2 * pos[0] + 1 + vec[0]] = '#'
                    prev = pos
                    pos = newPos
                    break
    def dfs(i, j):
        for n in range(4):
            di = i + d4[n][0]
            dj = j + d4[n][1]
            if tiles[di][dj] == '.':
                tiles[di][dj] = 'I'
                dfs(di, dj)

    def count():
        output = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                x, y = 2*j+1, 2*i+1
                if tiles[y][x] == 'I':
                    output += 1
                    for n in range(8):
                        if tiles[y + d8[n][1]][x + d8[n][0]] == '#':
                            output -= 1
                            tiles[y][x] = 'D'
                            break
        return output

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                for k in range(4):
                    
                    x, y = j - d4[k][0], i - d4[k][1]
                    if data[y][x] in pipes and d4[k] in pipes[data[y][x]]:
                        solve((x, y), (j, i), d4[k])
                        tiles[2*i+2][2*j] = 'I'
                        dfs(2*i+2, 2*j)
                        print(count())
                        break
