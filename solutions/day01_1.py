from sys import argv
from util import getFnIn

# Parse left and right list from input file
leftList = []
rightList = []
fd = open(getFnIn(argv[1:]), 'r')
for line in fd:
    split = line.strip().split('   ')
    leftList.append(int(split[0]))
    rightList.append(int(split[1]))
fd.close()

# Sort lists
leftList.sort()
rightList.sort()

# Find the sum of differences between list items
ret = 0
ptr = 0
while ptr < len(leftList):
    ret += abs(leftList[ptr]-rightList[ptr])
    ptr += 1

# Display sum
print(ret)