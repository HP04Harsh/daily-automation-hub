class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
head = a
def printList(node):
    while node is not None:
        print(node.data)
        node = node.next
    
# Adding a new node at the beginning of the linked list
newNode = Node(4)
newNode.next = head
head = newNode    

# Adding a new node at the end of the linked list
newNode1 = Node(0)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = newNode1

# Insertion at kth position
k = 2
newNode2 = Node(5)
curr = head
for i in range(k-1):
    curr = curr.next
newNode2.next = curr.next
curr.next = newNode2
  

# Deletion of a node at the end of the linked list
curr = head
while curr.next.next != None:
    curr = curr.next
curr.next = None    
printList(head)