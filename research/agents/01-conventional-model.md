# 01. The conventional three-way match: how it operates, where it came from, what is required, what the numbers show

Research line 01. Reconstruction only: this file does not evaluate whether the process should change. Retrieved 2026-11-04.

Tags: **[E]** Established (primary text or original data read). **[S]** Supported hypothesis (evidence points this way, not conclusive). **[Sp]** Speculative. **[R]** Rejected. Vendor material is labelled and never used as a benchmark.

## 0. Bottom line

1. **No US statute, SEC rule, PCAOB standard or UCC section found here names the three-way match.** [E for the texts read; COSO 2013 full text could not be read, see Gaps.] What the law requires is outcome language: books that "accurately and fairly reflect" transactions, controls giving "reasonable assurances", expenditures only as authorized. The match is the customary way of meeting that outcome. The nearest thing to a legal mandate is federal agency disbursing, which applies to agencies paying vendors, not to companies.
2. **The practice is much older than the name, and older than the audit rationale usually given for it.** The three-document logic is in railway supply manuals by 1887 and in audit texts by 1912. The exact trio "invoices, purchase orders and receiving reports" as a clerk's job is in print in 1949. The phrase "three-way match" is confirmed in software advertising from 1977. It predates SOX by decades, so SOX did not create it. [E]
3. **The early auditors valued the receiving record partly for a different reason than overpayment:** finding liabilities that were not on the books. Both purposes are documented in Montgomery 1912. [E]
4. **Payment obligation under UCC Article 2 turns on acceptance of goods, not on an invoice.** The invoice is not what creates the debt. [E]
5. **The conflicting Ardent figures resolve.** 18.4% is the all-respondent average, 2025 survey. 22% is the "All Others" group (excluding Best-in-Class), 2024 survey, not an average. 14% is the printed all-respondent average of that same 2024 survey, and it cannot be squared with its own subgroups. Details in 5.2. None of them measures three-way match failure: Ardent's "exception" includes coding errors and approval bottlenecks.
6. **The split between genuine error and harmless mismatch: no study found measures it directly across companies, and no dollar split exists in public.** The best proxy is an original tabulation of a real purchase-to-pay log (one Dutch-based multinational, 2018, section 5.7): 26.5% of invoiced three-way items had a payment block; about 80% of those blocks show no document correction and about 7% show the invoice corrected. Suggestive, one company, not a benchmark.

## 1. What it is called

