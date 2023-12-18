sum = 0

digits = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

starts = ['o', 't', 'f', 's', 'e', 'n']
keys = digits.keys()

def search(string, length, index):
    temp = ''
    for i in range(index, length):
        temp += (string[i])
        if temp in keys:
            return (digits[temp])
    return
    
with open('2023\day1\input.txt', 'r') as input:
    for line in input.read().splitlines():
        temp = []
        l = len(line)
        for i in range(l):
            if line[i].isdigit(): temp.append(int(line[i]))
            if line[i] in starts:
                digit = search(line, l, i)
                if digit: temp.append(digit)

        sum += temp[0] * 10 + temp[-1]


    print(sum)
