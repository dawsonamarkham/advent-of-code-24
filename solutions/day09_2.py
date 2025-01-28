from sys import argv
from util import getFnIn

# Parse input and create an array of blocks with the corresponding block index id 
# Blocks with id '-1' are empty
fd = open(getFnIn(argv[1:]), 'r')
ch = fd.read(1)
index = 0
blocks = []
while ch:
    if index%2:
        blocks += [-1]*int(ch)
    else:
        blocks += [index//2]*int(ch)
    ch = fd.read(1)
    index += 1
fd.close()

# Initialize variables
# Get left most freespace and rightmost occupied
lPtr = 0
while blocks[lPtr] != -1:
    lPtr += 1
rPtr = len(blocks) - 1

# Continue until pointers cross
while lPtr < rPtr:
    # Determine size of file (count blocks)
    size = 1
    while blocks[rPtr] == blocks[rPtr-size]:
        size += 1
    lim = rPtr-size
    
    # Determine amount of free space
    free = 1
    ptr = lPtr
    while free < size and ptr < lim:
        # Increment size of free space
        if blocks[ptr+free] == -1:
            free += 1
        # Find next set of free space if occupied block found
        else:
            ptr += free
            while ptr < lim and blocks[ptr] != -1:
                ptr += 1
            free = 1
    
    # If sufficient space found, move file
    if free == size:
        chng = blocks[rPtr]
        for i in range(size):
            blocks[ptr+i] = chng
            blocks[lim+i+1] = -1
        if ptr == lPtr:
            lPtr += free
            while lPtr < rPtr and blocks[lPtr] != -1:
                lPtr += 1
    
    # Find next file to move
    rPtr -= size
    while lPtr < rPtr and blocks[rPtr] == -1:
        rPtr -= 1

# Calculate and display checksum
ret = 0
for index in range(len(blocks)):
    if blocks[index] > 0:
        ret += blocks[index]*index
print(ret)