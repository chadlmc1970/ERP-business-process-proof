# 05 Adversarial review of lesser-of settlement

Research line 05. Date: 2026-11-04. Job: break PROPOSAL.md. Roles used in turn: skeptical researcher, operations executive, AP process owner, external auditor, supplier CFO, systems architect.

Tags: **[E]** Established. **[SH]** Supported hypothesis. **[SP]** Speculative. **[R]** Rejected. "Vendor" marks weak evidence. Legal and accounting readings are mine and need a lawyer, auditor or tax adviser where marked **[confirm]**. All simulation figures are synthetic, per 100,000 invoices, on illustrative parameters. They show how the argument behaves, not what would happen.

## 0. Verdict in brief

- **Not new. [E]** The exact rule is federal payment law, a University of California accounting rule, an SAP function, and everyday practice at Walmart, Target, Lowe's and Amazon. The novelty claim fails.
- **Rejected as a general redesign. [SH]** It trips four of the nine rejection conditions outright or in the main: already standard, no better than the straightforward optimization, benefits vanish once costs are counted, and worse outcomes under common conditions on a joint basis. It trips two more conditionally: an unfilled control gap on liability completeness, and legal or relationship risk for dominant buyers.
- **What did hold up. [SH]** The arithmetic. A record error on one side alone cannot cause an overpayment, and L's leakage is the lowest of the policies tested while the two records are independent (step 2). It is not robust to shared records: a 25% PO flip and some noise lift it from $13,933 to $90,296, and it is no longer lowest. It is simple to explain and audit. On buyer cost alone it beats plain wide tolerance in 239 of 240 random worlds. So it is a good answer to a small question: what to do with a supplier overbill against a locked price.
- **The burden shift is the weak part. [SH]** The same payment rule with the buyer working the difference (policy U) beat L on joint cost in all 240 worlds. In the moderate step, L saves the buyer $9,650 against the fair rival and costs suppliers $132,701 more, about $13.75 of supplier cost per buyer dollar. That is a transfer, not an efficiency.
- **Survives only as:** an exception action inside the conventional match, for supplier overbills against locked contract prices, with the buyer owning errors in its own records. See section 5.

## 1. Novelty

### 1.1 The rule already exists, word for word

