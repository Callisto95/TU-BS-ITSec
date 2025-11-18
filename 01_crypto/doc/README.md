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

Calculate

$$c0 \oplus c1 = (m0 \oplus k) \oplus (m1 \oplus k) = (k \oplus k) \oplus (m0 \oplus m1) = 0 \oplus (m0 \oplus m1) = m0 \oplus m1 = mx$$

Guess more and more of the key k to get the plaintext m0.

Once the key is known, decrypt using $c_0 \oplus k = m_0$ and $c_1 \oplus k = m_1$.

Since the decryption guesses the key k it is recovered.  
