# Working proposal under test: lesser-of settlement

Status: REJECTED in adversarial review (agents/05-adversarial.md). Kept as the record of a failed attempt. The rebuilt process is in report/REPORT.md.

## Idea in one line

Stop asking whether the records agree before paying. Pay the lower of what the buyer's records support and what the supplier claimed, on time, and let the supplier claim any difference with evidence on a running account.

## Mechanism

Let T be what is truly owed, E the buyer's entitlement (contract price times recorded receipt), and I the supplier's invoice.

1. Hard gates stay: real supplier, verified bank details, authorized commitment, something received, not a duplicate. Fail any of these and nothing is paid.
2. Amount is never a gate. On the due date the buyer pays min(I, E).
3. Any shortfall against the invoice goes to a running account per supplier, shown on the remittance.
4. The supplier claims against the account, with evidence, once per period. One correction (say, a stale price) can settle many lines.
5. Tolerances disappear. There is no safe harbor because padding is not paid.
6. Random audit of receipts and claims covers the remaining risk: both records too high, false claims.
7. Spend with no reliable E (services, no-PO, variable pricing) is outside scope and keeps its current control.

## Why it might matter

The gate treats every disagreement as the buyer's problem to solve before money moves. Lesser-of turns overpayments, which nobody is motivated to report, into underpayments, which the supplier is motivated to report and has the evidence to fix. A single wrong record can no longer cause an overpayment. Unlike evaluated receipt settlement, it keeps the invoice as an independent second opinion. Unlike pay-and-chase, it has no recovery problem on amount errors, because the excess never left.

Candidate central claim: the assumption that a mismatch must be resolved before payment is unnecessary for the amount dimension. The disagreement can be settled by arithmetic now, with the residual moved to the party holding both the motive and the evidence.

## Tests so far (all synthetic, written by the proposer, so treat with suspicion)

- tests/check_properties.py: exhaustive arithmetic checks. Overpayment happens only when both records are too high.
- tests/simulate2.py: policies G, T, A, R, L1, L. L came out cheapest on joint buyer plus supplier cost in every grid cell, which is suspicious.
- With supplier chase and delay costs set to zero, L's joint-cost lead over the simple fix nearly disappears.
- Without the running account, the early version of L lost to the simple fix on joint cost. That suggests much of the benefit depends on batching.

## Known worries

Cost shifted to suppliers rather than removed. Retail-style deduction abuse. Suppliers pricing in the friction. GAAP liability completeness, unclaimed property, sales and use tax on short-paid invoices. Stale POs being a leading mismatch cause. Late receipts becoming a stop in disguise. Possibly already standard under another name.
