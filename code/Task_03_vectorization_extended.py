"""Task 3 extended: (A) change the data size, (B) new case: VAT on transactions."""
import numpy as np, timeit

# ---------- PART A: change N ----------
print("PART A: speed-up for different sizes")
rng = np.random.default_rng(42)
for n in (1_000, 100_000, 1_000_000):
    data = rng.uniform(5, 250, n)
    def loop():
        out = []
        for v in data:
            out.append((v / 1000.0) ** 2)
        return out
    def vec():
        return (data / 1000.0) ** 2
    t_loop = timeit.timeit(loop, number=1)
    t_vec = timeit.timeit(vec, number=5) / 5
    print(f"N={n:>9,}: loop={t_loop:.5f}s vectorized={t_vec:.6f}s speed-up={t_loop/t_vec:.1f}x")

# ---------- PART B: new case ----------
# Assumptions: 1,000,000 shop sales in Kenya shillings (KES) between 50 and 20,000.
# VAT is 16 % and 1 USD = 129 KES (assumed fixed rate).
prices_kes = rng.uniform(50, 20000, 1_000_000)
vat = 0.16
rate = 129.0
total_with_vat = prices_kes * (1 + vat)
total_usd = total_with_vat / rate
print("\nPART B: VAT and currency conversion")
print("First three prices (KES)     :", np.round(prices_kes[:3], 2))
print("First three totals with VAT  :", np.round(total_with_vat[:3], 2))
print("First three totals (USD)     :", np.round(total_usd[:3], 2))
print(f"Total sales incl. VAT        : KES {total_with_vat.sum():,.0f}")
print(f"VAT collected                : KES {(prices_kes*vat).sum():,.0f}")
