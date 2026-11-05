"""Exhaustive check of the logic behind lesser-of settlement, over a grid of integer amounts.

T is what is truly owed, E the buyer's record, I the supplier's invoice. These are checks of
arithmetic, not of business outcomes. Gate model: pay I when E and I agree within tol,
otherwise a person pays T (the most favorable assumption for the gate).
"""
R = range(0, 41)
TOL = 2


def gate(T, E, I):
    return I if abs(I - E) <= TOL else T


def lesser(E, I):
    return min(E, I)


cases = worse = single = 0
worst_over_gate = 0
for T in R:
    for E in R:
        for I in R:
            cases += 1
            over_l = max(lesser(E, I) - T, 0)
            over_g = max(gate(T, E, I) - T, 0)
            over_ers = max(E - T, 0)
            assert over_l <= max(I - T, 0) and over_l <= over_ers
            # an overpayment needs BOTH records to be too high
            assert (over_l > 0) == (E > T and I > T)
            if E == T or I == T:
                single += 1
                assert over_l == 0
            if over_l > over_g:
                worse += 1
                assert E > T and I > T and abs(I - E) > TOL
                worst_over_gate = max(worst_over_gate, over_l)
            # every shortfall is visible to the party it hurts
            assert (T - lesser(E, I) > 0) == (E < T or I < T)

print(f"cases checked: {cases:,}")
print("P1 pays no more than the invoice and no more than ERS: holds in every case")
print("P2 overpayment occurs if and only if both records are too high: holds in every case")
print(f"P3 any single wrong record never causes overpayment: holds in all {single:,} such cases")
print(f"P4 lesser-of overpays more than a perfect gate in {worse:,} cases ({worse / cases:.1%} of the grid), "
      "all with both records too high and more than tolerance apart")
print("P5 every shortfall comes from a record below the truth, so the supplier is the party hurt")
