# 04 Prior art: what already exists for dropping or redesigning the three-way match

Research line 4. Date of research: 2026-11-04. Purpose: stop anyone claiming novelty that is not there.

Tags: [E] Established. [SH] Supported hypothesis. [SP] Speculative. [R] Rejected. "Vendor" marks weak evidence. Claims about what was "not found" mean not found in this search, not proof of absence.

## Bottom line

- [E] No precedent found omits verification altogether. Every one moves it, shrinks it, caps the exposure, or shifts the risk to someone else by contract.
- [E] Only one precedent actually pays before receipt is evidenced: federal fast pay. It is capped per order, limited by geography, backed by a supplier warranty, and followed by post-payment verification.
- [R] "Ford eliminated the match." Ford eliminated the invoice. Hammer says the match went from 14 data items across three documents to three data items across two, and it stayed automatic and before payment.
- [E] The cost-of-control rule has been written federal guidance for decades: sample if examination cost plus projected undetected loss is below the cost of examining everything.
- [E] Hammer and Champy argued in 1993, in print, that controls should be deferred or aggregated and should "tolerate modest and limited abuse". That idea is not new.
- [SH] What is missing is measurement. No public study found gives the catch rate of each leg of the match, or the loss experience of a commercial firm that relaxed it.

## 1. Evaluated Receipts Settlement (ERS) and pay-on-receipt

**What it is.** The buyer computes payment from receipt quantity times PO price, and the supplier sends no invoice. Oracle's documentation states it directly: "The amount on the invoice is determined by multiplying the Quantity received by the Purchase Order Item Unit Price." It also treats Payment on Receipt, ERS and Self Billing as one thing. [E] (Oracle docs, product documentation, used for mechanics only.)

**Origin.** The sources conflict, and the brief's "General Motors in the 1980s" could not be verified.
- [E] Ford's "invoiceless processing" was in print by July 1990 (Hammer), so it predates any 1994 date.
- NC State SCM article says GM pioneered ERS, citing Thomas, "Computers streamline GM supplier payments", Automotive News, Sept 1994, and gives about 1.5 million transactions a month. The "1994" looks like the article date, not the start date. [SP] The Automotive News piece was not retrieved.
- Turner and Weickgenannt (textbook): "In the mid-1990s, some companies, including those in the automotive industry, began implementing invoice-less matching systems." They add that the change is more process than technology.
- Soltec (Vendor) says it was a Japanese practice from the 1970s, introduced to Ford in 1986. Unsourced, commercial interest.
- [E] AIAG guidelines existed by November 1998, because the AISI steel guideline says its model "follows the basis AIAG" guidelines. That guideline covers about 80% of volume and leaves the rest to trading partner agreements. AIAG's own document was not found.

**Adoption.** Only one data source found, a member poll with no stated sample size. Weak.
- Peeriosity 2013: 56% of members implemented ERS, 7% tried and failed.
- Peeriosity 2019: 55% have under 10% of payments or none on ERS, 35% report over 30%, 28% do not use it.
- [SH] Broad adoption in name, thin in volume outside repetitive direct materials.

**Measured results.** No independent measurement found. The numbers in circulation are Ford's 75% head count claim (section 2) and GM's volume, which is not a result.

**Why it did not take over.** [SH] From Peeriosity (self-reported):
- PO quality problems. ERS pays the PO price, so a wrong PO is a wrong payment.
- Use tax concerns.
- Need for EDI, advance ship notices and clear remittance files.
- A pilot needing "significant post-payment reconciliation with the supplier".
- Suppliers opting out in favor of e-invoicing.
- Work shifting to the supplier. Hammer's own article has a Ford supplier printing invoices and throwing them away, "reconciling cash received against invoices never sent".
- A Chrysler ERS training deck runs 71 pages with reconciliation codes and "Supplier Responsible" discrepancy categories. Only the outline was visible, but the machinery is not trivial.

**Audit and tax treatment.**
- [E] The most authoritative control statement found is GAO, May 2000, on a federal entity paying without invoices. "Title 7, however, does not preclude payment from being authorized without an invoice if adequate internal controls exist." Three conditions: pay only after receipt and acceptance and "after matching the types and quantities received with those on the purchase order or contract"; duplicate payment controls; timing to due dates. GAO did not object. So the match is the stated condition for dropping the invoice.
- [E] State tax bodies treated it as an open documentation problem. A task force of COST, IPT, TEI, MTC and FTA studied ERS and tax compliance (publication date not confirmed), described as commerce "without invoices". A Sales Tax Institute guide tells firms to know whether ERS is in use and when it began.
- [E] Oracle's Payment on Receipt creates sales tax lines from the PO, and for use tax "No tax distribution is created". This is one concrete mechanism behind the use tax worry.
- No PCAOB or AICPA statement specific to ERS was found. Federal income tax records treatment (Rev. Proc. 98-25) was not verified.

**Does it prove the match can be omitted?** No. [E] It proves the invoice leg can be omitted, when POs are accurate, prices are contractual, receipts are reliable, and suppliers agree in advance.

**Weak evidence.** All adoption and benefit data.

## 2. Ford accounts payable (Hammer 1990): the closest precedent

