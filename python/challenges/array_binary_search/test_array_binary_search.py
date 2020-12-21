from array_binary_search.array_binary_search import binary_search

def test_binary_search():
	actual = binary_search([4,8,15,16,23,42], 15)
	expected = 2
	assert actual == expected
