from sys import argv
from util import getFnIn

# Parse left and right list from input file into number of occurences
leftOcc = {}
rightOcc = {}
fd = open(getFnIn(argv[1:]), 'r')
for line in fd:
    [leftVal, rightVal] = [int(val) for val in line.strip().split('   ')]
    if leftVal not in leftOcc:
        leftOcc[leftVal] = 0
    leftOcc[leftVal] += 1
    if rightVal not in rightOcc:
        rightOcc[rightVal] = 0
    rightOcc[rightVal] += 1
fd.close()

# Calculate similarity score
# Score = Summation of each left value times the product of occurences
ret = 0
for val in leftOcc:
    if val in rightOcc:
        ret += val*leftOcc[val]*rightOcc[val]

# Display similarity score
print(ret)