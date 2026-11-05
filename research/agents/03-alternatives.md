# Line 03: fundamentally different ways to get what the three-way match is for

Frame: US public mid/large company, SOX, US GAAP, external audit. Tags used on claims: **[Established]**, **[Supported hypothesis]**, **[Speculative]**, **[Rejected]**. Bracketed numbers point to the source list at the end. Written independently of the other research lines, as instructed.

## Bottom line

- The expensive part of the match is probably not the comparison. Comparing fields is nearly free by machine. The cost sits in the stop: the payment hold, the exception queue, the human chase. **[Supported hypothesis: logic plus the inspection-cost reasoning in [22]; no authoritative cost split found]**
- So the question to test is not "should we compare documents?" (a machine should keep comparing everything). It is "should a mismatch stop the payment, and should a person look at every one?"
- Best proven alternative: buyer-computed settlement (Approach B), for repeat purchases with a clean price file and a trustworthy receipt. It has run at industrial scale since around 1990, but mostly moves the check rather than removing it.
- Most deserves testing: audit-and-recover settlement (Approach A), which keeps the 100% machine check, stops holding payment for ordinary mismatches, and investigates a random plus risk-weighted sample, with results extrapolated to the whole supplier-period. Its evidence is good outside AP and absent inside AP. That gap is why testing it is worth more than testing B.
- The simple improvement (higher tolerances, no-PO thresholds, PO discipline) is a serious rival. If mismatches are mostly honest noise, it may win. Its weakness is specific: a published tolerance is a safe harbor. That weakness is the main thing a simulation should measure.
- Nothing in this line shows the three-way match should be abandoned. It shows that the match bundles several separable jobs, and that other fields settled each job differently.

## 1. What the business actually needs

Stated without reference to any workflow. A company buying from others needs:

1. **Authority.** Money leaves only for commitments someone entitled to commit actually made.
2. **Value received.** It pays only for what it really got, in the quantity and quality agreed.
3. **Agreed price.** It pays what was agreed, not more.
4. **Once, to the real party.** No duplicates, no payment to an impostor.
5. **True liabilities.** At any period end it knows what it owes, including goods received and unbilled.
6. **Provable to outsiders.** Auditors, tax authorities and courts can be shown 1 to 5.
7. **Deterrence.** Employees, suppliers and outsiders believe stealing or padding will not pay.
8. **Supplier willingness.** Suppliers are paid predictably enough to keep supplying on good terms.
9. **Tax and regulatory data** can be produced from the transaction.

The underlying economic problem is asymmetric information: the seller knows what it delivered and the buyer has to find out, at a cost. Economists call this costly state verification [17]. The objective is therefore not zero mismatches. It is to minimize expected leakage plus cost of control plus cost of friction, subject to reasonable assurance. The legal standard fits that framing: the "degree of assurance as would satisfy prudent officials in the conduct of their own affairs" [2], and the SEC says reasonableness is not "an absolute standard of exactitude" [3]. **[Established]**

Three observations follow.

- The match serves needs 1, 2 and 3 with one per-document gate, partly serves 5 and 6, and does little for 4 and 7. It does not check bank-account diversion: the FBI recorded $3.05 billion of reported business email compromise losses in 2025 across all victim types [13]. That category is not all AP, but a PO, receipt and invoice can all agree while the money goes to a criminal. **[Established for the figure; the inference about the match is logic]**
- It verifies agreement among records, not reality. Three records can agree and all be wrong if a receipt was keyed to clear a block, or a padded price was on the PO. **[Supported hypothesis; I found no authoritative rate]**
- Control law does not require per-document prevention. Management "may identify preventive controls, detective controls, or a combination of both" and is not required to identify every control [3]. **[Established]** I found no statute, PCAOB or SEC text that prescribes a three-way match, though that search was not exhaustive and I could only reach AS 2201 through excerpts [4].

## 2. The test for "level 3"

Applied strictly to every approach below. Level 3 requires all three of these:

- an assumption of the old process is rejected;
- either one of the three documents ceases to exist, or the per-document stop ceases to exist for the covered spend;
- something else demonstrably carries the control objective.

Faster, cheaper or smarter versions of the same steps are level 1. Better tuning of the same design is level 2. Age is not a test: a 35-year-old idea can be level 3, and a new AI product can be level 1.

## 3. The baseline any radical option must beat

**The simple improvement, no redesign:** raise tolerances to the point where cost of handling exceeds the expected value of the variance, apply no-PO thresholds with cards below a limit, use blanket POs and price agreements so that price variances stop arising, enforce same-day receipting, fix the top few recurring exception causes at the source, and run separate bank-change verification.

Precedent: the federal micro-purchase threshold rose from $10,000 to $15,000 on October 1, 2025, a formal statement that below a line the process costs more than it protects [14]. **[Established]**

Why it is hard to beat: it needs no contract changes, no supplier cooperation and no new control theory, and auditors already understand it. If most mismatches are honest noise, it may capture most of the available benefit. **[Supported hypothesis]**

Its specific weaknesses:

