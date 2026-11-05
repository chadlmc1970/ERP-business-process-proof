"""Is S really different from T+, or is the gap inside seed noise? Same invoices per seed, 10 seeds.

Also separates the two levers: changing the rule (T+ to S) and cleaning the buyer's records (S to Sc).
"""
import statistics

import final_test as f

SEEDS = range(1, 11)
print("Paired differences over 10 seeds, per 100,000 synthetic invoices. Positive means the second policy is cheaper.\n")
print("| World | Pair | Measure | Mean | Std dev of pair | Seeds second is cheaper |\n|---|---|---|---|---|---|")
for name, over in [("step 2", f.S2), ("step 3", f.S3), ("step 3, 5% padders", dict(f.S3, opportunist=0.05))]:
    rows = [f.scenario(over, seeds=(s,), pols=("T+", "S", "Tc", "Sc"), suppliers=200) for s in SEEDS]
    spend = statistics.mean(r["S"]["spend"] for r in rows)
    for a, b in (("T+", "S"), ("S", "Sc"), ("Tc", "Sc")):
        for m in ("buyer_total", "joint_total", "overpaid"):
            d = [r[a][m] - r[b][m] for r in rows]
            print(f"| {name} | {a} to {b} | {m} | {statistics.mean(d):,.0f} | {statistics.stdev(d):,.0f} | {sum(x > 0 for x in d)}/10 |")
    print(f"| {name} | | spend per 100,000 invoices | {spend:,.0f} | | |")
