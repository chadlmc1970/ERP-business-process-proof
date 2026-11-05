# Line 02: First principles, assumptions, and economics of the three-way match

Scope: logic and economics only. No product material, and no view on how AI would automate anything.
Claim tags: [Established], [Supported hypothesis], [Speculative], [Rejected].
Section 8 says which sources were actually read and which were not. Read it before citing anything from this file.

## 0. Bottom line

1. The process is not required by law for a US public company. The law requires an outcome (reasonable assurance) and leaves the means open. [Established]
2. The claim "it must be done in this form" is already falsified by long-standing practice: pay on receipt with no invoice, pay before verifying, sample after payment. GAO reviewed such designs and did not object, subject to conditions. [Established]
3. Each of those counterexamples keeps the same core: prior authority, evidence of performance that does not come from the claimant alone, a claim tied to the same obligation, a remedy, and evidence an outsider can re-perform. I found no case that dispenses with the core. [Supported hypothesis]
4. The form is held up by four quantities: how much of a wrong payment can be recovered, how independent the records are, how much the counterparty has to lose, and what a false hold costs. None of these is routinely measured. The largest unproven assumption is that agreement among three records is evidence of truth.
5. Cheaper comparison argues for checking everything, not for sampling. Random sampling is the answer to expensive comparison. The live economic question is the cost of exceptions and of producing the evidence, not the cost of the compare. [Supported hypothesis]
6. The data model has a real gap: nothing stores the obligation itself. It is inferred by comparing three shadows of it. Modeling it would remove mismatches that are artifacts of representation. It would not remove the need for independent evidence, and it would not make a wrong count right. [Supported hypothesis]

## 1. The business objective

### Plain language

Give up money only for value actually received on the terms agreed, to the party actually entitled to it, at the best time. Know at any moment what is owed. Keep good suppliers willing to deal. Spend less on all of this than it saves. Be able to show an outsider that this was so.

### If this process had never existed, what would the business still need?

- To know what it owes, to whom, and since when.
- To avoid paying for what it did not get, paying twice, or paying the wrong party.
- To avoid being robbed by outsiders or insiders, and to make robbery unattractive.
- To pay what it does owe, so supply continues and the price does not carry a risk premium.
- To state its liabilities, expenses and inventory correctly and on time.
- To show outsiders (owners, auditors, regulators, tax authorities) that the above is reliable.

None of these mentions a document. All of them are still needed in a world with no purchase orders.

### Formal statement

| Element | Content |
|---|---|
| Outcome | Settlement of each true obligation, in the right amount, to the entitled party, at the value-maximizing time; a correct statement of obligations at any reporting date |
| Information needed | What was authorized; what was actually performed; what is being claimed and by whom; whether the claimant is who it says it is; what has already been settled |
| Constraints | Reasonable assurance (15 USC 78m(b)(2)(B), with "reasonable" defined in 78m(b)(7) as what "would satisfy prudent officials in the conduct of their own affairs"); ICFR under 17 CFR 240.13a-15(f); contract and UCC terms; evidence that an outsider can re-perform |
| Risks controlled | Overpayment, duplicate payment, payment for nothing, payment to the wrong party, fraud (outsider, insider, collusive), misstated liabilities and expense, wrongful non-payment, supplier loss |
| Resources used | Effort to create evidence, effort to compare, effort to resolve differences (on both sides of the trade), delay, cost of assurance |
| Acceptable error | Two different thresholds. Financial reporting: no "reasonable possibility" of a material misstatement that is "not prevented or detected on a timely basis" (17 CFR 210.1-02(a)(4)). Economic: stop checking where the marginal cost of checking equals the marginal expected loss avoided. Zero error is not the objective. |

The second threshold has an official form. GAO's Title 7 test defined savings from sampling as the case where the cost of examining the sample plus projected losses from undetected errors is less than the cost of examining everything, with a "tolerable error rate" set by analysis (GAO/AIMD-21.3.2, May 2000, p. 18, n. 14). [Established]

### Simplified objective function

For a policy P (what to check, when, how, and when to pay):

```
minimize   E[ sum over obligations i of  c_i(P) + (1 - r_i) * O_i(P) + u_i * U_i(P) + D_i(P) ]  +  K(P)

subject to  Pr(material misstatement not prevented or detected in time) is not a reasonable possibility
            payment only to the entitled party; law and contract terms; evidence can be re-performed

c = cost of evidence, comparison, and exception handling, on both sides of the trade
O = amount overpaid           r = share recoverable, net of cost of recovery
U = amount wrongly withheld   u = cost per dollar withheld (friction, late interest, price premium)
D = timing cost or gain relative to the best payment date
K = fixed cost of the system plus the cost of proving it works to outsiders
```

The critical feature is that O depends on P through behavior. Suppliers and insiders react to the policy. Observed error rates are therefore outcomes of the policy, not parameters of the world. [Established as logic; size unmeasured]

Boundary note: this objective says nothing about whether the purchase was wise or the price good. The match takes the order as given. If most value leakage sits upstream of the order, the objective is being optimized inside the wrong boundary. I could not verify the split.

### Five results from the function

These are my derivations. The algebra was checked numerically. They are simple on purpose.

