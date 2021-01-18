class InvalidOperationError(BaseException):
    pass
class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
class Stack():
    def __init__(self,node = None):
        self.top = node
    def __str__(self):
        currentVal = self.top
        display_value = ''
        while currentVal:
            display_value += f'->{[currentVal.value]} '
            currentVal = currentVal.next
        return display_value
    def push(self,value):
        node_Add = Node(value)
        node_Add.next = self.top
        self.top =  node_Add
    def pop(self):
        if self.is_empty():
           raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = self.top.next
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
class PseudoQueue():
    def __init__(self,stack1 = None,stack2 = None):
        self.front = None
        self.rear = None
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self,value,stack = None):
        self.stack1.push(value)
    def dequeue(self, stack):
        stk_val_ret = 0
        added = []
        if stack:
            self.rear = stack.top
            current = self.rear
            while current.next is not None:
                added.append(current.value)
                stack.pop()
                current = current.next
            stk_val_ret = current
            stack.pop()
            while added:
                stack.push(added.pop(-1))
        return stk_val_ret.value
    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
if __name__ == "__main__":
    pq = PseudoQueue()
    pq.stack1.push(20)
    pq.stack1.push(15)
    pq.stack1.push(10)
    print(pq.stack1)
    pq.enqueue(5, pq.stack1)
    print(pq.stack1)
    print(pq.dequeue(pq.stack1))
    print(pq.stack1)