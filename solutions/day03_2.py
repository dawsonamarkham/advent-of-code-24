from sys import argv
from util import getFnIn

# Define state machine functions
# Sequence 'mul(AAA, BBB)' multiplies AAA*BBB and adds to sum
# Sequence 'do()' enables future 'mul(AAA, BBB)'
# Sequence 'don't()' disables future 'mul(AAA, BBB)'
def startFunc(character, state):
    if character == 'm' and state[1]:
        state[0] = 1
        state[2] = 0
        state[3] = 0
    elif ch == 'd':
        state[0] = 6
    else:
        state[0] = 0

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
        state[2] *= 10
        state[2] += int(character)
        if state[2] >= 1000:
            state[0] = 0
    elif character == ',' and state[2] > 0:
        state[0] = 5
    else:
        startFunc(character, state)

def mul5(character, state):
    if character.isdigit():
        state[3] *= 10
        state[3] += int(character)
        if state[3] >= 1000:
            state[0] = 0
    elif character == ')' and state[3] > 0:
        state[4] += state[2]*state[3]
        state[0] = 0
    else:
        startFunc(character, state)

def toggle1(character, state):
    if character == 'o':
        state[0] = 7
    else:
        startFunc(character, state)

def toggle2(character, state):
    if character == '(':
        state[0] = 8
    elif character == 'n':
        state[0] = 9
    else:
        startFunc(character, state)

def toggle3(character, state):
    if character == ')':
        state[1] = True
        state[0] = 0
    else:
        startFunc(character, state)

def toggle4(character, state):
    if character == '\'':
        state[0] = 10
    else:
        startFunc(character, state)

def toggle5(character, state):
    if character == 't':
        state[0] = 11
    else:
        startFunc(character, state)

def toggle6(character, state):
    if character == '(':
        state[0] = 12
    else:
        startFunc(character, state)

def toggle7(character, state):
    if character == ')':
        state[1] = False
        state[0] = 0
    else:
        startFunc(character, state)

# Initialize state machine and pass each character through machine
fd = open(getFnIn(argv[1:]), 'r')
ch = fd.read(1)
functions = [startFunc, mul1, mul2, mul3, mul4, mul5, toggle1, toggle2, toggle3, toggle4, toggle5, toggle6, toggle7]
state = [0, True, 0, 0, 0]
while ch:
    functions[state[0]](ch, state)
    ch = fd.read(1)
fd.close()

# Display output of state machine
print(state[4])
