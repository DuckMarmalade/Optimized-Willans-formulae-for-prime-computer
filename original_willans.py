import math

def wilsons_prime_detector(j):

    # Return 1 if j is prime, else 0.
    # Uses Wilson's theorem: for prime p, (p-1)! ≡ -1 (mod p).
    
    if j < 2:
        return 0

    fact_mod = 1
    # compute (j-1)! mod j
    for k in range(1, j):
        fact_mod = (fact_mod * k) % j
        # optimization: if factorial mod becomes 0 we already know j is composite
        # (for many composite j this will happen, though not for all, e.g. j=4).
        if fact_mod == 0:
            return 0

    # (fact_mod + 1) % j == 0  <=> (j-1)! ≡ -1 (mod j)
    return 1 if (fact_mod + 1) % j == 0 else 0


def willans_original(n):
    if n < 1:
        raise ValueError("n must be >= 1")

    # Simple upper bound for the nth prime: p_n < 2**n (this bound can be
    # shown using Bertrand's postulate by induction). Use B large enough.
    B = 2 ** n

    # count: running number of primes <= current m (π(m))
    count = 0 
    # total will accumulate the number of m such that π(m) + 1<= n.
    # That count equals p_n - 1, so we return 1 + total to get p_n.
    total = 0

    for m in range(1, B + 1):
        if wilsons_prime_detector(m) == 1:
            count += 1
        denom = 1 + count  # equals 1 + π(m)
        
        # term is an indicator: 1 if denom <= n else 0.
        # (equivalently: term = 1 if π(m) +1 <= n else 0)
        term = 1 if denom <= n else 0
        total += term
        if count >= n:# once we've seen n primes, total == p_n - 1, so return p_n
            return 1 + total
        

    raise RuntimeError("Bound was too small; increase B(n).")


print(willans_original(1000))
