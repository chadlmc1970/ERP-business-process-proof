"""Synthetic test of three-way match control policies. No real data.

Every parameter in P is an illustrative assumption, not a benchmark. The point is
to see which unknowns drive the answer and where each policy stops winning, not to
estimate savings. Run: python3 simulate.py   (stdlib only, fixed seeds)

Policies, all sharing the same invoice stream:
  A  conventional gate: any variance beyond a tight tolerance blocks payment
  B  simpler fix: same gate, wider tolerance
  B2 simpler fix plus supplier-level monitoring of variances that passed
  C  sensor not gate: match still computed on everything, but for known suppliers
     and modest amounts a variance no longer stops payment; it feeds monitoring,
     sampling and setoff. Missing PO or receipt still blocks.
  D  evaluated receipt settlement for eligible suppliers, A for the rest
  E  boundary case: no gate, no monitoring, random post-payment sampling only
"""
import json
import math
import random
import sys
from collections import defaultdict

P = dict(
    n=120_000, periods=12, suppliers=1500, new_share=0.10,
    value_median=1500.0, value_sigma=1.6,
    mismatch_rate=0.20,        # invoices with any variance
    genuine_share=0.10,        # of those, how many are real overbilling (the key unknown)
    harmless_up_bias=0.5,      # share of harmless variances that go against the buyer
    harmless_var=0.015, genuine_var=0.04,
    dup_rate=0.002, dup_check=0.95,
    fake_rate=0.0002,          # no real order or receipt behind it
    collusive_rate=0.00005,    # receipt forged, so all documents agree
    touch_cost=30.0,           # labor per human look at a mismatch
    discount_share=0.05, discount=0.02,
    recov_known=0.90, recov_new=0.30, recov_fraud=0.10,
    tight_pct=0.01, tight_abs=50.0, wide_pct=0.02, wide_abs=150.0,
    autopay_cap=25_000.0, autopay_var_cap=500.0,
    sample=0.05, z_flag=3.0, min_n=5,
    ers_eligible=0.60, ers_residual=0.30,
    adversary_share=0.0, adversary_every=1,
)


def make_stream(p, seed):
    r = random.Random(seed)
    weights = [1.0 / (i + 1) ** 0.8 for i in range(p["suppliers"])]
    sup_new = [r.random() < p["new_share"] for _ in range(p["suppliers"])]
    sup_ers = [(not sup_new[i]) and r.random() < p["ers_eligible"] for i in range(p["suppliers"])]
    known = [i for i in range(p["suppliers"]) if not sup_new[i]]
    sup_adv = set(r.sample(known, int(len(known) * p["adversary_share"])))
    ids = r.choices(range(p["suppliers"]), weights=weights, k=p["n"])
    stream = []
    for k, s in enumerate(ids):
        v = p["value_median"] * math.exp(r.gauss(0, p["value_sigma"]))
        u = r.random()
        kind, var = "clean", 0.0
        if u < p["fake_rate"]:
            kind = "fake"
        elif u < p["fake_rate"] + p["collusive_rate"]:
            kind = "collusive"
        elif u < p["fake_rate"] + p["collusive_rate"] + p["dup_rate"]:
            kind = "dup"
        elif r.random() < p["mismatch_rate"]:
            if r.random() < p["genuine_share"]:
                kind, var = "genuine", r.expovariate(1 / p["genuine_var"])
            else:
                sign = 1 if r.random() < p["harmless_up_bias"] else -1
                kind, var = "harmless", sign * r.expovariate(1 / p["harmless_var"])
        stream.append((k * p["periods"] // p["n"], s, sup_new[s], sup_ers[s], s in sup_adv,
                       v, kind, var, r.random(), r.random(), r.random()))
    return stream


def within(v, var, pct, ab):
    return abs(var) <= pct and abs(var) * v <= ab


