# Workflow: Freight Forwarder Inquiry

## Purpose

Standardize the process of obtaining written quotations from freight forwarders, ensuring all critical cost items and operational constraints are confirmed before quoting to clients.

## Trigger

User says: "询价", "问货代", "问价", "forwarder inquiry"

## Pre-Inquiry Checklist (Complete Before Contacting Forwarder)

| # | Item | Source | Status |
|---|------|--------|--------|
| 1 | Product name | Factory / client | ☐ |
| 2 | Outer packaging dimensions (L×W×H in mm or cm) | Factory packaging spec | ☐ |
| 3 | Gross weight per unit (kg) | Factory | ☐ |
| 4 | Net weight per unit (kg) | Factory | ☐ |
| 5 | Total quantity / units per container | Calculation | ☐ |
| 6 | Total volume (CBM) | Calculation | ☐ |
| 7 | Total gross weight (kg) | Calculation | ☐ |
| 8 | Container type (20GP / 40GP / 40HQ / 40FR OOG / LCL) | Based on cargo | ☐ |
| 9 | Port of loading (e.g., Shenzhen Yantian, Guangzhou Nansha) | Default or client-specified | ☐ |
| 10 | Port of discharge (exact name, country) | Client | ☐ |
| 11 | Special cargo type (battery / hazmat / chemical / toy / OOG) | Product nature | ☐ |
| 12 | SDS/MSDS available (if chemical/battery) | Factory | ☐ |
| 13 | Required delivery terms (CIF / FOB / DAP) | Client / boss decision | ☐ |
| 14 | Target shipping month | Client / boss | ☐ |

**Rule**: Do NOT contact forwarder until all items above are collected. Incomplete information leads to revised quotations and delays.

---

## Step-by-Step Inquiry Process

### Step 1: Verify Destination

**Question to resolve:** Is the destination a port, or an inland location?

- **If port**: Confirm exact port name, country, and whether the port accepts your container type (especially 40FR OOG).
- **If inland**: Identify the nearest operational port that accepts your cargo type. Quote to the port; inland transport is a separate discussion.

**Examples:**
- Wisconsin Elkhart Lake → NOT a port → nearest operational port for 40FR is New York
- Brazil Salvador → IS a port → but confirm if port handles LCL for your product category
- Brazil Ilhéus / Itajaí → Different ports with different capabilities; never confuse them

### Step 2: Confirm Service Scope by Country (v2.0 Multi-Country)

**USA:**
- Door-to-door generally available
- But: Oversized cargo (40FR OOG) may be port-only — 40FR OOG only discharges at New York; inland trucking requires lowbed trailer, state oversize permits, escorts
- IOR-based clearance (19 CFR 141.1; 2026 EO 14411 raising foreign IOR bar) — confirm who is importer of record
- Inland trucking for OOG requires special permits, escort vehicles, route planning
- Confirm: Can forwarder handle inland delivery to final ZIP code?

**Brazil:**
- Port-only for Chinese forwarders (no inland transport service)
- Customer must arrange own trucking from port to final destination
- Clearance requires a local entity with CNPJ + RADAR (IN RFB 1.984/2020 / Decreto 6.759/2009) — Chinese forwarder cannot act as Brazilian IOR
- Some product categories restricted to designated customs clearance ports (Salvador/Itajaí/Ilhéus are different ports)
- Confirm: Is your product HS code allowed at the target port? Does the buyer have a local customs entity/agent?

**EU (Germany / Netherlands / UK):**
- Door-to-door generally available (Rotterdam / Hamburg / Bremen discharge; rail/road inland)
- Buyer must hold EORI (EU) or UK EORI to clear; non-EU seller needs EU entity or Trust-and-Check indirect representative for e-commerce
- Transition note: UCC 952/2013 → (EU) 2026/2108 (fully applies 2027-09-21); PID for remote sales from 2026-11-01
- Confirm: buyer EORI status; whether delivery is CIF port / DAP / DDP

**Southeast Asia (Vietnam / Thailand / Singapore):**
- Door-to-door generally available
- Singapore: importer = party bringing goods into SG (SG buyer is importer); SG Customs Account + permit required (customs.gov.sg)
- Vietnam: NSW new decree 336/2026/ND-CP (effective 2026-10-15) unified declaration; buyer must be VN-registered importer
- Thailand: buyer/Thai customs agent clears via customs.go.th
- Confirm: buyer local import registration; LCL availability at target port

