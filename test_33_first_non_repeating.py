import importlib

module = importlib.import_module("33_first_non_repeating")

def test_first_non_repeating():
    assert module.first_non_repeating_char("swiss") == "w"
    assert module.first_non_repeating_char("aabbcc") is None