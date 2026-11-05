---
title: "The Enterprise Process Conjecture"
subtitle: "A first-principles challenge to the three-way match"
date: "November 4, 2026"
---

**How to read the tags.** Every major finding carries one of four labels. **Established:** directly supported by reliable sources or reproducible testing. **Supported hypothesis:** plausible, with meaningful evidence, not demonstrated. **Speculative:** interesting, needs substantial work. **Rejected:** contradicted by evidence, testing or constraints. All simulation figures are synthetic, per 100,000 invoices, on stated assumptions. They show how the argument behaves. They are not forecasts or benchmarks.

# 1. Executive Discovery

The three-way match bundles four separate decisions into one, and only one of them is worth keeping in its current form. Comparing the purchase order, receipt and invoice on every transaction should stay. The other three should change: stopping the whole invoice when only the difference is in doubt, working exceptions one document at a time, and publishing a tolerance that a dishonest supplier can bill up to.

The central assumption challenged was that a mismatch must be resolved before money moves. It is not required by any statute, SEC rule, PCAOB standard or UCC section I could read. For the amount in dispute, holding the money remains sensible. For the rest of the invoice, I found no reason to hold it beyond an old habit.

My first answer failed. "Pay the lesser amount and make the supplier claim the rest" was rejected in adversarial review. It is already Medicare law, an SAP function and standard big-box retail practice, and it moves cost onto suppliers rather than removing it.

The rebuilt process, Split Settlement, survived better, but its honest gain is modest: about 0.2 basis points of spend in a world of honest suppliers, inside the noise of the model. It is worth much more only if suppliers really do bill to the tolerance, which nobody has measured.

The larger finding was unexpected. In the model, cleaning the buyer's own records was worth about twelve times more than changing the rule. In the one real log available, about 80% of payment blocks ended with no document corrected. The match is presented as a check on suppliers. The evidence suggests it mostly reports errors in the buyer's own records.

**Verdict: B, meaningful optimization.** The machine survives, with one part removed.

# 2. Why This Process?

Eleven candidates were scored from 1 to 5 on ten criteria. Scores are analyst judgment, not measurements. The last two criteria are inverted risks, so 5 means low risk of confusing law with habit, and low chance the idea already exists.

| Candidate | Std | Breadth | Econ | Legacy | Handoffs | Room | Testable | Impact | Law clarity | Novelty | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Three-way match** | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 2 | **43** |
| Delegated approval chains | 3 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 3 | 3 | 39 |
| Annual budgeting | 3 | 5 | 5 | 4 | 4 | 4 | 2 | 5 | 5 | 2 | 39 |
| Periodic financial close | 4 | 5 | 5 | 4 | 5 | 3 | 3 | 5 | 2 | 2 | 38 |
| Intercompany reconciliation | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 3 | 4 | 2 | 36 |

The three-way match won because it is highly standardized, is performed at very high volume, rests on old assumptions, and can be tested on synthetic data and a public event log. Its weakness showed in the score from the start: novelty headroom of 2. That proved accurate.

Frame: US public mid or large company, SOX, US GAAP, external audit.

# 3. The Conventional Model

**What it is.** A buyer compares its purchase order, its goods receipt and the supplier's invoice before paying. If they agree within tolerance the invoice pays. If not, payment stops until a person resolves it. **Established**, from Oracle and SAP documentation.

**Why it exists.** Once the person who orders, the person who receives and the person who pays are different people, no one knows all three facts. Paying on the seller's word means trusting the party who benefits.

**History. Established from primary texts.** The three-document logic appears in Kirkman's railway supply manual in 1887. Montgomery's 1912 audit text gives nearly the modern control in one paragraph. Griffith wrote in 1917 that "Vouchers should never be made for invoices in dispute", the ancestor of the payment block. The American Institute of Accountants named a clerk "whose job is to match invoices, purchase orders and receiving reports" in 1949. The term "three-way match" is confirmed in 1977 software advertising. SOX did not create it, and it is not primarily a fraud control: the early sources stress shortage and clerical error, and Kirkman doubted its value against collusion in 1887. The origin of tolerances could not be found.

