#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    chcnt = dict()
    for ch in s:
        chcnt[ch] = chcnt.get(ch, 0) + 1

    cnts = dict()
    for val in chcnt.values():
        cnts[val] = cnts.get(val, 0) + 1

    if len(cnts) == 1:
        return "YES"
    if len(cnts) > 2:
        return "NO"

    pairs = list(cnts.items())
    occur = pairs[0] if pairs[0][1] > pairs[1][1] else pairs[1]

    total = sum(key * val for key, val in cnts.items())

    if total == occur[0] * occur[1] + 1 or total == occur[0] * (occur[1] + 1) + 1:
        return "YES"
    else:
        return "NO"
