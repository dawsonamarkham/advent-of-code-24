from sys import argv
from util import getFnIn

# Parse input for ordering rules
# In ordering, the key must come before the values
rules = {}
fd = open(getFnIn(argv[1:]), 'r')
line = fd.readline().strip()
while line:
    [key, val] = [int(val) for val in line.split('|')]
    if key in rules:
        rules[key].add(val)
    else:
        rules[key] = {val}
    line = fd.readline().strip()

# Parse remaining input for update page numbers
ret = 0
line = fd.readline().strip()
while line:
    pages = [int(val) for val in line.split(',')]
    
    # Check that each page is not preceded by a page intended to follow it
    rPtr = 1
    isCorrect = True
    while rPtr < len(pages):
        if pages[rPtr] in rules:
            lPtr = 0
            while lPtr < rPtr:
                if pages[lPtr] in rules[pages[rPtr]]:
                    isCorrect = False
                    break
                lPtr += 1
        if not isCorrect:
            break
        rPtr += 1
    
    # Increment by middle page if no rules broken
    if isCorrect:
        ret += pages[len(pages)//2]

    line = fd.readline().strip()

fd.close()

# Display result
print(ret)