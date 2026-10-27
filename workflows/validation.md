# Workflow: OOG & Route Validation

## Purpose

Validate special cargo requirements (OOG — Out of Gauge) and route-specific constraints before quotation and booking.

## Trigger

User says: "校验 OOG", "检查", "OOG", "validation", "oversized"

---

## OOG Cargo Definition

Cargo that exceeds standard container dimensions and cannot fit in a regular 20GP/40GP/40HQ container. Typically shipped on:
- **40FR (Flat Rack)**: Open-top, open-side container for oversized cargo
- **40OT (Open Top)**: Top-open container for tall cargo
- **Special equipment**: Project cargo solutions

---

## OOG Validation Checklist

### 1. Cargo Dimension Verification

| Measurement | Source | Critical? | Notes |
|-------------|--------|-----------|-------|
| Product dimensions (L×W×H) | Factory | Reference only | Do NOT use for shipping calc |
| **Outer packaging dimensions** | Factory packaging spec | **YES** | Always use this for volume/weight |
| Gross weight (with packaging) | Factory | **YES** | Used for container loading and freight |
| Net weight (product only) | Factory | For customs only | |
| Center of gravity | Factory / engineer | For lashing plan | |

**Critical Rule**: Never use product dimensions for shipping calculations. Always use outer packaging dimensions.

### 2. Container Suitability

| Cargo Dimension | 40HQ Internal | 40FR Available | Decision |
|-----------------|---------------|----------------|----------|
| Height ≤ 2.69m | Fits | Not needed | Use 40HQ |
| Height > 2.69m or width > 2.35m | Doesn't fit | Available | Use 40FR |
| Weight > 28 tons | Exceeds limit | Check capacity | May need special equipment |

### 3. Port Capability Verification

**For OOG cargo, the discharge port MUST have:**
- [ ] Crane capable of lifting the cargo weight + container
- [ ] Sufficient crane reach (height and radius)
- [ ] Storage area for flat rack after unloading
- [ ] Experience handling OOG cargo (not all ports do)

**Example — USA Wisconsin Project:**
- Elkhart Lake: No port (inland location)
- Milwaukee/Green Bay: Local ports, but may not handle 40FR OOG
- New York: Confirmed capable of handling 40FR OOG
- **Result**: Cargo must discharge at New York, then trucked inland

### 4. Inland Transport Constraints (OOG)

**Rail Transport:**
- [ ] Can the cargo fit on rail flatcar?
- [ ] Height restrictions in tunnels along route?
- [ ] Weight limits per railcar?
- **Note**: Many OOG cargos cannot use rail; road transport only

**Road Transport:**
- [ ] Route surveyed for bridge/tunnel height clearances?
- [ ] Oversize transport permits required per state/province?
- [ ] Escort vehicles required?
- [ ] Travel time restrictions (night bans, weekend bans)?
- [ ] Mid-route transloading required? Where?
- [ ] Lowbed trailer or special trailer needed?

**Example — USA Wisconsin Project:**
- New York to Wisconsin: ~1,370–1,450 km
- Cannot use rail (OOG restrictions)
- Must use lowbed trailer with escort
- Requires oversize permits for each state crossed
- Higher cost than standard trucking

### 5. Lashing and Securing

- [ ] Is lashing/securing included in forwarder quote?
- [ ] If not included, get separate quotation for lashing plan
- [ ] Verify lashing materials meet ocean voyage standards
- [ ] Request lashing plan drawing from forwarder

**Warning**: OOG lashing is often NOT included in base freight quote. Always confirm separately.

---

## Route-Specific Validation

### Regulation Gate Check (v2.0 — validate before any route decision)

For the destination country, confirm all three gates (see `regulations/<country>.md`):

| Gate | Brazil | USA | EU (DE/NL/UK) | VN/TH/SG | UAE/KSA | JP/KR |
|------|--------|-----|----------------|----------|---------|-------|
| 清关主体 | Buyer CNPJ+RADAR (IN RFB 1.984/2020) | Named IOR (19 CFR 141.1; EO 14411) | Buyer EORI (UCC 952/2013 → (EU) 2026/2108) | VN: buyer VN-importer; SG: SG buyer = importer | KSA: CR+ZATCA; UAE: trade license | JP: licensed customs agent; KR: broker |
| 门到门 | Port-only | Yes (OOG: NY only) | Yes | Yes | Yes (strict) | Yes |
| 产品准入 | Check products.md | Check products.md | CE mandatory | Check products.md | SABER for many | PSE/ST for many |

