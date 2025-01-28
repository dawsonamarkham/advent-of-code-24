from sys import argv
from util import getFnIn

# Parse input into array of integers
# Even indexes represent filled blocks and odds represent empty blocks
fd = open(getFnIn(argv[1:]), 'r')
arr = []
ch = fd.read(1)
while ch:
    arr.append(int(ch))
    ch = fd.read(1)
fd.close()

# Initialize variables
ret = 0
lPtr = 0
rPtr = len(arr) - 1
isFilling = False
index = 0

# Continue until pointers cross
while lPtr < rPtr:
    # If not currently filling blocks, continue through occupied blocks
    if not isFilling:
        # If occupied blocks remaining, continue to next index
        if arr[lPtr]:
            arr[lPtr] -= 1
            ret += index*(lPtr//2)
            index += 1
        # Otherwise, move to next set of unoccupied blocks
        else:
            isFilling = True
            lPtr += 1
    # Otherwise, fill unoccupied blocks
    else:
        # If unoccupied blocks and rightmost blocks remain, move and continue
        if arr[lPtr] and arr[rPtr]:
            arr[lPtr] -= 1
            arr[rPtr] -= 1
            ret += index*(rPtr//2)
            index += 1
        # Otherwise if only unoccupied blocks remain, move to next set of rightmost blocks
        elif arr[lPtr]:
            rPtr -= 2
        # Otherwise, move to occupied blocks
        else:
            isFilling = False
            lPtr += 1

# If not filling and occupied blocks remain, continue to end of set
if not isFilling:
    while arr[lPtr]:
        arr[lPtr] -= 1
        ret += index*(lPtr//2)
        index += 1

# Display return value
print(ret)