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


def solution(A):
    # The itea is to calculate forward sums of rows then Bob's choice is max of left on the row1 and row2
    # the alison's goal is minimize that max
    m = len(A[0])
    F1 = [0]
    F2 = [0]
    for i in range(m):
        F1.append(F1[-1] + A[0][i])
        F2.append(F2[-1] + A[1][i])

    ans = F2[m]
    for i in range(m):
        S2 = F1[m] - F1[i + 1]
        S3 = F2[i]
        ans = min(ans, max(S3, S2))
    return ans


def test(A):
    print(solution(A))


if __name__ == "__main__":
    n_tests = int(input())
    read_int_vec = lambda x: [int(c) for c in x.split(" ")]
    for _ in range(n_tests):
        m = int(input())
        A = []
        for i in range(2):
            l = read_int_vec(input())
            A.append(l)
        print(solution(A))
