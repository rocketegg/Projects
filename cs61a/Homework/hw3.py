# Name:
# Email:

# All combinations addition
# provides sum combinations of n using int up to size m
def combinations(n, m):
    """
    >>> combinations(6, 4)
    9
    >>> combinations(5, 5)
    7
    >>> combinations(10, 10)
    42
    >>> combinations(15, 15)
    176
    >>> combinations(20, 20)
    627

    #3+1
    #1+1+1+1
    #1+2+1
    #2+2
    """
    if (n < 0 or m <= 0):
        return 0
    elif (m == 1):
        return 1
    else:
        return combinations(n-m, m) + combinations(n, m-1)

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    """
    g(5) = g(4) + 2*g(3) + 3*g(2) + 4*g(1)
    g(4) = g(3) + 2*g(2) + 3*g(1)
    g(3) = 3
    g(2) = 2
    g(1) = 1
    g(4) = 1*g(3)+
    """
    "*** YOUR CODE HERE ***"
    if (n <= 3):
        return n
    return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    gn1, gn2, gn3 = 3, 2, 1
    count, result = 3, n
    while (count < n):
        result = gn1 + 2*gn2 + 3*gn3
        gn3, gn2, gn1, count = gn2, gn1, result, count + 1
    return result

# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(17)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if (k == 0):
        return False
    elif (k % 10 == 7):
        return True
    else:
        return has_seven(k // 10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(100)
    2
    """
    """
    pingpong7
    ping0 = ping 1 + 1
    ping 1 = ping 2 + 1
    ping 2 = ping 3 + 1
    ping 3 = ping 4 + 1
    ping 4 = ping 5 + 1
    ping 6 = ping 7 + 1
    ping 7 = 1
    """
    "*** YOUR CODE HERE ***"
    def ping(num):
        #print ("ping: {}".format(num))
        if (num == n):
            return 1
        if (num % 7 == 0) or (has_seven(num)):
            return pong(num+1) + 1
        return ping(num+1) + 1

    def pong(num):
        #print ("pong: {}".format(num))
        if (num == n):
            return -1
        if (num % 7 == 0) or (has_seven(num)):
            return ping(num+1) - 1
        return pong(num+1) - 1

    #how to decide whether to call ping or pong first?
    return ping(1)
# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(319)
    1
    >>> ten_pairs(3195)
    1
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def get_num_pairs(n, remainder):
        if (n == 0):
            return 0
        elif (n % 10 + remainder == 10):
            return 1 + get_num_pairs(n//10, remainder)
        else:
            return get_num_pairs(n//10, remainder)

    if (n < 10):
        return 0
    return get_num_pairs(n // 10, n % 10) + ten_pairs(n // 10)
    

# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def get_denoms(n):
        x = 0
        while (pow(2,x) <= n):
            x = x + 1
        return x

    def combination_base2(n, m):
        if (n < 0):
            #print("   > BASE: return 0 on call combination_base({},{})".format(n,m))
            return 0
        if (m == 0):
            #print("   > BASE: return 1 on call combination_base({},{})".format(n,m))
            return 1
        else:
            #print("CALL: combination_base2({},{}) + combination_base2({},{})".format(
            #    n-log2x.get(m), m, n, m-1))
            return combination_base2(n-pow(2,m), m) + combination_base2(n, m-1)

    biggest = get_denoms(amount)
    return combination_base2(amount, biggest)

# Q6.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return YOUR_EXPRESSION_HERE


if __name__ == '__main__':
    import doctest
    
    #doctest.run_docstring_examples(combinations, globals(), True, __name__)
   #doctest.run_docstring_examples(has_seven, globals(), True, __name__)
    #doctest.run_docstring_examples(g, globals(), True, __name__)
    #doctest.run_docstring_examples(g_iter, globals(), True, __name__)
    #doctest.run_docstring_examples(pingpong, globals(), True, __name__)
    #doctest.run_docstring_examples(ten_pairs, globals(), True, __name__)
    doctest.run_docstring_examples(count_change, globals(), True, __name__)