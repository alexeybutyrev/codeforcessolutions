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


def solution(s, t):
    if not t:
        return "YES"
    n, m = len(s), len(t)
    if n < m:
        return "NO"

    q = k = 0
    for i in range((n - m) & 1, n):
        if k == 1:
            k = 0
            continue
        if q < m and s[i] == t[q]:
            q += 1
        else:
            k += 1

    return "YES" if q == m else "NO"


def test():
    """4
    ababa
    ba
    ababa
    bb
    aaa
    aaaa
    aababa
    ababa

    YES
    NO
    NO
    YES
    """

    print(solution("ababa", "ba"))
    print(solution("ababa", "bb"))
    print(solution("aaa", "aaaa"))
    print(solution("aababa", "ababa"))


if __name__ == "__main__":

    # test()

    if 1:
        n_tests = int(input())

        for _ in range(n_tests):
            s = input()
            t = input()

            print(solution(s, t))
