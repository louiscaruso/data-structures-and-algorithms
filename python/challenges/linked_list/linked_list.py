# Code from class demo
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head, values=None):
        self.head = None
    
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node