R1. Check or not (static). With p = chance of error, d = chance the check catches it, L = size of error, c = cost of check, a check pays when `c < p * d * L`. This is the same structure as Deming's all-or-none rule for incoming inspection (break-even at p = k1/k2), which assumes a stable process. Under stable conditions the least-cost policy tends to be everything or nothing, and partial checking loses. [Established as algebra; Deming read only through secondary sources]

R2. The sequencing premium. Compare checking before payment with checking after, where a caught post-payment error recovers share r. Pre-payment is better by exactly `p * d * L * (1 - r) - (c_pre - c_post)` per invoice. If r is near 1 and the costs are equal, order does not matter at all. Everything that justifies "before" lives in `(1 - r)`. [Established as algebra]

R3. Deterrence. With audit rate q, detection d, gain g from cheating, and loss F if caught, cheating stops when `q >= g / (d * (g + F))`. For a supplier with a valuable ongoing relationship (large F) the required q is small. For a party with nothing to lose (F near 0) no audit rate deters: `(1 - q*d) * g` stays positive for any q below 1/d. A check against a throwaway vendor filters but does not deter. [Established as algebra]

R4. Commitment. If the buyer cannot commit and decides on inspection after seeing the invoice, the standard inspection-game result is a positive cheating rate `p* = c / (d * L)`. So cheating is positive in equilibrium, and lower comparison cost lowers it. A hard-coded rule is a commitment device, which is a benefit the "wasteful 100% check" critique ignores. [Supported hypothesis; consistent with Khalil 1997 abstract, full paper not read]

R5. Exceptions. Share of flagged items that are real errors = `s*p / (s*p + f*(1-p))`, with s = sensitivity, f = false alarm rate. Pure arithmetic illustration, not data: s = 0.9, f = 0.05, p = 0.001 gives about 1.8%. If real errors are rare, most of the exception queue is false alarms even with a good test. The cost then sits in c through f, not in the compare. [Established as arithmetic; real values of s, f, p not verified]

Corollary of R1 and R5: split c into compare cost, evidence cost, and exception cost. As compare cost falls, R1 pushes toward checking all, not toward sampling. Sampling theory is an answer to expensive comparison. Where data is structured, proposals to replace the match with sampling are therefore economically backward. Attacks should target evidence cost, false alarms, and sequencing. [Supported hypothesis]

### Process metrics that are not the objective

Match rate, touchless rate, cost per invoice, cycle time, exception count, and days payable are all proxies. Each can improve while the objective worsens: widening tolerances raises match rate and raises overpayment; auto-posting receipts raises match rate and destroys evidence; writing a purchase order after the invoice raises PO compliance and removes prior authorization. Fraud deterred generates no record at all, so the largest benefit term is invisible to every metric. Goodhart's point, that a regularity tends to collapse under pressure for control, applies directly to these measures. [Supported hypothesis]

## 2. Assumption ledger

Load (1 to 5) is my judgment of how much of the process rests on the assumption. It is not a measurement. Sorted by load.

Classes: Necessary (follows from the objective), Contingent (true under conditions that vary), Historical (true once, conditions changed), Conventional (a habit or coordination choice), Unproven (widely relied on, never shown).

| # | Assumption | Class | Load | Evidence that would prove or disprove necessity |
|---|---|---|---|---|
| A1 | Money should leave only against evidence of an obligation (authorized, performed, claimed) | Necessary | 5 | Disprove only by a viable firm paying claims on no evidence and no recourse. None found. Note that "evidence" can be ex post, and can be replaced by recourse for a limited time |
| A2 | Agreement among the records is evidence of truth | Unproven | 5 | Seed known errors and frauds, measure how many pass the match. Compare records with physical or supplier-side truth on a blind sample |
| A3 | The three records are independent | Contingent | 5 | Measure lineage: how often the receipt or invoice value was derived from the PO or from each other. If high, the check adds little (see Holmstrom, section 5) |
| A4 | Verification cost justifies per-transaction checking (R1) | Contingent | 5 | Measure c, p, d, L by category. Fails for tiny invoices; holds at near-zero compare cost |
| A5 | Holding cash beats chasing it (r well below 1, R2) | Contingent | 4 | Measure actual net recovery on post-payment errors, by supplier class. Near 1 for ongoing suppliers with set-off rights would remove the case for strict order |
| A6 | Fixed ordering: order, receipt, invoice, match, pay | Conventional | 4 | Exists in reverse: prepayment, C.O.D., letters of credit, fast pay. Test: loss rates by sequence |
| A7 | A strict, rule-bound, non-discretionary check is better than a judged one | Contingent | 4 | Compare error and override rates under fixed and discretionary regimes. Value comes from commitment and low assurance cost (R4) |
| A8 | The PO fully and correctly states what is owed | Unproven | 4 | Share of exceptions resolved by changing the PO rather than the invoice. Share of POs created after the invoice |
| A9 | Handoffs: separate people for order, receipt, payment | Contingent (the separation); Conventional (the department layout) | 4 | The objective needs that no single person controls a whole transaction. Whether that requires human handoffs is open: collusion evidence shows separation is not sufficient |
| A10 | A mismatch means something is wrong | Unproven | 4 | Classify a sample of exceptions by true cause: real error, timing, unit or format, legitimate change |
| A11 | Sequential inspection: wait until all three exist, then compare once at the end | Historical | 3 | Paper had to physically converge on one desk. Test: value of checking each event as it occurs, and time to discover errors |
| A12 | Information availability: AP cannot know a fact until a document reaches it | Historical (for transmission); Contingent (for capture) | 3 | Transmission is solved. Capture is not: someone or something must still observe the delivery |
| A13 | Evaluation speed: comparing is slow, so do it at one chokepoint | Historical | 3 | Compare time is no longer binding where data is structured. Resolution time may be |
| A14 | Human limits: few fields, tolerances, thresholds | Historical | 3 | Hammer's Ford account, as reported, had many items to match, later reduced. Not read; see section 8. Tolerances also encode economics, so they do not vanish with cheap compare |
| A15 | Exceptions can be anticipated and enumerated in rules | Unproven | 3 | Share of exceptions falling outside defined categories, and the rate of new categories appearing |
| A16 | Predictive history: past behavior does not reduce the need to check this invoice | Contingent | 3 | GAO required a "continuing relationship" as a condition for sampling, so history already counts. Limit: relationship history predicts honest error, not a deliberate last-period cheat or a compromised identity |
| A17 | Periodic versus continuous: batch cycles and period-end checks suffice | Contingent | 2 | Statute uses "reasonable intervals" for comparing recorded assets to actual assets. Note Montgomery (1916) already calls internal check "a continuous audit". The match is per-transaction; the periodic parts are accruals, statements and audits |
| A18 | Software architecture forces the design | Rejected as origin; Contingent as lock-in | 2 | The design is described in full in 1916, long before computers. Software encoded it and now holds it in place |

