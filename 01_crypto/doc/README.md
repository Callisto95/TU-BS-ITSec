# Report

## 1. Security Goals

### a

- idk
- Privacy
- Integrity

### b

- idk

## 2. Key Space

Set of possible values for $K_E$ and $K_D$.

### ROT13

0, since there's no key. The same function is always used.

### Vigènere with key length of n

Assuming only letters in the latin alphabet, $26^n$.

This is because $K_E$ and $K_D$ are the same and are simple words made up by 26 letters of length n.

### AES with 256-bit key

$2^{256}$, because AES is a symmetric key cipher.

### Monoalphabetic substitution with k letters

$k^n$.

It's a symmetric cipher with k base values of length n.

## 3. XOR

Calculate `c0 X c1 = (m0 X k) X (m1 X k) = m0 X m1 = mx`.

Guess part of the key to get a part of the plaintext of m0.