**What the original says** (HBR, July-August 1990; read in a transcribed copy, see limits):
- "Accounts payable in North American alone employed more than 500 people." Management aimed for about 20% fewer. Ford was "aspiring to a 400-person department", Mazda had "a total of 5 people", and even after adjusting for size Ford "figured that its accounts payable organization was five times the size it should be."
- The clerks' time went on mismatches: "The department spent most of its time on mismatches".
- The fix was upstream: "a better choice was to prevent the mismatches in the first place." The receiving clerk checks the online database. No match means return the goods.
- The key sentence: "Under the old procedures, the accounting department had to match 14 data items between the receipt record, the purchase order, and the invoice before it could issue payment to the vendor. The new approach requires matching only three items--part number, unit of measure, and supplier code--between the purchase order and the receipt record. The matching is done automatically".
- The qualifier: "Where it has instituted this new process, Ford has achieved a 75% reduction in head count".
- The rule: from "We pay when we receive the invoice" to "We pay when we receive the goods."

**What the book says** (Hammer and Champy; 2001 HarperBusiness text, pp. 44-46):
- "Instead of 500 people, Ford now has just 125 people involved in vendor payment."
- "Payment authorization, which used to be performed by accounts payable, is now accomplished at the receiving dock."
- Mismatches were "infrequent situations", and most invoices already matched. No rate is given.

**Reading.**
- [E] The check moved from AP clerks after the fact to the dock before acceptance. It became preventive at the earliest point.
- [E] The precondition was that purchasing owns correct data. Hammer: purchasing agents had to ensure POs "had the correct information", and clerks had "to make decisions about whether to accept the goods".
- [SH] Ford cut the labor of resolving exceptions by refusing goods that do not match. The exception cost moved to the supplier and the dock.

**Actual outcome.**
- [E] Could not be independently confirmed. No Ford document, audit or third-party study was found. The only numbers trace to Hammer and Hammer and Champy.
- The article's "where it has instituted" becomes an unqualified 500 to 125 in the book. Neither gives a date, the share of spend covered, payment error rates, or labor added at the dock and in purchasing.
- Retellings drift. A Soundview-type summary says the "purchasing department" fell to 125. strategy+business says Ford acted "after acquiring Mazda". The 400 figure is a target, not a baseline, and some retellings confuse them.
- From memory, not checked here: Ford held a minority stake in Mazda then, not ownership.

**Critique.**
- [E] Critique of BPR as a movement exists: Grint 1994 ("Reengineering History", disputes novelty), Grint and Willcocks 1995, Strassmann 1994, strategy+business (citing studies that 70% or more of projects made things worse, figure unverified). Jarvenpaa and Stoddard (1998) found redesign radical in intent, evolutionary in implementation (read second-hand).
- Strassmann's essay does not mention Ford. I found no critique that tests the Ford numbers specifically. That is a gap, not vindication.
- [SH] The case's evidentiary value is low: one self-reported head count, no loss data, no control test, a management guru as sole source.

**Does it prove the match can be omitted?** [R] No. It proves a reduced, automated, pre-payment PO-to-receipt check can replace the invoice comparison.

## 3. Self-billing, consignment, VMI, pay-on-production, fast pay, federal payment integrity

**Self-billing.**
- [E] UK: allowed with a formal prior agreement, supplier acceptance, a "SELF-BILLING" marker, and no HMRC approval since 2004 (HMRC Notice 700/62, VATREC15020). Agreements usually last 12 months.
- EU VAT Directive Art. 224 reportedly requires prior agreement and an acceptance procedure, seen only in a secondary glossary. No US federal equivalent was found.
- These are tax document rules. They say who may issue an invoice, not whether to verify delivery.

**Consignment and VMI.** Waller, Johnson and Davis (1999) is the standard VMI citation, confirmed bibliographically only. [SH] Consumption replaces receipt as the trigger, so the usage record does the receipt's job. This is my inference. No source measuring payment error or control outcomes was found.

**Pay-on-production.** The term is used loosely. Wikipedia describes a financing model where the supplier owns the equipment and is paid per unit produced, and cites a 2002 Automotive News headline, "Ford dumps pay-on-production plan" (headline only). Automotive and aerospace evidence on invoice checking was not found. Treat as unverified.

**Federal fast pay.** The only true precedent for paying first. [E]
- FAR 13.401: payment "prior to the Government's verification", based on the contractor's invoice certification of delivery to a carrier or post office.
- FAR 13.402 conditions, all required: orders up to $45,000 (agencies may go higher case by case); geographic separation and inadequate communications making payment on acceptance impractical; title passes on delivery to carrier; supplier agrees to replace, repair or correct; firm-fixed-price supplies only; a system to document performance, feed back deficiencies, and identify abusers.
- FAR 13.403: consignee reports problems, normally within 60 days. FAR 52.213-1: contractor bears "all responsibility and risk of loss" and corrects within 180 days if instructed.
- 5 CFR 1315.6: "payment may be made without evidence that supplies have been received", orders up to $25,000 unless higher is approved. Two thresholds are in force on paper.
- The FAR overhaul moves the procedure to subpart 32.12 and clause 52.232-90 (agency deviation texts). Whether all conditions survived was not checked.
- Purpose matters: fast pay expanded in the 1980s to meet Prompt Payment Act timing, not to save control cost (GAO, p. 8).

