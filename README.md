## Miller Rabin prime detection
```math
\mathrm{MR}_a(n) \iff \left( a^d \equiv 1 \pmod n \right)
\;\lor\;
\left( \exists r \in \{0, \dots, s-1\} : a^{2^r d} \equiv -1 \pmod n \right),
\quad\text{where } n-1 = 2^s d
```

## Definition of M(n)

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

## Optimized Willan's Prime computer P(n)

The function P(n) is defined as:
```math
p_n = \sum_{m=1}^{B(n)} \mathbf{1}\!\left\{\,1 + \sum_{j=1}^m M(j) \le n\,\right\}.
```
```math
\text{Note: } B(n) \\ = n(\log n + \log\log n) + 3.
```