def run(policy, stream, p):
    labor = loss = disc = 0.0
    touched = blocked = silent_genuine = genuine_n = 0
    pool = defaultdict(list)

    def recov(new):
        return p["recov_new"] if new else p["recov_known"]

    def gate(v, var, kind, u, new, pct, ab, monitored, key):
        """Returns True if the invoice was handled by the tolerance gate."""
        nonlocal labor, loss, disc, touched, blocked, silent_genuine
        if within(v, var, pct, ab):
            if kind == "genuine":
                silent_genuine += 1
                loss += var * v
            if monitored and var:
                pool[key].append((v, var, kind, new))
            return
        labor += p["touch_cost"]
        touched += 1
        blocked += 1
        if u < p["discount_share"]:
            disc += p["discount"] * v

    for period, s, new, ers, adv, v, kind, var, u1, u2, u3 in stream:
        key = (s, period)
        # A strategic supplier sizes each overbill to sit just inside the auto-pass rule.
        if adv and kind in ("clean", "harmless") and u3 < 1 / p["adversary_every"]:
            kind = "genuine"
            if policy in ("A",):
                var = min(p["tight_pct"], p["tight_abs"] / v) * 0.98
            elif policy in ("B", "B2"):
                var = min(p["wide_pct"], p["wide_abs"] / v) * 0.98
            elif policy == "D" and ers:
                var = 0.0
                kind = "clean"
            elif policy == "D":
                var = min(p["tight_pct"], p["tight_abs"] / v) * 0.98
            else:
                var = min(p["wide_pct"] * 2, p["autopay_var_cap"] / v) * 0.98
        if kind == "genuine":
            genuine_n += 1
        if kind == "dup":
            if u1 >= p["dup_check"]:
                loss += v * (1 - recov(new))
            continue
        if kind == "collusive":
            loss += v
            continue
        if kind == "fake":
            if policy == "E":
                loss += v * (1 - p["recov_fraud"])
            else:
                labor += p["touch_cost"]
                touched += 1
            continue
        if kind == "clean":
            continue

        if policy == "A":
            gate(v, var, kind, u1, new, p["tight_pct"], p["tight_abs"], False, key)
        elif policy == "B":
            gate(v, var, kind, u1, new, p["wide_pct"], p["wide_abs"], False, key)
        elif policy == "B2":
            gate(v, var, kind, u1, new, p["wide_pct"], p["wide_abs"], True, key)
        elif policy == "C":
            if new or v > p["autopay_cap"] or abs(var) * v > p["autopay_var_cap"]:
                gate(v, var, kind, u1, new, p["tight_pct"], p["tight_abs"], False, key)
            else:
                pool[key].append((v, var, kind, new))
        elif policy == "D":
            if ers:
                if kind == "genuine":
                    continue
                if u2 < p["ers_residual"]:
                    labor += p["touch_cost"]
                    touched += 1
            else:
                gate(v, var, kind, u1, new, p["tight_pct"], p["tight_abs"], False, key)
        elif policy == "E":
            if kind == "genuine":
                if u2 < p["sample"]:
                    labor += p["touch_cost"]
                    touched += 1
                    loss += var * v * (1 - recov(new))
                else:
                    loss += var * v

    # Harmless variances should roughly cancel within a supplier; real overbilling does not.
    # The running sum per supplier carries across periods and restarts after each investigation.
    if policy in ("B2", "C"):
        r = random.Random(7)
        by_supplier = defaultdict(list)
        for (s, period), items in sorted(pool.items(), key=lambda kv: kv[0][1]):
            by_supplier[s].append(items)

        def settle(item, looked):
            nonlocal labor, loss, touched, silent_genuine
            v, var, kind, new = item
            if looked:
                labor += p["touch_cost"]
                touched += 1
            if kind == "genuine":
                excess = var * v
                if policy == "B2":
                    # already counted as lost in the gate; a look claws part of it back
                    if looked:
                        loss -= excess * recov(new)
                else:
                    loss += excess * (1 - recov(new)) if looked else excess
                    if not looked:
                        silent_genuine += 1

        for periods in by_supplier.values():
            open_items = []
            for items in periods:
                open_items += items
                sq = sum((x[0] * x[1]) ** 2 for x in open_items)
                net = sum(x[0] * x[1] for x in open_items)
                if len(open_items) >= p["min_n"] and sq > 0 and net / math.sqrt(sq) > p["z_flag"]:
                    for item in open_items:
                        settle(item, True)
                    open_items = []
            for item in open_items:
                settle(item, policy == "C" and r.random() < p["sample"])

    n = len(stream)
    per = 100_000 / n
    return dict(policy=policy, labor=labor * per, unrecovered_loss=loss * per, lost_discount=disc * per,
                total=(labor + loss + disc) * per, human_touches=touched * per, blocked=blocked * per,
                genuine=genuine_n * per, genuine_never_examined=silent_genuine * per)


