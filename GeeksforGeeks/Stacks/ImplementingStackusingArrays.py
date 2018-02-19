from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")
def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()

S = createStack()
push(S,str(10))
push(S,str(11))
push(S,str(12))
push(S,str(13))
print(S)
pop(S)
print(S)
pop(S)
pop(S)
pop(S)
pop(S)
pop(S)
print(S)

