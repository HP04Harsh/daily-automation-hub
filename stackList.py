stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

def getTop():
    if len(stack) == 0:
        return None
    return stack[-1]    

def size():
    return len(stack)


    