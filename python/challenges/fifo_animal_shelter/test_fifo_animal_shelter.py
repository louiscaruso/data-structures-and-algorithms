from fifo_animal_shelter import  AnimalShelter, InvalidOperationError, Node

def test_enqueue():
  x = AnimalShelter()
  x.enqueue("dog")
  actual = x.start.value
  expected = "dog"
  assert actual == expected



def test_dequeue():
  x = AnimalShelter()
  x.enqueue("cat")
  actual = x.dequeue("cat")
  expected = "cat"
  assert actual == expected



def test_pref_dog_no_cat_no():
  x = AnimalShelter()
  x.enqueue("cat")
  x.enqueue("dog")
  actual = x.dequeue("zebra")
  expected = "null"
  assert actual == expected