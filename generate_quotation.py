#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cross-border-trade: Quotation Generator (Word/docx)
====================================================
Usage:
    python generate_quotation.py <input.json> [output.docx]

Input JSON schema (see templates/quotation-docx.md for field notes):
{
  "quote_no": "Q-20261026-001",
  "quote_date": "2026-10-26",
  "valid_until": "2026-11-25",
  "seller":  {"name": "Company Name", "contact": "Alice (email)"},
  "client":  {"name": "[Client Name]", "country": "Brazil",
              "destination": "Salvador, Brazil", "address_note": ""},
  "product": {"name": "Helmet Cleaning Machine", "model": "HC-2000",
              "hs_code": "8451.30", "qty": 1, "unit": "SET",
              "packing": "Wooden case 700x680x2000mm / 0.952 CBM / 144kg G.W."},
  "pricing": {
      "factory_price": 12000.0,
      "price_is_tax_inclusive": false,
      "tax_rate": 0.13,
      "profit_margin": 0.25,
      "exchange_rate": 6.5,
      "exchange_rate_note": "Fixed 6.5 per boss instruction"
  },
  "forwarder_costs": [
      {"item": "Ocean Freight (LCL, 1 CBM)", "amount": 1450.0, "currency": "USD", "confirmed": true},
      {"item": "Origin charges (起运港费)", "amount": 2945.0, "currency": "RMB", "confirmed": true},
      {"item": "Destination THC/CFS", "amount": 380.0, "currency": "USD", "confirmed": true}
  ],
  "insurance": {"basis": 1.10, "rate": 0.001},
  "trade_terms": "CIF Salvador CFS",
  "delivery_note": "Port-to-port. Inland trucking in Brazil arranged by buyer.",
  "edge_case_notes": [
      "【运输可达性】Destination port (Salvador) confirmed; inland to rural ZIP 45xxx-xxx is outside carrier standard service zone.",
      "【替代方案】Deliver to nearest CFS terminal in Salvador; buyer arranges last-mile pickup at own cost. No impact on quoted freight or lead time."
  ],
  "regulation_notes": [
      "Clearance in Brazil must be performed by a local entity holding CNPJ + RADAR per IN RFB 1.984/2020; this quote is CIF to port only."
  ],
  "payment_terms": "30% deposit by T/T, 70% against copy of B/L",
  "lead_time": "15-20 days after deposit",
  "currency": "USD",
  "language": "bilingual"
}

Calculation (company rule, per docs):
    tax_inclusive = factory_price * (1 + tax_rate)   [or factory_price if already incl.]
    with_profit   = tax_inclusive * (1 + profit_margin)
    product_usd   = with_profit / exchange_rate
    forwarder_usd = sum(item converted to USD at exchange_rate)
    insurance     = (product_usd + forwarder_usd) * basis * rate
    grand_total   = product_usd + forwarder_usd + insurance
