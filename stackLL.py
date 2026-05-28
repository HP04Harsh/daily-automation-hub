class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

     def push(self,data):
        node1 = Node(data)
        node1.next = self.top
        self.top = node1
        self.length += 1    

     def pop(self):
        if self.top is None:
            return None
        x = self.top.data
        self.top = self.top.next
        self.length -= 1
        return x

     def getTop(self):
        if self.top is None:
            return None
        return self.top.data


     def size(self):
        return self.length                      