- A published tolerance is a safe harbor. A strategic supplier can bill to the edge of it on every invoice, and the loss is invisible because no exception is raised. Maximum leakage is about tolerance times invoice count per supplier. **[Supported hypothesis: arithmetic; no data on how often it happens]**
- It leaves the stop in place for everything above the line.
- It produces no estimate of the true error rate, because passed invoices are never examined.

Decision rule: a radical option earns a recommendation only if it beats this baseline on total cost at equal or lower leakage, in the honest-supplier world and in the strategic-supplier world, and can be defended to an auditor.

## 4. Six approaches

### Approach A: audit-and-recover settlement (verification as an option, not a gate)

**Organizing principle:** deterrence. Make padding unprofitable in expectation instead of stopping each instance.

**Assumption rejected:** every mismatch must be resolved by a person before money moves.

**Mechanism replacing the old activity.** Machine comparison stays at 100% but stops being a gate for the covered population. Ordinary mismatches pay on terms. Each supplier-period, a random sample plus a risk-weighted sample gets real verification. Findings are extrapolated to the whole supplier-period and netted from the next payment. A hard value cap stays above which the old stop still applies. Contract terms set the audit window, the extrapolation method, the penalty and the cross-contract setoff right.

Two levers are bundled in "pay first, verify after" and should be separated:

- **Sampling** (not everything gets a person) carries most of the saving.
- **Timing** (paying before checking) carries almost none on normal terms. On net-30 or net-45, most sampled checks can finish before the due date, so "sample before paying" beats "pay then chase" unless speed itself earns something such as a discount. **[Supported hypothesis; simulation claim 6]**

**Precedents outside AP**

- FAR fast payment: the government pays before verifying receipt, on the contractor's certification that it shipped and will replace or repair anything lost or nonconforming. It is narrow: firm-fixed-price supplies, generally up to $45,000 per instrument, geographically separated delivery, and the agency needs a way to identify suppliers who abuse the procedure [1]. **[Established]**
- Oil and gas joint interest billing: non-operators pay the operator's bills, and payment does not waive the right to contest. Audit runs in a 24-month window, after which transactions are conclusively presumed correct [15]. A commercial, repeat-party example. **[Established for the form text as excerpted; real JOAs vary]**
- Airline interline settlement: IATA's manual includes a standard agreement for passenger accounting on a sampling basis [16]. Airlines evaluate a share of coupons and infer the total [16]. IATA counted about 10.25 million Form A/B items and about 143,000 Form D/E items in 2017 [16]. Note the counter-signal: those counts fell about 20% and 14% from 2015, and patent filings call the method's inaccuracy unacceptable [16]. I could not read the manual itself (paid), so the mechanics are partly inferred. **[Established that it exists; mechanics Speculative]**
- Medicare extrapolation: contractors may extrapolate overpayments from a sample, but only on a finding of a "sustained or high level of payment error" [18]. A useful template for a fair trigger. **[Established]**
- Income tax: self-assessment with random and targeted audits.

**Why it might work**

- Shi (QJE 2024): each dollar Medicare spent on audits generated $24 to $29 in savings, mostly from deterring future care rather than from reclaimed payments [19]. Deterrence, not recovery, carried the value. **[Established for that setting]**
- Olken (JPE 2007): raising audit probability from 4% to 100% cut missing expenditures by about 8 percentage points, from a baseline of about 24% [20]. Monitoring worked, but it did not eliminate the loss even at 100%. **[Established]**
- Random audits can dominate deterministic rules in theory [21]. **[Supported hypothesis: I relied on secondary descriptions of this result]**

The arithmetic of extrapolation is the key design point. Without it, a supplier padding invoices is deterred only if the share sampled s satisfies s(1+m) ≥ 1, where m is the penalty multiple. At m = 1, half of all invoices must be sampled. With extrapolation, the unit at risk is the whole supplier-period, and detection depends on the share of invoices affected (θ), not population size: 1 − (1 − θ)^n for a sample of n. Illustration, arithmetic only: at n = 20, θ = 20% gives about 98.8%, and θ = 0.1% gives about 2.0%. So a small sample reliably catches systematic padding and almost never catches a single rare event. That is why the hard value cap is not optional.

Deming's kp rule sharpens this. For a homogeneous stream, cost is minimized by inspecting all or none, with the break-even at k1/k2 (inspection cost over the cost of an escaped defect) [22]. With machine comparison, k1 is close to zero, so compare everything. **[Established as theory]** Sampling humans is justified by what kp assumes away: the sample also measures the error rate, and it changes supplier behavior. That is also why airlines' retreat from sampling is not fatal here: their sampling replaced evaluation that computers now do cheaply, while Approach A samples only the human part. **[Supported hypothesis]**

**What would make it fail**

