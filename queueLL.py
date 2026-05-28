class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def enqueue(self, value):
        node1 = Node(value)

        if self.tail is None:
            self.head = node1
            self.tail = node1
        else:
            self.tail.next = node1
            self.tail = node1
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None

        x = self.head.value
        self.head = self.head.next
        self.length -= 1

        if self.head is None:
            self.tail = None
        return x


    def getFront(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.length                            


