"""Task 11 extended: (A) change cash flows, (B) new case: loan interest rate."""
from scipy.optimize import root_scalar

def irr(cash):
    npv = lambda r: sum(cf/(1+r)**t for t, cf in enumerate(cash))
    d = lambda r: sum(-t*cf/(1+r)**(t+1) for t, cf in enumerate(cash) if t > 0)
    n = root_scalar(npv, fprime=d, x0=0.1, method="newton", xtol=1e-12)
    s = root_scalar(npv, x0=0.05, x1=0.2, method="secant", xtol=1e-12)
    return n, s

# ---------- PART A: change the initial investment 10000 -> 12000 ----------
print("PART A: IRR when investment rises")
for cash in ([-10000, 3000, 3500, 4000, 2500], [-12000, 3000, 3500, 4000, 2500]):
    n, s = irr(cash)
    print(f"Investment {-cash[0]}: IRR Newton={n.root:.4%} ({n.iterations} its), Secant={s.root:.4%} ({s.iterations} its)")

# ---------- PART B: new case ----------
# Assumptions: a customer borrows KES 100,000 and repays KES 9,000 monthly for 12 months.
# The monthly rate r makes the present value of repayments equal the loan.
cash = [-100000] + [9000]*12
npv = lambda r: sum(cf/(1+r)**t for t, cf in enumerate(cash))
d = lambda r: sum(-t*cf/(1+r)**(t+1) for t, cf in enumerate(cash) if t > 0)
n = root_scalar(npv, fprime=d, x0=0.02, method="newton", xtol=1e-12)
s = root_scalar(npv, x0=0.01, x1=0.03, method="secant", xtol=1e-12)
print("\nPART B: loan interest rate")
print(f"Monthly rate Newton={n.root:.4%}, Secant={s.root:.4%}")
print(f"Nominal annual rate = {12*n.root:.2%}, effective annual = {(1+n.root)**12-1:.2%}")
print(f"Total repaid = KES {sum(cash[1:]):,}, interest paid = KES {sum(cash[1:])+cash[0]:,}")
