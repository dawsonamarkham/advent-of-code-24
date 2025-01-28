from sys import argv
from util import getFnIn

# Parse input for node positions
fd = open(getFnIn(argv[1:]), 'r')
nodes = {}

line = fd.readline().strip()

colMin = 0
colMax = len(line)
rowMin = 0
rowMax = 0

while line:
    for ptr in range(colMax):
        if line[ptr] != '.':
            if line[ptr] not in nodes:
                nodes[line[ptr]] = []
            nodes[line[ptr]].append(rowMax*colMax+ptr)
    rowMax += 1
    line = fd.readline().strip()
fd.close()

antinodes = set()
for node in nodes:
    # Decode position value to (row, col)
    pnts = [(val//colMax, val%colMax) for val in nodes[node]]

    # For each pair of nodes, add antinodes
    for i in range(len(pnts)-1):
        for j in range(i+1, len(pnts)):
            deltaRw = pnts[i][0]-pnts[j][0]
            deltaCl = pnts[i][1]-pnts[j][1]

            nxtRw = pnts[i][0]+deltaRw
            nxtCl = pnts[i][1]+deltaCl
            if nxtRw >= rowMin and nxtRw < rowMax and nxtCl >= colMin and nxtCl < colMax:
                antinodes.add(nxtRw*colMax+nxtCl)

            nxtRw = pnts[j][0]-deltaRw
            nxtCl = pnts[j][1]-deltaCl
            if nxtRw >= rowMin and nxtRw < rowMax and nxtCl >= colMin and nxtCl < colMax:
                antinodes.add(nxtRw*colMax+nxtCl)


# Display number of antinodes
print(len(antinodes))