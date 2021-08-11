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


from collections import defaultdict
from bisect import bisect_left


def solution(s, x):
    
    return x + s.count("+") // 2 - s.count("-")//2

if __name__ == "__main__":


    if 1:
        n = int(input())
        x = 0
        for _ in range(n):
            x = solution(input(),x)

        print(x)
