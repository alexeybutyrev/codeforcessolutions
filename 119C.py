from __future__ import division, print_function
from math import inf
import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

read_int_vec = lambda x: [int(c) for c in x.split(" ")]

from math import inf, sqrt
from itertools import groupby
def solution(s,n,k,x):
    x -= 1
    s = list(s)
    s = s[::-1]
    i = 0
    res = []
    while i < n:
        if s[i] == "a":
            res.append("a")
        else:
            j = i
            while j + 1 < n and s[j+1] == s[i]:
                j += 1
            curr = (j-i+1) * k + 1
            res.append('b' * (x % curr))
            x //= curr
            i = j
        i += 1
    return "".join(res[::-1])

if __name__ == "__main__":
    """
    test(2,1,7,4, 8, 5, 4, 2)
    test(4,5,7,8, 8, 10, 8, 5)
    test(2,2,5,4, 5, 4, 3, 3)
    test(0,3,1,6, 1, 8, 1, 5)
    """
    n_tests = int(input())

    for _ in range(n_tests):
        n,k,x  = read_int_vec(input())
        s = input()
        print(solution(s,n,k,x))