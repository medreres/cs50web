from prime import is_prime


def test_prime(n: int, expected: int):
    if is_prime(n) != expected:
        return print(f"Error, on is_prime({n}), expected {expected}")
