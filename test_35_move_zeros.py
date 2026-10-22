import importlib

module = importlib.import_module("35_move_zeros")

def test_move_zeros():
    assert module.move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert module.move_zeros_to_end([0, 0, 1]) == [1, 0, 0]