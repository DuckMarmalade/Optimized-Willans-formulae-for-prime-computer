import math
import random

def is_prime(n):
    """
    Deterministic + probabilistic Miller–Rabin primality test.
    Correct for all 64-bit integers. For numbers beyond 64 bits, uses
    probabilistic MR with 8 random bases.
    """
    # Handle small numbers
    if n < 2:
        return False

    # Quick elimination using small primes
    small_primes = (2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small_primes:
        if n == p:            # n is prime if it matches any small prime exactly
            return True
        if n % p == 0:        # divisible by a small prime → composite
            return False

    # n-1 is even and can be expressed as d * 2^s where d is odd.
    d = n - 1
    s = 0
    while d % 2 == 0:         # factor out the powers of 2
        d //= 2
        s += 1

    # Bases sufficient to deterministically verify primality < 2^64
    witnesses_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    # Single MR round for base a
    def check(a, d, n, s):
        x = pow(a, d, n)      # a^d mod n
        if x == 1 or x == n-1:
            return True       # passes this round
        for _ in range(s-1):
            x = (x * x) % n
            if x == n-1:
                return True   # strong witness(either n is prime or a is a liar)
        return False          # composite

    # Deterministic Miller-Rabin test for 64-bit values
    if n < (1 << 64):
        for a in witnesses_64:
            if a % n == 0:    # avoid false positive when a == multiple of n
                continue
            if not check(a, d, n, s):
                return False
        return True           # all checks passed → prime

    # Probabilistic Miller-Rabin for numbers larger than 64-bits
    k = 8                    # number of random rounds (conventional, for crypto purposes 20 is suggested)
    for _ in range(k):
        a = random.randrange(2, n-1)
        if not check(a, d, n, s):
            return False
    return True               # strong probable prime error rate is (0.25)^k

def upper_bound_nth_prime(n):
    """
    Returns an upper bound for the nth prime using the Rosser–Schoenfeld inequality.
    """
    if n < 6:
        return 15            # Safe value for very small n
    # bound of order nlogn
    return int(n * (math.log(n) + math.log(math.log(n)))) + 3

def modified_willans(n):
    """
    Modified Willans-like computation to obtain the nth prime.
    Iterates integers up to B(n), counting primes until the nth is reached.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    B = upper_bound_nth_prime(n)   # search bound
    count = 0                      # number of primes found so far
    total = 0

    # Iterate from 1 to B and count primes
    for m in range(1, B+1):
        if is_prime(m):            # check primality
            count += 1
        # term is an indicator: 1 if denom <= n else 0.
        # (equivalently: term = 1 if π(m) +1 <= n else 0)
        denom = 1 + count
        term = 1 if denom <= n else 0
        total += term

        if count >= n:             # stop once nth prime is reached
            return 1 + total

    # Should not happen if B(n) is sufficient
    raise RuntimeError("Bound B was too small; increase B(n).")


print(modified_willans(1000))   