### Assumptions nobody lists

| # | Assumption | Class | Load | Why it matters |
|---|---|---|---|---|
| H1 | The individual invoice line is the right unit of control | Conventional | 4 | The real exposure is the running position with a supplier. A cumulative balance check would absorb timing and split-shipment differences that line matching flags |
| H2 | Consistency implies correspondence | Unproven | 5 | Same as A2 in philosophical form. Three records agreeing with each other is not the same as agreeing with the world |
| H3 | Errors are independent draws from a stable process | Contingent | 3 | Deming's rule and sampling both need this. A bad price or unit in a master record creates correlated errors, and all three records may inherit them |
| H4 | The cost of a false hold is negligible | Unproven | 3 | u is usually not on the buyer's books. If suppliers price it in, it reappears as a higher unit price nobody attributes to the match |
| H5 | Only the buyer needs to verify | Conventional | 3 | Barzel: "In every exchange, both the seller and the buyer will require some verification", and when the seller sorts, "each item is measured exactly once". Buyer and seller both measure the same shipment. This is possibly excess measurement, unless warranty or recourse replaces it |
| H6 | Delivery is a countable event at a dock | Contingent | 4 | True of stocked goods, false of much services spend. There the "receipt" may be a click whose only purpose is to satisfy the match |
| H7 | The receipt is a byproduct | Contingent | 3 | For inventory, the receipt is needed anyway, so its marginal control cost is near zero. For indirect spend it is produced only for the check, at high cost and low information |
| H8 | Delay is free to the buyer | Contingent | 3 | Under net terms, checking inside the credit period costs the buyer nothing. Part of why the order has survived. Trade credit theory says the terms may exist partly for this purpose (section 5) |
| H9 | Errors are mostly honest | Contingent | 3 | Tolerances and rules assume noise. An adversary who knows the tolerance can bill inside it. Tolerance is a public threshold, which is a poor property against a strategic opponent |
| H10 | The control must be cheap to prove, not just good | Contingent | 3 | A fixed automated rule is cheap for auditors to test and to carry forward year to year. A statistical control may perform better and be costlier to attest. K(P) can dominate the choice |
| H11 | The counterparty's identity is stable | Necessary for all reputation-based alternatives | 4 | Klein and Leffler assume identity is known and that "a terminated firm cannot begin business in this industry under a new name". Every trust-based shortcut inherits this. Master data is what makes that assumption true |

## 3. Challenges to the major assumptions

**A2/H2. Agreement implies truth.**
False: three records can agree and be wrong, through shared origin or collusion. If the opposite held (agreement carried no information) the check would be pure ritual. That is too strong: independent records do carry information.
Need: business need for evidence, no need for this specific test.
Constraint: information. Finding: agreement is evidence only to the degree the sources are independent, so it is a variable, not a constant. [Supported hypothesis]

**A3. Independence.**
False: if the invoice copies the PO, a wrong PO value passes every time. If the receiver sees the PO quantity and keys it, the receipt adds nothing.
This was understood in 1916: "copies of orders from which the quantities and prices have been eliminated are sent to the receiving clerk" (Montgomery, 2nd ed., p. 55). Blind receiving exists because of this exact flaw.
Opposite: fully independent records would disagree often through noise, so false alarms rise with independence. A real tradeoff.
Need: business. Constraint: information. [Established as logic; prevalence unverified]

**A4. Per-transaction verification pays.**
False for tiny invoices: GAO accepted sampling below a value limit (under $2,500 in Title 7 then, and it did not object to one design at $25,000).
Opposite: when compare cost is near zero, 100% is the cheap policy, and sampling adds selection logic and proof cost for no saving.
Need: economic, category by category. Constraint: neither physical nor legal. [Supported hypothesis]

