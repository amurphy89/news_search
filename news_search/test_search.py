import pytest

from search import search


@pytest.mark.parametrize("search_type, terms, expected", [
    ("or", ["Care", "Quality", "Commission"], [0, 1, 2, 3, 4, 5, 6]),
    ("or", ["September", "2004"], [9]),
    ("or", ["general", "population", "generally"], [6, 8]),
    ("and", ["Care", "Quality", "Commission", "admission"], [1]),
    ("and", ["general", "population", "Alzheimer"], [6])
])
def test_criteria(search_type, terms, expected):

    assert search(search_type, terms) == expected
