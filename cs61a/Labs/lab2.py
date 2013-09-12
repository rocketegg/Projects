#this is the last question

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def compose1(f, g):
        def h(x):
            return f(g(x))
        return h
    
    def nest(n):
        if (n == 0):
            return print
        if (n == 1):
            return f1

        k, r = 2, f1 #n >= 2 here
        while (k <= n):
            if (k % 3 == 1):
                r = compose1(f1, r)
            if (k % 3 == 2):
                r = compose1(f2, r)
            if (k % 3 == 0):
                r = compose1(f3, r)
            k = k + 1
        return r
    return nest

if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(cycle, globals(), True, __name__)
