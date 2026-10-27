# Template: CIF Quotation Item-by-Item Validator

## Purpose

Use this validator after completing a CIF quotation to verify every item is correctly calculated and documented. Run through each section sequentially.

---

## Section A: Product Cost Calculation

### A1. Factory Price Confirmation

```
[ ] Factory price confirmed in writing (WeChat/email/contract)
[ ] Price is tax-inclusive or tax-exclusive?  _________
[ ] If tax-exclusive: tax rate confirmed with factory = _______%
[ ] If tax-inclusive: no additional tax needed

Factory Price (RMB): ________________
Tax Rate: ________________%
Tax Amount: ________________ (Price × Rate)
Tax-Inclusive Base: ________________ (Price + Tax)
```

### A2. Profit Margin Application

```
[ ] Profit margin = 25% (standard)
[ ] If different margin: Boss approval obtained? [ ] Yes [ ] No

Profit Amount: ________________ (Tax-Inclusive Base × 0.25)
Total with Profit (RMB): ________________ (Tax-Inclusive Base × 1.25)
```

**Validation Rule**: Profit MUST be calculated on tax-inclusive base, NOT on raw factory price.

---

## Section B: Exchange Rate Conversion

### B1. Rate Selection

```
[ ] Standard client → Use real-time market rate
[ ] Special client (boss's friend, etc.) → Use fixed rate with boss confirmation
[ ] Fixed rate value: ________________
[ ] Boss confirmation received? [ ] Yes [ ] No
[ ] Rate source: [ ] Bank of China [ ] Other: ________________
[ ] Rate date/time: ________________
```

### B2. USD Conversion

```
RMB Amount (with profit): ________________
Exchange Rate: ________________
Product Cost in USD: ________________ (RMB ÷ Rate)
```

**Validation Rule**: Document rate source and date on quotation. Fixed rates require written boss approval.

---

## Section C: Forwarder Cost Validation

### C1. Origin Charges (China)

```
Item                          | Amount (USD) | Confirmed? | Notes
------------------------------|--------------|------------|-------
Factory pickup / trucking     |              | [ ] Yes    |
Export customs declaration      |              | [ ] Yes    |
Port handling (THC/ORC)       |              | [ ] Yes    |
Documentation fee             |              | [ ] Yes    |
Special handling (if applicable)|             | [ ] Yes    |
------------------------------|--------------|------------|-------
Origin Subtotal:              |              |            |
```

### C2. Ocean Freight

```
Item                          | Amount (USD) | Confirmed? | Notes
------------------------------|--------------|------------|-------
Base ocean freight            |              | [ ] Yes    |
BAF (Bunker Adjustment)       |              | [ ] Yes    |
CAF (Currency Adjustment)     |              | [ ] Yes    |
Peak season surcharge         |              | [ ] Yes    |
Other surcharges              |              | [ ] Yes    |
------------------------------|--------------|------------|-------
Ocean Freight Subtotal:       |              |            |

Container type: [ ] 20GP [ ] 40GP [ ] 40HQ [ ] 40FR OOG [ ] LCL
```

### C3. Marine Insurance

```
[ ] Insurance required? [ ] Yes [ ] No
Cargo value for insurance: ________________ USD
Insurance rate: ________________% (typical 0.1%)
Insurance amount: ________________ (Cargo value × 110% × Rate)

[ ] Insurance terms confirmed with forwarder/insurer? [ ] Yes [ ] No
```

### C4. Destination Charges

```
Item                          | Amount (USD) | Confirmed? | Notes
------------------------------|--------------|------------|-------
Port handling (THC)           |              | [ ] Yes    |
CFS fee (if LCL)              |              | [ ] Yes    |
Documentation fee             |              | [ ] Yes    |
Customs clearance (if included)|             | [ ] Yes    |
Other local charges           |              | [ ] Yes    |
------------------------------|--------------|------------|-------
Destination Subtotal:         |              |            |
```

**Brazil-specific**: Confirm these are port-only charges; inland is NOT included.

### C5. Inland Transport (if applicable)

