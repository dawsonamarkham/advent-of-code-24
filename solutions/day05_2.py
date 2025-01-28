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
    
    # Correct incorrectly ordered pages
    rPtr = 1
    wasCorrected = False
    while rPtr < len(pages):
        if pages[rPtr] in rules:
            lPtr = 0
            while lPtr < rPtr:
                if pages[lPtr] in rules[pages[rPtr]]:
                    pages.insert(lPtr, pages[rPtr])
                    del pages[rPtr+1]
                    wasCorrected = True
                    break
                lPtr += 1
        rPtr += 1
    
    # Increment return by middle value if corrected
    if wasCorrected:
        ret += pages[len(pages)//2]

    line = fd.readline().strip()

fd.close()

# Display result
print(ret)