def scenario(over=None, seeds=(1, 2, 3)):
    p = dict(P, **(over or {}))
    out = {}
    for pol in ("A", "B", "B2", "C", "D", "E"):
        rows = [run(pol, make_stream(p, sd), p) for sd in seeds]
        out[pol] = {k: (rows[0][k] if k == "policy" else sum(x[k] for x in rows) / len(rows)) for k in rows[0]}
    return out


def table(res):
    print("| Policy | Labor $ | Unrecovered loss $ | Lost discount $ | Total $ | Human touches | Blocked | Genuine never examined |")
    print("|---|---|---|---|---|---|---|---|")
    for k, r in res.items():
        print(f"| {k} | {r['labor']:,.0f} | {r['unrecovered_loss']:,.0f} | {r['lost_discount']:,.0f} | {r['total']:,.0f} | "
              f"{r['human_touches']:,.0f} | {r['blocked']:,.0f} | {r['genuine_never_examined']:,.0f} |")


def main():
    results = {}
    print("All figures per 100,000 synthetic invoices. Illustrative parameters, not benchmarks.\n")
    runs = [
        ("base", {}),
        ("genuine_1pct", dict(genuine_share=0.01)),
        ("genuine_30pct", dict(genuine_share=0.30)),
        ("genuine_60pct", dict(genuine_share=0.60)),
        ("low_recovery", dict(recov_known=0.30)),
        ("adversary_1pct_suppliers", dict(adversary_share=0.01)),
        ("adversary_low_and_slow", dict(adversary_share=0.01, adversary_every=5)),
        ("harmless_lean_against_buyer", dict(harmless_up_bias=0.75)),
    ]
    for name, over in runs:
        print(f"### {name} {over or ''}\n")
        results[name] = scenario(over)
        table(results[name])
        print()

    print("### Winner by assumption grid (cheapest of A, B, B2, C; D excluded because its setup cost is not modeled)\n")
    print("| Genuine share | Recovery | Touch $30 | Touch $60 |\n|---|---|---|---|")
    grid = {}
    for g in (0.01, 0.05, 0.10, 0.30, 0.60):
        for rec in (0.2, 0.5, 0.9):
            cells = []
            for c in (30.0, 60.0):
                res = scenario(dict(genuine_share=g, recov_known=rec, touch_cost=c, n=40_000), seeds=(1,))
                best = min(("A", "B", "B2", "C"), key=lambda x: res[x]["total"])
                grid[f"g={g},rec={rec},c={c}"] = {k: round(res[k]["total"]) for k in ("A", "B", "B2", "C")}
                cells.append(best)
            print(f"| {g:.0%} | {rec:.0%} | {cells[0]} | {cells[1]} |")
    results["grid"] = grid
    with open(sys.argv[1] if len(sys.argv) > 1 else "simulation-results.json", "w") as f:
        json.dump(dict(params=P, results=results), f, indent=1)


if __name__ == "__main__":
    main()
