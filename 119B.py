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


def find_shift(x1, x2, W, w0):
    # find if we can shift towards W | --- >-- |W
    # if yes then how much
    if w0 <= x1:
        return 0

    dx = w0 - x1
    if W - x2 >= dx:
        return dx
    return inf


def solution(x1, y1, x2, y2, W, H, w0, h0):
    # the idea is find if the table can be moved to the right with find_shift function
    # revert the view around y axis and apply the function and return min
    # do the same for y
    # return the min of dx and dy
    dx1 = find_shift(x1, x2, W, w0)
    dx2 = find_shift(W - x2, W - x1, W, w0)
    dx = min(dx1, dx2)

    dy1 = find_shift(y1, y2, H, h0)
    dy2 = find_shift(H - y2, H - y1, H, h0)
    dy = min(dy1, dy2)

    ans = min(dx, dy)
    if ans == inf:
        return -1

    return ans


def test(x1, y1, x2, y2, W, H, w0, h0):
    """8 5
    2 1 7 4
    4 2

    8 10
    4 5 7 8
    8 5

    5 4
    2 2 5 4
    3 3

    1 8
    0 3 1 6
    1 5
    """

    print(solution(x1, y1, x2, y2, W, H, w0, h0))


if __name__ == "__main__":
    """
    test(2,1,7,4, 8, 5, 4, 2)
    test(4,5,7,8, 8, 10, 8, 5)
    test(2,2,5,4, 5, 4, 3, 3)
    test(0,3,1,6, 1, 8, 1, 5)
    """

    n_tests = int(input())

    for _ in range(n_tests):
        W, H = read_int_vec(input())

        w0 = read_int_vec(input())
        wh = read_int_vec(input())
        S = 0
        S = max(S, H * (w0[-1] - w0[1]))
        S = max(S, H * (wh[-1] - wh[1]))

        h0 = read_int_vec(input())
        hw = read_int_vec(input())
        S = max(S, W * (h0[-1] - h0[1]))
        S = max(S, W * (hw[-1] - hw[1]))

        print(S)