```
[ ] Inland transport required? [ ] Yes [ ] No
[ ] Is this DAP (not CIF)? [ ] Yes [ ] No

Item                          | Amount (USD) | Confirmed? | Notes
------------------------------|--------------|------------|-------
Port to destination trucking  |              | [ ] Yes    |
Oversize permits              |              | [ ] Yes    |
Escort vehicles               |              | [ ] Yes    |
Crane / unloading             |              | [ ] Yes    |
Storage / detention           |              | [ ] Yes    |
------------------------------|--------------|------------|-------
Inland Subtotal:              |              |            |

Note: If any item is NOT confirmed, mark as "Budget / TBC" and do NOT include in firm quote.
```

### C6. Unconfirmed Items Summary

```
Unconfirmed Items:
1. ________________________ | Impact: ________________________
2. ________________________ | Impact: ________________________
3. ________________________ | Impact: ________________________

[ ] All unconfirmed items marked as "Budget / TBC" on quotation? [ ] Yes
[ ] Client informed of unconfirmed items? [ ] Yes [ ] N/A
```

---

## Section D: Port and Route Validation

### D1. Port Verification

```
Port of Loading: ________________________ , China
[ ] Correct spelling? [ ] Yes
[ ] Confirmed operational for container type? [ ] Yes

Port of Discharge: ________________________ , ________________________ (country)
[ ] Correct spelling? [ ] Yes
[ ] Confirmed operational for container type? [ ] Yes
[ ] Not confused with similar port names? [ ] Yes

Similar port names check:
- Brazil: [ ] Salvador ≠ Itajaí ≠ Ilhéus
- USA: [ ] Los Angeles ≠ Long Beach ≠ San Pedro
```

### D2. Service Scope by Country

```
Destination Country: ________________________

[ ] Brazil: Port-only (no inland by Chinese forwarder)? [ ] Yes [ ] No
  [ ] Customer informed they must arrange own trucking? [ ] Yes [ ] N/A
  [ ] Buyer has local CNPJ+RADAR entity / agent for clearance? [ ] Yes [ ] Pending
  [ ] Product HS code allowed at target port? [ ] Yes [ ] Pending

[ ] USA: Door-to-door available? [ ] Yes [ ] No [ ] Not applicable
  If OOG: [ ] Inland transport confirmed feasible (NY discharge)? [ ] Yes [ ] No
  [ ] Importer of Record (IOR) identified? [ ] Yes [ ] N/A

[ ] EU/UK: Buyer EORI/UK EORI confirmed for clearance? [ ] Yes [ ] N/A
  [ ] CE marking verified (if EU)? [ ] Yes [ ] N/A

[ ] SE Asia / ME / JP / KR: local importer & broker arrangement confirmed? [ ] Yes [ ] Pending

[ ] Other country: ________________________
  Special rules: ________________________
```

### D3. Regulation & Validity Check (v2.0 — MANDATORY)

```
Regulation library file consulted: regulations/________________________
List cited regulations:
  1. ________________________  (source URL: ________________________)
  2. ________________________  (source URL: ________________________)

[ ] Each cited regulation re-verified online (official source)?
    [ ] Yes — verification date: ________________________
    [ ] No — mark as "TBC", do NOT cite

[ ] Compliance notes in quotation kept brief (regulation name + one-line conclusion)?
    [ ] Yes   [ ] No — shorten
```

### D4. FCL vs LCL Confirmation

```
Container Mode: [ ] FCL [ ] LCL

If FCL:
[ ] Forwarder confirmed FCL available to destination? [ ] Yes
[ ] Container type accepted at destination port? [ ] Yes

If LCL:
[ ] Forwarder EXPLICITLY confirmed LCL available to destination? [ ] Yes
[ ] LCL consolidation service confirmed for this product type? [ ] Yes
[ ] CFS fees confirmed? [ ] Yes

Critical: "Route is available" ≠ "LCL is available". Must confirm separately.
```

---

## Section E: Quotation Document Check

### E1. Mandatory Elements

