def manachers(s: str) -> str:
    """
        Return longest palindrome
        also p contains all the possible palindromes
    """

    # modify string to cover edge cases
    # aab -> ^#a#a#b$
    t = "^#" + "#".join(list(s)) + "#$"
    Nt = len(t)
    p = [0] * Nt
    d = 1
    c = 1
    for i in range(2,Nt-1):

        # initialize p[i] as mirror if possible (it's inside the range) otherwise 0 
        mirror = 2 * c - i # c - (i - c) 
        p[i] = max(0, min(d-i,p[mirror]))

        while t[i+p[i]+1] == t[i-p[i]-1]:
            p[i] += 1

        if p[i] + i > d:
            d = p[i] + i
            c = i

    # find logest
    # note: p[i] is radius of the maximum palidrome
    r,i = max([ (r,i) for i,r in enumerate(p)])
    l, r = (i - r) // 2, (i + r) //2

    # the idea of praising palindromes like “aa” and “aba” for the case of “aa” the middle (i) would be # otherwise it would be a letter
    # we need to treat those cases differently  
    return s[l:r] 
if __name__ == '__main__':
    print(manachers("none"))
    print(manachers("abb")) 
    print(manachers("ccc")) 
    print(manachers("bab"))
    print(manachers("aba"))
    print(manachers("a"))
 