**The conventional sequence.**

| # | Step | Owner | Decision or handoff |
|---|---|---|---|
| 1-2 | Requisition raised and approved | Requester, budget owner | Approve, reject, return |
| 3 | PO issued | Buyer | Vendor, price, terms; handoff to vendor |
| 4 | Vendor ships | Vendor | Handoff to dock |
| 5 | Goods received, counted, posted | Receiving or requester | Accept, reject, partial; accrual posted |
| 6 | Invoice captured, duplicate check | AP | Handoff to matching |
| 7 | Match line by line | System | Within tolerance? If yes go to 12 |
| 8 | Whole invoice blocked | System | Payment stops; the supplier's clock keeps running |
| 9-10 | Exception triaged, cause checked | AP clerk, buyer, receiver, vendor | Who is right? Mostly email and phone |
| 11 | Resolved, block released | AP or manager | Release or reject |
| 12-14 | Posted, proposed, paid | System, treasury | Pay, hold, take discount |
| 15 | Clear and reconcile | AP, GL | Accrual, audit sample |

**Law versus custom. Established for texts read.** Exchange Act 13(b)(2), SOX 302 and 404, Rule 13a-15(f), SEC Release 33-8810 and AS 5 (now AS 2201) require outcomes: accurate books, authorized spending, reasonable assurance. None names the match. The filed text of AS 5 contains the words "invoice", "purchase order" and "matching" zero times. AS 2201 says testing depends on whether controls address the risk "rather than on how the control is labeled". The only official text found that requires the match by name is a Bureau of Indian Affairs manual. COSO 2013 could not be read in full. Under UCC Article 2 the debt arises from contract plus acceptance, and "The buyer must pay at the contract rate for any goods accepted" (2-607(1)). The invoice is a demand, not the source of the debt. Once a company names the match a key SOX control it must operate, which is why it feels mandatory: DXP Enterprises reported a weakness in 2024 over clearing match discrepancies.

**What it does not address.** Payment to a fraudster's bank account, collusion, and forged documents. McKesson & Robbins showed in 1938 that documents can agree perfectly because the fraudsters wrote all of them.

# 4. The Hidden Assumptions

Load is a 1 to 5 judgment of how much of the process rests on the assumption.

| Assumption | Class | Load | What would settle it |
|---|---|---|---|
| Money leaves only against evidence of an obligation | Necessary | 5 | A viable firm with no evidence and no recourse. None found |
| Agreement among records is evidence of truth | Unproven | 5 | Seed known errors and measure how many pass |
| The three records are independent | Contingent | 5 | Measure how often one record was copied from another |
| Per-transaction checking pays | Contingent | 5 | Measure cost, error rate, catch rate and size by category |
| Holding cash beats chasing it | Contingent | 4 | Measure net recovery by supplier class |
| A mismatch means something is wrong | Unproven | 4 | Classify exceptions by true cause |
| The PO fully states what is owed | Unproven | 4 | Share of exceptions fixed by changing the PO |
| The invoice line is the right unit of control | Conventional | 4 | Compare line and running-balance control |
| The whole invoice must wait | Historical | 4 | Loss and cost when only the difference waits |
| Fixed order: order, receipt, invoice, match, pay | Conventional | 4 | Already reversed by C.O.D., letters of credit, fast pay |
| A false hold costs nothing | Unproven | 3 | Prices of similar suppliers with different dispute rates |
| A tolerance protects without being exploited | Unproven | 3 | Distribution of overbills just under the limit |
| Comparing is slow | Historical | 3 | Solved for structured data |
| Software forced this design | Rejected as origin | 2 | The design is in print by 1912 |

The most central are the first three. The most exposed is "agreement implies truth". The one nobody defends when asked is that the whole invoice must wait.

**Schema and semantic drift. Supported hypothesis.** Schema drift fails loudly: a new field breaks a parser. Semantic drift fails silently. "PO exists" once meant prior authorization, but an after-the-fact PO keeps the field and loses the meaning. "Received" may mean counted at the dock or clicked by someone clearing a block. The match compares values, not meanings, so it keeps passing while its evidence erodes.

