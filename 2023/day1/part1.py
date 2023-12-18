with open('2023\day1\input.txt', 'r') as input:
    sum = 0
    for line in input.read().splitlines():
        for char in line:
            if char.isnumeric():
                first = char
                break

        for char in reversed(line):
            if char.isnumeric():
                last = char
                break
    
        sum += int(first + last)
print(sum)