from sys import argv
from util import getFnIn

def resValid(res, val, vals):
    """Returns True if response is a possible solution of multiplying/adding/concat to value."""
    # If no remaining vals, return True if value is expected response
    if not vals:
        return res == val
    # If the response is less than value return False
    if res < val:
        return False
    # Reursively check values
    nxt = vals[0]
    rem = vals[1:]
    return (
        resValid(res, val*nxt, rem) or
        resValid(res, val+nxt, rem) or
        resValid(res, int(str(val)+str(vals[0])), rem)
    )

# Parse response and values from input
# Increment by response if possible
ret = 0
fd = open(getFnIn(argv[1:]), 'r')
line = fd.readline().strip()
while line:
    splitLn = line.split(':')
    res = int(splitLn[0])
    vals = [int(val) for val in splitLn[1].strip().split()]
    if resValid(res, vals[0], vals[1:]):
        ret += res
    line = fd.readline().strip()

fd.close()

# Display result
print(ret)