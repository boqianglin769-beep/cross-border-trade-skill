# Template: 报价单生成说明（Quotation JSON → Word/docx）

## 工作方式

绑定本 Skill 的 Agent 在拿到 **产品报价信息** 与 **货代确认信息** 后：

1. 按 `scripts/generate_quotation.py` 的输入 JSON 结构组织数据；
2. 依 `regulations/` 法规库核实目的国清关主体、门到门可行性、产品准入要求，并把合规结论写入 `regulation_notes`（**简要提及法规名称即可，不写完整法条**）；
3. 运行脚本生成 Word 报价单（.docx），发给客户前完成 `templates/cif-validator.md` 校验与老板审批。

## JSON 字段对照说明

| 字段 | 说明 | 必填 | 示例 |
|------|------|------|------|
| `quote_no` | 报价单号（公司内部编号） | ✅ | `Q-20261026-001` |
| `quote_date` | 报价日期 YYYY-MM-DD | ✅ | `2026-10-26` |
| `valid_until` | 有效期（通常 15-30 天） | ✅ | `2026-11-25` |
| `seller.name/contact` | 公司名、联系人 | ✅ | `[公司名称]` / `[邮箱]` |
| `client.name` | 客户名称（脱敏占位符） | ✅ | `[客户名称]` |
| `client.country` | 目的国 | ✅ | `Brazil` |
| `client.destination` | 目的港/目的城市（完整名称） | ✅ | `Salvador, Brazil` |
| `client.address_note` | 门到门完整地址（含邮编） | 门到门时 | `[地址] [ZIP]` |
| `product.name/model/hs_code` | 品名、型号、HS 编码（美/日 8 位、沙特 12 位规则见 regulations） | ✅ | `Helmet Cleaning Machine` / `HC-2000` / `8451.30` |
| `product.qty/unit` | 数量与单位 | ✅ | `1` / `SET` |
| `product.packing` | **包装后**外尺寸、体积、毛重（不能用裸产品尺寸） | ✅ | `Wooden case 700x680x2000mm / 0.952 CBM / 144kg G.W.` |
| `pricing.factory_price` | 工厂价（RMB） | ✅ | `12000.0` |
| `pricing.price_is_tax_inclusive` | 工厂价是否已含税 | ✅ | `false` |
| `pricing.tax_rate` | 税点（13% 或 10%，**逐单向工厂确认**） | ✅ | `0.13` |
| `pricing.profit_margin` | 利润率（默认 0.25，25% 加在含税基础上） | ✅ | `0.25` |
| `pricing.exchange_rate` | 汇率（实时 or 老板固定，如巴西 6.5） | ✅ | `6.5` |
| `pricing.exchange_rate_note` | 汇率来源说明 | ✅ | `Fixed 6.5 per boss instruction` |
| `forwarder_costs[]` | 货代确认费用明细（金额、币种、是否书面确认） | ✅ | 见下 |
| `insurance.basis/rate` | 保险基数与费率（默认 110% × 0.1%） | 🟡 | `1.10` / `0.001` |
| `trade_terms` | 贸易术语（CIF [港口] / DAP / FOB） | ✅ | `CIF Salvador CFS` |
| `delivery_note` | 交货范围说明（到港/到门、内陆由谁负责） | ✅ | 见示例 |
| `edge_case_notes[]` | **特殊场景简要说明**（风险提示 + 替代方案） | 🟡 | 见特殊场景标注示例 |
| `regulation_notes[]` | **合规依据简要说明**（法规名称 + 一句结论） | ✅ | `Clearance in Brazil requires local CNPJ + RADAR holder per IN RFB 1.984/2020; quote is CIF to port only` |
| `payment_terms` | 付款方式（T/T、L/C） | ✅ | `30% deposit, 70% against B/L copy` |
| `lead_time` | 交期 | 🟡 | `15-20 days after deposit` |
| `currency` | 报价币种（默认 USD） | ✅ | `USD` |
| `language` | `en` / `bilingual` | 🟡 | `bilingual` |