- One-shot or thinly capitalized suppliers. Deterrence and netting need future payments to net against. Recovery is weakest exactly when most needed: the automatic stay limits setoff, §553(b) can claw back pre-petition setoffs that improved the creditor's position, and §547 covers preferences [23]. **[Established]**
- Weak recovery in practice. Pay-and-chase has a bad name in Medicare. GAO reports CMS and contractors regard prepayment review and suspensions as particularly effective at stopping potentially fraudulent claims, and CMS says it cannot deny a claim on analytics alone [24]. Congressional critics attacked reliance on pay-and-chase [24]. RACs reported a 77% recovery rate on overpayments in FY2023 [25]. Medicare's providers also cannot easily walk away, which a supplier can. **[Established; transfer to AP is Speculative]**
- Default law working against it. UCC 2-717 allows deduction from the price only under the same contract, and 2-607(3)(a) bars remedies without notice within a reasonable time after the buyer "discovers or should have discovered" a breach [26]. Sampling may have to be written into the contract, including the meaning of "should have discovered." **[Established statute; application is my reading, not legal advice]**
- Limitation: 2-725 gives four years, can shorten to one, cannot lengthen [26].
- Supplier refusal, or priced-in cost of extrapolated penalties.
- Auditor challenge on precision: see Approach D.

**Constraints unchanged:** GAAP liability and cutoff, vendor master and bank-change control, segregation of duties, payment authorization, 1099 and tax data, retention, purchasing authority.

**New risks:** a receivables book of claimed overpayments with valuation questions; dispute load concentrated at period end; supplier gaming of any non-random part of the sample; employee collusion with a supplier on sample selection.

**Change level:** 3, for the covered population, and only if the stop is really removed. Risk-routing exceptions while still holding them is level 2. **[Strict call]**

### Approach B: buyer-computed settlement (make the mismatch impossible)

**Organizing principle:** do not create the second version of the truth.

**Assumption rejected:** the seller's demand document is needed to trigger payment.

**Mechanism.** Three forms, in rising order of depth:

- Evaluated receipts settlement: the buyer computes the amount from receipt quantity times contract price and pays. No invoice exists [5][6].
- Jointly computed record: both parties work from one calculation built from contract terms and event data. Walmart Canada's freight network reports invoices jointly created on a platform, about 70 carriers, disputes down from about 70% to about 1.5%, and approval down from weeks to under a week [7]. The figures are the case study's own, from an interested party. **[Weak evidence, labeled]**
- Consumption settlement: the obligation arises at use or sale, not delivery. In scan-based trading the supplier keeps ownership until the point-of-sale scan, then is paid [8]. Power markets are the purest form: PJM calculates and issues netted weekly and monthly statements itself rather than receiving supplier invoices [9]. **[Established for PJM; SBT sources mostly vendor]**

**The honest reading of Ford.** Hammer's account says Ford's AP had more than 500 people, Mazda's had 5, Ford stopped asking for invoices, and a 75% head-count cut followed rather than the 20% from a conventional program [5]. I reached that through excerpts of the article, not the full text. **[Established, with that limit]** The check did not vanish. A PO-to-receipt comparison still ran, earlier in the flow. A commonly repeated detail, that receiving clerks refused goods not matching an open PO, could not be confirmed from the primary text.

**Information needed:** a contract-accurate price file, an accurate and independent receipt, tax determination on the buyer's side, and for consumption forms a trusted usage feed.

**Why it might work:** it removes the error class rather than handling it. The Danish tax experiment gives the closest rigorous analogy: evasion was close to zero on third-party-reported income and substantial on self-reported income. Deterrence by audit mattered far less than inability to cheat [10]. Brazil's NF-e shows the same logic in tax law: the invoice must be authorized before goods move [11]. **[Established for Denmark; Brazil sources are vendor and ERP documentation]**

**What would make it fail**

- Bad receipts. All the risk moves to the dock. An accounting text notes that ERS removes some of the match's controls and requires tighter receiving and firm pricing [6]. **[Established as textbook position]**
- Loss of the independent opinion. The invoice is a second, independently produced record. Without it, a keyed quantity error goes straight to payment. Suppliers will complain about underpayment, but not about overpayment, so the self-policing is one-sided. **[Supported hypothesis; simulation claim 3]**
- Price drift. A 2015 practitioner poll found no respondent with an automated process to clear PO-to-contract price differences on ERS [6]. **[Weak evidence, labeled]**
- Poor fit: services, one-off buys, variable pricing, freight and tax complications.
- I found no peer-reviewed study measuring ERS outcomes. That is a real gap.
- SBT has adoption and data-sync problems, and evidence on shrink conflicts [8].

**Constraints unchanged:** vendor master, receipt cutoff, tax, authorization. For consumption forms, ASC 606 control analysis decides who holds the inventory [12], and supplier-owned stock at a buyer's site raises perfection issues. UCC 9-102's consignment definition is about delivery to a merchant for sale [12], so factory consignment needs separate legal review. Outside the US, self-billing has formal rules: the UK requires a written agreement before starting, and marked self-billed invoices [27]. That matters for any non-US entity.

**New risks:** concentration of fraud risk at receiving, price-file tampering as a single point of failure, supplier revenue-recognition disagreements, and network dependence (any shared platform needs its own assurance).

**Change level:** 3 for ERS, jointly computed records and consumption settlement. All are level 3 by the test because the invoice, or the concept of a separate claim, disappears. A supplier portal, e-invoice, PO flip or a shared ledger that merely stores all three documents is level 1.

### Approach C: risk transfer by contract and supplier status (trusted-trader)

