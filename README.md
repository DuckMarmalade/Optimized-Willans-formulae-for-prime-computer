## Miller Rabin prime detection
```math
\mathrm{MR}_a(n) \iff \left( a^d \equiv 1 \pmod n \right)
\;\lor\;
\left( \exists r \in \{0, \dots, s-1\} : a^{2^r d} \equiv -1 \pmod n \right),
\quad\text{where } n-1 = 2^s d
```

## Probablistic-Determinstic Hybrid Miller Rabin prime detector M(n)

The function M(n) is defined as:

```math
M(n) =
\begin{cases}
\text{False}, & n < 2, \\[6pt]
\text{True}, & n \in S, \\[6pt]
\text{False}, & \exists p \in S : (p \mid n \ \wedge\ p \ne n), \\[8pt]
\displaystyle \bigwedge_{a \in W_{64}} MR_a(n), & n < 2^{64}, \\[12pt]
\displaystyle \bigwedge_{i = 1}^{k} MR_{a_i}(n), \quad a_i \sim \text{Unif}\{2, \ldots, n-2\}, & n \ge 2^{64}
\end{cases}

```
**Note:** S = {2,3,5,7,11,13,17,19,23,29,31,37\}, W<sub>64</sub>={2,325,9375,28178,450775,9780504,1795265022}

**Time Complexity:**  O(k (log n)³)

## Optimized Willan's Prime computer P(n)

The function P(n) is defined as:
```math
p_n = \sum_{m=1}^{B(n)} \mathbf{1}\!\left\{\,1 + \sum_{j=1}^m M(j) \le n\,\right\}.
```
```math
\text{Note: } B(n) \\ = n(\log n + \log\log n) + 3.
```
**Overall Time Complexity:**  O(n (log n)⁴)

# Explanation of Modified Willans Prime Computer

This project computes the **nth prime number** using a combination of:
- A fast **Miller–Rabin primality test**
- A **Rosser–Schoenfeld upper bound** for efficient searching
- A **modified Willans-style counting approach**

The implementation is optimized for correctness up to 64-bit integers and remains probabilistically reliable for larger values.

---

## 📌 Features

- Deterministic primality testing for all 64-bit integers
- Probabilistic testing for large numbers
- Efficient upper bound estimation for the nth prime
- Iterative counting method to extract the nth prime

---

## 📂 Function Explanations

---

### ✅ `is_prime(n)`

**Purpose:**  
Checks whether a given number `n` is prime using the **Miller–Rabin primality test**.

**How it works (brief):**
- Eliminates small numbers and small prime divisibility quickly.
- Decomposes `n-1` into the form `d × 2^s`.
- Uses:
  - A **deterministic witness set** for numbers less than `2^64`
  - A **probabilistic test** with 8 random bases for larger numbers

**Guarantees:**
- Exact correctness for all 64-bit integers
- Extremely low error probability beyond 64 bits

---

### ✅ `upper_bound_nth_prime(n)`

**Purpose:**  
Returns an **upper bound** large enough to guarantee that the nth prime lies below it.

**Method Used:**  
Rosser–Schoenfeld inequality: pₙ < n (log n + log log n)


**Why it’s needed:**  
This prevents unnecessary searching and ensures the loop in `modified_willans` terminates correctly.

---

### ✅ `modified_willans(n)`

**Purpose:**  
Computes the **nth prime number** using a modified Willans-style counting mechanism.

**How it works:**
1. Computes an upper bound `B(n)`
2. Iterates from `1` to `B(n)`
3. Counts primes using `is_prime`
4. Uses a counting indicator (`term`) to accumulate until the nth prime is reached
5. Terminates immediately once the nth prime is found

**Input Constraint:**  
- `n` must be ≥ 1

**Output:**  
- Returns the exact nth prime

---





