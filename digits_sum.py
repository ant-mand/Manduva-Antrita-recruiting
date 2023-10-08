def digits_sum(n: int) -> int:
    """
    Takes in a number and returns the sum of its
    individual decimal digits. Recursive algorithm.
    """
    if len(str(n)) == 1:
        return n
    else:
        first, rest = str(n)[0], str(n)[1:]
        total = int(first) + digits_sum(int(rest))
        return total
 