Three-way match, 3-way match, three-way matching, PO/receipt/invoice matching. In software: "Logistics Invoice Verification" (SAP), "match approval level" with 2-way, 3-way and 4-way (Oracle). In older usage: voucher audit, vouching, invoice audit, "O.K." of invoices. In US federal usage: voucher examination, prepayment examination. [E] Sources: [Oracle Payables, two-, three- and four-way matching](https://docs.oracle.com/cd/A60725_05/html/comnls/us/ap/point04.htm); [GAO Title 7](https://www.gao.gov/assets/a76199.html).

Variants [E]: two-way compares PO and invoice. Three-way adds receipt. Four-way adds inspection or acceptance. Oracle sets the level per PO shipment through "receipt required" and "inspection required" flags. SAP's GR-based invoice verification ties each invoice line to a specific goods receipt rather than to the PO total.

## 2. The business problem

**Stated purpose in the historical record.** Montgomery (1912, p. 83) describes the system of internal check as handling goods so as "to insure all goods paid for being actually received". [E] [Montgomery 1912](https://archive.org/stream/cu31924030163251/cu31924030163251_djvu.txt)

**Why the problem exists.** [S] Delegation and distance. Once the person who orders, the person who takes delivery and the person who pays are different people, no one person knows all three facts. Paying on the seller's own statement means trusting the party who benefits. The 1949 American Institute of Accountants report gives this logic directly: firm size means executive management "can no longer exercise personal supervision over the conduct of operations". [E] [AIA 1949](https://egrove.olemiss.edu/aicpa_comm/103) The railways are the first well-documented case because they bought huge volumes at remote points. Kirkman (1887) warns that receipt at remote points is where "imposition is much more likely to be practiced". [E]

**The problems it is meant to address, separated:**

| Problem | Does the match address it? | Tag |
|---|---|---|
| Paying for goods never received | Yes, its core purpose | E (1912 text) |
| Paying more than agreed price | Yes, via PO price | E (1912 rule: price approved by authorizer) |
| Paying for something unauthorized | Yes, if the PO itself was validly approved | S |
| Unrecorded liabilities and cut-off | Yes, this is what the 1912 audit text uses receiving records for | E |
| Paying the same invoice twice | Only partly. Kirkman says his stub notations "may be made aids to prevent duplication of invoices" (1887). In modern systems this is a separate duplicate check | E/S |
| Paying a fraudster's bank account | No. The match compares what and how much, not who gets paid. See vendor imposter data in 5.6 | S |
| Collusion between employee and vendor | Weakly. Kirkman doubted it in 1887. Kid Brands reported collusion defeating the match in 2012 | E |
| Forged documents | No. McKesson & Robbins | S |

## 3. How it really operates

### 3.1 Inputs, outputs, activities

**Inputs.** Approved PO (vendor, item, quantity, price, terms, account). Goods receipt or service entry. Supplier invoice. Vendor master record. Tolerance configuration. Authority matrix. Tax determination data. [E: Oracle and SAP documentation; S as to generality]

**Outputs.** Invoice posted and released for payment, or blocked. Liability recorded (often first as a goods-received-not-invoiced accrual, then cleared by the invoice). Price or quantity variance posting. Debit memo or vendor dispute. Audit evidence. [S]

**Activities.** Capture invoice. Identify PO. Compare price and quantity by line. Apply tolerance. Block or post. Route the exception. Resolve it. Release. Schedule payment by terms. Pay. Clear.

### 3.2 Conventional process map

Handoffs marked with `>>`. Decisions marked with `D`.

| # | Step | Owner | System | Decision or handoff |
|---|---|---|---|---|
| 1 | Need raised, requisition created | Requester | ERP or procurement suite | |
| 2 | Requisition approved | Budget owner per authority matrix | Workflow | **D1** approve, reject, return. Basis: budget, policy, delegation of authority |
| 3 | PO issued | Buyer | ERP | **D2** vendor, price, terms. `>>` vendor |
| 4 | Vendor acknowledges and ships | Vendor | Vendor system, EDI | `>>` receiving dock |
| 5 | Goods received, counted, inspected, posted | Receiving or requester (services: service entry by requester) | WMS or ERP | **D3** accept, reject, partial. Accrual posted. `>>` AP, through the system |
| 6 | Invoice received and captured | AP or shared services | Portal, EDI, OCR, AP automation | Duplicate check. `>>` matching |
| 7 | Match run line by line: PO vs receipt vs invoice | System | ERP | **D4** within tolerance? Yes goes to 12. No goes to 8 |
| 8 | Invoice blocked or held, reason code set | System | ERP | Payment stopped; supplier clock keeps running |
| 9 | Exception triaged | AP clerk | Workqueue, email | **D5** classify: price, quantity, no receipt, no PO, tax, freight, duplicate. `>>` buyer, receiver or requester |
| 10 | Root cause checked | Buyer (price), receiver or requester (quantity), vendor | Email, phone, ERP | **D6** who is right? Options: change PO, post late receipt, ask for credit, short pay, accept variance |
| 11 | Exception resolved and block released | AP, with buyer or manager approval above limits | ERP | **D7** release, or reject back to vendor. Some blocks release automatically when the cause disappears (for example, a late receipt) |
| 12 | Invoice posted, due date set | System | ERP | Non-PO invoices go through coding and approval here instead |
| 13 | Payment proposal run and reviewed | AP or treasury | ERP, bank | **D8** pay, hold, take discount. Second approval on the file |
| 14 | Payment released | Treasury | Bank | `>>` bank. Segregated from vendor master maintenance |
| 15 | Clear, reconcile, report | AP, GL | ERP | GR/IR clearing, accrual, audit sample |

Steps 7 to 8 use real configuration: Oracle "places a matching hold on the invoice" and "You must release the hold before you can pay the invoice", with tolerances by quantity or amount in percent or value ([Oracle](https://docs.oracle.com/cd/A60725_05/html/comnls/us/ap/pomatc04.htm), [Oracle Cloud tolerances](https://docs.oracle.com/en/cloud/saas/financials/24a/fappp/invoice-tolerances.html)). Oracle also lets users manually release certain holds without resolving the matching error ([Oracle Cloud](https://docs.oracle.com/en/cloud/saas/financials/24b/fappp/how-invoices-are-validated.html)). SAP's MRBR re-checks blocked items and can release them automatically where the blocking reason has gone ([SAP help](https://help.sap.com/saphelp_46c/helpdata/en/f5/24e57911b011d383750000e8a5eb64/content.htm)). [E]

### 3.3 Who decides and with what information

| Decision | Who | Knows | Does not usually know |
|---|---|---|---|
| D4 match | System | Three data sets and tolerance | Whether any of the three is right. It compares records, not reality |
| D5 triage | AP clerk | Documents, reason code, payment history | Commercial context, side agreements, whether goods are usable |
| D6 who is right | Buyer | Contract, negotiated price, recent emails | Current dock status |
| D6 quantity | Receiver or requester | What arrived | Price, contract terms |
| D7 release | AP lead or manager | Clerk's note and threshold | Usually relies on others' assertions |
| D8 pay | Treasury | Cash, terms, proposal total | Line-level match history |

Tag [S]. Built from the process logic and software documentation. No ethnographic or time-and-motion study of these decisions was found. The structural point is [E] by 1949: AIA divides the facts among purchasing, receiving and accounting, and accounting approves "based on the documentary support received from the other departments". The final approver sees evidence about the goods, not the goods.

### 3.4 Systems

ERP (SAP, Oracle, Workday, Dynamics, NetSuite); procurement suites; AP automation and OCR; EDI and e-invoicing networks; warehouse systems; bank portals; tax engines; workflow and email (where much resolution actually happens [S]); after-the-fact tools for duplicate checks and recovery audit.

### 3.5 Common exceptions and failures

Categories below recur across sources, but **no original survey with percentages for root causes was found** (IOFM, Levvel, PayStream and Aberdeen originals not located; the results were vendor blogs, which disagree on which cause leads). [E that the gap exists] The BPI log in 5.7 gives counts for one company.

- Timing: invoice arrives before receipt is posted. Invoice is right, record is late. Not an error in the commercial sense. [S]
- Price: PO not updated after a negotiated change, or genuine overcharge. [S]
- Quantity: partial shipment, over-shipment, unit-of-measure mismatch. [S]
- Missing PO or wrong PO number. [S]
- Freight, tax and fees not on the PO. [S, vendor labelled]
- Services: no physical receipt, so receipt is a requester's click. BIA's manual treats the receiving report as "the program office approval", which shows how a receipt turns into an approval. [E] [27 IAM 11](https://www.bia.gov/sites/default/files/dup/assets/public/raca/manual/pdf/27-iam-11_ap-2-way-and-3-way-match_final_signed_508.pdf)

Control failures reported by real issuers (10-K text, [E]):

| Filer, filing year | What it said |
|---|---|
| [Footstar, 2005](https://www.sec.gov/Archives/edgar/data/1011308/000095012305004248/y07291e10vk.txt) | "Controls over the three-way match of vendor purchase orders, receiving reports and invoices were not consistently effective" |
| [California Micro Devices, 2005](https://www.sec.gov/Archives/edgar/data/800460/000119312505125296/d10k.htm) | Expected to implement a three-way match in Oracle; manual checks in the interim |
| [MGP Ingredients, 2005](https://www.sec.gov/Archives/edgar/data/835011/000110465905043521/a05-15903_110k.htm) | New ERP to perform a 3-way match before generating payment |
| [Design Within Reach, 2006](https://www.sec.gov/Archives/edgar/data/1116755/000119312506080434/d10k.htm) | Policy to ensure "proper three-way matching of non-merchandise documents or adequate support" |
| [Intcomex, 2009](https://www.sec.gov/Archives/edgar/data/1359425/000119312509067467/d10k.htm) | Failure to verify procedures supporting three-way matching, at a foreign entity |
| [Kid Brands, 2012](https://www.sec.gov/Archives/edgar/data/739878/000119312512142447/d282162d10k.htm) | "former LaJobi management collusion and override... the accounts payable 3-way match failed" |
| [Karat Packaging, 2023](https://www.sec.gov/Archives/edgar/data/1758021/000162828023008299/krt-20221231.htm) | Remediation includes performance of the three-way match |
| [DXP Enterprises, 2024](https://www.sec.gov/Archives/edgar/data/1020710/000102071024000026/dxpe-20231231.htm) | Remediated weakness over "timely clearing of discrepancies arising from the three-way-match process" |

Note what DXP shows: the weakness was in clearing the discrepancies, not in the comparison. This shows the match sometimes appears as a key control in ICFR, in the eyes of the issuer, but says nothing about whether it had to.

### 3.6 Measures of success

Typical: first-time match rate, exception rate, touchless or straight-through rate, cost per invoice, cycle time, invoices per FTE, on-time payment, discount capture, duplicate or erroneous payment rate, PO coverage, GR/IR ageing, audit deficiencies. Hackett's tracked set is reported as invoice cycle time, first-pass match, on-time payment, DPO and cost per invoice ([SharedServicesLink, secondary](https://sharedserviceslink.com/article/p2p-performance-metrics-from-the-hackett-group)).

Note [S]: almost all of these measure the process's own throughput. None of the standard benchmarks reports dollars of loss prevented by the match. That gap is why section 5.7 is hard.

## 4. History

### 4.1 Timeline

**1887. Kirkman, *The Handling of Railway Supplies*.** [E] [Full text](https://archive.org/stream/handlingrailway00kirkgoog/handlingrailway00kirkgoog_djvu.txt). Marshall Kirkman, a Chicago and North Western officer, sets out requisition, stub or copy of requisition, receipt and inspection, invoice, voucher. Key passages (pp. 75 to 77, 190):
- "Discrepancies are more likely to be noticed, and accurate account taken, if goods are compared with the invoice as received"
- "Invoices should never be receipted without reference to the stub or copy"
- Stub notations "may be made aids to prevent duplication of invoices"
- "Upon receipt of invoices, they must be compared with requisitions to see that orders have been properly filled"
- "These invoices, and all reports upon which payments are based, should afterwards be carefully labeled and filed away for convenient reference or should be attached to the voucher upon which payment is made"

So the three-document logic (order record, receipt, invoice) feeding a payment voucher exists by 1887, in operations management, not audit. Two differences from today. The invoice was meant to arrive first and serve as the count sheet ("invoices should precede delivery"), which is the reverse of a blind independent receipt. And Kirkman was already sceptical that comparing a count to the invoice stops collusion: "One purpose of this practice is to prevent collusion, though it is not quite apparent how this object is accomplished."

This is the earliest text I found. It is likely not the earliest practice. [S]

**1912. Montgomery, *Auditing Theory and Practice*.** [E] [Full text](https://archive.org/stream/cu31924030163251/cu31924030163251_djvu.txt). The system of internal check is laid out, and the list of points includes this rule (following p. 83): "All goods purchased or expenses incurred shall be evidenced by an invoice from the vendor or creditor. Such invoices shall be checked as to extensions and additions, shall be duly approved as to quantity and quality by the persons receiving the goods, and as to price by the person authorizing the purchase. They shall then be approved for payment by the executive in charge of the accounting department and turned over to the treasurer for payment."

That is the modern control in one paragraph: receipt attests quantity, the authorizer attests price, accounting approves, treasury pays. Also:
- p. 151: "Most concerns keep order and receiving records of some description. The auditor should compare the entries in this record... with the purchase journal or voucher record to ascertain if the purchases indicated are entered." The concern is invoices "suppressed", meaning understated liabilities.
- Asks whether receiving clerks "keep an independent record of all goods received irrespective of invoices". This is the origin in print, in this search, of independent receiving.
- Refers to "checking invoices against order and receiving records".
- Speed pressure was present at once: department stores want "invoices approved as quickly after receipt thereof as possible, so that the discount day may not pass".

**1917. Griffith, *Corporation Accounts and Voucher System*.** [E] [Full text](https://archive.org/stream/corporationacco01socigoog/corporationacco01socigoog_djvu.txt). Invoice held in a pending file. "When the goods have been received, which will be attested by a report in some form by the receiving clerk, the invoice is O. K'd for quantities and prices by the buyer, and extensions are checked by the auditor or chief accountant." And "Vouchers should never be made for invoices in dispute". That is the manual ancestor of the payment block.

**1938 to 1939. McKesson & Robbins.** [S, secondary plus an AIA memo summarized from search, not read in full] Fictitious inventory and receivables were backed by [purchase orders, invoices and shipping advices](https://www.sechistorical.org/collection/papers/1930/1939_0304_AIAMcKesson.pdf). The documents agreed with each other because the fraudsters wrote all of them. The profession's response was physical observation and confirmation, not better document comparison. It is a demonstration, 85 years old, that document agreement is evidence of consistency, not of truth.

**1949. AIA, *Internal Control* special report.** [E] [eGrove](https://egrove.olemiss.edu/aicpa_comm/103). Definition: "Internal control comprises the plan of organization and all of the coordinate methods and measures adopted within a business to safeguard its assets, check the accuracy and reliability of its accounting data, promote operational efficiency, and encourage adherence to prescribed managerial policies" (end of quote reconstructed from the extraction, which cut off at "prescribed managerial p"). Purchasing example:
- "The responsibility for the receipt of the merchandise, its examination as to quantity and quality and comparison with the purchase order, notation of defects or shortages, and the transmission to stores rests with the receiving department."
- "The setting up of the liability, recording of the transaction, and approval for payment of the vendor's invoice based on the documentary support received from the other departments is an accounting department function."
- "Responsible to him may be another clerk whose job is to match invoices, purchase orders and receiving reports."

This is the earliest wording I found of the exact trio with the word "match". [E for the text; "earliest" is limited to this search.]

**1964 lead, unverified.** A Google Books snippet from *Journal of Data Management* (1964) on large-scale accounts payable shows "receiving memo" and then "three -" cut off. Could be an early computer-era use. Not confirmed.

**1977. Term confirmed.** *Computerworld*, 28 Feb 1977, p. 58, advertisement for a purchase order system: "Three-way match between invoice, receiver and P.O." Repeated in 1977 and 1978 issues. [E from Google Books snippets.] Also Informatics' Purchase Order Commitment Module (*Computerworld*, 3 Jul 1978) and Edds, *Management Auditing* (1980, p. 343): "three-way match-up of documents". Google Books also lists hits dated 1920 and 1941, but those are serial volumes with unreliable dates and I discount them. [S] Google Ngram shows "three-way match" low until about 1990 and rising to 2010, but it is contaminated by sports use. Inference [S]: the name came with computerized AP in the 1970s, when a manual clerk task became a named software feature. Earliest confirmed date is 1977, not necessarily the origin.

**1977. FCPA.** Created Exchange Act 13(b)(2), the internal accounting controls requirement. Named no specific control. [E]

**1990. Hammer, "Reengineering Work: Don't Automate, Obliterate" (HBR).** Ford's North American AP employed more than 500 people; Mazda's about 5. Ford introduced "invoiceless processing" and asked vendors not to send invoices. Later summaries say matching fell from 14 items to 3 and headcount fell about 75%. [S: article body seen only through search excerpts; the 14-item and 75% figures are from secondary summaries.] Relevant here as historical evidence that a large company ran without the invoice leg over 35 years ago. Evaluation belongs to other lines.

**1990s onward. ERP.** Oracle's 2-, 3- and 4-way levels, holds and tolerances; SAP Logistics Invoice Verification, tolerance keys, MRBR. Evaluated Receipt Settlement is in SAP 4.6C documentation ([SAP](https://help.sap.com/saphelp_46c/helpdata/en/a8/b99804452b11d189430000e829fbbd/content.htm)). IOFM credits Ford, via Mazda, with bringing ERS to the US (single source, unverified).

**2002 to 2007. SOX, AS 2, AS 5, SEC guidance.** See section 4.3. The evidence supports SOX having raised the documentation and testing around the match, as the 2005 to 2006 filings suggest. It did not originate it. [S]

### 4.2 Why each element exists

| Element | Earliest evidence found | Purpose in that evidence | How solid |
|---|---|---|---|
| Requisition, PO | Kirkman 1887 (requisition and stub); Montgomery 1912 ("purchase orders issued") | Prove the order was authorized and record what was ordered | Good for railways. Thin for the wider economy. No study found of when PO forms became general |
| Receiving report | Kirkman 1887 (inspection and tally); Montgomery 1912 (independent record) | Prove goods arrived. Also find unrecorded liabilities | Good |
| Invoice | Far older than this process. Kirkman treats it as the count sheet, Montgomery as evidence of the purchase | Seller's claim and the voucher support | Good for role; origin of the invoice itself not researched |
| Voucher, approver | Kirkman 1887; Montgomery 1912; Griffith 1917 | One responsible signature on assembled evidence; separates approval from cash | Good |
| Segregation | Montgomery 1912 ("no part of the accounts will be under the absolute and independent control of any one person"); AIA 1949 | Stop one person controlling a whole transaction | Good |
| Block or hold | Griffith 1917 (no voucher for disputed invoices; invoices held pending goods) | Stop payment until resolved | Moderate. The word "block" is ERP vocabulary; the behaviour is old |
| Tolerance | **Not found before ERP-era documentation.** Closest: Montgomery's remark that a practice with "a few items of small amount only... is not worth condemning" | Presumed: cost of chasing small differences exceeds their value; trade norms on over-shipment | **Thin.** The familiar explanation is plausible but I found no historical document stating it. [Sp] as to origin |

**The familiar story rejected in part.** "Three-way match exists because of SOX" is **[R]**. "It exists mainly to detect fraud" is **[S at best]**: the earliest sources stress accuracy, shortage and clerical error as much as dishonesty, and Kirkman doubted the anti-collusion effect. Thin spots: nothing located before 1887; no accounting-history paper devoted to document matching was found; the Mazda/Ford account is largely secondary; the origin of tolerances is unknown.

### 4.3 Legally or professionally required versus custom

Read as: does this text name the three-way match? Does it require the function?

| Source | Names it? | What it actually says | Binding on a US public company? |
|---|---|---|---|
| [Exchange Act 13(b)(2)(A)](https://www.law.cornell.edu/uscode/text/15/78m) | No | "make and keep books, records, and accounts, which, in reasonable detail, accurately and fairly reflect the transactions and dispositions of the assets of the issuer" | Yes |
| 13(b)(2)(B) | No | "devise and maintain a system of internal accounting controls sufficient to provide reasonable assurances that" transactions are authorized, recorded, and so on | Yes |
| 13(b)(7) | No | Standard is what "would satisfy prudent officials in the conduct of their own affairs" | Yes |
| [SOX 302](https://www.law.cornell.edu/uscode/text/15/7241) | No | Officers "are responsible for establishing and maintaining internal controls" and disclose deficiencies | Yes |
| [SOX 404](https://www.law.cornell.edu/uscode/text/15/7262) | No | Management must state its responsibility for "an adequate internal control structure and procedures for financial reporting"; auditor attests (not emerging growth companies) | Yes |
| [Rule 13a-15(f)](https://www.law.cornell.edu/cfr/text/17/240.13a-15) | No | Reasonable assurance that "receipts and expenditures of the issuer are being made only in accordance with authorizations of management and directors"; and "prevention or timely detection of unauthorized acquisition, use or disposition of the issuer's assets that could have a material effect on the financial statements" | Yes |
| [SEC 33-8810 (2007)](https://www.govinfo.gov/content/pkg/FR-2007-06-27/html/E7-12299.htm) | No | "does not require management to identify every control in a process"; "not intended to explain how management should design its ICFR"; "does not provide a checklist of steps"; warns against "one-size fits all". Footnote 34 gives "application controls that perform automated matching" as an example of a control type | Interpretive guidance, with a safe harbor |
| [PCAOB AS 5, now AS 2201](https://www.sec.gov/rules/pcaob/2007/34-55876.pdf) | No. "invoice", "purchase order", "matching" and "three-way" each appear zero times in the filed text of the release | ¶39: "The auditor should test those controls that are important to the auditor's conclusion about whether the company's controls sufficiently address the assessed risk of misstatement to each relevant assertion." ¶40: "There might be more than one control that addresses the assessed risk... It is neither necessary to test all controls related to a relevant assertion nor necessary to test redundant controls". A7: material weakness requires "a reasonable possibility that a material misstatement" will not be prevented or detected | Binds auditors. Live AS 2201 page blocked; text read from the 2007 SEC filing. Paragraph numbers carried into AS 2201 but check any later amendment |
| COSO 2013 | Not confirmed | Secondary sources show "verifications" and "reconciliations" among control activity types ([Deloitte](https://www.deloitte.com/ng/en/services/audit/perspectives/coso-control-activities.html)). COSO is a framework companies choose; Rule 13a-15(c) requires a "suitable, recognized control framework", not COSO by name | Indirect. **Full text not read** |
| [Treas. Reg. 1.6001-1(a)](https://www.law.cornell.edu/cfr/text/26/1.6001-1) | No | "such permanent books of account or records, including inventories, as are sufficient to establish the amount of gross income, deductions..." | Yes. IRS: "You may choose any recordkeeping system suited to your business" ([IRS](https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep)) |
| [Rev. Proc. 98-25](https://www.eitc.irs.gov/pub/irs-drop/rp-98-25.pdf) | No | Machine records need transaction detail so that "source documents" can be identified | Yes, if in scope. Requires traceability, not comparison before payment |
| [34 TAC 3.281 (Texas)](https://www.law.cornell.edu/regulations/texas/34-Tex-Admin-Code-SS-3-281); [Cal. Reg. 1698](https://www.cdtfa.ca.gov/lawguides/vol1/sutr/1698.html) | No | Records reflecting purchases, with invoices as examples. California keeps them four years. [Texas 2000 letter](https://ezel.ai/tax-rulings/tx/200007522l-electronic-storage-and-retention-of-records-source-documents-invoices): a purchase card summary without item, rate and jurisdiction detail fails | Yes, state by state. Two states sampled only. This is an argument for retaining invoice-grade detail, not for matching |
| [Prompt Payment Act, 31 USC 3901 ff.](https://www.law.cornell.edu/uscode/text/31/3903) | No | Binds federal agencies as payers. 30 days after proper invoice if no contract date. Improper invoice returned within 7 days | **No, unless the company is being paid by the government** |
| [FAR 32.905](https://www.acquisition.gov/far/32.905), [52.232-25](https://www.law.cornell.edu/cfr/text/48/52.232-25), [5 CFR 1315.9](https://www.law.cornell.edu/cfr/text/5/1315.9) | No | "Payment will be based on receipt of a proper invoice and satisfactory contract performance." Due date is the later of two events: proper invoice or acceptance. Lists required contents of contract, invoice and receiving report | Binds agencies. Closest legal text to the three documents |
| [GAO Title 7](https://www.gao.gov/assets/a76199.html) | No, but describes the function | §6.2.B basic payment documents: purchase orders, contracts, receiving reports, invoices. §7.3 "ensuring the consistency of information from invoices, obligating documents, and receiving reports." §7.4.D fast pay may allow paying "without evidence of receipt at the time of certification and payment" | Federal agencies only. Note the built-in exception |
| [31 USC 3528](https://www.govinfo.gov/link/uscode/31/3528) | No | Certifying officers personally liable ([Treasury job aid](https://www.fiscal.treasury.gov/training/cot/documents/JobAid1_LegalProperCorrect.pdf)) | Federal only. There is no private sector equivalent found |
| [BIA 27 IAM 11](https://www.bia.gov/sites/default/files/dup/assets/public/raca/manual/pdf/27-iam-11_ap-2-way-and-3-way-match_final_signed_508.pdf) | **Yes** | "A 3-way match is required" for covered contract payments; 2-way for miscellaneous | Agency policy, not law. It is the only official text found that requires the match by name |

**Filings search.** EDGAR full text search, 2001 onward, 10-K family incl. exhibits, run 2026-11-04: "three-way match" 36 documents, "three-way matching" 26, "3-way match" 6, "3-way matching" 2. Some are contract exhibits or sales-side uses (Liquidmetal, Karat's sales match), so the term is rare in public disclosure. Absence in filings does not show absence in practice. [E for counts]

**UCC Article 2. When does payment become owed, and what does the invoice do?** [E for text; state enactments vary; applies to goods, not services]

- [§2-301](https://www.law.cornell.edu/ucc/2/2-301): "The obligation of the seller is to transfer and deliver and that of the buyer is to accept and pay in accordance with the contract."
- [§2-310(a)](https://www.law.cornell.edu/ucc/2/2-310): unless otherwise agreed, "payment is due at the time and place at which the buyer is to receive the goods".
- [§2-513(1)](https://www.law.cornell.edu/ucc/2/2-513): buyer "has a right before payment or acceptance to inspect them", unless agreed otherwise. Not available for C.O.D. or payment against documents.
- [§2-606(1)](https://www.law.cornell.edu/ucc/2/2-606): acceptance occurs when the buyer signifies conformity after a reasonable opportunity to inspect, or "fails to make an effective rejection", or acts inconsistently with the seller's ownership.
- [§2-607(1)](https://www.law.cornell.edu/ucc/2/2-607): "The buyer must pay at the contract rate for any goods accepted." §2-607(3)(a): buyer must notify of breach within a reasonable time "or be barred from any remedy".
- [§2-709](https://www.law.cornell.edu/ucc/2/2-709): seller may sue for the price of goods accepted.
- [§2-717](https://www.law.cornell.edu/ucc/2/2-717): buyer "on notifying the seller of his intention to do so may deduct all or any part of the damages" from the price due under the same contract.
- **Invoice:** §2-310(d) gives its one direct effect here: "the credit period runs from the time of shipment but post-dating the invoice or delaying its dispatch will correspondingly delay the starting of the credit period". Between merchants a writing in confirmation can satisfy the statute of frauds unless objected to within 10 days ([§2-201(2)](https://www.law.cornell.edu/ucc/2/2-201)), and terms on it can be tested as additional terms under [§2-207](https://www.law.cornell.edu/ucc/2/2-207). [S that invoices commonly fall in these provisions; case law not reviewed.]

So [E]: **under the default rules the debt arises from contract plus acceptance. The invoice is a demand and a data carrier, and may start a credit period, but it does not create the obligation.** Parties can contract otherwise, and most credit terms are keyed to invoice date or receipt. A pending block does not by itself suspend a debt on accepted goods. The UCC gives the buyer inspection, rejection, notice and set-off, not a right to withhold for an unresolved internal match. [S, my reading of the text; case law not reviewed.] An internal block also does not stop acceptance: failing to reject after a reasonable opportunity to inspect is acceptance under §2-606(1)(b).

**Accounting consequence.** [S] Liability recognition follows receipt, which is why ERP systems post GR/IR at goods receipt. This agrees with the old audit concern for unrecorded liabilities. ASC text not read for this line.

**Summary of required versus custom.**

| Layer | Status |
|---|---|
| Accurate books, authorized spending, safeguarding, ICFR assessment | Law [E] |
| Keep records adequate for tax | Law [E] |
| Some control addressing existence, accuracy, authorization and cut-off of payables | Effectively required for a SOX filer, through the above. Which one is a management choice [S] |
| Three documents compared before payment | **Custom and professional convention.** Mandatory by name only in an agency manual found here [E] |
| Tolerances, blocks, 2-way versus 3-way, thresholds | Configuration and management judgment. No authority found [E for texts read] |
| Once designated a key control in a SOX program | It must then operate and be tested. A failure can become a reportable deficiency, as filings show [E]. This is the practical source of the feeling that the match is mandatory [S] |

Government contractor note: agencies' payment rules do not flow directly to a company's own AP. Separate accounting-system and purchasing-system rules (for example DFARS business-systems clauses) may apply to contractors; not read. See Gaps.

Non-US: VAT regimes make a valid invoice central to input tax deduction, which affects the invoice leg outside the US. Not researched here. [S]

## 5. Numbers

Read every figure below with its measure. Most of them are self-reported surveys.

### 5.1 Adoption

There is **no census of how many US public companies use a three-way match.**

| Figure | Source, year, sample | What it measures |
|---|---|---|
| 61% and 62% | [Ardent State of ePayables 2025](https://d15fjz85703yz4.cloudfront.net/1517/5157/1685/Ardent_Partners_-_State_of_ePayables_2025_-_Bottomline_-_FINAL.pdf), Mar to May 2025, n=204, 58% N. America, 54% over $1B, sponsored by Bottomline | Share with "two or three-way matching capabilities", by two groups (column labels inferred as All Others and Best-in-Class). Two and three combined |
| 65.4% (84.0% BIC, 47.3% others) | Same | Invoices linked to a PO |
| 88.0% median | [APQC 102136](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/percentage-invoice-line-items-matched), n=1,735 | Invoice lines matched with a PO |
| 85.0% median | [APQC 107992](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/percentage-supplier-invoices-matched), n=1,170 | Supplier invoices matched with PO |
| 6.0% median | [APQC 105902](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/percentage-invoice-line-items-0), n=1,346 | Lines approved by "evaluated (automatic) receipt settlement", which APQC glosses as online matching. Note this differs from the usual meaning of ERS |

APQC pages read live on 2026-11-04; values and n change as data accrue. APQC's samples are cumulative, self-reported, mixed-size organizations, with no stated year on the public page. The 25th and 75th percentile values are not public.

### 5.2 Ardent exception rates: resolved

All Ardent reports are sponsored web surveys of self-selecting AP leaders. Best-in-Class (BIC) is the top 20% by cost and cycle time, so comparing BIC to others on those metrics is partly circular.

| Report | Fieldwork, n | Average | BIC | All Others | Verified in |
|---|---|---|---|---|---|
| Study cited 2015 | Not known | 17.2% | 9.8% | | [Esker eBook](https://www.esker.com/sites/default/files/content/021_Esker_eBook_AP_Analytics-US.pdf), secondary, not opened |
| AP Metrics that Matter 2023 | Not checked | 22.5% | | | [PDF](https://tradeshift.com/wp-content/uploads/2023/02/ArdentPartners-AP-MTM2023-Tradeshift-FINAL.pdf) |
| AP Metrics that Matter 2024 | Mar to May 2023, n=190 | 20.7% | 11.1% | "60% lower" | [PDF](https://tradeshift.com/wp-content/uploads/2024/05/Ardent-Partners-AP-Metrics-that-Matter-in-2024-Tradeshift.pdf) |
| AP Metrics that Matter 2025 and State of ePayables 2024 | Mar to May 2024, n=212 | **14%** | 9.0% | **22.0%** | [PDF, Corcentric copy](https://corcentric-corpsite.s3.dualstack.us-east-1.amazonaws.com/pdfs/ap-metrics-that-matter-2025.pdf), pp. 17, 26 |
| State of ePayables 2025 | Mar to May 2025, n=204 | **18.4%** | 11.1% | 20.9% | [PDF](https://d15fjz85703yz4.cloudfront.net/1517/5157/1685/Ardent_Partners_-_State_of_ePayables_2025_-_Bottomline_-_FINAL.pdf), Tables 1, 2 |
| AP Metrics that Matter 2026 | n=194 | 19.9% | 11.8% | | [Medius summary](https://www.medius.com/resources/guides-reports/ardent-partners-accounts-payable-metrics-that-matter/), sponsor page; [Ardent](https://payablesplace.ardentpartners.com/2026/08/ap-metrics-that-matter-in-2026-the-state-of-ap/) confirms n only |

Resolution [E unless marked]:
- **18.4%** is the all-respondent average from the 2025 survey.
- **22%** is not an average. It is the All Others group from the 2024 survey. Vendors quote it as the "other organizations" number, correctly, and blogs then treat it as market average, wrongly.
- **14%** is real in that Ardent printed it: "Invoice exception rates have dropped dramatically to 14% in 2024." It is the all-respondent average of the same survey that gave 9% and 22%.
- **The 14% does not fit its own subgroups.** [my arithmetic] If BIC are 20% of respondents, 9% and 22% average to 19.4%. To get 14%, BIC would have to be about 62% of the sample. The 2025 survey fits far better: 11.1% and 20.9% give 18.9% against 18.4% reported. The 14% also sits alone in a series of 22.5, 20.7, 14, 18.4, 19.9. And the 2025 report labels 18.4% as "Declining", which is true against 20.7% but false against 14%.
- **Conclusion.** [S] Treat 14% as an anomaly: a data or calculation artifact, or a sample quirk. I cannot show which. Best reading: **Ardent's all-respondent exception rate has run around 18% to 22% in recent years.**

**What this number is not.** Ardent's description: "Invoices flagged due to coding errors, missing information, approval bottlenecks, lack of purchase order data, etc." That covers all invoices, including the roughly one-third not linked to a PO. So it is not a three-way match failure rate. It is a broader flag rate, self-estimated, with no shared definition among respondents.

### 5.3 First-pass match

| Figure | Source | Measure |
|---|---|---|
| 75.0% median | [APQC 102149](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/percentage-invoice-line-items-are), n=4,438 | Invoice **lines** matched the first time. "Matched" not further defined on the public page, so 2-way versus 3-way unknown. Implies about 25% of lines not matched first time |
| 73% and 90% | Hackett Performance Study 2015, via [Zycus](https://www.zycus.com/blog/e-invoicing/shows-senior-management-the-money-part-4-of-5-benchmarking-ap-operations), vendor blog | First-pass match, columns not visible; likely peer and world-class. Original not obtained. Weak |
| 35.4% (51.0 BIC, 29.0 others) | Ardent 2025 | Straight-through invoices, no human touch. Other years: 30.2% (2023 ed.), 32.4% (2024 ed.), 32.6% (2025 ed.) |

Line-level (APQC, 25% unmatched) and invoice-level (Ardent, about 18% to 22% flagged) rates are not comparable, but they point to the same order of magnitude: **roughly one in four or five items needs a human**. [S]

### 5.4 Cost and cycle time

| Figure | Source | Measure |
|---|---|---|
| $6.50 median | [APQC 100451](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/total-cost-perform-process-process-19), n=6,546 | Total process cost (outsourced, overhead, personnel, systems) per invoice |
| $9.84 avg; $2.65 BIC; $12.42 others | Ardent 2025, n=204 | "All-inclusive" cost per invoice |
| $9.40; $2.78; $12.88 | Ardent 2024 survey, n=212 | Same |
| 5.0 days median | [APQC 100154](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/cycle-time-days-receipt-invoice-until-0), n=10,382 | Invoice receipt to approved and scheduled |
| 15.0 days median | [APQC 100575](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/cycle-time-days-receipt-invoice-until), n=2,226 | Invoice receipt to payment sent |
| 8.2 days; 2.9 BIC; 13.5 others | Ardent 2025 | "Time to process a single invoice" |
| 11,667 median | [APQC 101290](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/number-invoices-processed-fte-1), n=4,448 | Invoices per AP FTE |
| 21.9% | Ardent 2025 | Staff time on supplier inquiries, which Ardent says is "in no small part caused by exceptions" |

**The cost of an exception as such is not reported in any original source found.** Ardent says exceptions are "typically the biggest single reason" costs are not lower, but gives no number. The figures above are whole-process, not match-specific.

### 5.5 Duplicate and erroneous payments

| Figure | Source | What it actually measures | Comment |
|---|---|---|---|
| 1.5% median | [APQC 105905](https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/percentage-total-annual-number), n=2,386 | **Count** of disbursements that are duplicate or erroneous | Often misquoted as percent of spend. It is not dollars, and "erroneous" may include things later corrected. Self-reported |
| 0.8% to 2.0% | APQC top and bottom performers, via recovery firm blog | Same | Vendor relay; quartiles are gated |
| About 1.5% of outgoing cash | "IOFM", via vendor blogs | Unclear | **Could not trace to an original.** Do not use |
| 0.1% to 0.5% of spend | Vendor and consultancy blogs | Unclear | Untraceable. Label as vendor |
| 1.29% of invoices | SAP Concur, via blog | Unclear | Vendor, unverified |
| 0.05% to 0.5% of audited spend | [Transparent Global blog](https://transparentglobal.com/blog/what-recovery-rates-should-you-expect-from-a-first-time-duplicate-payment-audit/) | First-time recovery audit yields | Vendor. Recovery, not error rate |

**Recovery audit, private.** PRGX's 10-Ks define the service but give no error rate; the FY2018 filing says claims versus client purchases is "non-linear" ([10-K](https://www.sec.gov/Archives/edgar/data/1007330/000100733019000004/a201810kprgx.htm)). Not usable as a benchmark. PRGX's recoveries include pricing, allowances and terms that a match would not catch anyway.

**US federal data: the only audited-style public source found.** Federal agencies run a comparable control.

| Period | Data | Calculated rate | Caution |
|---|---|---|---|
| [DoD FY2005 to FY2008](https://www.gao.gov/assets/gao-09-442.pdf) | Overpayments identified for recovery of $469.5M, $170.0M, $24.6M, $53.3M against $222.8B, $299.4B, $189.3B, $331.2B reviewed | 0.21%, 0.06%, 0.01%, 0.02% | GAO found the processes "inadequate" and not designed for this, and scope shifted. FY2005 included 67% underpayments. Treat as a floor, not a rate |
| [DFAS FY1999, GAO-01-309](https://www.govinfo.gov/content/pkg/GAOREPORTS-GAO-01-309/html/GAOREPORTS-GAO-01-309.htm) | 39 large contractors returned $351M on $30B paid. 77% contract administration, 18% billing or payment errors (about $64M), 5% unspecified | 1.17% gross; **about 0.21% from true billing or payment error** | Not projectable. Mostly progress-payment contracts, not PO goods. GAO: "small in relation to total contract payments" |
| [GAO-03-1067R](https://www.gao.gov/assets/a92152.html) | Sample of manually entitled DFAS invoices, Oct 2000 to Jul 2001: 13.4% primary error rate, about $4.8M overpaid in 10 months | | Not projectable; sample size undocumented; only first error counted. Also $49B of $198B in transactions were payment adjustments |
| [FY2010, FY2011](https://www.everycrsreport.com/reports/R42878.html) | $688M, then more than $1.2B recaptured from contractors and vendors across agencies | No denominator available | |
| [DoD recovery audit pilot, GAO NSIAD-99-12](https://legistorm.com/reports/view/gao/29411/Recovery_Auditing_Offers_Potential_to_Identify_Overpayments.html) | $19.1M overpayments identified at one supply center | | Shows that prepayment process leaves residual findable error. Denominator not obtained |

Comment [S]: on DFAS figures, the share caused by genuine billing or payment mistakes is about a fifth of the excess paid, and about 0.2% of dollars. Government contract payment is not corporate PO buying, so this is an analogy only.

### 5.6 Invoice fraud

| Figure | Source | Sample | What it measures |
|---|---|---|---|
| Billing schemes 22% of cases, median loss $100,000 | [ACFE 2024](https://www.ivey.uwo.ca/media/kjljj5cy/2024-report-to-the-nations.pdf) | 1,921 cases, Jan 2022 to Sep 2023 | 424 cases. Of known, CFE-investigated cases, worldwide, all sizes |
| Billing 21% of cases, median loss $90,000 | [ACFE 2026](https://www.acfe-mexico.com.mx/inicio/sitepad-data/uploads/2026/07/Reporte-a-las-Naciones-2026.pdf) (English text hosted by ACFE Mexico) | 2,402 cases, Jan 2024 to Sep 2025 | 508 cases. Same basis |
| Lack of controls 32%, override 19% | ACFE 2024 | Same | Examiner opinion, primary weakness. 2026: lack of controls 33% |
| 43% found by tip | ACFE 2024, 2026 | Same | Detection method. Tips lead. The categories read here do not isolate document matching, so its share of detection is unknown |
| 79% of organizations hit by attempted or actual fraud | [AFP 2025](https://truist.com/content/dam/truist-bank/us/en/documents/info/cci/2025-afp-payments-fraud-control-survey-report-key-highlights.pdf) | 521 corporate practitioners, Jan 2025, for 2024 | Share of organizations, any attempt |
| Invoice fraud 24%, vendor imposter 45%, BEC 62% to 63% | AFP 2025 | Same | Share of organizations reporting that type, attempts included. Not per invoice |
| 76%, invoice fraud 26% | [AFP 2026](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf) | 465 corporate practitioners, for 2025 | Same |

**What these cannot give:** a fraud rate per invoice or per dollar of spend. ACFE has no denominator; it is a sample of caught frauds. The often quoted "5% of revenue" is an estimate by CFEs, not a measurement. AFP counts organizations touched, including failed attempts. I found **no source that says how many billing frauds passed a working three-way match, or were stopped by one.** ACFE's billing category also includes shell companies and personal purchases, which may have POs and receipts.

### 5.7 Genuine error versus harmless mismatch

**No published cross-company study was found that takes a sample of match exceptions and classifies them as real loss prevented or harmless.** Not in Ardent, APQC, Hackett material available, ACFE, AFP or academic audit literature located. This is the central gap. [E that none was found; not proof that none exists. Paid IOFM and Hackett reports were not accessible.]

Triangulation, of limited quality:

**A warning on the obvious comparison.** Exception rates (about 20%) are measured before payment. Duplicate, recovery and fraud figures are measured after the control has run. Dividing one by the other does not give the harmless share, because what the match stopped is, by construction, missing from the after-the-fact figures. A low residual is consistent with both "the match works" and "there was little to catch". Only pre-payment evidence can split the two.

**Best pre-payment evidence found: BPI Challenge 2019 event log, original tabulation for this file.** [E for the counts; S for the interpretation.] Real purchase-to-pay log from [a large multinational in coatings and paints in the Netherlands](https://icpmconference.org/wp-content/uploads/BPI-Challenge-Submission-3.pdf), published with [DOI 10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1](https://doi.org/10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1). 251,734 PO items, mainly 2018. Item categories: 3-way invoice before GR 221,010; 3-way invoice after GR 15,182; consignment 14,498; 2-way 1,044. I streamed the full 728 MB file from 4TU on 2026-11-04 and counted activities; nothing was kept. Cross-check: a [KPMG Netherlands challenge submission](https://icpmconference.org/wp-content/uploads/BPI-Challenge-Submission-3.pdf) reports Remove Payment Block in 26% of cases for the main category; I get 26.8%.

Population: 210,692 three-way items with a recorded invoice.

| Measure | Items | Share |
|---|---|---|
| Payment block removed (block event logged) | 55,799 | 26.5% of invoiced items |
| Any document correction (price, quantity, cancelled GR, cancelled invoice, debit memo) | 28,187 | 13.4% |
| Invoice cancelled or vendor debit memo | 6,122 | 2.9% |
| of which vendor debit memo | 5,347 | 2.5% |

What accompanied the 55,799 blocks (mutually exclusive, in this order):

| Class | Items | Share of blocks | Plausible meaning |
|---|---|---|---|
| A. Invoice cancelled or debit memo on the item | 3,795 | 6.8% | Invoice actually corrected |
| B. Otherwise price or quantity changed, or GR cancelled | 7,115 | 12.8% | A record was changed. Could be a wrong PO rather than a wrong invoice |
| C. Otherwise a receipt or service entry posted between invoice and release | 13,710 | 24.6% | Timing: invoice arrived first |
| D. No document change visible | 31,179 | 55.9% | Released as is. Includes accepted variances, late confirmations, and anything the log does not capture |

Other results:
- **About 80% of blocks (C plus D) show no correction to any document on the item.** About 7% show the invoice itself corrected.
- 2,327 of 6,122 reversed or credited items (38%) never had a block, so corrections also arise outside the block.
- Block duration, first invoice to first release: median 6.2 days, 75th percentile 24.9, 90th 58.0.
- Invoice to clearing: median 43.5 days (invoice before GR), 29.4 days (invoice after GR), 5.2 days (2-way, only 303 items). These include payment terms and are not delay caused by the match.

Limits, all material:
- One company, non-US, one year, anonymized. Not a benchmark.
- Item level, not invoice level or dollars. The value field did not carry usable price change data (the value on Change Price events was almost always unchanged), so **dollar size of real errors could not be computed**.
- The log has no block reason code, so classes are inferred from what happened on the item. Class A may include routine credits and rebates; a cancelled invoice may be a keying fix. Class B changes may precede the invoice. Class D could hide real variances accepted within policy.
- "Corrected" is not "loss prevented". Nothing here shows what would have been paid without the block.

**Federal evidence.** On DFAS data in 5.5, 18% of excess payments came from billing or payment errors, 77% from contract administration. Post-payment and non-commercial, so an analogy only.

**Best supported statement, tagged [S]:** in the one real log available, a large majority of payment blocks ended with no document correction, and a small minority (under one in ten) with the invoice itself corrected. That suggests most exceptions are process mismatch rather than supplier error. It is one company. **Whether the same split holds for US public companies is unknown, and no dollar split between genuine loss and harmless mismatch exists in any public source found.**

## 6. Gaps

**Could not read**
- COSO 2013 full text (paid). Whether it uses the words "three-way match" or gives this example is **unverified**.
- PCAOB AS 2201 live page (403). Used the 2007 SEC filing of AS 5; later conforming amendments not checked. Also not read: AS 1105, AS 2110, AS 2401, AU-C 330, older SAS 1 section 320.
- Hammer 1990 full text. Only excerpts; the 14-item and 75% claims are secondary.
- Jans, Alles and Vasarhelyi (2014), *The Accounting Review* 89(5): payments without approval and segregation violations in a global bank's procurement, not caught by internal audit. Full text closed; counts not obtained. Possibly relevant.
- AICPA's 1949 definition extraction ended mid-word; 1917 Federal Reserve "Uniform Accounting", 1929 and 1936 AIA bulletins not read.
- Primary SEC report on McKesson & Robbins.
- APQC quartiles, Hackett, IOFM, Aberdeen, Levvel, PayStream originals. Some gated.
- State of ePayables 2024 full report (figures taken from MTM 2025, same survey by matching values; that identity is inferred).
- GAO NSIAD-99-12 denominator; DoD current Agency Financial Report data; current OMB contract recovery data.
- DFARS contractor business system clauses; FAR clause numbering after the 2025 to 2026 FAR overhaul should be rechecked.
- ASC text; UCC case law; states beyond Texas and California; use tax accrual rules.

**Does not seem to exist in public**
- A census of three-way match adoption among US public companies.
- A rate of exceptions by root cause from an original survey.
- Cost per exception from an original source.
- Fraud or loss prevented by the match, per dollar or invoice.
- Exceptions classified as genuine or harmless, across companies.
- A published history of document matching. Section 4 is assembled from primary texts by me, and "earliest" means earliest found.

**Method notes**
- Google Books dates are from snippets, and serial volumes can be misdated. The 1964 hit is unverified.
- EDGAR counts are phrase hits on 10-K family documents including exhibits.
- Rates in the tables marked calculated are my arithmetic from the cited figures.
- WebFetch summaries were used for some statutes. Quotes shown were checked against raw text where possible; Rev. Proc. 98-25, Title 7 and GAO-03-1067R quotes came through a summarizer.
</content>