**Middle East (UAE / Saudi Arabia):**
- Door-to-door possible, but clearance strict
- KSA: buyer must hold CR + ZATCA customs registration; SABER (SASO) certificates required for many product categories; 12-digit HS
- UAE: buyer trade license + Jebel Ali clearance via local agent
- Confirm: SABER certification responsibility & cost; 12-digit HS codes; DDP feasibility

**Japan / Korea:**
- Door-to-door generally available
- Japan: buyer must use licensed customs broker (通関士/通关代理) — foreign company cannot self-file; 8-digit HS mandatory; 2026 consumption tax on all imports incl. previously duty-free small parcels; PSE for electronics, ST for toys
- Korea: buyer Korean import license number + broker
- Confirm: buyer customs agent arranged; 8-digit HS; product certifications

**General (all countries):**
- Confirm: Is your product HS code allowed at the target port?
- Confirm: Are there any import restrictions or special documentation requirements?
- Confirm: Who performs destination customs clearance (buyer / buyer's agent / DDP seller)?

### Step 3: Separate FCL and LCL Confirmations

**Critical Rule**: Forwarder says "this route/destination is available" ≠ LCL is available. You must explicitly confirm both.

- **FCL (Full Container Load)**: Ask if 20GP / 40GP / 40HQ / 40FR are accepted at destination
- **LCL (Less than Container Load)**: Ask separately if LCL consolidation is available for this destination and product type
- If LCL not available, client must book FCL or find alternative routing

**Brazil helmet cleaning machine case**: Forwarder confirmed "front-end and ocean freight doable" but did NOT explicitly confirm Salvador LCL availability. This led to quotation errors.

### Step 4: Request Itemized Cost Breakdown

Forwarder must provide written confirmation of ALL the following:

**Origin (China):**
- Factory pickup / warehouse to port trucking
- Export customs declaration
- Port handling charges (THC, ORC, etc.)
- Documentation fees
- Special cargo handling (if battery/hazmat/OOG)

**Ocean Freight:**
- Base ocean freight
- Bunker adjustment factor (BAF) / fuel surcharge
- Currency adjustment factor (CAF)
- Peak season surcharge (if applicable)
- Other surcharges

**Insurance:**
- Marine cargo insurance (typically 110% of cargo value × rate)
- Confirm insurance rate and coverage terms

**Destination:**
- Port handling charges (THC)
- Container freight station (CFS) fee (for LCL)
- Documentation / telex release fee
- Other local charges

**Inland (if applicable):**
- Trucking from port to final destination
- Oversize permits and escort (for OOG)
- Crane / unloading equipment at destination
- Storage / detention / demurrage (if applicable)

**Mark unconfirmed items as**: "预算价 / 待确认 (Budget / Awaiting Confirmation)"

### Step 5: Confirm Schedule & Terms

- Sailing schedule (weekly / bi-weekly?)
- Transit time (port-to-port)
- Cut-off date for cargo delivery to port
- Free detention period at destination
- Quotation validity period (typically 15-30 days)

### Step 6: Document & Archive

Save forwarder's written confirmation (email / WeChat screenshot) with:
- Date of quotation
- Forwarder name and contact
- Reference number
- All confirmed cost items
- Explicitly noted unconfirmed items

---

## Post-Inquiry Actions

| Action | Responsible | Deadline |
|--------|-------------|----------|
| Compile cost summary for boss review | You | Within 1 day |
| Flag any unconfirmed items for follow-up | You | Immediate |
| Request clarification on ambiguous items | You | Within 4 hours |
| Update quotation checklist with confirmed costs | You | As received |

---

## Common Inquiry Pitfalls

1. **Assuming availability**: "They said the route is open" ≠ your container type is accepted
2. **Mixing port names**: Ilhéus ≠ Itajaí ≠ Salvador — always double-check spelling
3. **Ignoring product restrictions**: Brazil may restrict certain HS codes to specific ports
4. **Not confirming LCL separately**: FCL and LCL are different services with different costs
5. **Accepting verbal quotes**: Always request written/email confirmation for traceability
6. **Forgetting OOG constraints**: 40FR has crane, rail, and road restrictions that 40HQ doesn't
