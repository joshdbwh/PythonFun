"""Trying my best to help someone on stackoverflow."""

def main():
    rows = int(input("What size multiplication table would you like (2-10): "))
    if rows <= 1 or rows > 10:
        print(" Invalid Entry - Enter a number between 2 - 10 ")
    else:
        counter = 0
        multiplication_table(rows, counter)


def multiplication_table(rows, counter):
    size = rows + 1
    for i in range(1, size):
        for nums in range(1, size):
            value = i * nums
            if value % 2 == 0:
                print(f'#{value}', sep=' ', end="\t")
            else:
                print(value, sep=' ', end="\t")
            counter += 1
            if counter % rows == 0:
                print()
            else:
                counter


main()
