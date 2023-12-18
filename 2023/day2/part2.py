rgb = {
    "red":0,
    "green":1,
    "blue":2
}
output = 0

def findMinimum(bag: list[int]):
    cubes = [0, 0, 0]
    l = len(bag)
    for hand in range(0, l, 2):
        cubes[rgb[bag[hand + 1]]] = max(int(bag[hand]), cubes[rgb[bag[hand + 1]]])

    return cubes[0] * cubes[1] * cubes[2]


with open('2023\day2\input.txt', 'r') as input:
    for game in input.read().splitlines():
        n = game.replace(':', '').replace(';', '').replace(',', '')
        bag = n.split(' ')[2:]
        output += findMinimum(bag)
print(output)