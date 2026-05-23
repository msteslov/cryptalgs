"""Modular arithmetic primitives.

Planned:
- modular_pow
- extended_gcd
- modular_inverse
"""

def modular_pow(base: int, exponent: int, modulus: int) -> int:
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if exponent < 0:
        raise ValueError("exponent must be non-negative")

    r = 1
    while exponent != 0:
        if exponent % 2:
            r = r * base % modulus
        exponent //= 2
        base = base * base % modulus

    return r

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    pass

def modular_inverse(a: int, modulus: int) -> int:
    pass
