class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None
        self.prev = None

a= Node(1)
b= Node(2)
c= Node(3)

a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = a
a.prev = c

head = a

curr = head
while True:
    print(curr.data)
    curr = curr.next
    if curr == head:
        break