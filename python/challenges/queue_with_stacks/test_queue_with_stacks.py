from queue_with_stacks import InvalidOperationError, Node, Stack, PseudoQueue

def test_enqueue():
    pq = PseudoQueue()
    pq.enqueue(5)
    actual = pq.stack1.top.value
    expected = 5
    assert actual == expected
def test_dequeue():
    pq = PseudoQueue()
    pq.stack1.push(20)
    pq.stack1.push(15)
    pq.stack1.push(10)
    actual = pq.dequeue(pq.stack1)
    expected = 20
    assert expected == actual
    actual = str(pq.stack1)
    expected = '->[10] ->[15] '
    assert expected == actual