**The deeper data problem. Supported hypothesis.** No record stores the obligation itself. The PO is a commitment, the receipt an observation, the invoice a claim. What is owed is inferred by comparing three shadows of it. A single stateful record of the obligation would remove mismatches caused by representation, such as timing, partial delivery and approved changes. It would not remove the need for independent evidence, and a shared record could destroy the independence that makes comparison worth anything. An ontology names distinctions. It produces no evidence. **Rejected:** the claim that a better data model alone solves verification.

# 5. The Central Conjecture

The strongest fair form, deliberately not weakened:

> To settle every true obligation in the right amount, to the entitled party, at the best time, and to state what is owed correctly at every reporting date, with reasonable assurance and at a total cost below the loss prevented, where suppliers and insiders hold private information and may gain by misstating it, where money paid is harder to recover than money held, and where outsiders must be able to rely on the result, an organization must:
>
> **A.** Establish in advance, with authority, what will be owed.
>
> **B.** Obtain evidence of performance independent of the claimant.
>
> **C.** Bind the claim to that obligation and confirm the claimant.
>
> **D.** Compare A, B and C for every transaction above a trivial value, by a fixed rule interested parties cannot waive.
>
> **E.** Withhold the disputed amount until the difference is resolved.
>
> **F.** Send differences to someone with authority and no conflict.
>
> **G.** Keep evidence an outsider can re-perform.

This form explains why the process has lasted over a century. A universal rule gives detection, deterrence and commitment in one step, and it is cheap to prove to an auditor. Note clause E says the disputed amount. Practice goes further and holds the whole invoice. That gap became the most useful thing found.

# 6. The Challenge

**Counterexamples.** Federal fast pay pays "prior to the Government's verification", capped and with recourse. Evaluated receipt settlement drops the invoice. Procurement cards drop the match for low value. GAO has accepted sampling since the 1960s. So "it must be done in this form" is false. **Established.** But every counterexample keeps the core (authority, independent evidence, recourse, proof). No precedent found omits verification. Ford's famous case removed the invoice, not the match: Hammer says 14 items became three, still automatic and still before payment. **Rejected:** "Ford eliminated the match."

**Six alternatives investigated.**

| Approach | Principle | Rejects | Result |
|---|---|---|---|
| Audit and recover | Deterrence | Every mismatch needs a person first | Live rival. Strong evidence outside AP, none inside |
| Buyer-computed settlement (ERS) | No second version of truth | Seller's document triggers payment | Proven and narrow. Moves the check to the dock and loses the second opinion |
| Contract and trusted status | Move the risk | Buyer carries each transaction | Enabling layer only. Does nothing alone |
| Population monitoring | Process control | Assurance is a sum of document checks | Essential companion, weak replacement. Kogan et al. found high misses at small error sizes |
| Physical event evidence | Verify reality, not paper | Agreeing records prove value received | Strong truth, narrow and costly |
| Balance settlement with true-up | Change the unit of account | Payment maps to transactions | Elegant for steady relationships. Credit exposure limits it |

**The failed attempt: lesser-of settlement. Rejected.** My first proposal was to pay the lower of the invoice and the buyer's record on the due date and let suppliers claim the rest. It looked excellent: cheapest in every cell of my own simulation. That result was too good, so it went to an independent adversarial reviewer, which found:

- **It is not new. Established.** 42 CFR 414.21: "Medicare payment is based on the lesser of the actual charge or the applicable fee schedule amount." UC Accounting Manual D-371-36 says the same for invoices. SAP invoice reduction automates it. Walmart Code 11 and Amazon shortage claims run it at scale (vendor sources).
- **Seventeen biases in my model favored it.** The largest: I charged nothing for its own audit step, and my rival audit design was not really sampling.
- **It moves cost rather than removing it.** At moderate friction it saved the buyer $9,650 and cost suppliers $132,701 more, about $13.75 per dollar saved.
- **Burden shifting has a bad record. Established.** The UK Groceries Code Adjudicator found Tesco repaying acknowledged debts up to 24 months late, with margin hit when suppliers abandoned claims, and ruled that "Tesco must not make unilateral deductions." In Medicare Advantage only 1% of denials were appealed and 75% of appeals were overturned. Rite Aid booked unearned vendor credits as income. So my claim that suppliers would reliably report shortfalls was wrong: motive depends on the claim being worth filing.
- **It trips four rejection conditions:** already standard, no better than simple optimization, benefits vanish, worse on joint cost.

