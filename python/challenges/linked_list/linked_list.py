# Code from class demo
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        # { a } -> { b } -> { c } -> NULL"

        output = ''
        current = self.head

        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'None'

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

# code from mob coding
    def append_node(self, value):
        new_node = Node(value, next=None)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert_before(self, value, newVal):
        current_node = self.head
        if current_node.next is None:
            return "No Node Available"
        ll = LinkedList(current_node)
        if ll.includes(value) is False:
            return "Value does not exist!"
        while current_node.next is True:
            if current_node.next.value == value:
                current_node.next = Node(newVal, current_node.next)
            else:
                current_node = current_node.next        


if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    # print(new_linked)

    new_linked1 = LinkedList(new_node)
    new_linked1.insert(2)
    # print(new_linked1.includes(2))
    # print(new_linked1.includes(4))
    print(new_linked1)

    # test insert method
    new_linked2 = LinkedList(new_node)
    new_linked2.insert(2) 
    new_linked2.insert(3) 
    new_linked2.insert(4) 
    print(new_linked2.includes(3))
    print(new_linked2.insert_before(3, 10))
    print(new_linked2) # to see the value of inserted value 2

    # # test includes
    # new_linked1 = LinkedList(new_node)
    # new_linked1.insert(2) 
    # # print(new_linked1.includes(2))
    # # print(new_linked1.includes(5))
    # print(new_linked1.head.value) # to see if it includes values (boolean)

    # new_linked2 = LinkedList(new_node)
    # print(new_linked2.insert_before(1, 10))
    # print(new_linked2) 