| Field | Source | What it does | Tag |
|---|---|---|---|
| Medicare | [42 CFR 414.21](https://www.law.cornell.edu/cfr/text/42/414.21): "Medicare payment is based on the lesser of the actual charge or the applicable fee schedule amount." | Exactly min(I, E). Also throughout [42 USC 1395l(a)(1)](https://www.law.cornell.edu/uscode/text/42/1395l), for example "80 percent of the lesser of the actual charge for the services or the amount provided under the fee schedule". | E |
| Commercial health contracts | [HFMA example](https://www.hfma.org/payment-reimbursement-and-managed-care/contracting/62082/): $4,500 charge against a $4,800 contract rate, the plan pays $4,500. [ECG](https://www.ecgmc.com/insights/blog/the-lesser-of-trap-how-a-hidden-contract-clause-is-reducing-your-hospitals-revenue) (consultant, weak) calls the clause common. | Lesser-of billed or contract. | E for existence, weak for prevalence |
| University AP policy | [UC Accounting Manual D-371-36](https://financial.ucsc.edu/SiteAssets/Lists/Guide%20Nav%20Animal%20Life/UC%20D-371-36_TL102.pdf), TL 102, 9/30/11: "The lower of the amount charged by the vendor or the purchase authorization amount should be paid if the unit price is incorrect." | The proposal's price rule in one sentence, inside a two-way match. Quantity differences of 20% or more, and other discrepancies, still go to a person. | E |
| ERP | [SAP invoice reduction](https://help.sap.com/saphelp_sfin100/helpdata/en/f3/70b6531de6b64ce10000000a174cb4/content.htm): "This function automatically generates a credit memo when an invoice is posted"; "The vendor receives a letter of complaint detailing why the invoice was reduced." [SAP Learning](https://learning.sap.com/courses/invoice-verification-in-sap-s-4hana/reducing-invoices-1) describes two documents, invoice values and a credit memo for the gap. | Steps 2 and 3 of the proposal. SAP limits the total-based variant to a configured reduction tolerance, so its designers kept a bound. | E (product documentation, mechanics only) |
| Procurement network | [SAP Ariba FAQ](https://support.ariba.com/item/view/157914): "Exceptions trigger customer-specific actions such as PO adjustment, short payment, or rejection." | Short pay as a listed exception outcome. | E |
| Mass retail | Walmart Code 11: generated "if the invoice is higher than the cost on the PO", and "the difference will be removed from the check", disputes through the Accounts Payable Disputes Portal ([SPS Commerce](https://www.spscommerce.com/community/articles/code-11-pricing-overcharge-price-difference-between-po-and-invoice), Vendor). Target and Lowe's cost-difference deductions appeared in search summaries only ([cost difference](https://help.supplypike.com/en/articles/10104930-cost-difference), Vendor). | min(I, PO cost), running claims, supplier burden. | SH: consistent vendor sources, no retailer document read |
| Marketplace retail | Amazon shortage claims: deducted when fewer units are booked than invoiced, the vendor "can only prove that the delivery was correct with evidence", disputes batched, up to ten cases in a re-dispute ([Amalytix](https://www.amalytix.com/en/knowledge/logistics/shortage-claims/), Vendor). Two-year limit for both shortage and price disputes ([SPS](https://www.spscommerce.com/community/articles/updated-dispute-timeline-for-1p-amazon-suppliers), Vendor). | The closest whole-system match: pay on receipt and PO cost, supplier claims with evidence, batched, time-limited. | SH: vendor sources only |
| Freight | Shippers pay the undisputed amount, deduct the disputed amount, and give a reason code on the remittance ([search summary of practitioner sources](https://nexasphere.io/blog/short-paid-on-a-freight-invoice-here-is-how-to-dispute-it-with), Vendor). [49 USC 13710(a)(3)](https://www.law.cornell.edu/uscode/text/49/13710) gives 180 days to contest a bill. [49 USC 14705](https://www.law.cornell.edu/uscode/text/49/14705) gives 18 months to sue. | Short-pay with a statutory claim clock. | E for statute, SH for practice |
| Construction | [Tex. Prop. Code 28.003](https://texas.public.law/statutes/tex._prop._code_section_28.003): in a good faith dispute the obligor "may withhold ... not more than 100 percent of the difference" (110% residential). [Cal. Civ. Code 8800](https://codes.findlaw.com/ca/civil-code/civ-sect-8800/): up to 150% of the disputed amount, with a penalty of 2% per month on amounts wrongfully withheld. | Pay the undisputed part. Note the buyer-side penalty, which the proposal lacks. | E |
| Telecom wholesale | Interconnection clauses: pay undisputed amounts, disputed amounts into escrow ([Law Insider samples](https://lawinsider.com/clause/billing-disputes)); search summaries of Missouri commission dockets show escrow being contested. | Undisputed-amount rule, with neutral custody of the rest. | SH: sample clauses, not surveyed |
| Federal contracts | [31 USC 3907(c)](https://www.law.cornell.edu/uscode/text/31/3907): no interest penalty "on a payment that is not made because of a dispute". [FAR 52.232-25](https://www.law.cornell.edu/cfr/text/48/52.232-25) and [5 CFR 1315.10(c)](https://www.law.cornell.edu/cfr/text/5/1315.10) say the same, and cover "amounts temporarily withheld or retained in accordance with the terms of the contract". | Disputed amounts sit outside the prompt payment clock and go to the Disputes clause. The default for a defective invoice is to return it within 7 days ([5 CFR 1315.4](https://www.law.cornell.edu/cfr/text/5/1315.4)), not to pay part. I found no federal rule requiring or forbidding payment of the undisputed part. | E |

### 1.2 What the track record shows

Healthcare is the best natural experiment on "the claimant carries the burden", though the setting differs.

- **[E]** Medicare Advantage 2014-16: "beneficiaries and providers appealed only 1 percent of denials", plans "overturned 75 percent of their own denials", and "CMS cited 56 percent of audited contracts for making inappropriate denials" ([HHS OIG OEI-09-16-00410](https://oig.hhs.gov/reports/all/2018/medicare-advantage-appeal-outcomes-and-audit-findings-raise-concerns-about-service-and-payment-denials/)). These are service and payment denials, not lesser-of pricing. Later KFF work reported about 10% to 12% of prior authorization denials appealed and over 80% overturned (secondary summaries only, [LeadingAge](https://leadingage.org/new-kff-report-more-ma-prior-authorizations-appeals-remain-successful/)).
- **[SH]** Reading: when the party with the shortfall must act, few act, and of those who do most win. That is the signature of a rule that keeps money by default rather than by being right. It directly undercuts "the supplier is motivated to report". Motivation is conditional on claim value exceeding claim cost.
- **[SH]** A stale record hurts whoever holds it. Hospitals lose under lesser-of when chargemasters go stale against contract rates ([ECG](https://www.ecgmc.com/insights/blog/the-lesser-of-trap-how-a-hidden-contract-clause-is-reducing-your-hospitals-revenue), consultant, one unverified client figure of $26 million a year). In the proposal the party with a stale record is the buyer, but the party who loses is the supplier. That separation removes the feedback that healthcare at least keeps.

Retail deductions and groceries give the abuse record.

- **[E]** UK Groceries Code Adjudicator, [Tesco report, January 2016](https://assets.publishing.service.gov.uk/media/5a81a094ed915d74e33ff39b/GCA_Tesco_plc_final_report_26012016_-_version_for_download.pdf). This is the most useful single document found.
  - "Even in circumstances where a debt had been acknowledged by Tesco, on occasions the money was not repaid until over 12 months later with some amounts taking up to 24 months".
  - Para 7.6: "I consider any unilateral deduction to be a delay in payment." Implicit agreement can arise from 30 days' notice.
  - Data errors: Tesco "failed to rectify data input errors within a reasonable time". An incorrect price "continued to form the basis" of charges, "compounding the original error".
  - Short delivery: "with Tesco and the supplier having different numbers in their records", and suppliers "were required to produce evidence to rebut an incorrect claim" (27.1). One case took six months to repay (27.4).
  - Motive: margin targets. "Buyers frequently sought to use money owed to a supplier as leverage in negotiations".
  - Para 39.1: margin was hit "where suppliers abandoned a claim for repayment or negotiated a settlement".
  - The trigger was a £250 million profit overstatement, "a considerable proportion" of it "associated with the supply of groceries".
  - Recommendation 2: "Tesco must not make unilateral deductions." Recommendation 3: "Data input errors identified by suppliers must be resolved promptly."
- **[E]** Same report: most regular undisputed invoices were paid on terms. The harm sat exactly in the disputed residual, which is the proposal's running account.
- **[E]** Australia, [Food and Grocery Code 2024](https://legislation.gov.au/F2024L01651/asmade/2024-12-16/text/original/pdf), s 22(2): a large grocery business must not "set off any amount against a supplier's invoice or remittance unless the supplier has consented in writing". Under s 22(3)-(5) the exception needs a contract provision and a reasonable set-off, and the retailer carries the proof. Section 23 bars shrinkage payments. Civil penalty 600 penalty units.
- **[E]** SEC, [Rite Aid, 34-46099](https://www.sec.gov/litigation/admin/34-46099.htm): inflated income by "reducing its Vendor Accounts Payable and Cost of Goods Sold for unearned vendor credits"; up-charges on damaged goods deducted from vendors, where "The vendors did not agree to or know about the up-charge" (about $8 million FY1998, $28 million FY1999). This is a US public company precedent for vendor deductions as an earnings lever.
- **[SH, weak]** Size: Attaining Consulting and Credit Research Foundation 2018 survey, mainly vendors, non-trade deductions at a median 0.5% to 1% of receivables below $500 million revenue and 1.1% to 3% above; 48% set no time limit on write-offs ([SC Digest](http://www.scdigest.com/NEWSVIEWS/18-05-29-1.PHP?cid=14268&ctype=content), sample size not given). SPS Commerce says only 20% to 30% of deductions are disputed and 40% of those are won ([Vendor](https://www.spscommerce.com/community/articles/the-impact-of-retailer-deductions), no source named). Peer-reviewed measurement of deductions: not found.
- **[SH]** Pass-through: Murfin and Njoroge (RFS 2015) find slower payment by large retailers is linked to lower supplier investment, and a Yale summary reports higher supplier markups as payable days grow ([Yale](https://insights.som.yale.edu/insights/big-box-retailers-squeeze-smaller-suppliers-by-borrowing-from-them), secondary, paper not read). That is about terms, not deductions.

### 1.3 What is left

- **[R]** "Pay the lesser, supplier claims the rest" as a new idea.
- **[R]** "The assumption that a mismatch must be resolved before payment is unnecessary for amount" as a discovery. It is true, and it has been the working practice of Medicare, big-box retail and SAP's invoice reduction for years.
- **[SH]** Possibly unclaimed, and only in composition: using it as the default for a non-retail US public company's whole PO-backed spend, with tolerances removed, and treating it as a control with a stated ICFR argument. I found no such published design. That is absence from a search that ran out of budget, not proof.
- **[SH]** The useful contribution left is evidence: measured claim rates, abandonment, and buyer-fault share under a real short-pay rule. No public data found.

## 2. Legal and accounting

### 2.1 Contract law (US, UCC model text; state enactments vary) [confirm all]

- **Is paying less a breach?** [UCC 2-607(1)](https://www.law.cornell.edu/ucc/2/2-607): "The buyer must pay at the contract rate for any goods accepted." The debt follows contract rate and acceptance, not the invoice. So: **[SH]**
  - Invoice above contract, E correct: paying E is full performance. An invoice above contract is an offer to modify, not a debt. No breach, no deduction needed.
  - E wrong, for example a stale price or an undercounted receipt: payment falls short of the contract rate on accepted goods. That is a failure to pay, whatever the running account says. The rule is then a systematic, known source of partial non-payment on the 71% of short-pays that the proposer's own parameters attribute to buyer records (section 4.5).
- **Burden.** 2-607(4): "The burden is on the buyer to establish any breach with respect to the goods accepted." The proposal inverts this default. For a short-receipt dispute the seller suing for the price likely has to show delivery anyway, so the inversion bites mostly on price and quality deductions. The inversion needs to be written into the contract, not just into AP procedure. **[SH]**
- **[2-717](https://www.law.cornell.edu/ucc/2/2-717)**: deduction of damages needs notice and is limited to "any part of the price still due under the same contract". Fine for per-invoice min(). Not enough for netting audit recoveries or rejected claims across POs on a running account. A set-off clause is needed.
- **[2-209](https://www.law.cornell.edu/ucc/2/2-209)**: a modification "needs no consideration to be binding". So an agreed price change by email can bind the buyer while the PO record stays stale. That is the stale-price case, and it is why E is not the contract. A signed no-oral-modification clause helps, but 2-209(4) lets failed modifications work as waivers. 2-209 comments impose good faith on modifications (comment not read here).
- **[1-304](https://www.law.cornell.edu/ucc/1/1-304)** and **[1-201(b)(20)](https://www.law.cornell.edu/ucc/1/1-201)**: duty of good faith, meaning "honesty in fact and the observance of reasonable commercial standards of fair dealing". **[SH]** A buyer who knows a price record is stale and keeps short-paying has a problem here. A rule that removes every incentive to fix the record makes that state likely.
- **[2-309](https://www.law.cornell.edu/ucc/2/2-309)**: an unspecified time means a reasonable time, so claim review without an agreed time limit defaults to that standard. 2-309(2)-(3) lets either side end an indefinite relationship on reasonable notification. Supplier exit is a legal right, not a theoretical one.
- **[2-609](https://www.law.cornell.edu/ucc/2/2-609) and [2-612(3)](https://www.law.cornell.edu/ucc/2/2-612)**: repeated short-pays may give a seller reasonable grounds for insecurity, a demand for adequate assurance and suspension, and on instalment contracts a claim of breach of the whole. **[SP on application]**
- **Course of performance.** [1-303(f)](https://www.law.cornell.edu/ucc/1/1-303): conduct "is relevant to show a waiver or modification". Unprotested short-pays may build the buyer's case, so a careful supplier will protest each one under [1-308](https://www.law.cornell.edu/ucc/1/1-308). That adds supplier work per invoice, which simulate2 leaves out.
- **Accord and satisfaction.** [3-311](https://www.law.cornell.edu/ucc/3/3-311) needs a good faith tender of an instrument "as full satisfaction", a bona fide dispute, and a conspicuous statement. **[SH]** A remittance that says "claim the rest on your running account" is not a full-satisfaction tender, so accord should not arise. ACH likely is not an "instrument" at all, leaving common law accord. The risk runs the other way: if the buyer wants finality, it does not get it from this mechanism. 1-308(b) says reservation of rights does not defeat an accord, so any check with settlement language would be dangerous for the supplier. Keep such language off remittances.
- **Claim windows.** [2-725(1)](https://www.law.cornell.edu/ucc/2/2-725): four years, reducible by original agreement to not less than one, not extendable. A 90-day claim window would need to be drafted as a notice condition and could be attacked as an end run around that floor. Real windows for comparison: Medicare 120 days ([42 CFR 405.942](https://www.law.cornell.edu/cfr/text/42/405.942)), freight 180 days, Amazon two years (Vendor). **[confirm]**
- **Robinson-Patman.** [15 USC 13(a), (f)](https://www.law.cornell.edu/uscode/text/15/13). Section 2(a) targets a seller's price discrimination between purchasers. 2(f) reaches a buyer "knowingly to induce or receive" a prohibited discrimination. **[SP]** A uniformly applied rule does not obviously involve that. Unclaimed shortfalls could work as hidden discounts for a dominant buyer if competing buyers pay more, but that is a stretch. I did not read case law because the search budget ran out. Low priority, counsel to confirm.
- **Non-US.** UK GSCOP and the Australian code do not bind a US-only frame, but any covered grocery retailer or subsidiary would be caught. The proposal is unlawful by default for such a business in Australia without written consent. EU Directive 2019/633 could not be read.

### 2.2 US GAAP [confirm with auditor]

- **Derecognition.** ASC 405-20-40-1: a liability is derecognized only if the debtor pays the creditor or is legally released (read in secondary summaries, Codification not accessed). **[SH]** A shortfall that a supplier has not claimed is neither paid nor released. If the goods were accepted and T exceeds what was paid, the liability exists whether or not the claim arrives.
- **Which standard?** The likely view is that amounts owed for accepted goods at the contract rate are a liability, not a contingency. ASC 450-20 is the fallback for the truly disputed part: accrue when probable and reasonably estimable. The unasserted-claim step (ASC 450-20-50-6) is unlikely to help, because the invoice already asserted the amount. **[SH]**
- **Consequence.** SAP's credit-memo design removes the open item at posting. If a running account does the same and the shortfall is later paid, the first period's AP and inventory or COGS are understated. So L needs a period-end estimate of how much of the running account will be paid, based on claim history, plus an inventory or PPV entry when a claim lands. That is a new estimate with new judgment. In simulate2 it costs nothing.
- **Breakage.** Abandoned shortfalls can only go to income on legal release. Whether a contract claim window or time bar counts is not settled by anything I read. **[confirm]** Rite Aid and the Tesco overstatement show what this looks like when pressed. **[E for those cases]**
- **Size.** The balance would probably be small against materiality at a large company. In step 2, unclaimed shortfall is about $40,000 on about $540 million of spend. **[SP]** The concern is less quantitative than qualitative: a reserve that management sets, that releases to margin, and that a buyer can feed. SAB 99 style qualitative factors were not checked here.
- **Supplier side.** Under ASC 606 an expected short-pay may be variable consideration or an implicit price concession (from memory, not read). Suppliers would reserve for it, which supports pricing it in.

### 2.3 Unclaimed property [confirm]

- **[SH]** The running account may be the worst possible form. Delaware's 2010 S.B. 272 excluded "uninvoiced payables", including "out of balance transactions where the holder's purchase order for goods and the amount of goods received by the holder do not match". But those "specifically do not include accounts payable, accounts receivable, or any other type of credit or amount due to the creditor", and the law "shall not be construed to create" a B2B exemption ([Morris Nichols](https://www.morrisnichols.com/assets/htmldocuments/CorporateCounselWeeklyHoughtonMayrackUnclaimedPropertyDelawareMakesSignificantChanges.pdf), 2010; the statute was later rewritten and the current text was not checked). A per-supplier ledger of amounts shown as due looks more like the second category than the first.
- **[SH]** Bona fide disputed items generally are not treated as fixed obligations, but the source I saw is a vendor guide, not a statute ([example](https://invoicedataextraction.com/blog/unclaimed-property-accounts-payable), Vendor).
- **[E]** Delaware has reached B2B credits: a Kroll alert reports customer rebates held to be unclaimed property after five years ([Kroll](https://www.kroll.com/en/client-alerts/client-alert-delaware-court-rules-rebates-issued-by-staples-are-unclaimed-property)). Delaware also audited AP in [Temple-Inland v. Cook](https://www.skadden.com/insights/publications/2015/04/itempleinlandi-sheds-light-on-delawares-use-of-est), where estimation turned $147.30 of found property into a $2.1 million assessment, later held to violate due process (192 F. Supp. 3d 527, read through law firm summaries).
- **[SH]** State B2B exemptions are a patchwork, and RUUPA left them to each state ([UPPO](https://www.uppo.org/blogpost/925381/237086/Inside-the-B2B-exemption), dated).
- **Bind.** Saying "we owe this" helps the supplier and the auditor but feeds an escheat claim. Saying "we dispute it" protects against escheat but contradicts the accrual and the good faith story. The proposal has to pick a characterization per item. Nothing in it does.

### 2.4 Tax

- **Sales and use tax [confirm].** The invoice carries tax on I. If the buyer pays on E, the seller has remitted tax on an amount not collected and needs a credit memo or a bad debt route, and those rules vary. Examples: write-off required in [Oklahoma](https://regulations.justia.com/states/oklahoma/title-710/chapter-65/subchapter-11/section-710-65-11-2), proportional application of later payments in [Rhode Island](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18.1/44-18.1-21.HTM), and the Section 320 write-off question is argued in [a Washington filing](https://www.courts.wa.gov/content/petitions/96383-5%20Reply%20to%20answer%20to%20petition.pdf). A later claim payment reverses it. SAP asks whether tax goes "Only in the invoice document" or "In the invoice and credit memo documents". This is the same use tax trouble Peeriosity reported for ERS (see 04). **[SH]** min(I, E) must also be computed net of tax, or it compares a tax-inclusive number with a tax-exclusive one. The proposal is silent.
- **1099. [R as a worry for in-scope spend.]** [26 CFR 1.6041-3(c)](https://www.law.cornell.edu/cfr/text/26/1.6041-3) excepts "Payments of bills for merchandise, telegrams, telephone, freight, storage, and similar charges." Goods are mostly out of reporting, services are out of the proposal's scope, and reporting follows payment. The threshold rose to $2,000 for 2026 payments under Pub. L. 119-21 s 70433 (secondary sources). It is a minor system matter: a claim paid next year is reported next year.

### 2.5 SOX and AS 2201 [confirm with auditor]

- **[E]** AS 2201 has no preference for prevention or for any named control. Testing depends on whether controls address risk "rather than on how the control is labeled"; a compensating control needs precision to prevent or detect a material misstatement (.41, .68, as read in line 04). Automated controls get benchmarking (.B28-.B29, line 04).
- **[SH]** min() is an easy automated control to test, arguably easier than a tolerance match. There is no tolerance parameter to review. That is a real point in its favor.
- **[SH]** But it controls only one assertion: payment does not exceed either record. It does nothing for completeness of liabilities, and it creates a gap there. Under a gate, unresolved items sit visibly in blocked AP and GR/IR. Under L, the difference needs the new estimate in 2.2.
- **Does the auditor need a separate control over E? Yes. [SH]**
  - Under L, E is the ceiling on payment and is partly the sole record, because I no longer forces review of E. Price master maintenance, PO change authority and receiving become the key controls.
  - [AS 1105.10](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105) requires testing the accuracy and completeness of company-produced information, or the controls over it, including ITGCs.
  - The disagreement signal is lost for E too high: if E is above I the system pays I and nobody looks, so an inflated receipt can overstate inventory and GR/IR with no exception. The gate with two-sided tolerance would flag it. Line 02's point that the match's job includes liabilities and that early auditors used receipts to find unrecorded liabilities (01, Montgomery 1912) applies here.
- **[SH]** Step 6, random audit, is then a key compensating control and must be precise, documented, and followed through. Step 6 is the largest cost the simulation left out (section 3.2).
- **[SP]** An automated control that also feeds a management estimate invites more scrutiny, because AS 2501 is then in play (standard page blocked, not read).

## 3. Attacking the simulation

Script: `tests/attack_lesser_of.py`. Run: `cd tests; python3 -I attack_lesser_of.py`. Output: `attack-output.txt` and `attack-results.json` in the research folder. simulate2.py was not edited. With attacks off, this engine reproduces simulate2's joint totals within +1.0% to +4.8%. It always comes in higher, and the difference is RNG and heavy-tail noise that I did not fully trace.

### 3.1 Bugs and biases in simulate2.py (none fixed in that file)

Favoring L:

1. **Step 6 is missing. The biggest item.** The proposal's random audit of receipts and claims costs nothing in L. A was charged for its audit. Adding 0.5 looks per supplier-period raises L's buyer cost about $75,000.
2. **A is not a sampling design.** `audit_n=4` against about 2 mismatches per supplier-period means A looks at nearly every one: 10,686 human looks, more than the gate's 8,234. Cutting to `audit_n=1` gives 5,711 looks and joint $495,197, against $559,992. The rival was a strawman.
3. **A gives suppliers no way to fix underbilling.** That leaves $79,395 of "supplier unpaid", counted against A, while L's suppliers can claim it. A+ with debit memos drops this to under $10,000.
4. **Batching went to L alone.** L gets 10% looks per extra line. T and G pay a full touch per stop. The proposal already notes that batching drives much of the benefit, and nothing stops a gate from batching.
5. **T is not the simple improvement.** Line 03 defined it as tolerances plus PO discipline and fixing root causes. simulate2 widens the tolerance only.
6. **Every stop runs 10 days late.** In the one real log available, block duration is median 6.2 days and 75th percentile 24.9 (01, section 5.7), and invoice to clearing is about 30 to 44 days. Most blocks plausibly clear inside terms. Line 03 said this too.
7. **All true claims are paid, instantly.** The gate gets 97% accuracy, L 100%. No lag, no carrying cost on the shortfall, `sup_delay_cost` is zero.
8. **A 10% look beats a full look.** `claim_reject=0.98` at `review_line_share=0.1` beats `resolve_accuracy=0.97` at a full touch.
9. **`both_high` always sets E = I.** The case that check_properties P4 flags (both high, different, gate catches, L does not) has frequency zero in the simulation. L's one known weakness against a gate was left out.
10. **Records are independent.** Only 2.4% of E-too-high cases have I too high as well (0.0005 / 0.0205). Invoices flipped from POs, and PO flip is routine, make this far higher. See 4.2.
11. **Supplier cost of a short-pay is zero** unless a claim is filed. Honest overbills (`sup_over`) short-paid under L cost the supplier nothing, though they leave a residual in its receivables. Under the gate the same invoice gets a stop charge.
12. **Late receipts do not count as stops** for any policy, so L reports 0 stops. They hold the whole invoice. My engine shows 996 stops at the defaults.
13. **No learning.** Errors are independent draws, so a gate's fix to a record does nothing. The gate's main long-run benefit, that a stop forces the record to be fixed, cannot appear.
14. **No running account cost:** accrual, ageing, escheat, inquiries, statements.
15. **Transfers counted as costs.** `overpaid`, `sup_short` and `lost_discount` are not resources burned. They are 60% of R's "joint cost", 24% of A's and 11% of L's. Delay cost also ignores the buyer's float gain. The sign of this error depends on the policy, but it inflates R and A most.
16. **No common random numbers.** Policies consume the RNG differently, so each sees different invoices. Plain T's joint varies from $455,661 to $517,308 over 10 seeds (sd $17,969). The grid uses one seed. "Cheapest in every cell" compares noisy draws.
17. **Padders do not adapt.** Under L an opportunist still pads clean invoices 4%, which is pointless, and never bills up to a high E, which pays. False lines go in a separate claim, while a real padder would hide them in a true batch.

Favoring the rivals, for balance:

18. **Late-receipt chase is charged to L and A, not to G or T.** Small.
19. **No rounding, freight or tax noise.** Under a gate those small overbills get paid. Under L they do not. With no reconciliation cost, noise helps L (see 3.3).
20. **Gate stops resolve with no labor to fix the record**, and A's stopped items pay T with perfect accuracy.

check_properties.py:

21. P2 is a tautology. min(E, I) > T if and only if both exceed T. It proves nothing about business outcomes, and the file says so.
22. P4's 26.5% is a share of a grid, not a frequency.
23. The comment "every shortfall is visible to the party it hurts" is not what the assert shows. It only shows shortfalls need a low record. If I < T, then pay equals I, the remittance matches the invoice, and nothing on the remittance flags it. P5's conclusion is unproven.

### 3.2 Ladder

I changed my own first version before trusting it. It gave L twice A+'s audit budget, gave T+ suppliers no way to correct underbilling, and judged on "deadweight". The deadweight measure is invalid alone: a policy that pays every invoice unchecked (N in the script) scores best on it, with $85,959 deadweight and $363,351 overpaid. Those first results said L lost everywhere, 0 of 240. They overstated the case and are discarded. The table below gives both sides the same look budget.

Measures: buyer cost; buyer plus half of supplier cost (half passed back in price); full joint, which equals complete pass-through.

Policies: **T** simulate2's wide tolerance. **T+** that plus one-sided tolerance, batched exceptions, record fixes, and supplier debit memos. **A+** audit that truly samples (25% of supplier-periods, 2 looks, $100 floor). **U** pay min(I, E) on time, buyer works the difference in a batch. **L** the proposal.

| Step | Measure | T | T+ | A+ | U | L |
|---|---|---|---|---|---|---|
| 0. Attacks off | Buyer | 274,728 | 195,763 | 244,290 | 151,661 | **107,687** |
| | Joint | 487,931 | 346,472 | 379,357 | **191,508** | 256,249 |
| 1. Bugs fixed: audit, claim accuracy, lag, late receipts as stops, both-high-and-different | Buyer | 279,795 | 204,517 | 249,262 | 235,228 | **189,757** |
| | Joint | 528,839 | 394,627 | 383,267 | **281,302** | 362,370 |
| 2. Plus 30% of stops run late | Buyer | 279,795 | 204,517 | 249,262 | 235,228 | **189,757** |
| | Half | 363,323 | 271,659 | 291,660 | **258,265** | 276,063 |
| | Joint | 446,852 | 338,802 | 334,059 | **281,302** | 362,370 |
| 3. Moderate friction: $10 reconciliation, 10% inquiries, 3% noise, some stale prices, 25% PO flip | Buyer | 374,052 | 300,501 | 346,191 | 329,759 | **290,851** |
| | Half | 462,459 | **376,945** | 397,624 | 405,465 | 433,645 |
| | Joint | 550,865 | 453,389 | **449,057** | 481,171 | 576,440 |
| 4. Harsh stress (see limits) | Buyer | 802,471 | 686,084 | **479,184** | 621,423 | 678,704 |
| | Joint | 1,192,589 | 1,084,412 | **755,338** | 1,434,516 | 2,832,982 |

Overpaid, step 2: L $13,933, U $13,439, G $25,838, T $39,944, T+ $44,559, A+ $149,506, R $347,304, N $363,351. **L's low leakage is real while the records are independent.** A+'s joint figure is flattered by letting overbills through. It rests on independence, though: at step 3, with a 25% PO flip, L overpays $90,296, more than A's $59,161, and at step 4 $258,682, more than A+'s $200,286. See 4.2.

Reading:

- **[SH]** "L cheapest in every cell" does not survive. U beats L on joint at every step, with no attacks at all. So the supplier-claim feature costs more than it saves on a joint basis, because a claim needs both parties to touch it. Moving the work does not remove it.
- **[SH]** Bugs alone take L's joint lead over T+ from $90,224 to $32,257. Realistic stop timing takes it to -$23,568. L and T+ are about tied at step 2, inside what the assumptions can support.
- **[SH]** At step 3, L loses on joint to everything including plain T (by $25,575).
- **[SH]** L stays cheapest for the buyer through step 3. That is the transfer: at step 3, against T+, the buyer saves $9,650 and suppliers pay $132,701 more. At step 2 it is $14,760 against $38,328.
- **[SH]** The buyer's lead is thin against any price response. One basis point of spend is about $54,000 here (spend about $540.2 million). The price rise that erases the buyer's lead over T+ is **0.27 basis points** at step 2, 0.18 at step 3. Against plain T it is 1.67 and 1.55. Against A+ about 1.1. The proposer's original lead over T was about 2.9 basis points. No source tells me suppliers would price in exactly that. But 0.27 basis points is 0.0027% of price, on a friction that surveys put at 0.5% to 3% of receivables in retail (weak source). The benefit is very easy to lose.

### 3.3 Where L wins and loses, one parameter at a time from step 2

L loses on joint to U in every row tested. Against T+ and A+:

- **Own audit depth decides it.** At 0 audit looks L beats T+ and A+ on joint by $40,703 and $67,825. At 0.25, about even. At 0.5, loses to both. At 1, loses by $111,970 and $84,848. The proposal's safety depends on the same step whose cost decides its case.
- **Supplier reconciliation cost.** Against T+ at half pass-through, L is behind even at $0 (-$11,582). Against A+ it flips between $10 and $20 per short-paid invoice. No figure exists. The sim's own touch is $30, and at that level L is behind by about $65,000 to $100,000 at half pass-through.
- **Stops running late.** L beats T+ on joint only if most stops run late: +$19,028 at 100%, -$16,918 at 50%. One real log suggests well under 50%. That is one company.
- **Claim acceptance.** Every 10 points of valid lines wrongly refused costs about $60,000 joint. Buyer cost improves as it falls: L's buyer margin over T+ goes from +$9,743 to +$27,337 as acceptance drops from 97% to 60%. **[SH]** The buyer is paid to be a harsher reviewer. That is the abuse incentive, shown in numbers.
- **Claim backlog.** The same pattern. At 80% review capacity, joint margin against T+ goes to -$165,138 and the buyer margin improves to +$20,518.
- **Dock undercount, deliberate or not.** Same pattern again against T+. At 5% of invoices, joint -$123,269, buyer +$20,378. At 1% to 2%, L falls level with or behind A+ at half pass-through.
- **Dirty records.** Buyer lead over T+ grows with `buyer_low` (from +$9,743 at 5% to +$46,210 at 20%) while joint worsens sharply: at 20% the joint margin against A+ is -$249,990. Against T+, L looks better to the buyer as the buyer's data gets worse. **[SH]** This is the moral hazard in one line.
- **Inquiries.** At 10% of short-pays creating an AP contact at half a touch, L's buyer lead over T+ is gone (-$726).

Things that did **not** hurt L much, reported because they cut against my brief:

- **Correlated stale prices alone.** Stale rate up to 15% per supplier-period moved joint against T+ to about -$70,000 to -$80,000, and L actually gained against A+. "One correction settles many lines" holds for the batch mechanism. The stale harm depends on the fix happening, which is the Tesco finding, and I only tested slower fixing and worse buyer behavior together in step 4.
- **Late receipts.** Timing up to 30% does not change the gap, because all receipt-gated policies carry it equally. It does not hurt L relative to others. It just shows L does not remove that cost.
- **Noise.** With zero reconciliation cost, noise helps L by up to +$72,732 against T+ at 30%. It only hurts when each short-pay has a supplier cost.
- **Review share.** Batch review cost hardly matters.

### 3.4 Clean master data

Step 2, 70% of buyer record errors removed on both sides. Cost of cleaning not counted, for either.

| | Buyer | Joint | Overpaid |
|---|---|---|---|
| T+ clean | 154,302 | 243,348 | 44,559 |
| L clean | 153,230 | 252,788 | 13,845 |
| L, dirty | 189,757 | 362,370 | 13,933 |

**[SH]** Clean data does more than the rule. A clean simple improvement beats a dirty L by $119,022 joint. Given clean data, the buyer difference is $1,072, about 0.02 basis points. At step 3, T+ clean is $291,592 joint against L clean $353,696. L's advantage is largely a tax on bad data, which is an argument for fixing the data. T+ clean is the best policy on joint at steps 2 and 3 once cleaning is free. It is not free, and I have no figure.

### 3.5 Random worlds

240 draws across stated ranges, with audit budget equal for L and A+. A range is not a probability, so these are not odds.

| Measure | L beats T | T+ | A+ | U | All of T+, A+, U |
|---|---|---|---|---|---|
| Buyer cost | 239 | 163 | 84 | 202 | 53 |
| Half pass-through | 149 | 63 | 8 | 0 | 0 |
| Full joint | 101 | 34 | 2 | 0 | 0 |

### 3.6 Limits of this attack

- All rates are mine. Nothing here is a benchmark. Step 4 is a stress test and is not symmetric: the review queue caps claims and debit memos, and unreviewed claims die after six periods, while gate exception queues are never capped. L's $1,045,965 unpaid at step 4 should not be quoted as a comparison.
- **Supplier loss and switching are not simulated.** I found no sourced cost of replacing a supplier. The break-even is simple: exits per roughly 417 supplier-years = L's lead divided by cost per switch.
- **Price pass-through** is treated as the half and full measures and the basis point break-even, not as behavior.
- Buyers letting records go stale was tested only inside step 4, with other things at once.
- In the random worlds, opportunist share has the strongest correlation with L's relative position (-0.74). I do not trust this. Padders in the model keep padding under L, and every padded invoice then costs reconciliation. A rational padder would stop. Treat it as a model artifact.
- A+'s audit is cheap partly because it leaves a large overbill leak. At step 2 it overpays ten times L's amount. A+ is not a clean winner. Its recovery also has none of the failure modes line 03 lists.
- LS (section 5) has an arbitrary design.

## 4. Logic

### 4.1 Is it a new operating model?

**[SH] Mostly not.** Mechanically it is tolerance set to zero, with the block action replaced by auto-reduce. That is a configuration of existing ERP functions, plus a claims portal that large retailers run today. By line 03's strict test it does remove the per-document stop for the amount dimension, so it can claim level 3 there, but only there. The receipt stop, the duplicate stop and the vendor stop all stay. What actually changes is who must act after a disagreement. That is a contract and power question. Calling it a process redesign hides what is being moved.

### 4.2 "Overpayment errors have no motivated detector"

**[R] as stated. [SH] in weaker form.**

- Detectors exist. Recovery audit is an entire contingency-fee business and "standard industry practice" in a 2006 Virginia report (search summary, [likely this one](https://rga.lis.virginia.gov/Published/2006/RD385/PDF)), with fees around 13.5% to 25% in the public or listed examples seen. [31 USC 3352](https://www.law.cornell.edu/uscode/text/31/3352) mandates it federally where cost effective.
- FAR 52.232-25(d) puts a duty on the contractor: if it "becomes aware" of an overpayment it shall remit. Commercial contracts can copy this.
- Suppliers holding unapplied credits may have their own unclaimed property duty (vendor sources).
- The weaker claim stands: nobody is motivated in real time, and those detectors work late and partly.
- The converse fails harder. Underpayments do not have a reliable motivated detector either. Motive scales with claim value net of claim cost, and the evidence is 1% appeal, 20% to 30% disputed (Vendor), and Tesco suppliers giving up.
- Independence is overstated too. "A single wrong record can no longer cause an overpayment" assumes the records are separate. The PO is the common parent of E, and with a PO flip, of I. One bad PO price is then two bad records. Also, a supplier who sees a high PO has an incentive to bill it. Under L, all the safety on that path falls on step 6.

### 4.3 Is the conventional gate better, given GAO's automation point?

**[SH] Not decisive.** GAO's line, that with full automation sampling and fast pay become unnecessary, is about compare cost, which the proposal does not attack. L keeps a 100% machine compare, and pays only after a match on what was received. So GAO's argument lands harder on A than on L. What GAO does not address is the cost of the stop, which is the real target. The argument does not save the gate. It does not help the proposal either, because the stop's cost is what the simple improvement also removes.

### 4.4 Is min(I, E) a stop in disguise when the receipt is late?

**[SH] Yes.** With no receipt, E is zero, or partial on a split delivery. The hard gate "something received" then holds the invoice, whole. In the only real log, 24.6% of blocks are that timing class (01, section 5.7, one company, inferred). L cannot touch those, and they are the ones with an invoice that is right. A partial receipt is worse: the buyer short-pays, and when the rest posts, the proposal's only route is a supplier claim. It needs automatic true-up. Amazon's vendors are told to wait about 30 days because late units may still be booked (Vendor), which is this problem in production. "On time" in the proposal really means "on time if the dock was on time".

### 4.5 Who pays when the buyer's data is wrong?

- On the proposer's defaults, buyer records cause 71% of short-pays (`buyer_low` 0.05 against `sup_over` 0.02, so 5 of 7). In the real log, of blocks with a visible document change, 65% changed a record rather than the invoice (7,115 of 10,910), with heavy caveats: class B may include wrong POs from either side.
- **[SH]** The supplier pays for an error it cannot fix. The proposal's phrase, "the party holding both the motive and the evidence", leaves out the third thing that matters: the power to fix the record. Only the buyer has that. On a least-cost view, cost should sit where the error can be prevented.
- The proposal has no consequence for the buyer. Compare California's 2% a month for wrongful withholding, Australia's reversed proof, or GSCOP's recommendation 3.
- **[R]** "Fair." It is a transfer that also adds a second human touch. It is fair only on invoices where the supplier is the party in error.

### 4.6 Strongest case that the conventional process survives

- The law's default already fits it. Debt follows acceptance and contract rate, the buyer proves breach, and the buyer owns its records.
- It keeps cost on the party that can prevent the error, and a stop is what forces the fix. L removes that pressure. The gate's weakness, about 80% of blocks showing no correction in one log, argues for one-sided tolerance, invoices waiting for receipts without an exception, and cleaner records. It does not argue for moving the burden.
- It needs no supplier consent, no contract change, no new estimate, no escheat analysis, no tax rework, and auditors already accept it.
- Disagreement carries information, including when E is too high. min() throws it away.
- Most stops likely finish inside terms, so the supplier may never feel them.
- With batching, one-sided tolerance and clean records, it ties or beats L on joint cost in this test. Its weakness remains overpayment leakage about 3 times L's at step 2, and the tolerance safe harbor.

## 5. Verdict

| Rejection condition | Result | Why |
|---|---|---|
| Fails to preserve a necessary control | **Conditional trip** | Overpayment control is stronger. Liability completeness and the E-too-high signal are weaker. Fixable with an accrual control, a two-sided compare that logs and routes, and control over E. None are in the proposal. |
| Worse outcomes under common conditions | **Tripped on joint, not on buyer cost** | Moderate friction: L worst of T, T+, A+, U on joint, and still cheapest of those five for the buyer. Supplier cost nearly double T+'s. |
| Needs unobtainable information | Not tripped | E exists for in-scope spend. Reliable E is hard but obtainable, and the scope excludes the rest. |
| Cannot be validated | Not tripped, but not yet validated | Everything so far is synthetic. A pilot on a supplier subset could measure claim rate, abandonment, buyer-fault share and price response. |
| Raises risk beyond an acceptable threshold | **Conditional trip** | Fine for a buyer with balanced relationships and signed terms. For a dominant buyer it recreates the Tesco pattern, with margin pressure, an adjustable reserve and a SOX issuer's books. Unlawful by default for covered Australian grocers. |
| Benefits vanish once costs are counted | **Tripped** | Buyer lead over T+ is 0.27 basis points of spend. Joint lead is negative. Own audit decides the result. |
| No better than a straightforward optimization | **Tripped** | T+ ties at step 2. Clean-data T+ beats L on joint, and buyer cost differs by $1,072. U, an obvious variant, beats L on joint everywhere. |
| Cannot be explained or audited | Not tripped | One of its real strengths, subject to the new estimate. |
| Already standard practice under another name | **Tripped outright** | Lesser-of, invoice reduction, short pay, deductions. |

**Conclusion. [SH]** As a redesign of the three-way match, reject it. As a claim of discovery, reject it **[E]**. The conventional process survives the attack in modified form: keep the compare, keep the gate where the buyer's record may be the problem, and remove the stops that carry no information.

**Scope where something survives. [SH]** A supplier-side overbill (I above E), on a repeat supplier, against a locked contract price or a machine-verified receipt, with signed terms, at a buyer that is not dominant. There, auto-reduce instead of block. That is SAP invoice reduction, used deliberately. Everything else stays with the buyer or the gate.

**Changes needed for that scope to hold:**

1. Split by likely cause before acting. Reduce only where E is locked and recently verified. If the pattern suggests a stale record (many lines, same ratio), route to the buyer, not the supplier.
2. Buyer works its own errors (the U form). In this test, it is the one change that consistently lowers joint cost. My LS variant, with detection, a small-difference pass and buyer-paid claim costs, cut L's step 4 joint from $2,832,982 to $1,573,358. It still lost to T+ and A+, at step 3 by about $87,000 to $91,000, so it is damage control, not a win.
3. Keep a small-difference pass, so pennies do not become short-pays. Accept that it is a small safe harbor.
4. Automatic true-up when a late receipt posts. No claim needed.
5. Consequences for the buyer: a service level on claim review, interest on upheld claims, repayment of supplier claim cost when the buyer's record was wrong, and a metric on buyer-fault short-pays that reaches the CFO.
6. Keep claim outcomes and running-account balances away from buyer margin targets, and never release them to income without a legal basis.
7. Contract: signed terms covering the burden, set-off across POs, a claim window of at least one year or counsel-approved notice terms, and no settlement language on remittances.
8. Controls: period-end accrual of expected claim payments, controls over price master and receiving, a two-way compare that logs E above I, tax computed net and credit memos issued, and a stated unclaimed property position per item type.
9. Step 6 must be funded and sized before the business case is run, since its cost decides the outcome.
10. A pilot with measured claim rate, abandonment, buyer-fault share, supplier price response and exit, stopped if abandonment is high or if overturn rates look like Medicare Advantage's.

## 6. Could not be verified

- **Search budget ran out** (shared session limit) before a dedicated search on Robinson-Patman cases, EU rules or further deduction studies. Later reading was limited to known URLs.
- EU Directive 2019/633: page returned empty, not read. Australian code read in the registered version; later amendments not checked. GSCOP Code text read only as quoted in the Tesco report.
- ASC 405-20, 450-20 and 606: Codification not accessed. Secondary summaries or memory. Deloitte DART returned no content. AS 2501 blocked. AS 2201 relied on line 04's reading. AS 1105.10 read directly.
- Target and Lowe's rules: vendor summaries only. No retailer vendor manual, Walmart or Amazon primary document read. Walmart "does not reimburse" (one vendor guide) not confirmed, so not relied on. Whether retailers apply the rule at line or invoice level unknown.
- No peer-reviewed measure of deduction costs. All deduction rates are vendor or survey. KFF 2022-24 appeal figures seen secondhand. ECG's $26 million unverified. The 80% overturn range is for prior authorization, not payment.
- No figure for supplier cost to reconcile a short-pay, price pass-through of deductions, supplier switching cost, or review capacity. Those are swept, not estimated.
- Delaware law checked only through a 2010 article and a client alert; the current statute and the case caption of the rebate decision not checked. State B2B exemption list dated. Temple-Inland read through law firm summaries. Treatment of disputed amounts rests on a vendor guide.
- Sales tax: SSUTA Section 320 text not read. State examples only. Pub. L. 119-21 threshold from secondary sources.
- 2-209 comments, Automatic Canteen-type case law on 2(f), courts' treatment of contractual claim windows against 2-725, whether ACH is an instrument under 3-311: my reasoning, no cases read.
- SAB 99 factors not checked. No real auditor consulted. No real supplier consulted.
- Calibration from the BPI log is one company, non-US, without dollar values or reason codes.
- My engine's constant +1% to +5% gap to simulate2 was not fully explained. It does not change any ranking.

## Sources

Listed inline. Primary: [42 CFR 414.21](https://www.law.cornell.edu/cfr/text/42/414.21), [42 USC 1395l](https://www.law.cornell.edu/uscode/text/42/1395l), [42 CFR 405.942](https://www.law.cornell.edu/cfr/text/42/405.942), [HHS OIG OEI-09-16-00410](https://oig.hhs.gov/reports/all/2018/medicare-advantage-appeal-outcomes-and-audit-findings-raise-concerns-about-service-and-payment-denials/), [FAR 52.232-25](https://www.law.cornell.edu/cfr/text/48/52.232-25), [5 CFR 1315.4](https://www.law.cornell.edu/cfr/text/5/1315.4), [5 CFR 1315.10](https://www.law.cornell.edu/cfr/text/5/1315.10), [31 USC 3907](https://www.law.cornell.edu/uscode/text/31/3907), [31 USC 3352](https://www.law.cornell.edu/uscode/text/31/3352), [49 USC 13710](https://www.law.cornell.edu/uscode/text/49/13710), [49 USC 14705](https://www.law.cornell.edu/uscode/text/49/14705), [15 USC 13](https://www.law.cornell.edu/uscode/text/15/13), [26 CFR 1.6041-3](https://www.law.cornell.edu/cfr/text/26/1.6041-3), UCC [1-201](https://www.law.cornell.edu/ucc/1/1-201), [1-303](https://www.law.cornell.edu/ucc/1/1-303), [1-304](https://www.law.cornell.edu/ucc/1/1-304), [1-308](https://www.law.cornell.edu/ucc/1/1-308), [2-209](https://www.law.cornell.edu/ucc/2/2-209), [2-309](https://www.law.cornell.edu/ucc/2/2-309), [2-607](https://www.law.cornell.edu/ucc/2/2-607), [2-609](https://www.law.cornell.edu/ucc/2/2-609), [2-612](https://www.law.cornell.edu/ucc/2/2-612), [2-717](https://www.law.cornell.edu/ucc/2/2-717), [2-725](https://www.law.cornell.edu/ucc/2/2-725), [3-311](https://www.law.cornell.edu/ucc/3/3-311), [Tex. Prop. Code 28.003](https://texas.public.law/statutes/tex._prop._code_section_28.003), [Cal. Civ. Code 8800](https://codes.findlaw.com/ca/civil-code/civ-sect-8800/), [GCA Tesco report](https://assets.publishing.service.gov.uk/media/5a81a094ed915d74e33ff39b/GCA_Tesco_plc_final_report_26012016_-_version_for_download.pdf), [Australian Food and Grocery Code](https://legislation.gov.au/F2024L01651/asmade/2024-12-16/text/original/pdf), [SEC Rite Aid 34-46099](https://www.sec.gov/litigation/admin/34-46099.htm), [PCAOB AS 1105](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105), [UC Accounting Manual D-371-36](https://financial.ucsc.edu/SiteAssets/Lists/Guide%20Nav%20Animal%20Life/UC%20D-371-36_TL102.pdf).

Product documentation (mechanics only): [SAP Help](https://help.sap.com/saphelp_sfin100/helpdata/en/f3/70b6531de6b64ce10000000a174cb4/content.htm), [SAP Help 2](https://help.sap.com/saphelp_sfin100/helpdata/en/df/6fb6531de6b64ce10000000a174cb4/content.htm), [SAP Learning](https://learning.sap.com/courses/invoice-verification-in-sap-s-4hana/reducing-invoices-1), [SAP Ariba](https://support.ariba.com/item/view/157914).

Secondary, law firm or vendor (weak where labeled): [HFMA](https://www.hfma.org/payment-reimbursement-and-managed-care/contracting/62082/), [ECG](https://www.ecgmc.com/insights/blog/the-lesser-of-trap-how-a-hidden-contract-clause-is-reducing-your-hospitals-revenue), [SPS Code 11](https://www.spscommerce.com/community/articles/code-11-pricing-overcharge-price-difference-between-po-and-invoice), [SPS impact](https://www.spscommerce.com/community/articles/the-impact-of-retailer-deductions), [SPS Amazon timeline](https://www.spscommerce.com/community/articles/updated-dispute-timeline-for-1p-amazon-suppliers), [Amalytix](https://www.amalytix.com/en/knowledge/logistics/shortage-claims/), [SC Digest](http://www.scdigest.com/NEWSVIEWS/18-05-29-1.PHP?cid=14268&ctype=content), [Yale Insights](https://insights.som.yale.edu/insights/big-box-retailers-squeeze-smaller-suppliers-by-borrowing-from-them), [LeadingAge on KFF](https://leadingage.org/new-kff-report-more-ma-prior-authorizations-appeals-remain-successful/), [Morris Nichols](https://www.morrisnichols.com/assets/htmldocuments/CorporateCounselWeeklyHoughtonMayrackUnclaimedPropertyDelawareMakesSignificantChanges.pdf), [Kroll](https://www.kroll.com/en/client-alerts/client-alert-delaware-court-rules-rebates-issued-by-staples-are-unclaimed-property), [Skadden on Temple-Inland](https://www.skadden.com/insights/publications/2015/04/itempleinlandi-sheds-light-on-delawares-use-of-est), [UPPO](https://www.uppo.org/blogpost/925381/237086/Inside-the-B2B-exemption), [Virginia recovery audit](https://rga.lis.virginia.gov/Published/2006/RD385/PDF), [Nexasphere](https://nexasphere.io/blog/short-paid-on-a-freight-invoice-here-is-how-to-dispute-it-with), [Law Insider](https://lawinsider.com/clause/billing-disputes).

Research lines used: agents/01-conventional-model.md (BPI log, Montgomery), 02, 03, 04 (GAO/AIMD-21.3.2, AS 2201, ERS).