**A5. Holding cash beats chasing it.**
False where r is near 1: a supplier you will pay again next week can be netted. But be careful: UCC 2-717 permits deduction from "any part of the price still due under the same contract". Netting against other contracts depends on terms or other law, so r is partly a drafting choice.
Opposite: where r is near 0 (one-off, overseas, insolvent, fake vendor), pre-payment checks are worth everything and even more evidence is warranted.
Need: business, specific to the counterparty. Constraint: legal and economic. This is the one assumption that could be changed by contract instead of by process. [Supported hypothesis]

**A6. Fixed ordering.**
False, routinely. Unless otherwise agreed, the buyer has a right to inspect before payment or acceptance (UCC 2-513(1)), but that right is a default that parties can change, and it is absent for C.O.D. and payment against documents (2-513(3)). A letter of credit pays on documents, with obligations independent of the underlying contract (UCC 5-103(d)). Federal fast pay pays "prior to the Government's verification" (FAR 13.401(a)). Rent, insurance and subscriptions are paid in advance.
What the examples share: the risk moved to something else (title rules, repair or replace duty, tracking of abusers). FAR 13.402(d) and (f) are explicit. Note the current FAR limits are narrow: $45,000, plus geographic separation that makes timely acceptance evidence impractical.
Need: order is a business choice, not a logical need. Constraint: there is one true physical order (performance happens before it can be observed) and no such order for payment. [Established]

**A7. Rule-bound checking.**
False where judgment catches what rules miss. Opposite: pure discretion invites both bribery and non-commitment. Kofman and Lawarree: internal auditors are costless but may collude, external ones costly but do not, and the optimal contract may use random external audits.
Need: business and assurance. A random policy is also a rule and can bind just as well, provided the randomness cannot be gamed. [Supported hypothesis]

**A8. PO as truth.**
False when terms change after issue: amendments, verbal changes, master contract prices, surcharges. Then the match compares reality to an old intention.
Opposite: if the PO were always wrong, exceptions would always resolve in the invoice's favor, and the PO would be noise. Measurable.
Need: business needs prior authority, not necessarily a transaction-level document. A contract with a rate card can supply it. [Supported hypothesis]

**A9. Handoffs.**
False as sufficient: ACFE 2024 reports median losses of $75,000 for one perpetrator and $329,000 for three or more, and 19% of cases cite override of existing controls. This is a sample of detected, investigated frauds, global, so it shows the collusion tail is real, not its rate.
Opposite: one person controlling everything is ruled out by the 1916 definition, "no part of the accounts will be under the absolute and independent control of any one person".
Need: the principle is business; a department per step is convention. Constraint: incentive, not physical. [Supported hypothesis]

**A10. Mismatch means error.**
False when the cause is timing, unit of measure, or a legitimate change. Opposite: if nearly all mismatches were noise, R5 says humans are mostly clearing false alarms.
Need: software need, largely. The rule "values must be equal" exists because the record has no way to express "these differ for a known reason". Constraint: information. [Supported hypothesis; proportions not verified]

**A11/A12/A13/A14. Sequential inspection, information availability, speed, human limits.**
False today for transmission and comparison. These were physical constraints of paper that became habits.
Keep one exception: capture. Observing a delivery remains a physical act, and someone must do it or a device must.
Opposite (everything known instantly): the check could run on each event, which moves error discovery earlier. It does not supply truth.
Also UCC 2-607(3)(a) gives a separate reason to look at goods soon: the buyer must notify the seller within a reasonable time after it "discovers or should have discovered" a breach, or be barred from any remedy. That clock runs from delivery, not from payment. So a check at the end of the chain can be too late for reasons that have nothing to do with AP.
Need: mostly historical, and partly legal in the direction of checking sooner. [Supported hypothesis]

**A15. Exceptions can be anticipated.**
False in an open world: Ashby's variety argument says a regulator with fewer responses than the disturbances must pass the remainder on. In practice that remainder goes to people.
Opposite: if exceptions were fully enumerable, no human work would remain. Not observed.
Need: neither. It is an empirical property of the spend category. [Speculative as to size]

**A16. Predictive history.**
False in the sense that history clearly informs: GAO's fourth sampling condition is "a continuing relationship with the vendor", and FAR 13.402(f) requires identifying suppliers with a history of abusing the procedure.
Opposite (history is fully reliable): fails on three grounds. A cheat can build reputation before a final large gain (the end-game problem). Policy changes behavior, which is the Lucas and Goodhart point. And an identity takeover inherits the victim's clean history. Once a trusted lane exists, it is exactly what an attacker wants to enter.
Need: business, with a limit. History may set the level of checking but cannot be the only control. [Supported hypothesis]

**A17. Periodic versus continuous.**
False as a binary. Statute: "compared with the existing assets at reasonable intervals" (78m(b)(2)(B)(iv)), which fixes neither frequency nor method. Continuous checking adds value only if action can follow quickly, and it can raise alarm volume.
Need: reporting periods are a legal need; checking cadence is not. [Supported hypothesis]

**A18. Software limits.**
Rejected as origin. Montgomery's 1916 text has order copies, a receiving record, comparison with invoices, price and extension checks, initials, approval, marking to prevent double payment, and a mark on the order against duplicates. Nearly the whole design predates computers by decades.
Software keeps line-key and field-equality forms in place. Those are software needs; the underlying goal is not.
The phrase "three-way match" could not be dated. [Established for the design; origin of the term unverified]

