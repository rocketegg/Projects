# Name:
# Email:

def next(x):
    return x + 1

def identity(x):
    return x

def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    k, result = 1, 1
    while (k <= n):
        result, k = result * term(k), next(k)
    return result


def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    """
    "*** YOUR CODE HERE ***"
    return product(n, identity)

# Q2.

from operator import add, mul
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    """ Combiner = a function
        term = a function
        start = base value to use to start the accumulation
        n = n terms to accumulate
    """
    "*** YOUR CODE HERE ***"
    k, result = 1, start
    while (k <= n):
        result = combiner(result, term(k))
        k = next(k)
    return result

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    >>> summation_using_accumulate(3, square)
    14
    >>> summation_using_accumulate(5, identity)
    15
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(3, square)
    36
    
    #same as factorial

    >>> product_using_accumulate(4, identity)
    24

    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)

# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"


# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    "*** YOUR CODE HERE ***"


def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

# Q5.

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"

def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    """
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> three = successor(two)
    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> three = successor(two)
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    import doctest
    #doctest.run_docstring_examples(a_plus_abs_b, globals(), True, __name__)
    #doctest.run_docstring_examples(two_of_three, globals(), True, __name__)
    #doctest.run_docstring_examples(product, globals(), True, __name__)
    #doctest.run_docstring_examples(factorial, globals(), True, __name__)
    #doctest.run_docstring_examples(summation_using_accumulate, globals(), True, __name__)
    doctest.run_docstring_examples(product_using_accumulate, globals(), True, __name__)
