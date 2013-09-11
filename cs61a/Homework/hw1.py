# Q1.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

# Q2.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    return a*a + b*b + c*c - min(a,b,c) * min(a,b,c)

# Q3.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    return 0/0

def testif():
    """
    >>> with_if_statement()
    1
    >>> with_if_function()
    not 1
    """

# Q4.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while (n != 1):
        print(n)
        if (n % 2 == 0):
            n, count = n // 2, count + 1
        else: 
            n, count = n * 3 + 1, count + 1
    print(n)
    return count

if __name__ == '__main__':
    import doctest
    #doctest.run_docstring_examples(a_plus_abs_b, globals(), True, __name__)
    #doctest.run_docstring_examples(two_of_three, globals(), True, __name__)
    doctest.run_docstring_examples(testif, globals(), True, __name__)
    #doctest.run_docstring_examples(hailstone, globals(), True, __name__)



