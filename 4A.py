from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def solution(x):
    return 'YES' if x & 1 == 0 and x > 3 else 'NO'

if __name__ == '__main__':
    print(solution(int(input())))