**Organizing principle:** verify the supplier's system once, assign the residual loss by contract, and price it.

**Assumption rejected:** the buyer must carry the risk of each transaction and therefore check each one.

**Mechanism.** Qualified suppliers accept audit rights, an overbilling warranty, a penalty schedule, a setoff right and possibly a bond or holdback. Status is earned by measured performance, and lost automatically.

**Precedents**

- Customs trusted trader: importers who passed ISA were removed from the Focused Assessment audit pool, but could still get single-issue audits [28]. Status narrows inspection and does not end it. **[Established]**
- Texas gold card: physicians with at least 90% approvals over a six-month period are exempt from prior authorization for that service, subject to periodic re-evaluation and rescission [29]. Very close to the design wanted here: earned, measured, revocable, and specific to the service. **[Established; effect on outcomes not assessed]**
- Skip-lot inspection: ISO 2859-3 and ASQ S1 formalize qualifying suppliers, reducing inspection, and reverting on failure [30]. **[Established that the standards exist; details not read in full text]**
- Card schemes: disputes are handled by a rulebook, and an excess ratio (Visa's merchant threshold reportedly 1.5% from April 2026) triggers program consequences [31]. Network rules allocate loss so the individual buyer need not check each charge. Consumer protection also sets dispute windows and allows withholding of the disputed amount [32], though corporate programs run mostly under scheme and contract terms. **[Reg Z Established; VAMP figures are from vendor summaries, weak evidence]**

**Why it might work:** it matches how repeat relationships actually behave, and a bond converts unknown recovery risk into a known cap.

**What would make it fail**

- Paper without enforcement. A warranty nobody tests deters nothing, so C depends on A or D to detect anything.
- Auditor independence. Duflo et al. found that when firms chose and paid their auditors, reports clustered just under the standard while true emissions were higher, and changing the incentives produced more truthful reports [33]. A supplier-commissioned attestation inherits that problem. **[Established for that setting]**
- A sleeper: a supplier builds a score and then defects. Exposure must be capped below the bond.
- Program drift: the DHS OIG found CBP did not always validate importers' self-reported final values, and that this may have put about $751 million in reconciliation refunds at risk, partly because procedures did not require source documentation and ports did not assess liquidated damages consistently [34]. A trust program with weak enforcement decays. **[Established]**
- Bonds and warranties cost money. Small suppliers cannot carry them, and costs come back in price.

**Constraints unchanged:** all the accounting and tax ones. Liability for misstatement stays with the registrant: a contract moves the loss, not the responsibility for ICFR. **[Established in principle]**

**New risks:** tiering may look discriminatory for diverse or small suppliers, legal cost, score manipulation.

**Change level:** 2 alone, because it changes who pays rather than what happens. It becomes 3 only for a qualifying tier where per-invoice verification really stops, and then it is relying on A or D for enforcement.

### Approach D: control as population-level monitoring

**Organizing principle:** statistical process control. The unit of control is the process and the ledger, not the document.

**Assumption rejected:** assurance is the sum of per-document checks.

**Mechanism.** No per-document stop. Continuous tests run on all postings: price drift by item and supplier, duplicates, invoice number patterns, split purchases, GR/IR aging, supplier share shifts, cost per unit against commodity indices, employee-supplier links, change-point tests. An alarm opens a process investigation, not a document exception.

**Evidence**

- Kogan, Alles, Vasarhelyi and Wu simulated a continuous data-level audit system on procurement data from a large health care provider, comparing detection models [35]. Directly on point, but a simulation, and I could not read the full results. **[Established that it was done; findings not verified]**
- PCAOB amendments effective for fiscal years beginning on or after December 15, 2025 clarify auditor duties when using technology-assisted analysis [36]. These concern auditors, not management controls.
- ACFE data: tips detect far more fraud than other methods (43% in the 2024 edition) [37]. A caution against assuming analytics is the primary detector. ACFE's data are CFE-reported cases, not a random sample. Billing schemes were 21% of cases in the 2026 edition [37], with conflicting median-loss figures in sources I saw.
- Medicare's analytics target billing patterns rather than single claims, and savings claims have been repeatedly cut: CMS reported $454 million for 2014 against an estimated $133 million actual [24]. FPS-linked figures are estimates and GAO says no reliable total-fraud estimate exists [24]. **[Established]** Claimed analytics savings should be discounted.

**Why it might work:** it sees what a per-document match cannot: slow drift, patterns across documents, padding below tolerance. It is also the only approach that yields a measured error rate.

**What would make it fail.** The main barrier is precision. The SEC says that "if the amount of potential misstatement that could exist before being detected by the monitoring control is too high, then the control may not adequately address the financial reporting risks" [3], and PCAOB material says a compensating control must operate at a level of precision that would prevent or detect a misstatement that could be material [4]. That is likely passable for financial statement risk, because AP noise is small against materiality. **[Supported hypothesis]** However, the books-and-records and safeguarding duties in Section 13(b)(2) use reasonableness language, not the same materiality framing [2], and cash leakage below materiality still matters to the business. Other failure modes:

- Aggregate tests have low power for one-off events. A single fictitious invoice does not move a control chart.
- False alarms exhaust investigators.
- Monitoring finds problems after the money is gone, so it needs A's recovery mechanism.

**Constraints unchanged:** all, plus Section 404 evidence. Detective controls must themselves be testable, with documented thresholds and follow-up.

**New risks:** model drift, opaque thresholds an auditor cannot reperform, adversaries who learn the thresholds, and management override of alarms.

**Change level:** 2 as usually deployed, as an addition alongside the match. Level 3 only if it actually replaces the gate, and I found no public-company example of that. **[Could not verify any]**

### Approach E: verify the economic event (change what is verified)

**Organizing principle:** check physical or economic reality, not paper.

**Assumption rejected:** agreement among records is good evidence of value received.

**Mechanism.** Reconcile quantities in aggregate against independent physical facts: mass balance (material in equals product out plus scrap plus stock change), metered flow, production counts, carrier-independent weigh tickets, site telemetry, time-on-site for services. Payment is released or adjusted by the physical reconciliation, not a document chain.

**Evidence:** Olken measured missing funds by having engineers independently estimate the materials actually in the roads and comparing that with reported spending [20]. Paper agreed, reality did not, and only physical measurement exposed the roughly 24% gap. **[Established]** Power settlement works on metered data [9]. Pomeranz found paper trails deter by themselves and also that audit effects spill up the chain [38], so paper has real value and E should not be read as "paper is useless." **[Established]**

**Why it might work:** it is the only approach that tests need 2 directly, and it is hard for one person to fake across independent sensors. It covers services and bulk materials, where a goods receipt is often a formality.

**What would make it fail:** sensor cost; no natural balance for indirect spend; attribution (the balance is short, but which supplier?); a measured quantity does not establish quality or price. Physical evidence does nothing for needs 3 and 4 by itself.

**Constraints unchanged:** price, authority, tax, vendor master, GAAP cutoff (and measurement periods must align with close).

**New risks:** IT and OT security of measurement devices, tampering, and dispute over calibration.

**Change level:** 3 where physical reconciliation replaces the receipt and match. A scanner or RFID gate that auto-posts a goods receipt is level 1 and should not be described as this approach.

### Approach F: settle the balance, not the transaction

**Organizing principle:** change the unit of account from invoice to period balance.

**Assumption rejected:** payment must correspond to individual transactions.

**Mechanism.** The buyer pays a scheduled amount based on forecast or prior period, and the two parties true up on a period total, with the true-up reconciled once against contract and aggregate evidence. Individual invoices stop being payment triggers.

**Precedents:** Medicare periodic interim payments, biweekly estimated amounts with final settlement against the cost report [39]. CBP Reconciliation, entry on estimates with a later final value [34]. Joint interest cash calls and audit [15]. Estimated income tax. PJM's month-to-date netted statements [9]. **[Established]**

**Why it might work:** one reconciliation replaces many, supplier cash flow is steady, and the error budget is measured on a total, so small errors offset and stop costing anything.

**What would make it fail:** the CBP finding applies directly: unsubstantiated final values put revenue at risk [34]. A true-up is only as good as what backs it. Large forecast error creates overpaid balances that are unsecured credit to the supplier. Offsetting errors can conceal real overbilling inside an aggregate. It fits steady, high-frequency relationships only (utilities, logistics, MRO, contract labor).

**Constraints unchanged:** accrual accuracy gets harder, not easier. Monthly close needs an estimate of the balance. Prepaid and payable classification must be right, and any supplier-side revenue recognition should line up. Tax timing needs checking. Cash forecasts change, which affects DPO.

**New risks:** credit exposure, bankruptcy of a supplier holding a positive balance, and pressure to settle true-ups by negotiation.

**Change level:** 3 in the covered spend. Consolidated invoicing alone is level 1.

## 5. Where AI helps, and where it does not

"AI not needed" is the correct answer more often than vendors suggest. Evidence on AI here is thin: I found no peer-reviewed benchmark for LLM invoice work, only preprints, one of which reports up to 92% accuracy on legal invoice approval decisions against a 72% ceiling for experienced lawyers [40]. Treat those as unverified.

| Approach | Reasoning | Prediction | Classification | Retrieval | Information integration | Plain deterministic computing |
|---|---|---|---|---|---|---|
| A audit-and-recover | Drafting a dispute case from evidence; a person decides | Risk score for the targeted half of the sample | Sorting mismatches by likely cause | Pulling contract clause and history for a sampled item | Assembling the audit file | **Core:** random draw, extrapolation, netting. Random selection should stay non-AI so it cannot be learned |
| B buyer-computed | Rarely needed | Not needed | Not needed | Contract terms to price file, with human sign-off. Likely the top AI use here | Integrating carrier, receipt and contract data | **Core:** quantity times price, tax rules. AI in the payment calculation is a liability |
| C trusted supplier | Reviewing contract deviations | Default and defection risk | Tiering help; rules should decide status | Finding clauses, certificates, sanctions and credit data | Supplier 360 file | Score formula and revocation should be fixed, reperformable rules |
| D monitoring | Explaining an alarm, proposing a hypothesis | **Core:** anomaly and drift models. Classic statistics first | Alarm triage | Case lookup | Joining ledger, vendor, HR and commodity data | Duplicate checks, control charts, Benford-type tests |
| E event evidence | Explaining a balance gap | Expected yield and scrap | Reading images of delivery or site | Linking tickets to orders | **Core:** fusing sensor, carrier and ledger data | Mass balance arithmetic |
| F balance settlement | Rarely needed | Forecasting the scheduled payment. Standard forecasting usually suffices | Not needed | Not needed | Period evidence package | **Core:** true-up arithmetic |

**Possible today, with human review:** reading unstructured contracts and invoices, classifying mismatch causes, gathering evidence, drafting dispute letters, statistical anomaly scoring. **[Supported hypothesis; preprint and practitioner evidence only]**

**Would need more capable or more reliably proven models:** an unattended decision to claw back or deny; judging whether an unusual charge is legitimate in context, since statistical detection flags oddity not legitimacy [40]; reliably explaining reasons in a form an auditor can reperform; holding up against adversaries who actively test the model. CMS's rule that a claim cannot be denied on analytics alone [24] is a useful default. **[Speculative on timing]**

**A caution from the same technology:** generative tools also lower the cost of convincing fake invoices and emails. Controls that depend on a document looking right get weaker, which favors approaches B and E. **[Speculative]**

## 6. Ranking

Ranked by expected advantage over the simple improvement across the spend each can cover, discounted by evidence.

1. **B, buyer-computed settlement.** Best proven, removes the error class, no statistical argument needed with the auditor. Limited to repeat, price-stable, well-received spend, and it moves the risk to receiving.
2. **A, audit-and-recover.** Widest coverage and best rigorous evidence for the mechanism, but no AP-specific evidence and real recovery limits.
3. **E, event evidence.** Strongest truth, narrow and capital-heavy. Best for bulk materials, energy and field services.
4. **D, population monitoring.** Essential companion, weak as a stand-alone replacement because of precision and rare-event blindness.
5. **F, balance settlement.** Elegant for a small slice of steady relationships. Credit exposure limits it.
6. **C, contract and status.** Necessary enabling layer for A and possibly F. Does nothing alone.

A, C and D are not rivals in practice: A needs C's contract terms and D's detection. They remain different principles (deterrence, risk allocation, process control), and each can be judged separately. A likely end state is a portfolio by spend type rather than a single winner. **[Supported hypothesis]**

**Most deserves testing: Approach A.** B ranks higher but testing it would teach little: the unknown is local data quality, not the idea. A has the widest coverage, the largest unresolved question and a sharp contest with the simple improvement. The evidence behind it comes from settings different from AP, so it could fail in an instructive way. It can be meaningfully simulated, because its value depends on strategic behavior that a static cost model cannot show.

### Claims a small synthetic simulation can check

The simulation needs supplier types (honest but careless, opportunist, fraudster, sleeper), a receipt error process, a recovery process with supplier failure, and costs for machine check, human review and delay. **Every rate should be swept as a parameter, not assumed**, because I found no authoritative base rates for mismatch, overbilling or recovery in commercial AP. Outputs: net leakage, control cost, days to pay, maximum exposure, detection delay. All outputs must be labeled synthetic.

1. **Tolerance leakage.** With opportunist suppliers, a public tolerance leaks about tolerance times invoices, while random audit with extrapolation drives padding to about zero once q(1+m) ≥ 1, with q the chance of detection per supplier-period. Fails if: suppliers do not adapt, or the leak is too small to pay for the program.
2. **Where the money is.** With automated matching, sampling the comparison saves about nothing, and sampling the human investigation saves most of what is available. Fails if: machine comparison has a material per-item cost.
3. **ERS and receipt quality.** There is a receipt error rate above which ERS loses to the match, because the independent second record has gone, and overpayment errors are not reported by suppliers. Find the crossover and how sensitive it is to correlated errors.
4. **Rare events.** A fixed sample of about n = 20 per supplier-period catches systematic padding at high rates but rare single events at about 2%, so a value cap is required. Find the cap that bounds worst-case loss at acceptable review load.
5. **Recovery break-even.** A beats the simple improvement only above some recovery rate and repeat-purchase rate. Find the frontier, and show which supplier segments must stay gated. Include failure clustering around supplier bankruptcy.
6. **Timing is minor.** Sample-then-pay within terms matches pay-then-sample on leakage, at better recovery, unless early payment has explicit value.
7. **Honest world.** With no strategic suppliers, the simple improvement matches or beats A on total cost. If so, A's whole case rests on how much strategic behavior exists, and a real-world estimate of that becomes the next research task. This claim is included to make the test able to reject A.
8. **Sleeper exposure.** A supplier that builds a good record and then defects extracts a bounded amount set by caps and sample frequency. Find the worst case.
9. **Monitoring latency.** A drift test finds slow padding faster than an annual recovery audit, but not rare single events. Measure the amount at risk before detection, since that is what the SEC precision language turns on.

A simulation can show internal logic and sensitivities. It cannot show that a real auditor would accept the design, that suppliers would sign, or what actual base rates are.

## 7. What could not be verified

- No authoritative split of AP cost between comparison and exception handling, and no authoritative commercial base rates for mismatch, overbilling or recovery.
- Full text of AS 2201 (site returned 403): I relied on excerpts and older PCAOB text. Hammer's full text was not readable, only excerpts. The IATA Revenue Accounting Manual is paid.
- Full text of Kogan et al., Shi, Kleven et al., Olken and Mookherjee and Png: I used abstracts and summaries.
- No peer-reviewed ERS outcome study, no independent SBT shrink study, no independent verification of the Walmart Canada figures.
- No public-company example of a three-way match replaced by detective or sampling controls with auditor acceptance. Absence from my search is not proof of absence.
- Insurance claims handling was only covered through theory [41]. I found no good source on real straight-through thresholds, so it is not used as a precedent.
- US GAAP treatment of claimed overpayments, including credit-loss treatment, and 1099 implications were not source-checked here and need review.
- Legal readings of UCC and bankruptcy provisions are mine, and a lawyer should confirm them.

## Sources

Primary and authoritative unless labeled.

1. FAR Subpart 13.4, Fast Payment Procedure. https://www.acquisition.gov/far/subpart-13.4
2. 15 U.S.C. §78m(b)(2), (b)(7). https://www.law.cornell.edu/uscode/text/15/78m
3. SEC Release 33-8810, Commission Guidance Regarding Management's Report on ICFR (2007). https://www.sec.gov/rules/interp/2007/33-8810.pdf
4. PCAOB AS 2201 (excerpts only). https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 ; archived AS 2 Appendix C on safeguarding. https://pcaobus.org/oversight/standards/archived-standards/details/auditing-standard-no-2_1808 ; inspection report quoting AS 2201.68. https://pcaobus.org/Inspections/Reports/Documents/104-2020-002-Moss-Adams-LLP.pdf
5. Hammer, M., "Reengineering Work: Don't Automate, Obliterate," Harvard Business Review, July-August 1990 (excerpts). https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate
6. ERS: Accounting Information Systems textbook on risks and controls. https://www.oreilly.com/library/view/accounting-information-systems/9781118162309/c09-33.html ; NC State SCM article. https://scm.ncsu.edu/scm-articles/article/what-is-evaluated-receipt-settlement ; Peeriosity 2015 poll (practitioner, weak). https://www.peeriosity.com/shared-services/articles/2015/02/resolving-evaluated-receipt-settlement-price-discrepancies/
7. Walmart Canada / DLT Labs case study (interested party, weak). https://www.lfdecentralizedtrust.org/case-studies/dltlabs-case-study ; University of Arkansas summary. https://talkbusiness.net/2021/04/ua-blockchain-case-study-shows-technology-benefits/
8. Scan-based trading (vendor and encyclopedic, weak). https://en.wikipedia.org/wiki/Scan-based_trading ; https://www.truecommerce.com/blog/scan-based-trading-basics-why-who-and-how/
9. PJM Manual 29, Billing. https://www.pjm.com/-/media/documents/manuals/m29.ashx ; https://pjm.com/markets-and-operations/billing-settlements-and-credit.aspx
10. Kleven, Knudsen, Kreiner, Pedersen, Saez, "Unwilling or Unable to Cheat?" Econometrica 79(3), 2011. https://www.nber.org/papers/w15769
11. Brazil NF-e (ERP and vendor documentation, weak). https://learn.microsoft.com/ar-sa/dynamicsax-2012/appuser-itpro/bra-about-the-nf-e-process ; https://invoicedataextraction.com/blog/brazil-nf-e-nota-fiscal-eletronica-guide
12. PwC Viewpoint on ASC 606 consignment (secondary). https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/revenue_from_contrac/revenue_from_contrac_US/chapter_8_practical__US/86consignment_arrang_US.html ; UCC §9-102. https://www.law.cornell.edu/ucc/9/9-102
13. FBI IC3, 2025 Internet Crime Report. https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf
14. FAR inflation adjustment, 90 FR 41872, Aug. 27, 2025. https://www.federalregister.gov/documents/2025/08/27/2025-16412/federal-acquisition-regulation-inflation-adjustment-of-acquisition-related-thresholds
15. COPAS materials and form excerpts. https://copas.org/wp-content/uploads/COPAS-National-Fall-2025-EI-Discussion-Topics.pdf ; https://lawinsider.com/clause/audits-by-non-operators ; Squire Patton Boggs alert. https://www.squirepattonboggs.com/en/insights/publications/2008/12/oil-and-gas-alert-copas-audits-and-ag19
16. IATA Revenue Accounting Manual listing. https://www.iata.org/en/publications/manuals/revenue-accounting-manual/ ; SIS Rejection Memo annual report 2017, Sampling Billing Analysis. https://www.iata.org/contentassets/3c9d2e2266c74c77be3301f32aa0997e/sis-rm-rm-annual-report-2017.pdf ; US Patent 8,190,456 (description of sampling). https://patents.google.com/patent/US8190456
17. Townsend, R., "Optimal Contracts and Competitive Markets with Costly State Verification," Journal of Economic Theory 21(2), 1979. https://econpapers.repec.org/RePEc:eee:jetheo:v:21:y:1979:i:2:p:265-293
18. 42 U.S.C. §1395ddd(f)(3) as quoted by the Fifth Circuit. https://www.ca5.uscourts.gov/Opinions/pub/16/16-50398-CV0.pdf ; CMS Program Integrity Manual ch. 8. https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads//pim83c08.pdf
19. Shi, M., "Monitoring for Waste: Evidence from Medicare Audits," QJE 139(2), 2024. https://www.nber.org/papers/w31559
20. Olken, B., "Monitoring Corruption: Evidence from a Field Experiment in Indonesia," JPE 115(2), 2007. https://www.nber.org/papers/w11753
21. Mookherjee, D. and Png, I., "Optimal Auditing, Insurance, and Redistribution," QJE 104(2), 1989. https://www.gsb.stanford.edu/faculty-research/working-papers/optimal-auditing-insurance-redistribution
22. Deming kp rule: Deming, Out of the Crisis (MIT CAES, 1986; chapter not confirmed); explainer. https://spcforexcel.com/knowledge/basic-statistics/inspecting-supplier-material ; "The Deming Inspection Criterion." https://scilit.com/publications/640d2b14aebfc1ea24790905a453ab7e
23. 11 U.S.C. §547. https://www.law.cornell.edu/uscode/text/11/547 ; §553. https://www.law.cornell.edu/uscode/text/11/553
24. GAO-26-107799. https://files.gao.gov/reports/GAO-26-107799/index.html ; GAO-17-710. https://www.gao.gov/assets/gao-17-710.pdf ; Ways and Means letter. https://waysandmeans.house.gov/house-wm-ec-senate-finance-leaders-call-cms-prevent-fraudulent-medicare-spending/
25. CMS, Medicare and Medicaid Program Integrity Report to Congress FY2023. https://www.cms.gov/files/document/fy2023-medicare-and-medicaid-report-congress.pdf
26. UCC §2-512. https://www.law.cornell.edu/ucc/2/2-512 ; §2-607. https://www.law.cornell.edu/ucc/2/2-607 ; §2-717. https://www.law.cornell.edu/ucc/2/2-717 ; §2-725. https://www.law.cornell.edu/ucc/2/2-725
27. HMRC VAT Notice 700/62, Self-billing. https://www.gov.uk/guidance/self-billing-notice-70062
28. CBP Importer Self-Assessment bulletin. https://www.Cbp.Gov/bulletins/Vol_46_No_44_Title.pdf ; Federal Register notice, Oct. 5, 2012. https://www.govinfo.gov/content/pkg/FR-2012-10-05/html/2012-24592.htm
29. Texas Medical Association on HB 3459 gold card. https://www.texmed.org/GoldRush/ ; https://www.texmed.org/Template.aspx?id=60393
30. ISO 2859-3:2005 skip-lot procedures. https://standards.iteh.ai/catalog/standards/iso/27cbc4c8-fa4e-46d0-892a-82c9c1a146e3/iso-2859-3-2005
31. Visa VAMP summary (vendor, weak; Visa's own documents not checked). https://www.chargeflow.io/blog/what-are-visas-new-vamp-rules-a-2025-guide-for-merchants
32. Regulation Z, 12 CFR §1026.13. https://www.law.cornell.edu/cfr/text/12/1026.13
33. Duflo, Greenstone, Pande, Ryan, "Truth-telling by Third-party Auditors," QJE 128(4), 2013. https://dspace.mit.edu/handle/1721.1/81785
34. DHS OIG-20-79, CBP's Entry Reconciliation Program Puts Revenue at Risk. https://www.oversight.gov/sites/default/files/oig-reports/OIG-20-79-Sep20.pdf
35. Kogan, Alles, Vasarhelyi, Wu, "Design and Evaluation of a Continuous Data Level Auditing System," Auditing: A Journal of Practice & Theory 33(4), 2014. https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Design-and-Evaluation-of-a-Continuous/991031654460104646
36. PCAOB technology-assisted analysis amendments, 2024. https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-updates-its-standards-to-clarify-auditor-responsibilities-when-using-technology-assisted-analysis
37. ACFE, Report to the Nations. https://www.acfe.com/fraud-resources/report-to-the-nations ; 2024 edition. https://legacy.acfe.com/report-to-the-nations/2024/ ; 2026 press release. https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=occupational-fraud-2026-a-report-to-the-nations-pr
38. Pomeranz, D., "No Taxation without Information," AER 105(8), 2015. https://www.nber.org/papers/w19199
39. 42 CFR §413.64. https://www.law.cornell.edu/cfr/text/42/413.64 ; 42 CFR §412.116. https://www.law.cornell.edu/cfr/text/42/412.116
40. "Better Bill GPT" (preprint, not peer reviewed). https://arxiv.org/pdf/2504.02881 ; "Invoice Information Extraction" (preprint). https://arxiv.org/pdf/2510.15727
41. Crocker, K. and Morgan, J., "Is Honesty the Best Policy?" JPE 106(2), 1998. https://econpapers.repec.org/RePEc:ucp:jpolec:v:106:y:1998:i:2:p:355-375
