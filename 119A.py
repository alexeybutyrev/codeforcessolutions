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
    UF = {}
    def find(x):
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x,y):
        UF.setdefault(x,x)
        UF.setdefault(y,y)
        UF[find(x)] = find(y)
    
    N = len(S)
    for i in range(N-1):
        union(i,i)
        if S[i] == "E":
            union(i,i+1)
    union(N-1,N-1)
    if S[N-1] == "E":
        union(0,N-1)
    for i in range(N-1):
        if S[i] == "N":
            if find(i) == find(i+1):
                return 'NO' 
    if S[N-1] == "N" and find(0) == find(N-1):
        return 'NO'
    return 'YES'
def test(s = "asdasdasdasdas"):
    return solution(s)
if __name__ == '__main__':
    
#    print(solution('EEE'))
#    print(solution('EN'))
#    print(solution('ENNEENE'))
#    print(solution('NENN'))
    if 1:
        n = int(input())
        for _ in range(n):
            print(solution(input()))
