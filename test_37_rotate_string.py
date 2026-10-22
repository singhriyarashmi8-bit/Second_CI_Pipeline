import importlib

module = importlib.import_module("37_rotate_string")

def test_rotate_string():
    assert module.rotate_string("hello", 2) == "lohel"
    assert module.rotate_string("python", 3) == "honpyt"