**GAO's guide (AIMD-21.3.2, May 2000) is the closest thing to a published design review.** [E]
- "Statistical sampling was initially implemented in the 1960s", on invoices below $2,500 at that time, to reduce cost while keeping confidence.
- The rule (p. 9): "Savings would be achieved if the combined costs of (1) examining the sample and (2) projected losses due to undetected errors on invoices not examined are less than the administrative cost of examining all invoices." Plans must set a tolerable error rate (p. 18, n. 14).
- Statutory base: 31 USC 3521(b)-(c). Agencies may audit vouchers by sampling, and officials acting in good faith are not liable for unaudited vouchers.
- Fast pay plus sampling, meaning no 100% verification even afterward, was acceptable under $2,500 with risk-scaled examination, effective monitoring, and a continuing vendor relationship.
- One agency proposed sampling up to $25,000 with exception-only notice within 20 days of invoice receipt. GAO accepted this if controls were followed and benefits exceeded cost. That is negative confirmation, in federal guidance, in 2000 or earlier.
- GAO suggested excluding first-time vendors and those with a history of abuse.
- Internal control is not reduced: these procedures "neither reduce the need for effective internal control nor relieve the certifying/disbursing officer of his or her responsibility."
- Direction of travel: "With full automation, statistical sampling of invoices prior to payment to make inferences about the universe would no longer be necessary", and "fast pay could be eliminated in most situations." [SH] GAO saw relaxation as a workaround for costly manual matching. If the match is free, the relaxation has no purpose. This is the strongest counterargument to dropping an automated match.

**Loss experience.**
- [E] Only one figure found: an unnamed agency's OIG reported that "over a 5-month period, 10 per cent of the invoices paid under the fast pay process had incorrect or missing support" (GAO, p. 19). That is a documentation error rate, not a loss rate. GAO said sampling should not go ahead if that rate exceeded the tolerable rate.
- No GAO, OIG or Treasury evaluation of fast pay losses across government was found. DoD OIG 08-096 appears to touch improper payments on DLA fast pay contracts, but the PDF could not be retrieved.

**Federal improper payments and recovery.**
- [E] FY2025: about $186 billion across 64 programs, 15 agencies, $153 billion overpayments, $136 billion in five program areas (GAO-26-108694). FY2024: $162 billion (GAO-25-107753). This is dominated by benefits and health programs and tells you almost nothing about B2B payables.
- [E] Nearest comparator is DoD Commercial Pay, MOCAS: FY2025 $225.0 billion outlays. GAO lists $1.4 billion and 0.6%, up $1.3 billion, "No reason provided". The paymentaccuracy.gov page shows conflicting FY2025 totals ($96.3 million in one section, larger cause amounts in another). FY2024 shows $96.3 million on $222.3 billion.
- These are rates with receipt verification in place, so they are not a baseline for removing it. DoD OIG found earlier estimates unreliable: DODIG-2021-024 reports 302 improper payments, $136 million, not identified.
- [SH] Named MOCAS causes are payment terms keyed from contract modifications, line item and accounting setup, and credits on multi-funded invoices. These are contract data errors, which a match against the same contract data may not catch.
- [E] Recovery audits: 31 USC 3352(i) requires them for programs of at least $1,000,000 a year if cost effective. Contractors may not make final determinations. The law began as 31 USC 3561 (FY2002 NDAA s.831) and was repealed and folded in by IPERA 2010, per search results. Federal recapture rates were not retrieved.
- [E] Against pay-and-chase: GAO-16-394 (Medicare) said prepayment review "can better protect Medicare funds because not all overpayments can be collected". CMS disagreed with the recommendation but said it is moving away from pay and chase. No head-to-head recovery rate was found. Different payment domain.
- [E] Green Book 2025 "emphasizes preventive control activities" (GAO, May 2025). Federal, not SOX, but it shows where the standard setter is leaning.

**Does it prove the match can be omitted?** Partly. [E] Fast pay proves pre-payment verification can be omitted for low-value supplies from known suppliers with contractual recourse. Nothing proves it can be omitted without recourse or at large value.

## 4. Procurement cards

**Logic.** Spend limit plus category and vendor limits, pay first, monthly review, dispute right. Hammer and Champy (pp. 61-62) describe it: a $500 limit per unit, bank tape run against budget, and "it was better to swallow the limited exposure to abuse". Bragg recommends avoiding the match "entirely by shifting more purchases to company procurement cards". [E]

**Measured.**
- GAO-17-276 (FY2014): $8.7 billion of micropurchases, 300 sampled from over 17 million, "little evidence of improper or potentially fraudulent purchases", but 22% lacked complete approval documentation. Not a loss rate. Small sample.
- GAO-08-333: 41% (CI 31-51) failed key control tests, FY2005-06. CRS on CIGIE: about 51% of sampled purchases broke at least one policy, few fraud examples. [E] Policy noncompliance is common, proven dollar loss is low.
- Palmer, Gupta and Brandt (2019, Administrative Issues Journal; RPMG 2017 survey of 350 institutions): loss from fraud and misrepresentation 0.008% of spend ($80 per $1 million), policy violations another 0.008%. Self-reported, and one author is at RPMG.
- RPMG 2005 via American City and County: 0.67 incidents per 10,000 transactions, $340 per $1 million. Search snippet only, page blocked.
- Current RPMG figures are paid products, not seen. JPMorgan's "below the industry average" gives no number (Vendor).

**Liability and chargebacks.**
- [E] 15 USC 1645 and 12 CFR 1026.12: firms with 10 or more cards may agree to liability terms beyond the default, but cannot push it to employees. The default consumer cap is $50.
- Commercial dispute rights are mainly contractual. Visa 13.1 (merchandise not received) reportedly allows 120 days, capped at 540 days from processing (Vendor blogs citing Visa Core Rules, rulebook not read).
- [SH] Chargebacks are post-payment recourse run by a third party who can debit the seller. A corporate AP department has no such intermediary unless it pays by card. That is what fast pay's contract clause tries to copy.
- NAPCP-linked material says issuers typically absorb misuse, while network waiver program terms were not found.

