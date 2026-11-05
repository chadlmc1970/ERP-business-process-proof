"""Second test: who ends up carrying each error, with strategic suppliers. No real data.

Each invoice has a truth T (what is really owed), a buyer entitlement E (contract price
times recorded receipt) and a supplier claim I. Rates and costs are illustrative
assumptions that get swept, not benchmarks.

Policies:
  G  conventional gate, tight tolerance
  T  simple improvement, wide tolerance
  A  audit-and-recover: pay I, sample supplier-periods, extrapolate and net
  R  evaluated receipt settlement: pay E, no invoice
  L  lesser-of settlement: pay min(I, E) at once, no stop on amount. The difference goes
     on the supplier's running account, claimed with evidence once per supplier-period.
  L1 same, but each short-paid invoice is claimed on its own (no running account)

Costs are shown for both sides, since moving work to suppliers is not a saving.
Run: python3 simulate2.py [results.json]
"""
import json
import math
import random
import sys

P = dict(
    suppliers=400, periods=12, invoices_per_period=20,
    value_median=1500.0, value_sigma=1.6,
    # shares of all invoices, by what went wrong
    buyer_low=0.05,     # buyer record too low, invoice right (stale price, short receipt)
    buyer_high=0.02,    # buyer record too high, invoice right
    sup_over=0.02,      # honest supplier overbill, buyer record right
    sup_under=0.01,     # honest supplier underbill, buyer record right
    both_high=0.0005,   # both records too high
    timing=0.05,        # receipt not posted yet
    size=0.03,          # mean size of a variance, share of value
    opportunist=0.0,    # share of suppliers that pad to whatever pays best
    tight=(0.01, 50.0), wide=(0.02, 150.0),
    touch=30.0,         # buyer labor per human look
    resolve_accuracy=0.97,
    discount_share=0.05, discount=0.02,
    timing_auto=0.8,    # share of timing cases where the receipt lands before the due date
    sup_claim_cost=40.0,
    claim_reject=0.98,  # share of false claims rejected
    claim_line_cost=2.0, review_line_share=0.1,  # added cost per line in a batched claim
    chase_share=0.5,    # stopped invoices where the supplier has to chase
    delay_days=10, supplier_capital=0.10,
    audit_n=4, penalty=1.0, recovery=0.8, value_cap=25_000.0,
)


def variance(r, p):
    return min(r.expovariate(1 / p["size"]), 0.5)


def within(v, x, tol):
    return x <= tol[0] and x * v <= tol[1]


def pad_rate(p, policy):
    """Share of value a rational opportunist adds to each invoice, given the policy's rule."""
    return {"G": p["tight"][0] * 0.98, "T": p["wide"][0] * 0.98, "A": 0.04, "L": 0.04, "L1": 0.04, "R": 0.0}[policy]


def audit_detect(theta, n):
    return 1 - (1 - theta) ** n


def best_theta(p):
    """Padding frequency that maximizes the opportunist's expected gain per unit padded under A."""
    best, gain = 0.0, 0.0
    for i in range(1, 101):
        th = i / 100
        q = audit_detect(th, p["audit_n"])
        g = th * (1 - q) - q * th * p["penalty"]
        if g > gain:
            best, gain = th, g
    return best