**H1. Unit of control.**
If false, control moves to a running balance per supplier and contract. Benefit: timing noise cancels. Risk: offsetting errors hide, and line detail remains needed for accounting and tax. Likely a complement, not a replacement. [Speculative]

**H4. Free false holds.**
If false, the buyer pays for friction through price, service or supplier exit. Evidence would be a price difference between otherwise similar suppliers with different dispute rates. I found none. [Speculative]

**H10. Cost of proof.**
If proof cost was ignored, statistically better controls might win. It is not ignored: benchmarking of automated controls in AS 2201 Appendix B (known to me only through secondary sources) lets a stable automated control be carried forward cheaply. This favors deterministic rules regardless of detection quality. [Supported hypothesis]

## 4. What the records are

### What each record actually represents

Treating them as three copies of the same fact is the root confusion. They do different jobs. Using speech act terms (Austin, Searle; applied to work by Winograd):

| Record | What it is | Direction of fit | Leaves out |
|---|---|---|---|
| Purchase order | An authorized commitment or offer at a moment: an act, not a description. It creates a status, so it cannot be "wrong" as a sensor reading can | World should come to match the record | Whether the supplier accepted; later changes and side agreements; the governing contract; the need behind it; how price was formed; substitutes allowed |
| Goods receipt | A person's or device's assertion that something was observed at a time | Record should match the world | How the count was done; whether quality was assessed (Montgomery already notes the receiver may not be competent to judge it); when the event occurred as distinct from when it was posted; when title or risk passed; condition; confidence; anything for services |
| Invoice | A claim for payment by an interested party, and a legal and tax document | Asks the buyer to act | The seller's own shipment evidence; credits in progress; why the price differs; proof of the claimant's identity beyond its data |

So the match does not compare like with like. It tests a compound proposition: the promise was kept, and the claim is consistent with both. That is a performance evaluation, not a data quality check. GAO's plain version is the same: authorized, delivered and accepted, and "a claim has been made against the government" (p. 20). The records evidence three different propositions. [Supported hypothesis; GAO text Established]

### What all three leave out

The obligation itself. No record holds "what is owed to this party, now, and why". It is inferred at comparison time from three derived records, each of which has its own timing, units and revision history. Most structural exceptions come from that inference step (claim about proportion is unverified).

McCarthy's REA model is relevant here: it sets out resources, events and agents in place of debit and credit structures, so that accounting views are derived from a shared description of economic events. From the partial abstract read, it supports the idea of modeling the event, not the document. Full paper not read.

Other gaps: the relationship between the parties, the contract as the source of tolerances, and the buyer's reason for accepting a difference.

### Schema drift and semantic drift

Schema drift: the structure changes. New fields, split lines, a new tax line, a changed unit code, a new supplier format. It fails loudly: parsing fails or fields mismatch. It is expensive but visible.

Semantic drift: the field stays and its meaning moves. Examples, all from logic rather than measured prevalence:

- "PO exists" used to mean prior authorization. An after-the-fact PO keeps the field and loses the meaning.
- "Received" may mean at the dock, released by quality, or confirmed by a requester who never saw the item.
- "Receipt" for services may mean only that someone agreed to clear a blocked invoice.
- "Quantity" on a blanket order may be a dollar amount with quantity one.
- "Vendor" may survive a merger or change of bank details while the entity behind it has changed.
- "Price" may be net or gross of rebates in different eras.

Semantic drift is the more dangerous of the two because it fails silently. The match compares values, not meanings, so it continues to pass while its evidentiary value erodes. Match rate can even rise. This is analogous to concept drift (Gama et al. 2014: the relation between input and target changes over time) in the sense that the statistic looks stable while the relationship it stood for is gone. Analogy only. [Supported hypothesis]

Test: from event logs, measure the share of POs created after the invoice date, receipts posted within minutes of the invoice, and receipts by users who are also the requester. The BPI Challenge 2019 event log (van Dongen, 4TU; a coatings and paints multinational; 251,734 purchase items with categories for 3-way with and without goods-receipt-based invoicing, 2-way, and consignment) is an open dataset suitable for this. I did not analyze it. Jans, Alles and Vasarhelyi (2014) report, from abstract level only, that process mining of a bank's procurement logs found payments without approval and segregation breaches that internal audit had missed, which is at least evidence that the stated process and the real one can diverge.

### Does the data model embed an incomplete understanding?

Yes, in one specific way: it treats a commercial relationship as a chain of documents, when it is a stateful commitment with changes, partial performance, and disputes. Winograd's conversation for action fits better: request, promise, performance reported, satisfaction declared, with renegotiation as a normal path and not an exception. Note the PO record usually has no slot for the promise, and the receipt doubles as the declaration of satisfaction.

### Would a different understanding remove work?

Partly. Suppose one record of the obligation holds its current state, and each event (commitment, amendment, delivery, claim, settlement, dispute) changes that state, with tolerances held as contract terms.

Likely removed: mismatches caused by legitimate amendments, timing, partial delivery, and units, because differences become states with reasons. [Supported hypothesis]

Not removed: the need for evidence of performance, fraud, real disputes, the cost of capturing the event, and collusion. [Established as logic]

New risk: if buyer and seller share one record, the independence that made comparison informative may disappear. A single source of truth is a single point of failure for truth. A model that removes the comparison has to keep two independently produced observations somewhere. [Supported hypothesis]

