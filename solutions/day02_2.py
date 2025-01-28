from sys import argv
from util import getFnIn
from day02_1 import isSafe

# Count the number of 'safe' lines
# Including tolerance for single bad value
ret = 0
fd = open(getFnIn(argv[1:]), 'r')
for line in fd:
    vals = [int(val) for val in line.strip().split(' ')]

    # Check if line is safe when ignoring a single value
    for i in range(0, len(vals)):
        if isSafe(vals[:i]+vals[i+1:]):
            ret += 1
            break
fd.close()

# Display the number of safe rows
print(ret)