**Validity rule**: re-verify online + record date before final quote; unverified = TBC.

### Brazil Routes

| Port | OOG Capability | Inland Transport | Special Restrictions |
|------|---------------|-------------------|---------------------|
| Salvador | Confirm with forwarder | Port-only; customer self-collect | Some HS codes restricted |
| Itajaí | Confirm with forwarder | Port-only; customer self-collect | Different from Ilhéus! |
| Ilhéus | Confirm with forwarder | Port-only; customer self-collect | Different from Itajaí! |

**Brazil Critical Checks:**
1. Product HS code allowed at target port?
2. Product category restricted to designated customs ports?
3. Is the target port a designated customs clearance port for this product type?
4. Customer aware they must arrange own trucking from port?
5. Forwarder confirmed they only handle to port, not inland?

**Common Brazil Mistake:**
Assuming forwarder can arrange delivery to customer's warehouse. Chinese forwarders do NOT provide inland transport in Brazil. Customer must arrange own trucking.

### USA Routes

| Port | OOG Capability | Inland to Wisconsin | Notes |
|------|---------------|---------------------|-------|
| Los Angeles/Long Beach | Yes | Long inland distance (~3,000 km) | West Coast entry |
| Chicago | Varies | Closer to Wisconsin (~200 km) | Confirm 40FR handling |
| New York | Yes | ~1,370–1,450 km to Wisconsin | Confirmed OOG capable |

**USA Critical Checks:**
1. Can destination port handle 40FR OOG?
2. If inland delivery required: full address with ZIP code?
3. Oversize permits required for each state?
4. Escort vehicles needed?
5. Bridge/tunnel height restrictions on route?
6. Delivery window / appointment required at destination?

**Common USA Mistake:**
Quoting CIF to an inland city (like Elkhart Lake) instead of CIF to nearest operational port. CIF terms cover cost to port only; inland transport is additional.

---

## Validation Output Format

After completing validation, produce:

```
VALIDATION REPORT — [Project Name]
Date: [YYYY-MM-DD]
Cargo: [Product Name]

1. CARGO SPECIFICATIONS
   - Outer dimensions: [L] × [W] × [H] mm
   - Gross weight: [X] kg
   - Container type: [40HQ / 40FR / 20GP / LCL]
   - Special requirements: [battery / hazmat / OOG / none]

2. PORT VERIFICATION
   - Discharge port: [Name, Country]
   - OOG capability: [Confirmed / Not confirmed / Not available]
   - Inland transport: [Forwarder provides / Customer arranges / N/A]

3. INLAND TRANSPORT (if applicable)
   - Final destination: [Address / City]
   - Distance from port: [X] km
   - Transport mode: [Rail / Road / Not available]
   - Permits required: [Yes / No]
   - Escort required: [Yes / No]
   - Estimated cost: [Confirmed $X / Budget $X / TBC]

4. RISK ASSESSMENT
   - High risks: [List]
   - Medium risks: [List]
   - Mitigation actions: [List]

5. CONFIRMATION STATUS
   - Forwarder written confirmation: [Received / Pending]
   - Unconfirmed items: [List with impact]

Validated by: [Your Name]
```

---

## Quick Reference: OOG Decision Tree

```
Is cargo oversized? (> standard container dimensions)
    ├── No → Use 40HQ or 20GP → Standard process
    └── Yes → Use 40FR OOG
            ├── Can discharge port handle OOG?
            │   ├── No → Find alternative port
            │   └── Yes → Continue
            ├── Can cargo use rail?
            │   ├── Yes → Rail transport possible
            │   └── No → Road transport only
            │       ├── Permits required?
            │       │   ├── Yes → Apply for permits
            │       │   └── No → Proceed
            │       ├── Escort required?
            │       │   ├── Yes → Arrange escort
            │       │   └── No → Proceed
            │       └── Route surveyed?
            │           ├── Yes → Proceed with booking
            │           └── No → Survey route first
            └── Is lashing included?
                ├── Yes → Confirm in writing
                └── No → Get separate lashing quote
```