**Does it prove the match can be omitted?** Yes, for low-value spend. [E] Conditions: capped exposure per card, known categories, cardholder review, third-party recourse. It does not extend to high-value direct materials.

**Weak evidence.** Loss rates are survey self-reports. Undetected loss is uncounted by definition, and the 22% documentation gap makes that worse.

## 5. Continuous auditing and monitoring

**Vasarhelyi and Halper (1991).** CPAS at AT&T Bell Laboratories monitored billing systems. Metrics are compared to standards and raise alarms. "Continuous Process Auditing then, is really an analytical review technique". [E] It is about billing, not payables, and it adds to controls rather than replacing them. AICPA/CICA published *Continuous Auditing* in 1999 (citation confirmed, text not read).

**Procure-to-pay evidence.**
- Kogan, Alles, Vasarhelyi and Wu (AJPT 2014): nine months of procurement data from a health care provider, simulated. Rule-based verification came first, and the client "considered the list of exceptions identified at this stage as a major source of value added". Analytic models on daily aggregates had excellent detection at errors of 2-4% of voucher balance, and "If the error size drops to 0.1% and 0.5% level, all of the models have high false negative errors." [E] Aggregate analytics did not catch small errors in that study. [SH] Aggregate detective monitoring is too coarse to replace a transaction-level check, though it may be enough for an ICFR material-misstatement objective.
- Jans, Alles and Vasarhelyi (TAR 2014): a global bank, 26,185 POs, 31,817 payments in January 2007. Process mining found payments without approval, 175 segregation-of-duties violations, and 742 cases (2.8%) lacking a sign-off and failing the conditions for that. Internal audit had not detected them. 265 payments lacked an invoice, all explained by another document type. Authors do not determine fraud or loss. [E] Full-population review finds more than sampling, even at a firm with a match. One bank, one month.
- The same paper notes ERP flexibility: "while ideally there would be a three-way match", allowances exist, and the bank's goods-receipt indicator allows invoices to pay without receipt.
- Alles et al. (2006, Siemens; 2008): monitoring of control settings. Citation and abstract only.

**Did detective monitoring replace preventive controls anywhere?** [E] No documented case found. Adoption surveys (Vendor or firm-sponsored) show use for audit planning and risk assessment, for example Protiviti's 86% of internal audit analytics functions "to some degree". A study of nine leading internal audit organizations found none at the true continuous stage. The field's direction is the reverse: Kuenkaikaew and Vasarhelyi (2013) define a "preventive audit" with filtering rules "to block highly probable faulty transactions prior to their execution."

**PCAOB and auditor practice.** [E] AS 2201 (read in a 2024 archive copy):
- .41: testing depends on whether controls "sufficiently address the assessed risk of misstatement to a given relevant assertion rather than on how the control is labeled (e.g., entity-level control, transaction-level control, control activity, monitoring control, preventive control, detective control)."
- .A8: effective ICFR "often includes a combination of preventive and detective controls."
- .68: a compensating control "should operate at a level of precision that would prevent or detect a misstatement that could be material".
- .B28-.B29: "Entirely automated application controls are generally not subject to breakdowns due to human failure", which permits benchmarking if IT general controls are effective and the control is unchanged. .B30 flags dependence on tables and parameters.
- Staff Audit Practice Alert 11 (2013) and later Spotlights: inspectors focus on precision of review controls and on system-generated data. About 17% of comment forms in the 2021-22 cycles involved information accuracy and completeness.
- PCAOB Release 2024-007 tightens technology-assisted analysis for fiscal years beginning on or after December 15, 2025. A July 2025 request sought deferral of AS 1105.10A, outcome not confirmed.
- Exchange Act 13(b)(7): "reasonable assurances" means what "would satisfy prudent officials in the conduct of their own affairs". Cost-benefit sits in legislative history, per a 1983 SEC-era paper.
- COSO 2013 Principle 10 point of focus on a mix of controls was seen only in a reproduction.

[SH] So PCAOB text has no preference for preventive over detective. The test is precision and timeliness. An automated match is also cheap to audit, which removes one savings case for dropping it. [SH] ICFR concerns material misstatement, not cash leakage, so the match's audit role (likely accruals and existence of liabilities) differs from its payment-accuracy role. That split is my reading. No PCAOB text naming the three-way match was found.

**Does it prove the match can be omitted?** No.

## 6. Blockchain, shared ledgers, e-invoicing

**Blockchain.**
- No procure-to-pay pilot with measured results was found.
- IBM Global Financing: 25,000 disputes a year, over 40 days, about $100 million tied up, under 10 days in a simulation on two years of data. Press and vendor reporting from 2016-17, production result not found, legacy process retained. Disputes, not matching.
- Trade networks closed or failed: TradeLens (announced November 2022), we.trade (2022), Marco Polo (2023), Contour (2023, later reportedly bought).
- [E] Ledgers do not prove delivery. Sheldon (2021, JIS) treats oracles as service organizations. Caldarelli (2025, JRFM) reports 67% of surveyed accounting blockchain papers do not mention oracles.
- [SH] A shared ledger of PO and receipt is functionally Ford's shared database, across firm boundaries. The dock event still needs a trusted reporter.

