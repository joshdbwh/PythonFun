"""" Advent Day of Code Day 02 (https://adventofcode.com/2018) """

if __name__ == '__main__':
    with open('strings.txt') as f:
        strings = f.readlines()

    two, three = 0, 0
    for l in strings:
        s = set([l.count(x) for x in l if l.count(x) > 1])

        for i in s:
            if i == 2:
                two += 1
            elif i == 3:
                three += 1

    print(two*three)

    from itertools import combinations, compress

    for one, two in combinations(strings, 2):
        diff = [e1 == e2 for e1, e2 in zip(one, two)]
        if sum(diff) == (len(one) - 1):
            res2 = ''.join(list(compress(one, diff)))
            break

    print(res2)