> `delivery_note` 示例：
> ```
> Port-to-port. Inland trucking in Brazil arranged by buyer.
> 【偏远地址限制】Buyer address (Rural district, ZIP 45xxx-xxx) is outside carrier's standard service zone. 
>   Alternative: Delivery to nearest CFS terminal in Salvador; buyer arranges last-mile pickup. 
>   Cost impact: USD 0 (buyer bears inland); lead time unchanged.
> ```
>
> `forwarder_costs` 每项：`{"item": "费用名", "amount": 金额, "currency": "USD"|"RMB", "confirmed": true|false}`；
> 未书面确认的项目，脚本自动在费用名后标注 `(TBC)`，不得当作确认价。

## 计算规则（脚本内置，与公司规则一致）

```
税额      = 工厂价 × 税点            （工厂价已含税则跳过）
含税价    = 工厂价 + 税额
含利润价  = 含税价 × 1.25            （25% 利润加在含税基础上）
产品美元价 = 含利润价 ÷ 汇率
货代美元合计 = Σ（各费用项折算美元，RMB 项 ÷ 汇率）
保险      = (产品美元价 + 货代美元合计) × 110% × 费率
总价      = 产品美元价 + 货代美元合计 + 保险
```

## 特殊场景标注示例

以下三种典型特殊场景，应在 `edge_case_notes` 中以**一句话风险 + 一句话替代方案**的格式写入；脚本自动输出到报价单 "Special Conditions / 特殊条款" 区域。

### 1. 运输可达性受限
```json
"edge_case_notes": [
  "【运输可达性】Destination port (Salvador) confirmed by forwarder; inland trucking to rural ZIP 45xxx-xxx is outside carrier standard service zone.",
  "【替代方案】Deliver to nearest CFS terminal in Salvador; buyer arranges last-mile pickup at own cost. No impact on quoted ocean freight or lead time."
]
```

### 2. 产品属性突变（电压/认证差异）
```json
"edge_case_notes": [
  "【产品属性突变】Default model HC-2000 runs on 380V/3-phase. Buyer requested 220V/1-phase variant, which requires alternate motor and CE re-verification.",
  "【替代方案】Switch to HC-2000-LV (220V certified variant). Factory price +RMB 800; lead time +5 days for additional testing. Quote below reflects HC-2000-LV pricing."
]
```

### 3. 条款对齐冲突（客户 PO 与报价条款不一致）
```json
"edge_case_notes": [
  "【条款对齐】Client PO states DDP terms; this quotation is CIF to port per company standard for Brazil. DDP would require local IOR, import VAT prepayment, and inland liability transfer.",
  "【替代方案】Maintain CIF to port in this quote; append optional DDP addendum if client provides valid Brazil IOR and accepts 12% import VAT advance."
]
```

**原则**：`edge_case_notes` 仅列“已识别、已评估、已给出替代方案”的风险；未确认的风险不入报价单正文，改写入内部明细供追溯。

## 生成示例

```bash
cd scripts
python generate_quotation.py ../templates/sample-quotation.json "C:/Users/.../报价单_Q20261026-001.docx"
```

## 合规说明书写法（对客户可见，只"大致提及"）

- **巴西**：`进口清关须由持 CNPJ+RADAR 的巴西本土主体办理（IN RFB 1.984/2020），本报价为 CIF 到港价，内陆段由买方安排。`
- **美国**：`买方或其指定美国代理作为 IOR 完成进口申报（19 CFR 141.1 / 现行 CBP 规则）；本报价按 CIF 港口计，内陆段另议。`
- **欧盟**：`非欧盟卖方进口须由欧盟境内进口方（EORI 持有人）清关；本报价按 CIF 港口计（现行 UCC 952/2013，过渡至 (EU) 2026/2108）。`
- **产品（锂电池/化学品）**：`产品含锂电池，按 UN38.3 与 IMDG 第 9 类危险品申报，须提供 UN38.3 报告及 MSDS/SDS（详见附件）。`

**原则**：报价单正文出现法规名称 + 一句话结论即可；完整法条、复核过程与官方链接保存在内部工作底稿（`regulations/`）供追溯，不写入客户报价单。