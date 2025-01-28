from sys import argv
from util import getFnIn

# Initialize grid with border values
fd = open(getFnIn(argv[1:]), 'r')
line = fd.readline().strip()
grid = ['_'*(len(line)+2)]
while line:
    grid.append(f"_{line}_")
    line = fd.readline().strip()
grid.append('_'*len(grid[0]))
fd.close()


# Initialize values
ret = 0
wrd = 'XMAS'
rw = 1
offsets = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Iterate through grid. For every 'X', check all directions for 'XMAS' and increment count
while rw < len(grid):
    cl = 1
    while cl < len(grid[0]):
        if grid[rw][cl] == wrd[0]:
            for offset in offsets:
                ptr = 1
                while ptr < len(wrd) and wrd[ptr] == grid[rw+offset[0]*ptr][cl+offset[1]*ptr]:
                    ptr += 1
                if ptr == len(wrd):
                    ret += 1
        cl += 1
    rw += 1

# Display result
print(ret)