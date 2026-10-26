# Workflow: Regulation-Aware Quotation Preparation (Word .docx)

## Purpose

Standardize the **regulation-verified** calculation and generation of client-ready quotations (Word .docx), ensuring: correct cost components, correct profit base, correct exchange rate, and a **brief, time-verified compliance note** for the destination country.

## Trigger

User says: "做报价", "报价", "CIF", "出报价单", "生成报价单", "quotation"

---

## Step 0: Destination-Country Regulation Check (MANDATORY FIRST)

Open `regulations/<country>.md` and confirm:

| Gate | Question | Where to look |
|------|----------|---------------|
| A. 清关主体 | Who is the importer of record? Does the country require a local entity (Brazil CNPJ+RADAR; EU EORI; USA IOR; KSA CR+ZATCA; SG Customs Account)? | regulations/<country>.md |
| B. 门到门 | Port-only (Brazil) or door-to-door (USA/EU/SEA/ME/JP/KR)? OOG restrictions (USA 40FR → NY)? | regulations/<country>.md |
| C. 产品准入 | Battery → UN38.3/MSDS/IMDG; chemical → SDS; CE/FCC/PSE/SABER as applicable | regulations/products.md |

**Validity re-check**: search official source for each cited regulation; record `核实日期 + 现行状态`. If a regulation status cannot be confirmed → do NOT cite it; mark the item as TBC.

**Output into quotation**: for each gate, one brief compliance note in `regulation_notes` (regulation name + one-line conclusion; no full legal text).

---

## Company Quotation Formula

```
Step 1: Product Original Price (confirm tax-inclusive or tax-exclusive with factory)
Step 2: Add Tax = Price × Tax Rate (13% or 10% — confirm per project)
Step 3: Tax-Inclusive Base = Price + Tax
Step 4: Add Profit = Tax-Inclusive Base × 1.25 (25% margin ON TAX-INCLUSIVE AMOUNT)
Step 5: Convert to USD = Amount ÷ Exchange Rate (real-time or boss-fixed)
Step 6: Add Forwarder Costs (ocean freight, insurance, origin/destination charges, in USD)
Final Quoted Price (USD)
```

**Formula Summary:**
```
Quoted Price (USD) = [(Product Price × (1 + Tax Rate)) × 1.25 + Forwarder Costs] ÷ Exchange Rate
```

⚠️ Common mistake: applying 25% profit on tax-exclusive price then adding tax — WRONG. Tax first, then 25% on the tax-inclusive total.

---

## Exchange Rate Rules

| Scenario | Rate Source | Approval Required |
|-----------|-------------|-------------------|
| Standard client | Real-time market rate | No |
| Boss's friend / special client | Fixed rate (e.g., 6.5 for Brazil) | Yes — boss must explicitly confirm |
| Long-term contract | Rate locked for contract period | Yes — boss + finance confirm |

**Rule**: State fixed rate explicitly in quotation: "Exchange rate fixed at [X.XX] per boss instruction."

---

## Step-by-Step Quotation Generation

### Step 1: Gather Product Information

- Product name/model; factory price (RMB; tax-inclusive or not — confirm!)
- Tax rate (13% or 10% per factory capability)
- **Outer packing dimensions** (L×W×H mm), gross/net weight, CBM
- Quantity per order/container; HS code (verified with broker; 8-digit for US/JP, 12-digit for KSA/UAE where applicable)
- Certifications: UN38.3 (battery), SDS/MSDS (chemicals), CE (EU), FCC (US), PSE (JP), SABER (KSA), etc.

### Step 2: Regulation Notes (per Step 0)

Example notes (brief):
- Brazil: `进口清关须由持 CNPJ+RADAR 的巴西本土主体办理（IN RFB 1.984/2020）；本报价 CIF 到港价，内陆段买方自理。`
- USA: `买方 IOR 完成进口申报（19 CFR 141.1；2026 EO 14411 新规）；本报价 CIF 港口价。`
- EU: `买方 EORI 清关（UCC 952/2013，过渡至 (EU) 2026/2108）；本报价 CIF 港口价。`
- Battery product: `含锂电池，UN38.3 + IMDG 第 9 类危险品申报，须提供 UN38.3 报告及 MSDS（详见附件）。`

### Step 3: Build Quotation JSON

Follow `templates/quotation-docx.md` schema. When unsure of a field, leave it as placeholder `[待填]` rather than invent data.

Reference sample: `templates/sample-quotation.json`

### Step 4: Generate Word Quotation

```bash
python scripts/generate_quotation.py <input.json> "C:/path/to/报价单_Qxxx.docx"
```

Script output shows computed figures (product USD base, forwarder USD, insurance, grand total) for cross-check.

### Step 5: Validate (11 Mandatory Checks)

Run `templates/cif-validator.md`:

1. Factory price confirmed (written)
2. Tax rate confirmed (13% or 10%)
3. Tax applied to correct base
4. Profit 25% on tax-inclusive amount
5. Exchange rate confirmed (real-time or boss-fixed)
6. Forwarder costs confirmed in writing; unconfirmed = TBC
7. Port names accurate (spelling; Brazil Salvador≠Itajaí≠Ilhéus)
8. Container type correct for cargo
9. Unconfirmed costs marked TBC
10. Validity period stated (15-30 days)
11. Boss approval obtained (fixed rate / special pricing)

**NEW (v2.0):** 12. Regulation notes present & brief; 13. Regulation validity re-checked with date recorded.

### Step 6: Boss Approval & Send

- Submit .docx + work sheet (costs, regulations, validity) to [老板]
- Approval required for: first quote, amount change, fixed rate, margin ≠ 25%, special client
- Send to client only after approval; keep forwarder written confirmations archived

---

## Container Type Selection Guide

| Cargo Type | Dimensions | Weight | Container | Notes |
|------------|------------|--------|-----------|-------|
| Standard | fits 40HQ | < 28t | 40HQ | Most common |
| Bulky | slightly over | < 28t | 40HQ + special packing | Check dimensions |
| Oversized (OOG) | > standard | varies | 40FR | Crane + permits required |
| Small quantity | < 15 CBM | < 10t | LCL | Confirm LCL separately |
| Heavy | > 28t | varies | 20GP / special | Check weight limits |

---

## Common Quotation Errors (Lessons Learned)

1. **Brazil helmet cleaning machine**: quoted without confirming LCL at Salvador; assumed door-to-door when Brazil is port-only; clearance assumed local when buyer has no CNPJ+RADAR entity
2. **USA mobile house**: quoted CIF to Elkhart Lake (inland); ignored 40FR OOG restriction (NY only)
3. **Exchange rate**: used real-time when boss fixed 6.5 for special client
4. **Dimensions**: used product dims instead of outer packing (0.84 vs 0.952 CBM)
5. **Regulation (v2.0)**: citing outdated regulation without re-checking validity → always verify + date