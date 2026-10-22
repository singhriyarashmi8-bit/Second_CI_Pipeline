import importlib

module = importlib.import_module("36_most_frequent")

def test_most_frequent():
    assert module.most_frequent([1, 2, 2, 3, 3, 3, 4]) == 3
    assert module.most_frequent(["apple", "banana", "apple"]) == "apple"