**E-invoicing.**
- Italy SdI mandatory B2B from January 2019. Mexico CFDI from 2014 (sources differ on month). Mostly Vendor sources, and reported Italian VAT gains are not causal estimates.
- Bellon et al. (Peru, IMF WP 2019, reportedly J. Public Economics 2022): effects concentrated in smaller firms and non-compliant sectors. Tax outcome, not payables.
- US: Business Payments Coalition pilot with Federal Reserve involvement led to DBNAlliance. No B2B mandate (mostly Vendor sources). OMB M-15-19 (July 2015) moved agencies to e-invoicing by end FY2018. Treasury's "up to $450 million" sits beside a PwC-for-Treasury $266 million, with no GAO check found.
- [E] Clearance authenticates that an invoice was issued and reported. It does not attest delivery or price agreement, so it does not touch the match logic. Non-US items do not change any conclusion here.

**Does it prove the match can be omitted?** No. [SH] It could cut invoice data mismatch and invoice forgery risk.

## 7. Academic work on risk-based checking and cost of control

**Directly on payables.** I found no peer-reviewed paper that models optimal invoice checking, match tolerance, or sampling of invoices before payment. [SH, uncertain: paywalled databases were not searched.] GAO's guide is the closest.

**Adjacent and usable.**
- Deming kp all-or-none rule (*Out of the Crisis*, 1986), Papadakis (1985, JQT), Vander Wiel and Vardeman (1994, Technometrics 36(1)). With independent identical items and additive costs "An optimal inspection policy will inspect either every item produced or no item". Other cost structures or informative inspection can break this. [SH] By analogy, within a stable supplier and invoice class, random sampling is hard to justify on cost alone. Sampling earns its place through learning and deterrence. Not tested on invoices.
- Economic inspection and variance investigation: Dyckman (1969), Kaplan (1975, JAR 13(2)), Magee (reported to find model differences have little cost effect). A direct analog to tolerance setting. Abstract level only.
- Control reliability: Cushing (1974, TAR 49(1)), Bodnar (1975, TAR 50). Internal control modeled as a reliability and cost design problem 50 years ago. Citations confirmed, text not read.
- Strategic audit: Border and Sobel (1987, RES 54(4)) find optimal audit probability falls with reported income and can be stochastic. Townsend (1979) and Reinganum and Wilde (1985) confirmed through secondary citation. [SH] Against strategic vendors, predictable thresholds invite gaming, so randomness has value that Deming's model ignores. Fellingham and Newman (1985), Shibano (1990) and Avenhaus, von Stengel and Zamir were not confirmed in search.
- Audit sampling: Elder et al. (2013, AJPT 32 Supp. 1): research gives limited insight on current practice, and recent studies find low sample error rates in many populations.
- Expense audits run on risk-tiered sampling with 100% review of high-risk items (Vendor: Corpay, AppZen). No research confirms the claimed rates.
- UCC 3-103: an automating bank need not examine each instrument if its procedures do not vary unreasonably from general banking usage. [E] Commercial law already blessed "no individual check" as ordinary care, within reason. Oregon's *Medford* case, as discussed in a later decision, warns that doing nothing below a cutoff can fail.

## 8. AI-based AP products (market claims only, Vendor throughout)

- [E] Dominant claim: automate the match and leave humans the exceptions. Dooap, despite "Rethinking 3-Way Matching", keeps the comparison and lets "the user … make the final call".
- Boldest found: Blackbee AI says agentic validation "does not just check whether an invoice matches a PO" and "resolves exceptions autonomously", reading contracts and using statement of work plus delivery confirmation for services. It still reads PO and goods receipt data. Its 60-80% claim has no support.
- [E] I found no vendor claiming to remove the match itself. Closest are non-PO and contract-based flows (SAP Ariba categories per secondary source; Stampli says non-PO validation is human budget-owner confirmation, Vendor) and two-way matching for low-value items (Kognitos).
- Touchless numbers conflict and definitions vary. Corpay citing Ardent: $2.78 and 49.2% best-in-class against $10.89 average. Other sites cite $9.84. APQC appears as $6.00 and $21.40. Primary reports not seen. Not benchmarks.
- Dissent inside the vendor world: PredictAP (bias disclosed) argues agents can be gamed by fraudsters staying inside the rules, and that approval needs independent human authority. RedHub: "AI approves nothing."
- PCAOB staff Spotlight (July 2024, not a rule): firms view human involvement as essential to review GenAI output. Primary not opened.
- [E] Independent evaluation of AI match performance: none found. Gartner or similar coverage not confirmed.

## 9. Writing that argues the match is overused or should go

**Argued.**
- Hammer (1990): "a better choice was to prevent the mismatches in the first place."
- Hammer and Champy (1993; 2001 text pp. 61-62): "reengineered processes use controls only to the extent that they make economic sense." "the cost of the checking may even exceed the cost of the goods being purchased." "These control systems will, by design, tolerate modest and limited abuse, by delaying the point at which abuse is detected or by examining aggregate patterns rather than individual instances."
- Steven Bragg, AccountingTools: "It is especially expensive for low-value purchases, where the matching labor may cost more than the bill being paid." "You can make three-way matching more efficient by excluding small-dollar and recurring invoices from the matching requirement."
- CFO Club: "It's best not to bother with three-way matching for a $50 invoice."
- Kognitos (Vendor): for low-value purchases the cost of three-way matching "can exceed the risk of overpayment".
- Palmer, Gupta and Brandt on cards: "Few administrators will support losing the proverbial dollar to control a dime".

**Not found.** [E] Anyone serious arguing the match should be dropped across the board, or that it is a poor control on evidence. No peer-reviewed critique of the three-way match itself was found, and no phrase like "the three-way match is dead". Mainstream writing defends it. [R] Claiming "nobody has challenged it" is false. [SH] Claiming "nobody has tested it with loss data in public" looks true.

