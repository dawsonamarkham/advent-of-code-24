from sys import argv
from util import getFnIn

def isSafe(arr):
    """Returns True if array is 'safe'.
    
    An array is safe if sorted in increasing or decreasing order
    and each element differs by 1-3 in value.
    """
    # Initialize
    ptr = 1
    diff = arr[ptr] - arr[ptr-1]
    ptr += 1

    # If within increasing range, check rest of array
    if diff > 0 and diff < 4:
        while ptr < len(arr) and diff > 0 and diff < 4:
            diff = arr[ptr] - arr[ptr-1]
            ptr += 1
        if diff > 0 and diff < 4:
            return True
    # Otherwise if within decreasing range, check rest of array
    elif diff < 0 and diff > -4:
        while ptr < len(arr) and diff < 0 and diff > -4:
            diff = arr[ptr] - arr[ptr-1]
            ptr += 1
        if diff < 0 and diff > -4:
            return True
    
    return False

# If running as main
if __name__ == "__main__":
    # Count the number of 'safe' lines
    ret = 0
    fd = open(getFnIn(argv[1:]), 'r')
    for line in fd:
        if isSafe([int(val) for val in line.strip().split(' ')]):
            ret += 1
    fd.close()

    # Display the number of safe rows
    print(ret)