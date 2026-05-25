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
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r

        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    if old_r < 0:
        return -old_r, -old_s, -old_t

    return old_r, old_s, old_t


def modular_inverse(a: int, modulus: int) -> int:
    if modulus <= 0:
        raise ValueError("modulus must be positive")

    gcd, x, _ = extended_gcd(a, modulus)

    if gcd != 1:
        raise ValueError("inverse does not exist")

    return x % modulus