## What is already standard practice under another name

Do not present these as new:

- Pay on goods, no invoice: ERS, Payment on Receipt, invoiceless processing, self-billing (Ford by 1990; SAP and Oracle standard functions).
- Skip checks on low value: P-cards, small-dollar exclusions, two-way match.
- Tolerances: ERP settings, Bragg, Jans et al.
- Pay first, verify later: fast pay, with supplier recourse and abuser lists.
- Sample instead of checking all: federal since the 1960s, 31 USC 3521(b).
- Cost-of-control inequality with tolerable error rate: GAO Title 7 guidance.
- Trust tiers by supplier: GAO's first-time and abuser exclusions, FAR 13.402(f).
- Exception-only confirmation: GAO's 20-day variant.
- Deferred or aggregate controls: Hammer and Champy.
- Post-payment recovery: recovery audits.
- Full-population detection: continuous auditing, process mining.
- Shared record of PO and receipt: Ford's database, now called a shared ledger.
- AI handling exceptions: the current market pitch.

## Where real room may remain

1. [SH] Measuring the control. Per leg of the match: real errors caught, false alarms, cost, and what would have been caught anyway. Nothing public found. The BPI Challenge 2019 log is a public real P2P dataset with three-way categories, but it has no loss outcomes.
2. [SH] Commercial loss experience where the match was relaxed, on the GAO inequality. Only a federal 10% documentation figure exists.
3. [SH] A formal model applying all-or-none inspection and strategic audit to invoices, with informative supplier signals, gaming, and tolerance setting. Pieces exist separately, the assembly was not found.
4. [SH] Splitting the match's jobs: payment accuracy, fraud, accrual completeness, audit evidence. This would show whether SOX needs what AP pays for, and where AS 2201 .68 precision is the binding test.
5. [SP] Whether a learned, changing model fits ".B28 entirely automated" benchmarking at all. No authority found.
6. [SH] The threat may have moved. AFP 2025: 79% of organizations hit by attempted or actual payments fraud, vendor imposter fraud cited by 45%, checks most targeted (survey, summary only). ACFE 2024 (secondary summaries): billing schemes 22% of cases, $100,000 median, tips 43% of detection. A match compares PO, receipt and invoice, so it is not designed to catch a changed bank account. My inference. Worth testing.

Any contribution here would be evidence and formalization, not the concept. If the conventional match survives the disproof attempt, GAO's "automation makes the workaround unnecessary" argument is the likely reason.

## Could not be verified

- GM ERS origin in the 1980s; Thomas (1994) and Tax Executive (1998) articles; AIAG's own document; COST/MTC task force date and text (page reached by snippet only).
- Any Ford primary record, the share of spend covered, the implementation date, or any test of the 75% claim. Ford's Mazda stake (from memory).
- Hammer (1990) was read in a student-hosted transcription with typos (NTNU reprint returned 401). The book was read in a 2001 edition; 1993 wording and paging were not compared.
- Davenport and Stoddard (1994); Case (1999); Davenport (1995), not retrieved.
- GAO Title 7 current sampling limit (the $2,500 is as of 2000). Whether 13.402 conditions survive unchanged in RFO 32.12.
- DoD OIG 08-096 content. Any government-wide fast pay loss study. Federal recapture rates. CMS demonstration evaluation.
- Rev. Proc. 98-25 application. EU Art. 224 primary text. Green Book 2025 paragraph text (cost-benefit language seen in a search summary only; PDF extraction failed). COSO primary text. Current AS 2201 text effective 12/15/2026.
- AICPA/CICA 1999 and AICPA 2015 contents. Siemens findings. Dyckman venue (sources disagree), Kaplan, Cushing, Bodnar, Papadakis, Border and Sobel beyond abstracts. Hughes (1977), Yu and Neter original, Fellingham and Newman, Shibano, Avenhaus et al.
- Current RPMG, Nilson, Ardent, APQC, Gartner, ACFE and AFP primaries. Visa Core Rules and network waiver terms. Protiviti survey original.
- Aerospace pay-on-consumption practice. Chrysler deck contents beyond its outline.
- Kogan et al. read in the author's manuscript version on the Rutgers site, not the journal copy.

## Sources

Ford and BPR
- Hammer 1990 transcription: https://studydaddy.com/attachment/123157/Hammer+BPR.pdf
- Reprint (blocked): https://folk.idi.ntnu.no/thomasos/paper/hammer_reengineering.pdf
- Hammer and Champy, 2001 ed.: https://repo.darmajaya.ac.id/4493/1/Michael%20Hammer_%20James%20Champy-Reengineering%20the%20corporation%20_%20a%20manifesto%20for%20business%20revolution-HarperBusiness%20(2001).pdf
- Book summary: https://sohailumar.wordpress.com/wp-content/uploads/2014/03/reengineering_the_corporation-clean.pdf
- strategy+business: https://www.strategy-business.com/article/19570
- Strassmann: https://www.strassmann.com/pubs/across/hocus-pocus.html
- Grint 1994: https://journals.sagepub.com/doi/10.1177/135050849400100116
- Jarvenpaa and Stoddard: https://ideas.repec.org/a/eee/jbrese/v41y1998i1p15-27.html

