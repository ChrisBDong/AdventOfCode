rgb = {
    "red":12,
    "green":13,
    "blue":14
}
output = 0

def checkValid(bag: list[int]):
    
    l = len(bag)
    for hand in range(0, l, 2):
        if int(bag[hand]) > rgb[bag[hand + 1]]:
            return False
    return True

with open('2023\day2\input.txt', 'r') as input:
    for game in input.read().splitlines():
        n = game.replace(':', '').replace(';', '').replace(',', '')
        bag = n.split(' ')[2:]
        if checkValid(bag):
            output += int(n.split(' ')[1])
print(output)