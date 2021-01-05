# Python program to merge a linked list into another at 
# alternate positions 
class LinkedList(object): 
    def __init__(self): 
    # head of list 
        self.head = None

    # Linked list Node 
    class Node(object): 
        def __init__(self, d): 
            self.data = d 
            self.next = None

    # Inserts a new Node at front of the list. 
    def push(self, new_data): 

    # 1 & 2: Allocate the Node & 
        # Put in the data 
        new_node = self.Node(new_data) 

        # 3. Make next of new Node as head 
        new_node.next = self.head 

        # 4. Move the head to point to new Node 
        self.head = new_node 

    # Main function that inserts nodes of linked list q into p at 
    # alternate positions. Since head of first list never changes 
    # and head of second list/ may change, we need single pointer 
    # for first list and double pointer for second list. 
    def merge(self, q): 
        p_curr = self.head 
        q_curr = q.head 

        # While there are available positions in p; 
        while p_curr != None and q_curr != None: 

            # Save next pointers 
            p_next = p_curr.next
            q_next = q_curr.next

            # make q_curr as next of p_curr 
            q_curr.next = p_next # change next pointer of q_curr 
            p_curr.next = q_curr # change next pointer of p_curr 

            # update current pointers for next iteration 
            p_curr = p_next 
            q_curr = q_next 
        q.head = q_curr 