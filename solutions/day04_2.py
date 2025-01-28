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
rw = 1

# Iterate through grid. For every 'A', check all directions for 'M-A-S' cross and increment count
while rw < len(grid):
    cl = 1
    while cl < len(grid[0]):
        if grid[rw][cl] == 'A':
            if (((grid[rw-1][cl-1] == 'M' and grid[rw+1][cl+1] == 'S') or (grid[rw-1][cl-1] == 'S' and grid[rw+1][cl+1] == 'M')) and
                ((grid[rw-1][cl+1] == 'M' and grid[rw+1][cl-1] == 'S') or (grid[rw-1][cl+1] == 'S' and grid[rw+1][cl-1] == 'M'))):
                ret += 1
        cl += 1
    rw += 1

# Display result
print(ret)