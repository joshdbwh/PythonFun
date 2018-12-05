"""" Advent Day of Code Day 01 (https://adventofcode.com/2018) """

def firstDuplicateSet(a):
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)

    return -1

if __name__ == '__main__':
    with open('frequency.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += int(line)

    print("Part 1: " + str(count))

    counts = set()
    count = 0
    ind = 0
    while (True):
        count += int(lines[ind % len(lines)])
        if (count in counts):
            break
        counts.add(count)
        ind += 1

    print("Part 2: " + str(count))



