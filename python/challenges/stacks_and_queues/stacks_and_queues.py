# worked with jae choi

class InvalidOperationError(BaseException):
    pass


class Node():

    def __init__(self, value):
        self.value = value


class Stack():

    def __init__(self, node = None):
        self.top = node
    def push(self, value):

    # create a node from value
        node = Node(value)
    # new Node to top
        node.next = self.top
    # assign node to top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        # create a temp node
        # assign to node top
        node = self.top
        # top and reassign to top.next
        self.top = self.top.next
        # return value of temp node
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


class Queue():

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            # add node to front
            self.front = node
        else:
            self.rear.next = node
            # in Queue you can only add to rear
        self.rear = node

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.front
        self.front = self.front.next
        # node.next = None
        return node.value
        
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False