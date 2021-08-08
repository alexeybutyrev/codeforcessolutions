from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def solution(S):
    return S if len(S) <= 10 else S[0] + str(len(S) - 2) +S[-1]

def test(s = "asdasdasdasdas"):
    return solution(s)
if __name__ == '__main__':
    print(test())
    if 0:
        n = int(input())
        for _ in range(n):
            print(solution(input()))
