import importlib

module = importlib.import_module("40_is_prime")

def test_is_prime_true():
    assert module.is_prime(11) is True
    assert module.is_prime(2) is True

def test_is_prime_false():
    assert module.is_prime(4) is False
    assert module.is_prime(1) is False