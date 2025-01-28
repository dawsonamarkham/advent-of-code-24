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
            antinodes.add(pnts[i][0]*colMax+pnts[i][1])
            antinodes.add(pnts[j][0]*colMax+pnts[j][1])
            deltaRw = pnts[i][0]-pnts[j][0]
            deltaCl = pnts[i][1]-pnts[j][1]

            nxtRw = pnts[i][0]+deltaRw
            nxtCl = pnts[i][1]+deltaCl
            while nxtRw >= rowMin and nxtRw < rowMax and nxtCl >= colMin and nxtCl < colMax:
                antinodes.add(nxtRw*colMax+nxtCl)
                nxtRw += deltaRw
                nxtCl += deltaCl

            nxtRw = pnts[j][0]-deltaRw
            nxtCl = pnts[j][1]-deltaCl
            while nxtRw >= rowMin and nxtRw < rowMax and nxtCl >= colMin and nxtCl < colMax:
                antinodes.add(nxtRw*colMax+nxtCl)
                nxtRw -= deltaRw
                nxtCl -= deltaCl


# Display number of antinodes
print(len(antinodes))