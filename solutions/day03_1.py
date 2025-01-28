from sys import argv
from util import getFnIn

# Define state machine functions
# Sequence 'mul(AAA, BBB)' multiplies AAA*BBB and adds to sum
def startFunc(character, state):
    if character == 'm':
        state[0] = 1
        state[1] = 0
        state[2] = 0

def mul1(character, state):
    if character == 'u':
        state[0] = 2
    else:
        startFunc(character, state)

def mul2(character, state):
    if character == 'l':
        state[0] = 3
    else:
        startFunc(character, state)

def mul3(character, state):
    if character == '(':
        state[0] = 4
    else:
        startFunc(character, state)

def mul4(character, state):
    if character.isdigit():
        state[1] *= 10
        state[1] += int(character)
        if state[1] >= 1000:
            state[0] = 0
    elif character == ',' and state[1] > 0:
        state[0] = 5
    else:
        startFunc(character, state)

def mul5(character, state):
    if character.isdigit():
        state[2] *= 10
        state[2] += int(character)
        if state[2] >= 1000:
            state[0] = 0
    elif character == ')' and state[2] > 0:
        state[3] += state[1]*state[2]
        state[0] = 0
    else:
        startFunc(character, state)

# Initialize state machine and pass each character through machine
fd = open(getFnIn(argv[1:]), 'r')
ch = fd.read(1)
functions = [startFunc, mul1, mul2, mul3, mul4, mul5]
state = [0, 0, 0, 0]
while ch:
    functions[state[0]](ch, state)
    ch = fd.read(1)
fd.close()

# Display output of state machine
print(state[3])