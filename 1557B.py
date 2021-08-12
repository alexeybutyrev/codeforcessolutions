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

from collections import defaultdict


def solution(A, k):
    # The idea is we find followers in the soreted array and if in the orriginal array that doesn't work we make a cut
    # then we check if we used more cuts than needed
    N = len(A)
    if N == k:
        return "YES"

    B = sorted(A)

    followers = defaultdict(lambda: inf)
    for i in range(N - 1):
        followers[B[i]] = B[i + 1]

    c = 1
    for i in range(1, N):
        if followers[A[i - 1]] != A[i]:
            c += 1
    return "YES" if c <= k else "NO"


def test():
    print(solution([6, 3, 4, 2, 1], 4))
    print(solution([1, -4, 0, -2], 2))
    print(solution([1, 2, 3, 4, 5], 1))


if __name__ == "__main__":
    # test()
    if 1:
        n_tests = int(input())
        for _ in range(n_tests):
            n, k = read_int_vec(input())
            A = read_int_vec(input())
            print(solution(A, k))