### An ontology does not create intelligence

An ontology names distinctions. It produces no evidence. A better class for "receipt" does not make the count right. Searle's formula (X counts as Y in C) shows that POs and invoices are constituted by agreement, so a clean model of them is possible; receipts answer to the physical world, so a model of them is only as good as the observation. Suchman's critique of Winograd (reported, not read) adds that formal speech-act categories impose a discipline on people, and do not simply describe them. Conant and Ashby's "every good regulator must be a model" is not a safe foundation here: Virgo et al. (2025) argue it shows only that some good regulators are models, and that models in their stronger sense can be trivial. [Rejected: the claim that a better ontology by itself solves the verification problem]

## 5. Theory check

| Source | What it says (as read) | Bearing | Where it does not transfer | Tag |
|---|---|---|---|---|
| Townsend 1979, JET 21(2) | Verification is costly, and contracts are shaped by when to verify. Deterministic audits, per Mookherjee and Png's account | The right frame: pay to verify only in states where it is worth it | Models bilateral financing and insurance, not high-volume procurement | Established (frame) |
| Mookherjee and Png 1989, QJE 104(2): 399-415 | "[A]ll audits must be random in any optimal contract" given positive consumption in every state; always optimal to reward agents verified truthful | Argues against both 100% and fixed-threshold checks when audit is costly | Assumes commitment and a risk-averse agent with private income. Corporate suppliers are not this. Loses force when audit cost is near zero | Supported hypothesis |
| Border and Sobel 1987 (via M&P) | With a risk-neutral agent an optimal scheme may not exist without a bound on rewards | Limits the random-audit result | Read only as described by M&P | Supported hypothesis |
| Dye 1986, RAND 17(3) | Abstract: optimal monitoring is typically deterministic and lower-tailed | Supports "cheap signal, then investigate on threshold", which is how an exception works. Opposes a simple "theory says randomize" | Agency model on output; abstract only | Supported hypothesis |
| Khalil 1997, RAND 28(4); Melumad and Mookherjee 1989, RAND 20(2) | Without commitment, audit probability comes out higher; delegation can restore commitment | Fixed system rules and separated audit functions have commitment value | Abstracts only; tax and regulation settings | Supported hypothesis |
| Avenhaus, von Stengel, Zamir 2002 | Inspection games extend hypothesis testing to strategic data; announcing and committing makes the inspector a leader | Best single frame: statistics alone is wrong because the data can be manipulated | Abstract level. Applied to arms control and accountancy models | Supported hypothesis |
| Holmstrom 1979, Bell J. | Any additional information about action, "however imperfect", can improve contracts, subject to a sufficient-statistic condition | Exact test for A3: a record adds value only if the others are not sufficient without it. A derived receipt fails the test | Concerns inference of effort for pay, so use is by analogy. Later work qualifies the result (first-order approach) | Supported hypothesis |
| Barzel 1982, JLE 25(1): 27-48 | Measurement errors let people transfer wealth at a resource cost. Warranties and brands reduce excess measurement: terms "depend on subsequent performance rather than relying entirely on measuring the commodity by the time of exchange" | Strongest economic case that buyer re-measurement can be excessive, and that recourse can replace it. FAR fast pay is this trade in regulatory form | Mostly consumer goods; ignores internal fraud | Supported hypothesis |
| Klein and Leffler 1981, JPE 89(4) | Repeat-purchase enforcement works through the value of future rents, and requires known identity | Gives F in R3. Reputation can replace some checking for suppliers with rents at stake | Depends on identity and no re-entry. Thin-margin suppliers may have little F. Says nothing about employees | Supported hypothesis |
| Long, Malitz, Ravid 1993 (secondary) | Trade credit lets buyers assess quality before paying | If so, the credit period and the check are parts of one mechanism. Reduces the claim that pre-payment checking is pure delay | Abstract not retrieved; quality more than quantity or price | Speculative |
| Kofman and Lawarree 1993, Econometrica 61(3) | Internal auditors may collude; external ones cost money and do not; random external audits may be optimal; higher manager punishment raises the bribe | Supports layered control: routine check plus random independent re-check | Stylized two-auditor setting | Supported hypothesis |
| Fellegi and Sunter 1969, JASA 64 | Three decisions (link, possible link, nonlink) by likelihood ratio; minimizes clerical review at fixed error levels | Maps onto pass, exception, reject, and shows equality-or-tolerance is one coarse rule among many. Sets an optimal goal: fix error levels, then minimize the human region | Solves "same entity?", not "is the claim right?" Assumes non-strategic errors. Depends on estimates; Winkler notes sensitivity and independence issues | Supported hypothesis (original not read) |
| Wald 1945; Wald and Wolfowitz 1948 | Sequential tests reach the same errors with fewer observations on average | Evidence can be gathered until a decision is justified, not in a fixed amount | Needs one-at-a-time sampling and specified hypotheses; evidence here arrives on its own schedule | Supported hypothesis |
| Deming, Out of the Crisis (secondary) | All-or-none inspection minimizes total cost when stable | R1. Argues against partial checks in a stable process, and for fixing causes over inspecting | Stable process assumption fails with adversaries and correlated errors. Chapter number unconfirmed | Supported hypothesis |
| Lamport, Shostak, Pease 1982, TOPLAS 4(3) | With oral messages, three generals cannot handle one traitor; with unforgeable signatures it is solvable. Majority voting assumes nonfaulty units "use the same input" | Three parties and one liar: disagreement shows a fault, not who. Provenance (who signed what) matters more than count of records | Consensus is about agreement among processes, not truth about the world. All can agree on a false value. Records do not share one input | Supported hypothesis (analogy) |
| Shannon-style redundancy | Error detection needs redundancy with independent noise | Supports A3 | The three records are not encodings of one symbol, so mismatch is not channel noise. Mostly does not transfer | Rejected as a direct model |
| Kalman 1960 (abstract) | Observability: can state be inferred from outputs? | If services have no independent output, the state is unobservable, whatever the checking effort | Linear systems; concept only | Supported hypothesis (analogy) |
| Ashby 1956 (not read) | Requisite variety | A15 | Qualitative only | Speculative |
| Conant and Ashby 1970 | See section 4 | Does not support "must model" | Contested | Rejected as support |
| Goodhart 1975; Lucas 1976 (secondary) | Regularities collapse under control pressure; history cannot simply predict under a new policy | Limits any history-based lane, and any metric target | Macroeconomic origin; logic carries, not the models | Supported hypothesis |
| Montgomery 1916, pp. 53-55 and an earlier passage on audit scope | Internal check defined; "a continuous audit will be made of the details"; where internal check is satisfactory the auditor should not attempt a detailed audit | The design's purpose was partly to let outsiders rely on the system. Assurance economics are original to the design, not an add-on | Pre-SOX | Established (history) |
| AS 1105 (search extract of the PCAOB text) | Evidence from a knowledgeable independent source is more reliable than internal-only; electronic information depends on controls | Supports weighting evidence by source, not by count | Applies to auditors, not management's control design | Established |
| SEC 33-8810 | No checklist; preventive, detective, or a combination; not necessary to identify all controls; costs may be weighed (n. 8) | Means are free | Auditors still judge effectiveness; a design being allowed does not mean it will be accepted | Established |
| Power 1997 (secondary); Meyer and Rowan 1977 (not read) | Verification can become ritual and maintain credibility in itself | Explains why form persists after function erodes | Weak empirical base per a reviewer; not a claim about this control | Speculative |
| Alexander et al. 2013, JAE 56 | 2,901 insiders: most see benefits, on average do not think they exceed costs; abstract only | Perceived cost of SOX in general | Perceptions, not this control | Supported hypothesis |

