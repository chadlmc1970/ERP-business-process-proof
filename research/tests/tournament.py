"""Selection tournament. Scores are analyst judgment (1-5, 5 = better candidate), not measurements.
The last two criteria are inverted risks: 5 = low risk of confusing law with convention / low chance the idea already exists."""
C = ["Standardized","Breadth","Economic","Legacy assumptions","Decisions/handoffs","Discovery room","Testable","Impact","Law-vs-habit clarity","Novelty headroom"]
S = {
 "Three-way match (PO / receipt / invoice)": [5,5,4,5,5,4,5,4,4,2],
 "Delegated approval chains":                [3,5,4,5,5,4,3,4,3,3],
 "Annual budgeting":                         [3,5,5,4,4,4,2,5,5,2],
 "Periodic financial close":                 [4,5,5,4,5,3,3,5,2,2],
 "Intercompany reconciliation":              [4,3,3,5,4,4,4,3,4,2],
 "Cash application":                         [4,4,3,4,3,3,5,3,5,2],
 "Cycle counting / physical inventory":      [5,4,4,3,2,3,5,3,3,3],
 "Sales and operations planning":            [3,3,5,3,4,3,3,4,5,2],
 "Competitive bidding (RFP)":                [3,4,4,4,4,3,2,4,3,3],
 "Bank reconciliation":                      [5,5,2,4,2,2,5,2,3,2],
 "Vendor onboarding":                        [4,5,3,3,4,2,3,3,2,3],
}
print("| Candidate | " + " | ".join(C) + " | Total |")
print("|---|" + "---|"*(len(C)+1))
for k,v in sorted(S.items(), key=lambda x:-sum(x[1])):
    print(f"| {k} | " + " | ".join(map(str,v)) + f" | {sum(v)} |")
