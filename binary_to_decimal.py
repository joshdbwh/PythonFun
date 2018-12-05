"""
Binary to Decimal Converter

   ...128     64      32      16      8       4       2       1
2^n...2^7    2^6     2^5      2^4    2^3     2^2     2^1     2^0

"""

def binary_to_decimal(binary):
    binary_conv = [int(i) for i in str(binary)]
    power = len(binary_conv)-1
    decimal = 0
    for i in binary_conv:
        if i == 1:
            decimal += pow(2, power)
            power -= 1
        else:
            power -= 1

    return decimal

if __name__ == '__main__':
    binary = int(input("Enter a binary number to convert to a decimal: "))
    print(f"decimal (base 10): {binary_to_decimal(binary)}")
