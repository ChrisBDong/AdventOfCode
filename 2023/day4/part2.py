points = 0
start = 1
cardNum = 0
cardValue = [0 for i in range(196)]
cardCount = [1 for i in range(196)]

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
                right.remove(i)
                
        cardValue[cardNum] = score
        cardNum += 1
    
    for i in range(196):
        for j in range(i+1, i+1+cardValue[i]):
            cardCount[j] += cardCount[i]

print(sum(cardCount))