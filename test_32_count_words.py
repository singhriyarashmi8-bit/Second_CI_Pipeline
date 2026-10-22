import importlib

module = importlib.import_module("32_count_words")

def test_count_words_basic():
    assert module.count_words("Hello world") == 2

def test_count_words_multiple_spaces():
    assert module.count_words("  Python is awesome  ") == 3

def test_count_words_empty():
    assert module.count_words("") == 0