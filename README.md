# cryptalgs

Educational implementations of cryptographic algorithms and supporting math.

This repository is for learning and experimentation. Code in `cryptalgs/` should not be treated as production-ready cryptography unless a module explicitly says otherwise.

## Scope

First version:

- modular exponentiation
- extended Euclidean algorithm
- modular inverse
- Miller-Rabin primality test
- arithmetic in GF(p)
- toy RSA
- Diffie-Hellman
- HMAC-SHA256
- HKDF-SHA256
- constant-time comparison

Later:

- ChaCha20
- educational SHA-256
- practical examples using established libraries

## Layout

```text
cryptalgs/
  math/          number theory and finite-field arithmetic
  asymmetric/    toy RSA and Diffie-Hellman
  hashes/        hash-based constructions
  kdf/           key derivation functions
  symmetric/     symmetric primitives
  utils/         implementation utilities
tests/
```

## Development

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
```
