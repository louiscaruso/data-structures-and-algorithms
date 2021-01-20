import pytest
from multi_bracket_validation.multi_bracket_validation import bracket_type


def test_curly():
    string = '{}'
    actual = bracket_type(string)
    expected = True
    assert actual == expected

def test_square_bracket():
    string = '[]'
    actual = bracket_type(string)
    expected = True
    assert actual == expected

def round_bracket():
    string = '()'
    actual = bracket_type(string)
    expected = True
    assert actual == expected

def test_two_brackets():
    string = '[]()'
    actual = bracket_type(string)
    expected = True
    assert actual == expected

def test_one_false():
    string = '[)'
    actual = bracket_type(string)
    expected = False
    assert actual == expected    

def test_two_false():
    string = '[)(]'
    actual = bracket_type(string)
    expected = False
    assert actual == expected


def test_weird_placement():
    string = '{[}()]'
    actual = bracket_type(string)
    expected = False
    assert actual == expected
