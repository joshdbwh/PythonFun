# FizzBuzz, a classic.

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    [1, n]
    multiple of 3, Fizz
    multiple of 5, Buzz
    multiple of 3 and 5, FizzBuzz
    """
    if n == 1:
        return ["1"]
    ln = []
    for j in range(1, n+1):
        if j % 5 == 0 and j % 3 == 0:
            ln.append("FizzBuzz")
        elif j % 5 == 0:
            ln.append("Buzz")
        elif j % 3 == 0:
            ln.append("Fizz")
        else:
            ln.append(str(j))
    return ln


#TODO: Can I make it run a little faster?
def fizzBuzzV2(n):
    """
    :type n: int
    :rtype: List[str]
    [1, n]
    multiple of 3, Fizz
    multiple of 5, Buzz
    multiple of 3 and 5, FizzBuzz
    """

    if n == 1:
        return ["1"]
    ln = list(range(1, n+1))
    print(ln)
    for j in range(len(ln)):
        print(ln[j])
        if j % 5 == 0 and j % 3 == 0:
            ln[j] = "FizzBuzz"
        elif j % 5 == 0:
            ln[j] = "Buzz"
        elif j % 3 == 0:
            ln[j] = "Fizz"
        else:
            ln[j] = str(j)
    return ln


if __name__ == "__main__":
    import timeit
    num = int(input("Enter n: "))
    start_time = timeit.default_timer()
    print(fizzBuzz(num))
    trial1 = timeit.default_timer() - start_time

    start_time1 = timeit.default_timer()
    print(fizzBuzzV2(num))
    trial2 = timeit.default_timer() - start_time1

    if trial2 < trial1:
        print(f"trial 2 is faster by {trial1 - trial2}.")
    else:
        print(f"trial 1 is faster by {trial2 - trial1}.")