def run(policy, p, seed):
    r = random.Random(seed)
    out = dict(labor=0.0, overpaid=0.0, lost_discount=0.0, sup_short=0.0, sup_claim_cost=0.0, sup_delay_cost=0.0,
               stopped=0, human=0, invoices=0, claims=0)
    theta = best_theta(p)
    for s in range(p["suppliers"]):
        opp = r.random() < p["opportunist"]
        for _ in range(p["periods"]):
            period_overpaid = 0.0
            mism = []
            open_gaps = []
            false_lines = []
            for _ in range(p["invoices_per_period"]):
                out["invoices"] += 1
                T = p["value_median"] * math.exp(r.gauss(0, p["value_sigma"]))
                E = I = T
                u = r.random()
                edges = 0.0
                kind = "clean"
                for k in ("buyer_low", "buyer_high", "sup_over", "sup_under", "both_high", "timing"):
                    edges += p[k]
                    if u < edges:
                        kind = k
                        break
                x = variance(r, p)
                if kind == "buyer_low":
                    E = T * (1 - x)
                elif kind == "buyer_high":
                    E = T * (1 + x)
                elif kind == "sup_over":
                    I = T * (1 + x)
                elif kind == "sup_under":
                    I = T * (1 - x)
                elif kind == "both_high":
                    E = I = T * (1 + x)
                padded = False
                if opp and kind == "clean":
                    if policy != "A" or r.random() < theta:
                        I = T * (1 + pad_rate(p, policy))
                        padded = True

                stopped = False
                if kind == "timing" and policy in ("G", "T"):
                    out["labor"] += p["touch"] * (1 - p["timing_auto"])
                    out["human"] += 1 - p["timing_auto"]
                    pay = I
                elif kind == "timing":
                    pay = I
                    if r.random() > p["timing_auto"]:
                        # receipt missed the due date: supplier chases, nobody loses money
                        out["sup_claim_cost"] += p["sup_claim_cost"]
                        out["labor"] += p["touch"]
                        out["human"] += 1
                elif policy in ("G", "T"):
                    tol = p["tight"] if policy == "G" else p["wide"]
                    gap = abs(I - E) / max(E, 1e-9)
                    if within(E, gap, tol):
                        pay = I
                    else:
                        stopped = True
                        out["labor"] += p["touch"]
                        out["human"] += 1
                        pay = T if r.random() < p["resolve_accuracy"] else I
                elif policy == "A":
                    if T > p["value_cap"] and I != E:
                        stopped = True
                        out["labor"] += p["touch"]
                        out["human"] += 1
                        pay = T
                    else:
                        pay = I
                        if I != E:
                            mism.append((I - T, padded))
                else:
                    pay = E if policy == "R" else min(I, E)
                    if T - pay > 0:
                        open_gaps.append(T - pay)
                    if padded and policy != "R":
                        false_lines.append(I - T)

                if stopped and r.random() < p["discount_share"]:
                    out["lost_discount"] += p["discount"] * T
                if stopped:
                    out["stopped"] += 1
                    out["sup_delay_cost"] += T * p["supplier_capital"] * p["delay_days"] / 365
                    if kind != "sup_over" and r.random() < p["chase_share"]:
                        out["sup_claim_cost"] += p["sup_claim_cost"]
                diff = pay - T
                if diff > 0:
                    out["overpaid"] += diff
                    period_overpaid += diff
                else:
                    out["sup_short"] += -diff

            groups = [open_gaps] if policy in ("L", "R") else [[g] for g in open_gaps]
            for lines in groups:
                total = sum(lines)
                cost = p["sup_claim_cost"] + p["claim_line_cost"] * (len(lines) - 1)
                if lines and total > cost:
                    out["claims"] += 1
                    looks = 1 + p["review_line_share"] * (len(lines) - 1)
                    out["labor"] += p["touch"] * looks
                    out["human"] += looks
                    out["sup_claim_cost"] += cost
                    out["sup_short"] -= total
            if false_lines and (1 - p["claim_reject"]) * sum(false_lines) > p["sup_claim_cost"]:
                out["claims"] += 1
                out["labor"] += p["touch"]
                out["human"] += 1
                out["sup_claim_cost"] += p["sup_claim_cost"]
                out["overpaid"] += sum(x for x in false_lines if r.random() > p["claim_reject"])

            if policy == "A" and mism:
                n = min(p["audit_n"], len(mism))
                sample = r.sample(mism, n)
                out["labor"] += p["touch"] * n
                out["human"] += n
                found = [m for m in sample if m[0] > 0]
                if found:
                    claim = max(period_overpaid, 0.0)
                    recovered = claim * p["recovery"]
                    out["overpaid"] -= recovered
                    if any(m[1] for m in found):
                        out["overpaid"] -= claim * p["penalty"] * p["recovery"]

    scale = 100_000 / out["invoices"]
    res = {k: v * scale for k, v in out.items() if k != "invoices"}
    res["buyer_total"] = res["labor"] + res["overpaid"] + res["lost_discount"]
    res["supplier_total"] = res["sup_claim_cost"] + res["sup_delay_cost"] + res["sup_short"]
    res["joint_total"] = res["buyer_total"] + res["supplier_total"]
    return res


def scenario(over=None, seeds=(1, 2, 3)):
    p = dict(P, **(over or {}))
    res = {}
    for pol in ("G", "T", "A", "R", "L1", "L"):
        rows = [run(pol, p, s) for s in seeds]
        res[pol] = {k: sum(x[k] for x in rows) / len(rows) for k in rows[0]}
    return res


def table(res):
    print("| Policy | Stopped | Human looks | Labor $ | Overpaid net $ | Discount lost $ | Buyer total $ | Supplier unpaid $ | Supplier chase and claim $ | Supplier delay $ | Joint total $ |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, x in res.items():
        print(f"| {k} | {x['stopped']:,.0f} | {x['human']:,.0f} | {x['labor']:,.0f} | {x['overpaid']:,.0f} | {x['lost_discount']:,.0f} | "
              f"{x['buyer_total']:,.0f} | {x['sup_short']:,.0f} | {x['sup_claim_cost']:,.0f} | {x['sup_delay_cost']:,.0f} | {x['joint_total']:,.0f} |")


def main():
    print("All figures per 100,000 synthetic invoices. Illustrative parameters, not benchmarks.\n")
    results = {}
    for name, over in [
        ("honest_world", {}),
        ("opportunists_5pct", dict(opportunist=0.05)),
        ("opportunists_20pct", dict(opportunist=0.20)),
        ("dirty_buyer_records", dict(buyer_low=0.20)),
        ("very_dirty_buyer_records", dict(buyer_low=0.35)),
        ("costly_claims", dict(sup_claim_cost=150.0)),
        ("low_recovery", dict(recovery=0.3, opportunist=0.05)),
        ("weak_claim_review", dict(claim_reject=0.8, opportunist=0.05)),
        ("no_supplier_chase_cost", dict(chase_share=0.0, delay_days=0)),
    ]:
        print(f"### {name} {over or ''}\n")
        results[name] = scenario(over)
        table(results[name])
        print()

    print("### Crossover: cheapest policy on joint cost (both sides), G/T/A/L\n")
    print("| Buyer record too low | Opportunists 0% | 5% | 20% |\n|---|---|---|---|")
    grid = {}
    for b in (0.02, 0.05, 0.10, 0.20, 0.35, 0.50):
        row = []
        for o in (0.0, 0.05, 0.20):
            res = scenario(dict(buyer_low=b, opportunist=o), seeds=(1,))
            best = min("GTAL", key=lambda k: res[k]["joint_total"])
            grid[f"b={b},o={o}"] = {k: round(res[k]["joint_total"]) for k in "GTAL"}
            row.append(best)
        print(f"| {b:.0%} | {row[0]} | {row[1]} | {row[2]} |")
    results["grid"] = grid
    with open(sys.argv[1] if len(sys.argv) > 1 else "simulation2-results.json", "w") as f:
        json.dump(dict(params=P, results=results), f, indent=1)


if __name__ == "__main__":
    main()
