"""
benchmark_compare.py

Compares execution speed of:
  1. original Willans formula (willans_original)
  2. modified Willans (modified_willans)

Benchmark method A: simple wall-clock timing using time.perf_counter()
Benchmark method C: plot timing results for range of n using matplotlib

NOTE: The original Willans becomes extremely slow beyond n≈7.
The benchmark restricts original Willans to small n values.

To run:
  python3 benchmark_compare.py

Requirements:
  - matplotlib installed for plotting

Modify ranges below as desired.
"""

import time
import matplotlib.pyplot as plt

# import the two algorithms (assumes same directory)
from original_willans import willans_original
from modified_willans import modified_willans


def benchmark(n_values):
    results = []  # list of tuples: (n, t_original, t_modified, prime1, prime2)

    for n in n_values:
        print(f"Benchmarking n={n} ...")

        # --- time original Willans ---
        t0 = time.perf_counter()
        try:
            p1 = willans_original(n)
        except Exception as e:
            p1 = None
        t1 = time.perf_counter() - t0

        # --- time modified Willans ---
        t2 = time.perf_counter()
        p2 = modified_willans(n)
        t3 = time.perf_counter() - t2

        results.append((n, t1, t3, p1, p2))

    return results


def print_results(results):
    print("\nResults:")
    print("n\tOriginal(s)\tModified(s)\tp_original\tp_modified")
    for n, t1, t2, p1, p2 in results:
        print(f"{n}\t{t1:.6f}\t{t2:.6f}\t{p1}\t{p2}")


def plot_results(results):
    n_vals = [r[0] for r in results]
    orig_times = [r[1] for r in results]
    mod_times = [r[2] for r in results]

    plt.figure()
    plt.plot(n_vals, orig_times, marker='o')
    plt.plot(n_vals, mod_times, marker='x')
    plt.xlabel("n (nth prime)")
    plt.ylabel("time (seconds)")
    plt.title("Original Willans vs Modified Willans Speed Comparison")
    plt.legend(["Original", "Modified"])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # choose n range (small values only for original Willans)
    n_values = range(1, 1500)  # up to n=8 safe; beyond this original is too slow

    results = benchmark(n_values)
    print_results(results)
    plot_results(results)