Where the theory as a whole does not transfer:

- Economic audit models mostly study one principal and one agent, a few states, and costly audits. The match is mass, nearly free to compare, and multi-party.
- Random and deterministic results conflict across models (Mookherjee and Png versus Dye). No general theorem picks one here.
- None of the theory values the assurance cost K. Regulatory proof is outside these models.
- Statistics assumes stable or specified error processes. Fraud is neither.
- I found no peer-reviewed study that measures the three-way match's own detection or deterrence effect. That absence is the largest evidence gap. The search was limited, so this is not proof that none exists.

## 6. The strongest fair form of the conjecture

> To settle every true obligation in the right amount, to the entitled party, at the best time, and to state what is owed correctly at every reporting date, with reasonable assurance and at a total cost below the loss prevented, in a setting where suppliers and insiders hold private information and may gain by misstating it, where money paid is harder to recover than money held, and where outsiders must be able to rely on the result, an organization must:
>
> A. Establish, before performance and by someone with authority, what will be owed and on what terms.
>
> B. Obtain evidence of performance from a source independent of the claimant and of the person who authorized the commitment.
>
> C. Bind the counterparty's claim to that same obligation, and confirm the claimant's identity and entitlement.
>
> D. Compare A, B and C for every transaction above a trivial value, by a rule fixed in advance that interested parties cannot waive, because comparison is cheap, because error is correlated and strategic, and because a committed universal check deters as well as detects.
>
> E. Withhold settlement of the disputed amount until the difference is resolved, because holding is the cheapest remedy, and because within credit terms the wait costs the buyer nothing.
>
> F. Send differences to someone with the authority and no conflict of interest to resolve them.
>
> G. Keep evidence that lets an outsider re-perform the decision.

This version is stronger than "three documents must match", because it does not depend on any department or document type. It explains why the design has lasted over a century: it gives detection, deterrence, commitment, separation of duties, cheap proof, accrual data, and use of the credit period in one step. Its defenses against the easy attacks:

- "Compare is cheap, so sample": wrong way round. Cheap compare favors checking all.
- "Trust good suppliers": depends on identity, on rents at stake, and on no end-game.
- "Fast pay and evaluated receipt settlement (ERS, paying from the receipt with no invoice) prove it is unnecessary": they retain A, B, C, F and G, and keep a remedy in place of E.
- "Share one record": removes independence, which is B.

### Where each clause stands today

