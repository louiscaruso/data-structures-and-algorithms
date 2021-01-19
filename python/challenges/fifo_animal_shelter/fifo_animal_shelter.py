class InvalidOperationError(BaseException):
    pass


class Node():
    def __init__(self, value, next = None):
      self.value = value
      self.next = next
        


    
class AnimalShelter():
    def __init__(self):  
        self.start = None
        self.end = None

    def __str__(self):
      current = self.start
      output = ""
      while current:
        output += f' {current.value}'
        current =  current.next
      return output



    def enqueue(self, animal):
    
      node = Node(animal)
      if not self.start:
          self.start = node
          self.end = node

      else:
          self.end.next = node
          self.end = self.end.next

  
    def dequeue(self, choice = None):
      if self.is_empty():
          raise InvalidOperationError("Method not allowed on empty collection")

      if choice == "dog" or choice == "cat":
        current = self.start
      elif choice != "dog" or choice != "cat":
        return "null"

  
      if current.value == choice:
          node = current
          self.start = self.start.next
          return node.value
      else:
          while current.next.value is not choice:
            current = current.next
          ret_value = current.next.value
          current.next = current.next.next
          return current.value

    
    def is_empty(self):
      if self.start == None:
          return True
      else:
          return False

  

if __name__ == "__main__":
  x = AnimalShelter()
  x.enqueue("dog")
  x.enqueue("cat")
  x.enqueue("dog")
  x.enqueue("dog")
  x.enqueue("dog")
  x.enqueue("cat")

  print(str(x))
  x.dequeue("cat")
  print(str(x))

