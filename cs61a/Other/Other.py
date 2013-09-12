def high_low(number):
    """returns the difference between the largest and smallest digit in a 2+ digit number
    Does this using modulus and division

    >>> high_low(1947)
    8
    >>> high_low(184600)
    8
    >>> high_low(29647)
    7
    >>> high_low(111111)
    0
    >>> high_low(5)
    Traceback (most recent call last):
    AssertionError
    """
    assert(number > 9)

    high, low = -1, 10
    while (number > 0):
        digit = number % 10
        high = max(high, digit)
        low = min(low, digit)
        number //= 10
    return high - low

def high_low_string(number):
    """returns the difference between the largest and smallest digit in a 2+ digit number
    Does this using string conversion

    >>> high_low_string(1947)
    8
    >>> high_low_string(184600)
    8
    >>> high_low_string(29647)
    7
    >>> high_low_string(111111)
    0
    >>> high_low(5)
    Traceback (most recent call last):
    AssertionError
    """
    assert(number > 9)
    digitsString = str(number)
    listDigits = list(digitsString)
    high, low = int(max(listDigits)), int(min(listDigits))
    return high - low

if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(high_low, globals(), True, __name__)
    doctest.run_docstring_examples(high_low_string, globals(), True, __name__)