| Clause | Status |
|---|---|
| A prior authority | Survives in substance. Transaction-level form is contingent: a contract or rate card can do it. [Supported hypothesis] |
| B independent evidence | Survives. The hardest core. [Supported hypothesis] |
| C bound claim | Survives in substance, but the claim need not be a supplier's invoice: GAO did not object to payment on receipt with no invoice (p. 20), with controls on matching, duplicates and due dates. Identity is not covered by the three-way match itself. [Established for invoice form] |
| D universal rule | Contingent. Survives where compare is cheap. Weak at the low-value tail, where GAO accepted sampling. Whether a fixed rule outperforms a committed random-plus-threshold design is open. [Supported hypothesis] |
| E withhold first | Weakest clause. Already reversed in practice under conditions, with recourse in its place. Depends on r. [Established that it is not necessary; size of r unmeasured] |
| F conflict-free resolution | Survives. [Supported hypothesis] |
| G re-performable evidence | Survives within the SOX frame, though a deterministic rule is not the only re-performable design. [Supported hypothesis] |

What would falsify the core: a large population of spend, under audit, with no independent evidence of performance and no recourse, and with losses no higher than controlled spend. I found none. What would falsify D and E for a defined segment: measured r near 1, low g relative to F, stable identity, and a post-payment regime with total cost lower than the conventional one and loss rates no worse. This is testable.

### Questions other lines should take up

- Measure r, p, d, L, and false alarm rate by spend class. All are unverified here.
- Seed tests to measure A2 directly.
- Lineage tests to measure A3.
- Whether auditors accept a post-payment design at a public company. I found federal precedent, not private-sector evidence.

## 7. Could not be verified

- Any real figure for error rate, detection rate, exception causes, recovery rate, or cost of a false hold.
- When the term "three-way match" first appeared. The design is in print by 1916 (copyright 1912, 1915, 1916 on the copy read). I could not establish earlier origins or how widely it was used then.
- How often the practice is used and on what share of spend.
- The Ford numbers: secondary sources conflict (about 400 or over 500 staff; Mazda 5; about a 75% reduction). Who pioneered ERS also conflicts between sources (GM or Ford). Treat as anecdote until the original is read.
- Current effect of GAO's 2000 positions. Title 7 limits and fast-pay limits have changed; FAR now says $45,000. Federal practice has certifying-officer liability, so the a fortiori argument to corporations is reasonable but untested.
- Text of AS 2201 itself (the PCAOB site refused access). Material weakness wording is cited from Regulation S-X instead. Appendix B benchmarking is from secondary sources, and one secondary source says amendments take effect for fiscal years starting on or after December 15, 2026, which I did not confirm.
- 5 CFR 1315.6 language was read in the 2020 edition; check the current one.

## 8. Sources and how they were accessed

Primary text read (in part or in the passages cited):
- 15 USC 78m(b)(2)(B), (b)(7). Cornell LII.
- 17 CFR 240.13a-15(f); 17 CFR 210.1-02(a)(4). Cornell LII.
- SEC Release 33-8810, 72 FR 35324 (June 27, 2007). First 100,000 characters of the Federal Register text.
- UCC 2-513, 2-607, 2-717, 5-103(d). Cornell LII (model text; state enactments vary).
- FAR 13.401, 13.402, 52.213-1. acquisition.gov.
- 5 CFR part 1315 (2020 edition). govinfo.
- GAO, Streamlining the Payment Process While Maintaining Effective Internal Control, GAO/AIMD-21.3.2, May 2000, pp. 6-7, 18-20.
- Montgomery, Auditing Theory and Practice, 2nd ed., pp. 53-55. Internet Archive OCR text, identifier auditingtheorya01montgoog.
- ACFE, Occupational Fraud 2024: A Report to the Nations. 1,921 cases investigated January 2022 to September 2023; billing 22% of cases, $100,000 median loss, 18 months median duration; tips 43%, internal audit 14%, management review 13%, document examination 6%, account reconciliation 5%, automated monitoring 3%. Original survey, detected cases only. Copy hosted by Ivey.
- Winkler, Matching and Record Linkage, Census RR93/8 (for Fellegi and Sunter).

Read through passages from copies hosted outside the publisher (check quotes against the journal version before external use):
- Barzel 1982 (SFU), Holmstrom 1979 (gwern.net), Klein and Leffler 1981 (edegan.com), Mookherjee and Png 1989, pp. 399-401 (kylewoodward.com), Lamport, Shostak, Pease 1982 (UMass), Winograd 1987-88 (lri.fr).
- A permission block stopped further fetching of walled articles from third-party copies, partway through this work. The items above were read before it. Nothing was fetched from such copies afterward.

Abstract or bibliographic level only: Townsend 1979; Dye 1986; Khalil 1997; Melumad and Mookherjee 1989; Kofman and Lawarree 1993; Avenhaus, von Stengel, Zamir 2002; Border and Sobel 1987 (via M&P); Wald 1945; Wald and Wolfowitz 1948; Alexander et al. 2013; Jans, Alles, Vasarhelyi 2014; McCarthy 1982 (partial abstract); Gama et al. 2014; Kalman; Virgo et al. 2025 (arXiv 2508.06326, summary).

Secondary only, original not read: Fellegi and Sunter 1969 (search extracts and Winkler); Deming 1986; Long, Malitz, Ravid 1993; Goodhart 1975; Lucas 1976; Power 1997; Searle 1995; Suchman 1994; AS 1105, AS 2315 and AS 2201 Appendix B (search extracts); Hammer 1990 (HBR 68(4), paywalled; primary copy not obtained).

Not read, and carrying no weight here: Ashby 1956 and Meyer and Rowan 1977 (named above from general knowledge only). Sought but not obtained, and not used: Macaulay 1963; Kent 1978; COSO 2013 full text; Kogan et al. 2014.
