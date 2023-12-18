points = 0
start = 1

with open('2023\day4\input.txt', 'r') as input:
    data = input.read().splitlines()
    for card in data:
        score = 0
        left = card[10:39].replace('  ', ' ').split(' ')
        right = card[42:].replace('  ', ' ').split(' ')
        if '' in left: left.remove('')
        if '' in right: right.remove('')

        for i in left:
            if i in right:
                score += 1
                
        if score:
            points += 2 ** (score - 1)
print(points)
