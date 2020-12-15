from challenges.array_shift.array_shift import insert_array


def test_one():
	actual = insert_array([1,2,2,2,2,4], 4)
	expected = [1,2,2,4,2,2,4]
	assert actual == expected

def test_two():
	actual = insert_array([], 4)
	expected = [4]
	assert actual == expected