"""

import json
import sys
import os

try:
    import docx
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn
except ImportError as e:
    sys.exit(f"python-docx required: pip install python-docx ({e})")


# ---------- helpers ----------

def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.makeelement(qn("w:shd"), {qn("w:val"): "clear", qn("w:color"): "auto", qn("w:fill"): hex_color})
    tcPr.append(shd)


def set_cell_text(cell, text, bold=False, size=9, align=None, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    if align:
        p.alignment = align
    run = p.add_run(str(text))
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    if color:
        run.font.color.rgb = RGBColor(*color)
    return p


def set_para(doc, text, size=10, bold=False, align=None, space_after=4, color=None):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(str(text))
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    if color:
        run.font.color.rgb = RGBColor(*color)
    return p


def fmt(n, currency="USD"):
    return f"{currency} {n:,.2f}"


def money(n):
    return round(float(n) + 1e-9, 2)


# ---------- main ----------

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python generate_quotation.py <input.json> [output.docx]')
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    out_path = sys.argv[2] if len(sys.argv) > 2 else "quotation_output.docx"

    parent = os.path.dirname(os.path.abspath(out_path))
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)

    lang = data.get("language", "bilingual")

    # --- pricing calculation ---
    p = data["pricing"]
    fx = float(p["exchange_rate"])
    factory = float(p["factory_price"])
    if p.get("price_is_tax_inclusive"):
        tax_incl = factory
        tax_amount = 0.0
    else:
        tax_amount = factory * float(p["tax_rate"])
        tax_incl = factory + tax_amount
    margin = float(p.get("profit_margin", 0.25))
    with_profit = tax_incl * (1 + margin)
    product_usd = with_profit / fx

    forwarder_usd = 0.0
    fwd_rows = []
    for c in data.get("forwarder_costs", []):
        amt = float(c["amount"])
        if c.get("currency") == "RMB":
            amt_usd = amt / fx
        else:
            amt_usd = amt
        forwarder_usd += amt_usd
        fwd_rows.append((c["item"], amt, c.get("currency", "USD"), amt_usd, c.get("confirmed", False)))

    ins = data.get("insurance", {})
    basis = float(ins.get("basis", 1.10))
    rate = float(ins.get("rate", 0.001))
    insurance = (product_usd + forwarder_usd) * basis * rate
    grand_total = product_usd + forwarder_usd + insurance

    currency = data.get("currency", "USD")

    # --- document ---
    doc = Document()

    # margins
    for section in doc.sections:
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)

    # Title
    if lang in ("en", "bilingual"):
        set_para(doc, "QUOTATION / 报价单", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
        set_para(doc, "Sales Quotation - Cross Border Trade", size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8, color=(0x66, 0x66, 0x66))

    # header info table
    seller = data.get("seller", {})
    client = data.get("client", {})
    info_rows = [
        ("Quote No. / 报价单号", data.get("quote_no", "")),
        ("Date / 日期", data.get("quote_date", "")),
        ("Valid Until / 有效期至", data.get("valid_until", "")),
        ("Seller / 卖方", str(seller.get("name", "")) + ("  " + seller.get("contact", "") if seller.get("contact") else "")),
        ("Buyer / 买方", str(client.get("name", ""))),
        ("Destination / 目的港", str(client.get("destination", ""))),
    ]
    t = doc.add_table(rows=len(info_rows), cols=2)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (k, v) in enumerate(info_rows):
        set_cell_text(t.rows[i].cells[0], k, bold=True, size=9)
        set_cell_bg(t.rows[i].cells[0], "EEF2F7")
        set_cell_text(t.rows[i].cells[1], v, size=9)

    # product table
    prod = data.get("product", {})
    set_para(doc, "", size=4)
    set_para(doc, "Product / 产品明细", size=12, bold=True, space_after=4)
    pt = doc.add_table(rows=2, cols=6)
    pt.style = "Table Grid"
    headers = ["Item / 序号", "Description / 品名", "Model / 型号", "HS Code", "Qty / 数量", "Unit / 单位"]
    for j, h in enumerate(headers):
        set_cell_text(pt.rows[0].cells[j], h, bold=True, size=9)
        set_cell_bg(pt.rows[0].cells[j], "DCE6F1")
    vals = ["1", str(prod.get("name", "")), str(prod.get("model", "")), str(prod.get("hs_code", "")),
            str(prod.get("qty", "")), str(prod.get("unit", ""))]
    for j, v in enumerate(vals):
        set_cell_text(pt.rows[1].cells[j], v, size=9)
    if prod.get("packing"):
        set_para(doc, "Packing / 包装: " + str(prod["packing"]), size=9, space_after=6)

    # costing table
    set_para(doc, "Cost Breakdown / 费用构成", size=12, bold=True, space_after=4)
    ct = doc.add_table(rows=1, cols=4)
    ct.style = "Table Grid"
    cheaders = ["Item / 项目", "Amount / 金额", "Currency / 币种", "USD Equivalent / 折合美元"]
    for j, h in enumerate(cheaders):
        set_cell_text(ct.rows[0].cells[j], h, bold=True, size=9)
        set_cell_bg(ct.rows[0].cells[j], "DCE6F1")

    def add_cost_row(label, amount, ccy, usd_equiv, bold=False, bg=None):
        row = ct.add_row()
        set_cell_text(row.cells[0], label, size=9, bold=bold)
        set_cell_text(row.cells[1], f"{amount:,.2f}", size=9, bold=bold)
        set_cell_text(row.cells[2], ccy, size=9, bold=bold)
        set_cell_text(row.cells[3], f"{usd_equiv:,.2f}", size=9, bold=bold)
        if bg:
            for c in row.cells:
                set_cell_bg(c, bg)

    add_cost_row("Product price incl. tax & 25% profit (base)", money(with_profit), "RMB", money(product_usd), bg="F7F9FC")
    for item, amt, ccy, usd_equiv, confirmed in fwd_rows:
        tag = "" if confirmed else "  (TBC)"
        add_cost_row(str(item) + tag, money(amt), ccy, money(usd_equiv))
    add_cost_row("Marine insurance (110% x 0.1%)", money(insurance), "USD", money(insurance))
    add_cost_row("TOTAL (Grand Total)", money(grand_total), currency, money(grand_total), bold=True, bg="DCE6F1")

    set_para(doc, f"Grand Total: {fmt(grand_total, currency)}  (Exchange rate {fx}; {p.get('exchange_rate_note','')})",
             size=11, bold=True, space_after=8)

    # terms
    set_para(doc, "Terms & Conditions / 条款与条件", size=12, bold=True, space_after=4)
    terms = [
        ("Trade Terms / 贸易术语", data.get("trade_terms", "")),
        ("Delivery / 交货说明", data.get("delivery_note", "")),
        ("Payment / 付款方式", data.get("payment_terms", "")),
        ("Lead Time / 交期", data.get("lead_time", "")),
    ]
    tt = doc.add_table(rows=len(terms), cols=2)
    tt.style = "Table Grid"
    for i, (k, v) in enumerate(terms):
        set_cell_text(tt.rows[i].cells[0], k, bold=True, size=9)
        set_cell_bg(tt.rows[i].cells[0], "EEF2F7")
        set_cell_text(tt.rows[i].cells[1], str(v), size=9)

    # special conditions / edge_case_notes
    edge_cases = data.get("edge_case_notes", [])
    if edge_cases:
        set_para(doc, "", size=4)
        set_para(doc, "Special Conditions / 特殊条款", size=12, bold=True, space_after=4)
        for ec in edge_cases:
            set_para(doc, "- " + str(ec), size=9, space_after=2)
        set_para(doc, "Disclaimer: Edge-case alternatives are quoted based on current information; actual feasibility to be reconfirmed before order confirmation.",
                 size=8, color=(0x88, 0x88, 0x88), space_after=4)

    # regulation notes (brief, as user required)
    regs = data.get("regulation_notes", [])
    if regs:
        set_para(doc, "", size=4)
        set_para(doc, "Compliance Notes / 合规说明（简要依据）", size=12, bold=True, space_after=4)
        for r in regs:
            set_para(doc, "- " + str(r), size=9, space_after=2)
        set_para(doc, "Term & validity: Regulation status verified as of quotation date; subject to change by issuing authority.",
                 size=8, color=(0x88, 0x88, 0x88), space_after=4)

    if data.get("remarks"):
        set_para(doc, "Remarks / 备注: " + str(data["remarks"]), size=9, space_after=6)

    # signature
    set_para(doc, "", size=8)
    set_para(doc, "Prepared by / 制单人: ____________________     Approved by / 审批: ____________________",
             size=9, space_after=2)

    doc.save(out_path)
    print(f"OK: quotation saved -> {out_path}")
    print(f"    Product USD base: {money(product_usd)} | Forwarder USD: {money(forwarder_usd)} | Insurance: {money(insurance)} | Grand Total: {money(grand_total)}")

    # write internal calculation detail file next to the quotation
    try:
        detail_lines = [
            "=== INTERNAL CALCULATION DETAIL (do NOT send to client) ===",
            f"Quote No        : {data.get('quote_no','')}",
            f"Date            : {data.get('quote_date','')}",
            f"Client          : {client.get('name','')} ({client.get('country','')})",
            f"Product         : {prod.get('name','')} x {prod.get('qty','')} {prod.get('unit','')}",
            f"Factory price   : {factory:,.2f} RMB (tax-inclusive input: {p.get('price_is_tax_inclusive', False)})",
            f"Tax rate        : {float(p.get('tax_rate',0))*100:.0f}% -> tax amount {tax_amount:,.2f} RMB",
            f"Tax-inclusive   : {tax_incl:,.2f} RMB",
            f"Profit margin   : {margin*100:.0f}% -> {tax_incl*margin:,.2f} RMB",
            f"With profit     : {with_profit:,.2f} RMB",
            f"Exchange rate   : {fx} ({p.get('exchange_rate_note','')})",
            f"Product USD     : {with_profit/fx:,.2f} USD",
        ]
        for item, amt, ccy, usd_equiv, confirmed in fwd_rows:
            tag = "" if confirmed else " (TBC)"
            detail_lines.append(f"Forwarder {item}{tag}: {amt:,.2f} {ccy} = {usd_equiv:,.2f} USD")
        detail_lines += [
            f"Forwarder USD   : {forwarder_usd:,.2f} USD",
            f"Insurance       : ({product_usd:,.2f} + {forwarder_usd:,.2f}) x {basis} x {rate} = {insurance:,.2f} USD",
            f"GRAND TOTAL     : {grand_total:,.2f} {currency}",
        ]
        if edge_cases:
            detail_lines.append("Edge-case / special scenario notes:")
            detail_lines += ["  - " + ec for ec in edge_cases]
        detail_lines += [
            "Regulations (brief citation):",
        ]
        detail_lines += ["  - " + r for r in regs]
        detail_lines.append("Validity: regulation status as of quotation date; re-verify before shipping.")
        detail_path = os.path.join(parent or ".", "calculation_detail_" + data.get("quote_date", "date") + ".txt")
        with open(detail_path, "w", encoding="utf-8") as f:
            f.write("\n".join(detail_lines))
        print(f"OK: calculation detail saved -> {detail_path}")
    except Exception as e:
        print(f"WARN: could not write calculation detail: {e}")


if __name__ == "__main__":
    main()