**What survived the failure.** A single wrong record cannot cause an overpayment under this rule, the rule is easy to audit, and the same payment rule with the buyer doing the work beat the supplier-claim version on joint cost in all 240 test worlds. The burden shift was the defect.

**Other ideas rejected.** Sampling the comparison (cheap comparison favors checking everything). Shared ledgers (a shared record of PO and receipt is Ford's database again, the dock still needs a trusted reporter, and several trade networks closed). AI making the match unnecessary (no vendor claims it, no independent evaluation exists).

# 7. The Discovery

**The assumption that no longer appears necessary:** that a disagreement about part of an invoice justifies stopping all of it.

The practice traces to a paper voucher that could not be split: one document, one signature, one payment. **Speculative as to cause. Established as to the 1917 rule.** The law does not require it. The debt on accepted goods exists regardless of an internal block, and a block does not stop acceptance (UCC 2-606, my reading). Comparison is now close to free and a payment can be split at no cost, yet every ERP still holds the document. Clause E of the conjecture survives. The habit built on top of it does not.

**The assumption that remains necessary:** independent evidence and a universal machine comparison. Every attempt to remove them failed, and cheaper computing strengthens them.

**The insight that matters more:** the match mostly reports on the buyer. In the one real log available, 26.5% of invoiced three-way items were blocked. About 80% of blocks showed no correction to any document. About 7% showed the invoice corrected, and about 13% showed a change to another record. Of blocks with any document change, 65% changed something other than the invoice. **Established for the counts. Supported hypothesis for the reading.** It is one Dutch-based company, without dollar values or reason codes. Federal data points the same way: of $351 million returned by 39 contractors, 77% traced to contract administration and 18% to billing or payment errors. The analogy is loose.

In the model, the same pattern holds by a wide margin:

| Change, moderate friction, 10 seeds, per 100,000 invoices | Joint saving | Share of spend |
|---|---|---|
| Change the rule (T+ to Split Settlement), honest suppliers | $11,877 (std dev $12,869) | about 0.2 bp |
| Clean the buyer's records (70% fewer record errors) | $148,033 (std dev $16,429) | about 2.8 bp |
| Change the rule, 5% of suppliers billing to the tolerance | $185,543 (std dev $42,044) | about 3.5 bp |

Cleaning is treated as free in this table, which flatters it. Its real cost is unknown.

# 8. A Different Purpose

| | Original | Proposed |
|---|---|---|
| Purpose | Confirm the documents agree before paying | Keep a true record of what is owed, and pay it |
| Who is being checked | The supplier | The buyer's records first, the supplier second |
| What a mismatch is | A reason to stop | A defect report with an owner |
| Measure of success | Match rate, cycle time | Dollars misallocated, repeat causes, share of blocks with a real correction |

This is a real change of emphasis, but I stop short of claiming it as outcome E. **Supported hypothesis.** It rests on one company's log and a model. If a dollar-weighted study showed most blocks catch real supplier errors, the original purpose stands.

# 9. The Reconstructed Operating Model: Split Settlement

Designed from the objective, not from the old steps. Activities came back only where something required them.

**Scope.** Repeat PO-backed goods with a reliable record. Services, non-PO spend and variable pricing keep their current control.

| # | Step | Who | Why it exists |
|---|---|---|---|
| 1 | **Hard gates.** Real supplier, verified bank details, authorized commitment, something received, not a duplicate. Fail any one and nothing pays | System | Conjecture clauses A, B and C. Payee check is added because the match never covered it |
| 2 | **Compare everything,** both directions, on arrival, not at the end | System | Clause D. Near free |
| 3 | **Small differences pass,** up to the same limit as the simple fix | System | Pennies are not worth a person |
| 4 | **Watch the passes.** A running one-sided sum per supplier revokes the pass and opens a case. A limit that is watched stops being a safe harbor | System | Closes the tolerance gap |
| 5 | **One case per supplier per period,** grouped by likely cause, owned by the party who can fix it. Stale record goes to the buyer. A supplier is asked only when its own invoice looks wrong | Buyer | Moves the unit of work from document to cause. No supplier claim process |
| 6 | **Work the case inside terms.** Fix the record, and every line it touched corrects itself. Late receipts true up automatically | Buyer | Uses the credit period the old process already has |
| 7 | **At the due date, pay what is not in doubt.** Only the difference waits, as an open payable | System | Clause E, applied as written |
| 8 | **Circuit breaker.** A sudden spike in differences for a supplier or item is treated as one record fault, and short payments stop until a person looks | System and buyer | Stops a bad price upload becoming thousands of short payments |
| 9 | **Small random audit** of receipts and passes, chosen by plain random draw | Internal audit | Covers the case where both records are wrong together, and measures the true error rate |
| 10 | **Report repeat causes** to the people who own the records, in dollars | Finance | Serves the new purpose |

**Controls kept unchanged.** Segregation of duties, vendor master and bank-change control, payment authorization, retention, period-end accrual. The open difference stays a recorded payable, so nothing reaches income through abandonment.

**Buyer accountability.** Interest on any difference that was the buyer's error, and a measure of buyer-fault differences that reaches the CFO. Claim outcomes stay away from buyer margin targets. Tesco is the reason.

**What changes for a supplier.** On a stale price, it may receive part of an invoice on time instead of none of it late, and it never files a claim.

# 10. The Role of AI

Almost nothing at the core of this process needs AI. That is a finding, not a gap.

| Capability | Where used | Needed? |
|---|---|---|
| Deterministic computing | Gates, comparison, pass limit, payment split, running sums, random draw, true-up | **Core, and should stay non-AI.** Auditable, cheap to prove, cannot be talked around |
| Classification | Sorting differences by likely cause in step 5 | Useful. Rules first, models where rules run out |
| Retrieval | Pulling the contract clause, amendment or email behind a difference | Useful, likely the best fit today |
| Information integration | Joining contract, ERP and carrier records into one case | Useful, mostly ordinary data work |
| Reasoning | Proposing a cause, drafting the case and supplier note, for a person to decide | Helpful, human decides |
| Prediction | Spotting records likely to go stale before they cause a mismatch | Speculative value |

**Possible today, with review:** reading contracts into a price file with sign-off, classifying causes, gathering evidence, drafting. Evidence is preprints and vendor claims only. I found no independent evaluation of AI match performance.

**Would need better proof:** unattended decisions to withhold or recover money, judging whether an unusual charge is legitimate, and resisting adversaries who probe the model. A model should never sit in the payment calculation. Generative tools also make convincing fake invoices cheaper, which favors controls that do not depend on a document looking right. **Speculative.**

# 11. The Evidence

**Actual tests (reproducible, in `research/tests/`).** All synthetic, using no company data.

*Baseline: verified figures. Self-reported surveys unless noted.*

| Measure | Figure | Source |
|---|---|---|
| Cost per invoice | $6.50 median; $9.84 average | APQC n=6,546; Ardent 2025 n=204 |
| Invoice lines matched first time | 75.0% median | APQC n=4,438 |
| Exception rate (broader than match failure) | 18.4% | Ardent 2025 |
| No human touch | 35.4% | Ardent 2025 |
| Invoice receipt to payment | 15.0 days median | APQC n=2,226 |
| Duplicate or erroneous disbursements | 1.5% median, by count, not dollars | APQC n=2,386 |
| Staff time on supplier inquiries | 21.9% | Ardent 2025 |
| Blocks: share of items; median length | 26.5%; 6.2 days | BPI 2019 log, one company, tabulated for this study |

The conflicting Ardent exception rates resolve: 18.4% is the 2025 average, 22% is the 2024 "All Others" group, and 14% is a printed 2024 average that does not fit its own subgroups. None measures match failure. No public source gives cost per exception, root causes from an original survey, loss prevented by the match, or a dollar split of real against harmless mismatch. That is the largest gap in the field.

*Policies compared at moderate friction (reviewer's step 3), per 100,000 invoices, spend about $534 million.*

| Policy | Buyer cost | Joint buyer and supplier | Overpaid |
|---|---|---|---|
| T: wider tolerance | $374,052 | $550,865 | $124,822 |
| T+: fair simple fix (batched, one-sided, record fixes) | $300,501 | $453,389 | $129,437 |
| A+: true sampling audit | $346,191 | $449,057 | $221,413 |
| U: pay the lesser, buyer works it, with foresight | $329,759 | $481,171 | $90,956 |
| L: lesser-of, supplier claims (rejected) | $290,851 | $576,440 | $90,296 |
| **S: Split Settlement** | **$277,899** | **$440,495** | $112,241 |
| Tc: T+ with clean records | $188,740 | $291,592 | $70,214 |
| **Sc: Split Settlement with clean records** | **$179,596** | **$281,824** | $55,392 |

*240 random worlds, the reviewer's ranges. A range is not a probability.*

| S is lower than | T | T+ | A+ | U | L |
|---|---|---|---|---|---|
| Buyer cost | 240 | 198 | 110 | 235 | 187 |
| Joint cost | 232 | 144 | **18** | 121 | 239 |
| Overpaid | 238 | 240 | 160 | 3 | 78 |

**How to read this honestly.**

- S beat the simple fix in 144 of 240 worlds on joint cost. That is a lean, not a win.
- **The sampling audit beat S on joint cost in 222 of 240 worlds.** It is a serious rival. I still prefer S because A+ leaks about twice as much at step 3, its model assumes 80% recovery plus penalties with no supplier failure, and I found no public company whose auditor accepted it. Those are arguments, not test results.
- **S was changed after its first run failed.** Run 1 lost to the simple fix at every step of the reviewer's ladder. Part of that was a bug: underbilled suppliers had no way to rebill. I then widened its pass limit to match T+ and cut its audit depth from 0.5 to 0.1 looks per supplier-period. At depth 0.5 it loses to T+ by about $71,000 joint. Run 1 is kept in `final-output-run1.txt`. This tuning is a real weakness, and the proposer wrote S.
- S loses to T+ on joint when supplier reconciliation cost passes about $14 per short-paid invoice (interpolated; about $24 if suppliers pass back half their cost), when buyer records are very dirty (15% or more of invoices), when records are already very clean (1%), and when nearly all differences clear inside terms.
- Its advantage over T+ at 5% padders rests on model padders who stop once revoked. Real ones might re-enter under a new name.

**Controlled thought experiments. Reasoned, not tested, except where noted.**

| Scenario | Conventional | Simple fix | Split Settlement |
|---|---|---|---|
| 1. Normal: repeat supplier, all agree | Pays | Pays | Pays. No difference at all |
| 2. Multiple systems: price raised in the contract system, ERP stale, 40 invoices | 40 full invoices stopped, 40 chases | One batched case, invoices still held | One case, one fix, all lines correct. If unfixed at due date, each pays at the old price and the rest follows. Supplier reconciliation cost is the risk (tested) |
| 3. Missing or conflicting: split shipment, receipt late | Invoice held | Invoice held | Received part pays, the rest trues up. A wholly late receipt still stops payment. **Not solved** |
| 4. Changing meaning: "received" now means a requester clicked to clear a block | Passes silently | Passes silently | Passes silently in steps 1 to 7. Only the random audit can see it. Services stay out of scope for this reason |
| 5. Adversarial: supplier bills to the limit every time | Leaks up to tight tolerance | Leaks up to the wide limit, forever | Pass revoked (tested). A forged receipt with insider collusion beats all three. Bank diversion is caught only by the payee gate |
| 6. Scale and failure: bad price upload hits 50,000 lines | Mass stops, visible, nobody paid | Mass stops | Without step 8, mass short payments. Step 8 is what makes this safe, and it is untested |

**Formal checks.** `check_properties.py` confirms by exhaustive arithmetic that under a lesser-of payment rule one wrong record alone never causes overpayment. The reviewer correctly noted that this is close to a tautology and proves nothing about business outcomes. No business result here is proven in any mathematical sense.

# 12. The Strongest Objections

**"GAO already said it: automation makes relaxation unnecessary."** Fair for sampling. GAO's point concerns the cost of comparing, which this process keeps. It does not address the cost of the stop.

**"This is just tolerance plus partial pay, a configuration change."** Largely true. It uses existing functions and known ideas. Hammer and Champy wrote in 1993 that controls may "tolerate modest and limited abuse". The contribution is the separation of the four decisions and the evidence on where the money is, not a new mechanism. I accept this objection.

**"Stops are mostly harmless because they finish inside terms."** Possibly. Median block length was 6.2 days against about 30 to 44 days to clear in the one log. If so, the whole-invoice hold costs little, and S's gain shrinks. In the model it falls to about nothing when almost all stops clear in time.

**"Partial payment creates supplier work."** Yes. Reconciling a part-paid invoice is real cost, unmeasured anywhere. Above about $14 per item S loses on joint cost. That is a low bar, and the most likely way this design fails.

**"The buyer loses the pressure a stop creates to fix records."** Serious. A stop forces attention. S replaces this with case ownership and reporting, which may be weaker in a real organization.

**"Min-style payment hides the case where the record is too high."** Correct for a plain lesser-of rule, so S compares both ways and logs it. A control over the record itself is required. PCAOB AS 1105 requires testing of company-produced information.

**"Your simulation was written by the person proposing the answer."** True, and it was tuned once. That is why an independent reviewer attacked it, why the failed runs are kept, and why I claim only a modest result.

**Accounting and legal questions, all needing a professional to confirm.** Liability completeness for open differences (ASC 405, ASC 450), sales and use tax when paid differs from invoiced, unclaimed property on aged differences, and contract terms for partial payment. The legal readings here are mine, not counsel's.

# 13. Economic and Operational Implications

**Benefits, if the model's shape holds.** Fewer full-invoice stops, fewer late payments, better discount capture, one case in place of many, the safe harbor closed, and a measured error rate for the first time.

**Costs.** Case and record ownership work in purchasing, supplier reconciliation, contract language, a new accrual routine, and the audit step. Implementation cost is not modeled and could erase a gain of 0.2 basis points. On $534 million of spend that is about $12,000, which would not pay for a project.

**So the rule change alone does not justify itself unless strategic overbilling is real.** The record-cleaning effect might, and it needs no redesign. An organization could capture most of the modeled benefit by working the top causes of blocks.

**Organizational effect.** Accountability moves from AP clerks chasing documents toward purchasing owning record accuracy. That is the hard part, and it is a change in who gets blamed.

**Commercial note, stated neutrally.** Since the core is deterministic and available in existing ERPs, this does not obviously imply a new product. Measuring the true causes of blocks in dollars is a real unmet need. What to do with that is your decision.

# 14. The Verdict

**Outcome: B. Meaningful optimization.**

The fundamental logic of the match is sound and survives: authority, independent evidence, universal comparison, resolution by someone without a conflict, proof. One clause was overextended in practice, and the surrounding routine can improve.

I considered C (structural redesign) and did not earn it: the gain over a simple fix is inside the noise unless strategic overbilling exists. I considered D (elimination): **Rejected**, since no precedent omits verification. E (purpose transformation) is the most interesting open possibility, but it rests on one company's log.

| Finding | Status |
|---|---|
| No US statute, SEC rule or PCAOB text read names the match | Established |
| The form is not necessary; the core is | Established for the form, Supported hypothesis for the core |
| Lesser-of settlement is a new discovery | Rejected |
| Shifting the burden to suppliers is efficient | Rejected (synthetic, plus real abuse record) |
| Holding the whole invoice is unnecessary | Supported hypothesis |
| A watched limit closes the tolerance safe harbor | Supported hypothesis (synthetic) |
| Most blocks reflect buyer records, not supplier error | Supported hypothesis (one company) |
| Split Settlement beats the simple fix on honest suppliers | Speculative: inside model noise |
| Record quality matters more than the rule | Supported hypothesis (synthetic, cleaning cost excluded) |
| The match should be eliminated | Rejected |

**Confidence.** High that the match is custom rather than law and that its core survives. Moderate that the whole-invoice hold is unnecessary. Low on any dollar figure.

**Most important unresolved.** The dollar split of blocks by true cause. How much overbilling sits just under tolerances. What a part-paid invoice costs a supplier. Whether an auditor would accept the design. No auditor, lawyer or supplier was consulted.

**The redesign should be rejected if:** a dollar-weighted study shows most blocks catch real supplier errors; supplier reconciliation cost exceeds about $14 per part-paid invoice; suppliers raise prices by more than a fraction of a basis point; its gain disappears against a well-run simple fix after implementation cost; or auditors will not accept it.

# 15. The Next Experiment

**Blind cause audit of payment blocks.** Do not build anything. This one test settles the central finding, and it is cheap.

**Evidence required.** At one or two willing US companies, a random, dollar-stratified sample of about 1,000 blocked invoices from the past year, and an equal sample of invoices that passed, with contracts and receipts. For passed invoices, include amounts just under tolerance.

**Conditions.** Reviewers independent of AP and purchasing assign each item a true cause and a true amount owed, blind to how it was resolved. Add a seeded set of known errors in a test copy to measure what the match really catches.

**Measurements.** Dollars by cause (supplier error, buyer record, timing, legitimate change); share of blocks clearing inside terms; true error in passed invoices; clustering of overbills just under tolerance; catch rate on seeded errors.

**Success criteria for the central finding.** More than half of blocked dollars trace to buyer records or timing, fewer than one in five to real supplier overbilling, and most blocks would have delayed a payment that was right.

**Falsified if.** Real supplier overbilling accounts for most blocked dollars, or passed invoices show no clustering under the tolerance and no meaningful true error, in which case the simple fix is enough.

The public BPI 2019 log can be used first at no cost to refine the method, though it lacks dollar values.

# 16. The One Question That Changes Everything

**If most invoices you stop turn out to be right, whose records are you really checking?**

# Appendix: Sources and Limits

The full evidence, with URLs, is in the repository under `research/agents/`: `01-conventional-model.md` (history, law, numbers), `02-assumptions.md` (ledger, theory), `03-alternatives.md`, `04-prior-art.md`, `05-adversarial.md` (attack and legal analysis). Tests and outputs are in `research/tests/` and `research/`.

Key primary sources: 15 USC 78m(b); SOX 302 and 404; 17 CFR 240.13a-15(f); SEC Release 33-8810; PCAOB AS 2201 and AS 1105; UCC 2-310, 2-513, 2-606, 2-607, 2-717; FAR 13.4; 42 CFR 414.21; GAO/AIMD-21.3.2 (2000); GAO-01-309; Kirkman (1887); Montgomery (1912); Griffith (1917); AIA, Internal Control (1949); Hammer (1990); Hammer and Champy (1993, read in 2001 edition); UK Groceries Code Adjudicator, Tesco report (2016); HHS OIG OEI-09-16-00410; SEC Release 34-46099 (Rite Aid); Kogan et al. (2014); Jans et al. (2014); BPI Challenge 2019 event log, DOI 10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1.

**Could not be verified.** COSO 2013 full text. The live AS 2201 page in some lines (read through a 2007 filing and an archive copy). ASC text. EU Directive 2019/633. Several theory papers read only in abstract. Retail deduction rules, from vendor sources only. Ford's numbers, which trace only to Hammer. OpenAI's two index pages returned 403, though a summary of the `openai/math` repository was reviewed. The inspiration was its practice of keeping results open to verification and revision, not any undisclosed method. Nothing here claims access to private techniques.

Evidence is limited to what could be reached in one working session. Claims that something was not found mean not found here, not proof of absence.