ERS and self-billing
- NC State: https://scm.ncsu.edu/scm-articles/article/what-is-evaluated-receipt-settlement
- Turner and Weickgenannt: https://www.oreilly.com/library/view/accounting-information-systems/9781118162309/c09-32.html
- Peeriosity 2013: https://www.peeriosity.com/shared-services/articles/2013/06/increasing-accounts-payable-efficiency-with-evaluated-receipts-settlement-ers/
- Peeriosity 2019: https://www.peeriosity.com/shared-services/articles/2019/05/using-evaluated-receipts-settlement-in-p2p/
- Soltec (Vendor): https://soltecinc.com/evaluated-receipts-settlement/
- AISI guideline: https://www.steel.org/steel-technology/steel-production/outside-processors/outside-processors-publications/aisi-op-council-evaluated-receipts-settlement-ers-process/
- Chrysler deck: https://www.yumpu.com/en/document/view/17276581/evaluated-receipt-settlement-ers-chrysler
- Oracle: https://docs.oracle.com/cd/A60725_05/html/comnls/us/po/tevlrec.htm
- SAP ERS: https://help.sap.com/saphelp_46c/helpdata/en/a8/b99804452b11d189430000e829fbbd/content.htm
- ERS tax task force: https://law-journals-books.vlex.com/vid/evaluated-receipts-settlement-ers-compliance-53818184
- Sales Tax Institute: https://www.salestaxinstitute.com/wp-content/uploads/dlm_uploads/2018/03/Best-Practices-for-Managing-a-Sales-Tax-Audit-0220.pdf
- HMRC: https://www.gov.uk/guidance/vat-self-billing-arrangements and https://gov.uk/hmrc-internal-manuals/vat-trader-records/vatrec15020
- Pay on production: https://en.wikipedia.org/wiki/Pay_on_production

Federal
- GAO/AIMD-21.3.2: https://www.gao.gov/assets/aimd-21.3.2.pdf
- FAR 13.4: https://www.acquisition.gov/far/subpart-13.4
- FAR 52.213-1: https://www.acquisition.gov/far/52.213-1
- RFO Part 32 deviation (GSA): https://login.acquisition.gov/sites/default/files/page_file_uploads/GSA_RFO_Deviation_Part-32.pdf
- 5 CFR 1315.6: https://www.law.cornell.edu/cfr/text/5/1315.6
- 31 USC 3521: https://www.law.cornell.edu/uscode/text/31/3521
- 31 USC 3352: https://www.law.cornell.edu/uscode/text/31/3352
- 31 USC 3561 history: https://law.justia.com/codes/us/2015/title-31/subtitle-iii/chapter-35/subchapter-vi/sec.-3561/
- GAO-26-108694: https://www.gao.gov/assets/gao-26-108694.pdf
- GAO-25-107753: https://www.gao.gov/products/gao-25-107753
- MOCAS: https://paymentaccuracy.gov/program/dow-commercial-pay-mechanization-of-contract-administration--94c59ea7
- DODIG-2021-024: https://www.oversight.gov/sites/default/files/oig-reports/DODIG-2021-024.pdf
- DoD OIG 08-096 (not retrieved): https://media.defense.gov/2008/May/20/2001712473/-1/-1/1/08-096.pdf
- GAO-16-394: https://www.gao.gov/products/GAO-16-394
- Green Book release: https://www.gao.gov/press-release/strengthening-accountability-federal-government-gao-issues-revisions-green-book

Cards
- GAO-17-276: https://www.gao.gov/products/gao-17-276
- GAO-08-333: https://www.gao.gov/assets/gao-08-333.pdf
- CRS R46106: https://www.congress.gov/crs-product/R46106
- Palmer et al.: https://files.eric.ed.gov/fulltext/EJ1204083.pdf
- American City and County: https://www.americancityandcounty.com/2007/09/01/charging-it/
- 12 CFR 1026.12: https://www.law.cornell.edu/cfr/text/12/1026.12
- 15 USC 1645: https://www.law.cornell.edu/uscode/text/15/1645
- Visa 13.1 (Vendor): https://chargebacks911.com/chargeback-reason-codes/visa/13-1-merchandise-services-not-received/
- JPMorgan (Vendor): https://www.jpmorgan.com/content/dam/jpm/commercial-banking/documents/commercial-card/fraud-management-commercial-cards.pdf