```
[ ] Trade terms clearly stated: CIF ________________________
[ ] Port of loading: ________________________
[ ] Port of discharge: ________________________
[ ] Exchange rate stated: ________________ (source: ________________)
[ ] Quotation validity period: until ________________
[ ] Payment terms: ________________________
[ ] Delivery terms: ________________________
[ ] HS Code: ________________________
[ ] Product specifications match client's PO
[ ] All amounts in USD
[ ] Client name correct: ________________________
```

### E2. Special Notes (if applicable)

```
[ ] OOG cargo note included? [ ] Yes [ ] N/A
[ ] Brazil port-only note included? [ ] Yes [ ] N/A
[ ] Unconfirmed costs marked as "Budget / TBC"? [ ] Yes [ ] N/A
[ ] Insurance terms stated? [ ] Yes [ ] N/A
[ ] Any country-specific restrictions noted? [ ] Yes [ ] N/A
```

---

## Section F: Final Approval

### F1. Self-Validation

```
[ ] All calculations double-checked
[ ] Product cost formula: (Price + Tax) × 1.25 ÷ Rate = ________________
[ ] Forwarder costs all confirmed or marked TBC
[ ] Port names verified, not confused with similar names
[ ] FCL/LCL confirmed separately
[ ] Special client pricing (fixed rate) approved by boss
[ ] Quotation validity period reasonable (15-30 days)
  [ ] No fabricated sailing schedules or promised costs
  [ ] All numbers use consistent units (USD, kg, CBM)
  [ ] (v2.0) Destination-country regulation checked & cited regulations verified online
  [ ] (v2.0) Compliance notes present but brief (no full legal text)
  [ ] (v2.0) Regulation validity date recorded in work sheet
  [ ] (v2.1) Transport accessibility verified: address not remote/height-restricted, or alternatives provided
  [ ] (v2.1) Product compliance confirmed with factory (battery/chemical/magnetic/powder)
  [ ] (v2.1) Trade terms clearly stated and client understands (CIF=port, DAP=door, no DDP where prohibited)
  [ ] (v2.1) Quotation validity & terms mirror forwarder's written quote exactly
  [ ] (v2.1) Forwarder quote has clear validity period and firm terms (or marked TBC / backup forwarder consulted)
  [ ] (v2.1) Change management: time/place/qty defined; client changes trigger re-verification
  [ ] (v2.1) Exchange-rate adjustment clause present (>3% trigger)
  [ ] (v2.1) Force Majeure clause present in contract/quotation
```

### F2. Boss Approval (if required)

```
[ ] Standard client + standard margin (25%) + real-time rate
  → [ ] Can send without boss approval? [ ] Yes [ ] No

[ ] Special client OR fixed rate OR margin ≠ 25%
  → [ ] Boss approval obtained? [ ] Yes [ ] No
  → [ ] Approval method: [ ] WeChat [ ] Email [ ] Verbal (documented)
  → [ ] Approval date: ________________
```

### F3. Send Authorization

```
[ ] All Sections A-F completed
[ ] No critical items outstanding
[ ] Quotation reviewed by colleague (if applicable)
[ ] Ready to send to client: [ ] YES [ ] NO — hold for: ________________
```

**Validator Signature**: ________________ **Date**: ________________

---

## Quick Reference: Validation Red Flags

| Red Flag | Action Required |
|----------|----------------|
| Forwarder only gave verbal quote | Request written confirmation before including |
| LCL not explicitly confirmed | Contact forwarder again, ask specifically about LCL |
| Port name similar to another | Verify spelling with map, confirm with forwarder |
| Product dimensions ≠ packaging dimensions | Recalculate using outer packaging dimensions |
| Tax rate not confirmed with factory | Call factory, confirm before calculating |
| Exchange rate source unclear | Check official source, document in quotation |
| OOG cargo without lashing confirmation | Contact forwarder, get separate lashing quote |
| Brazil quote includes inland transport | Remove inland, add note about port-only |
| CIF quote to inland city | Change to CIF [nearest port] + separate inland note |
| Sailing schedule not from forwarder | Remove estimated schedule or mark as "TBC" |