Audit and monitoring
- Vasarhelyi and Halper: https://raw.rutgers.edu/MiklosVasarhelyi/Resume%20Articles/CHAPTERS%20IN%20BOOKS/C05.%20the%20continuous%20audit%20of%20online%20systems.pdf
- Kogan et al.: https://raw.rutgers.edu/MiklosVasarhelyi/Resume%20Articles/MAJOR%20REFEREED%20ARTICLES/M73.%20Design_and_Ev%20Cont_Data_Level_Aud_System-05-18-2014-cleaned%20w%20title%20fin.pdf
- Jans et al.: https://files.fluxicon.com/Cases/Process-Mining-Field-Study-TAR.pdf
- Alles et al. 2008: https://www.researchgate.net/publication/251005680_Putting_Continuous_Auditing_Theory_into_Practice_Lessons_from_Two_Pilot_Implementations
- Siemens pilot: https://core.ac.uk/display/104870461
- Internal audit adoption: https://raw.rutgers.edu/docs/Previousprojects/p2a.1%20Techadoption%20jp%202%20EAA.pdf
- Protiviti: https://www.protiviti.com/sites/default/files/2022-09/internal-audit-data-analytics_e.pdf
- Predictive audit: https://ariasmontano.uhu.es/entities/publication/1f4755e4-c9a7-41cb-8216-975427797ea8/full
- AS 2201: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 (read at https://web.archive.org/web/2024/https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201)
- SAPA 11: https://pcaobus.org/standards/qanda/10-24-2013_sapa_11.pdf
- Data and reports Spotlight: https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/data-and-reports-spotlight.pdf?sfvrsn=4b2cb315_2
- PCAOB 2024-007: https://pcaobus.org/oversight/standards/implementation-resources-PCAOB-standards-rules/amendments-related-to-aspects-of-designing-and-performing-audit-procedures-that-involve-technology-assisted-analysis-of-information-in-electronic-form
- CAQ letter: https://www.thecaq.org/wp-content/uploads/2025/07/CAQ-_Letter-to-PCAOB_SIGNED_TAA_RFD_7.23.25.pdf
- GenAI Spotlight: https://pcaobus.org/documents/generative-ai-spotlight.pdf
- SEC 13(b): https://SEC.Gov/spotlight/fcpa/fcpa-recordkeeping.pdf
- 1983 paper: https://test.sechistorical.org/collection/papers/1980/1983_0603_FraudLevine_Part04.pdf
- COSO P10 reproduction: https://documentation.wazuh.com/4.14/compliance/tsc/common-criteria/cc5.1.html

Ledgers and e-invoicing
- Contour: https://www.ledgerinsights.com/contour-blockchain-trade-finance-network-shutter/
- TradeLens: https://piernext.portdebarcelona.cat/en/technology/the-closure-of-tradelens
- Marco Polo: https://www.fintechfutures.com/blockchain-crypto-digital-assets/blockchain-trade-finance-firm-marco-polo-reportedly-enters-insolvency
- IBM: https://www.coindesk.com/ibm-building-blockchain-dispute-resolution-system and https://cointelegraph.com/news/ibm-to-launch-one-of-the-largest-blockchain-implementations-in-the-world
- Sheldon: https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_2521111937
- Caldarelli: https://econpapers.repec.org/RePEc:gam:jjrfmx:v:18:y:2025:i:9:p:491-:d:1741252
- Dai and Vasarhelyi: https://cdecker.github.io/btcresearch/2017/dai2017towards.html
- OMB M-15-19: https://trumpwhitehouse.archives.gov/sites/whitehouse.gov/files/omb/memoranda/2015/m-15-19.pdf
- Treasury: https://fiscal.treasury.gov/financial-management-solutions/financial-innovation-transformation-fit/e-invoicing
- IPP white paper: https://www.ipp.gov/-/media/files/ipp/downloads/electronic-invoicing-why-it-matters-part1.pdf
- DBNAlliance (Vendor): https://edicomgroup.com/blog/the-united-states-begins-an-electronic-invoicing-pilot-project and https://www.storecove.com/blog/en/the-future-of-e-invoicing-in-the-u-s/
- Italy (Vendor): https://www.avalara.com/vatlive/en/country-guides/europe/italy/italy-sdi-real-time-e-invoices.html
- Mexico (Vendor): https://www.vertexinc.com/en-gb/node/8088
- Peru: https://www.imf.org/en/publications/wp/issues/2019/11/01/digitalization-to-improve-tax-compliance-evidence-from-vat-e-invoicing-in-peru-48672

Theory and sampling
- Vander Wiel and Vardeman: https://scilit.com/publications/5aafa28ba3ee06f9bc19a4b9e6041137
- Papadakis: https://scilit.com/publications/640d2b14aebfc1ea24790905a453ab7e
- Kaplan 1975: https://ideas.repec.org/a/bla/joares/v13y1975i2p311-337.html
- Variance literature: https://tsukuba.repo.nii.ac.jp/record/21204/files/1.pdf
- Cushing and Bodnar citations: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1911-3846.1987.tb00641.x
- Border and Sobel: https://feeds.library.caltech.edu/people/Border-K-C/monograph.json
- Elder et al.: https://www.econbiz.de/Record/audit-sampling-research-a-synthesis-and-implications-for-future-research-elder-randal/10009761279
- UCC 3-103 (Ohio): https://codes.ohio.gov/ohio-revised-code/section-1303.01/10-6-2026
- Vending Chattanooga discussion of Medford: https://hallapproved.com/il/cases/appeals/1988/2091386/
- Expense audit (Vendor): https://www.corpay.com/resources/blog/expense-audit and https://www.appzen.com/learn/how-to-audit-expense-reports-at-scale-with-agentic-ai
- BPI Challenge 2019: https://research.tue.nl/en/datasets/bpi-challenge-2019/

Market and practitioner (Vendor or practitioner)
- AccountingTools: https://www.accountingtools.com/articles/what-is-three-way-matching.html
- CFO Club: https://thecfoclub.com/operational-finance/3-way-matching-accounts-payable/
- Kognitos: https://www.kognitos.com/blog/two-way-vs-three-way-vs-four-way-match-when-to-use-each-2026/
- Dooap: https://www.dooap.com/blog/3-way-matching-with-machine-learning
- Blackbee: https://www.blackbeeai.com/blog/ai-invoice-validation
- PredictAP: https://blog.predictap.com/gaming-the-agent-why-ai-invoice-approval-still-needs-an-independent-human-control
- RedHub: https://blog.redhub.ai/ai-invoice-matching
- Stampli: https://www.stampli.com/resources/non-po-invoice-processing/
- Corpay on Ardent: https://www.corpay.com/resources/blog/ap-team-productivity-benchmarks
- AFP 2025: https://www.financialprofessionals.org/about/learn-more/press-releases/Details/survey-79-percent-of-organizations-were-victims-of-attempted-or-actual-payments-fraud-activity-in-2024
- ACFE 2024: https://legacy.acfe.com/report-to-the-nations/2024/
