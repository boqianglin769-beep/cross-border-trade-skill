# Cross-Border Trade Execution Skill

> 一套面向中国出口贸易执行专员的通用 Agent Skill，覆盖从货代询价、目的国法规核实、CIF 报价生成（Word 报价单）到向老板汇报、催单跟进的全流程。适配 Codex、Skyl 及通用大模型平台。

---

## 适用场景

- **产品**：通用全品类 —— 移动房屋（Mobile Houses）、头盔清洗机（Helmet Cleaning Machines）、含电池/电子产品、化学品/液体、机械设备/大件（OOG）、普通货物等
- **起运地**：广东（广州/深圳/东莞等港口）及全国主要出口港
- **目的国/地区**：
  - **美洲**：美国（门到门、40FR OOG 仅纽约）、巴西（到港、客户自提、指定口岸清关）
  - **欧洲**：欧盟（德国/荷兰/法国等，新海关改革 (EU) 2026/2108）、英国（脱欧后独立规则）
  - **东南亚**：越南、泰国、新加坡
  - **中东**：阿联酋（电子发票分阶段）、沙特（SABER/SASO + ZATCA）
  - **东亚**：日本（2026 消费税改革、通关代理）、韩国
- **核心任务**：货代询价、港口核对、目的国法规与时效性核实、CIF 报价生成（Word 报价单）、老板汇报、催单话术、OOG 超限柜校验

---

## 包含内容

| 模块 | 文件 | 说明 |
|------|------|------|
| **主入口** | `SKILL.md` | 技能定义（v2.0）、触发指令、法规核实门（Gate A/B/C）、工作流分支、10 条硬规则 |
| **角色设定** | `agents/trade-agent.md` | 外贸执行专员身份、5 大职责、多国服务范围、10 条硬规则 |
| **询价工作流** | `workflows/inquiry.md` | 货代询价全流程：目的地核实、FCL/LCL 分开确认、费用拆分 |
| **报价工作流** | `workflows/quotation.md` | Step 0 法规核实门 + CIF 报价公式 + 汇率规则 + 生成 Word 报价单 + 13 项校验 |
| **校验工作流** | `workflows/validation.md` | OOG 超限货决策树、港口能力验证、Regulation Gate 多国对照表 |
| **法规库索引** | `regulations/_INDEX.md` | 六区域法规文件索引、时效性规则（Authority / Validity / Verified date） |
| **各国法规库** | `regulations/brazil.md` 等 6 文件 | 巴西、美国、欧盟、东南亚、中东、日韩 + `products.md` 产品准入规则，全部标注官方依据与时效性 |
| **报价单脚本** | `scripts/generate_quotation.py` | 输入 JSON（产品报价+货代信息+汇率+法规说明）→ 直接生成 Word 报价单 + 计算明细 |
| **报价单说明** | `templates/quotation-docx.md` | JSON 字段对照、计算公式、各国合规说明简要写法 |
| **示例输入** | `templates/sample-quotation.json` | 可直接运行的示例报价输入（巴西场景占位数据） |
| **英文询价模板** | `templates/enquiry.md` | WhatsApp/Email 英文询价模板（标准/LCL/OOG/跟进） |
| **中文跟进模板** | `templates/follow-up.md` | 微信催货代、催工厂、给老板汇报话术 |
| **报价核对表** | `templates/checklist.md` | CIF 报价前 67 项自检清单（含第七部分法规与时效性核对） |
| **报价校验器** | `templates/cif-validator.md` | 逐项验证报价单计算、文档完整性与法规时效性（D1–D4） |
| **使用说明** | `README.md` | 本文件 |
| **开源协议** | `LICENSE` | MIT License |

---

## 快速开始

### 方式一：直接复制提示词（通用大模型）

1. 打开 `agents/trade-agent.md`，复制全文
2. 粘贴到你的 AI 对话中作为 System Prompt 或角色设定
3. 输入触发指令开始使用，如：
   - `询价 巴西 Salvador` → 启动货代询价流程
   - `做报价` → 启动法规核实 + CIF 报价生成（Word 报价单）
   - `汇报` → 生成给老板的双语汇报
   - `催货代` → 生成跟进话术
   - `校验 OOG` → 启动超限货验证

### 方式二：导入 Skill 文件（支持 Skill 格式的平台）

1. 将整个 `cross-border-trade/` 目录复制到你的 Agent 平台的 skills 目录
2. 确保 `SKILL.md` 位于目录根级别
3. 平台会自动识别触发指令并加载工作流

### 方式三：用脚本生成本机 Word 报价单

```bash
# 1. 安装依赖（只需 python-docx）
python -m pip install python-docx

# 2. 编辑示例输入文件，填入实际产品报价与货代信息
#    templates/sample-quotation.json

# 3. 运行脚本生成 Word 报价单 + 计算明细（输出在当前目录 quotation_output/）
cd cross-border-trade
python scripts/generate_quotation.py templates/sample-quotation.json
```

脚本输出：
- `quotation_output/quotation_[客户]_[日期].docx` —— 面向客户的正式报价单（含合规简要说明）
- `quotation_output/calculation_detail_[日期].txt` —— 内部计算明细（税额、利润、汇率、货代费、保险、总价全部可追溯）

### 方式四：GitHub 导入（Codex / 支持远程 Skill 的平台）

```bash
git clone https://github.com/[your-username]/cross-border-trade-skill.git
```

---

## 触发指令速查表

| 指令 | 功能 | 对应文件 |
|------|------|----------|
| `询价 [目的地]` | 货代询价工作流 | `workflows/inquiry.md` |
| `做报价` / `CIF` | 法规核实 + CIF 报价生成（Word 报价单） | `workflows/quotation.md` + `scripts/generate_quotation.py` |
| `汇报` / `给老板` | 老板汇报话术 | `templates/follow-up.md` |
| `催货代` / `催工厂` | 跟进话术 | `templates/follow-up.md` |
| `校验 OOG` / `检查` | 超限货验证 | `workflows/validation.md` |
| `巴西航线` | 巴西规则（CNPJ+RADAR、到港自提、指定口岸） | `regulations/brazil.md` |
| `美国航线` | 美国规则（IOR、EO 14411、40FR 仅纽约） | `regulations/usa.md` |
| `欧盟 / 欧洲` | 欧盟规则（UCC 改革、EORI、PID） | `regulations/eu.md` |
| `东南亚 / 越南 / 泰国 / 新加坡` | 东南亚规则 | `regulations/southeast-asia.md` |
| `中东 / 阿联酋 / 沙特` | 中东规则（电子发票、SABER/ZATCA） | `regulations/middle-east.md` |
| `日本 / 韩国` | 日韩规则 | `regulations/japan-korea.md` |
| `产品准入 / UN38.3 / MSDS` | 产品合规（电池、液体、机械） | `regulations/products.md` |
| `报错提醒` / `教训` | 常见错误提醒 | `templates/checklist.md` |
| `全流程` | 完整流程总览 | `SKILL.md` |

---

## 核心规则（硬约束）

1. **不编造船期** — 只能报货代书面确认的船期和航程
2. **不私自承诺运费** — 所有费用必须有货代书面确认，未确认的标"预算/TBC"
3. **区分 CIF / DAP / EXW** — CIF 是到港价，DAP 是到门价，EXW 不含出口费用，不能混淆
4. **用包装尺寸** — 运费计算必须用外箱尺寸，不能裸产品尺寸
5. **FCL ≠ LCL** — 整柜能做不代表拼箱能做，必须分开确认
6. **法规核实门（Gate）** — 报价前必须核实目的国进口清关主体、门到门可行性、产品准入，未核实不得出价
7. **官方依据 + 时效性** — 所有法规内容标注来源（Authority）、生效/废止状态（Validity）、核实日期（Verified date）；报价单内仅简要提及，不完整摘录法条
8. **含税加利润** — 25% 利润加在含税基础上，顺序不能错；税点 13%/10% 逐单向工厂确认
9. **巴西到港** — 境外（中国）货代不能作为巴西 IOR，清关主体须为持 CNPJ+RADAR 的本土主体；客户自提，不含内陆
10. **未确认收支默认保守** — 不确定的费用标 `(TBC)`，不猜测、不编造；时效敏感法规执行前必须复核最新状态

---

## 法规库与时效性说明（v2.0 核心）

所有法规文件采用统一时效性标注：

```
**Authority**  ：法规名称与官方来源（如 IN RFB nº 1.984/2020）
**Validity**   ：现行有效（截至核实日）/ 已废止 / 待生效（含生效日期）
**Verified**   ：核实日期（YYYY-MM-DD）
**Note**       ：官方原文可查位置或验证途径
```

重要提示：
- 巴西：IN RFB nº 1.984/2020 + Decreto nº 6.759/2009 现行有效（截至 2026-10-26）；RFB 于 2026-06-18 起就整合进口清关规章的 IN 草案征求意见，未来可能合并修订，执行前须复核
- 美国：EO 14411（2026-06-03 签署）重塑 IOR 监管，CBP 90–180 天内出台配套细则；19 CFR 141.1(b) 现行
- 欧盟：(EU) 2026/2108 已于 2026-09-20 生效、2027-09-21 适用并废止 UCC (EU) 952/2013；(EU) 2026/1022 要求 2026-11-01 起 M-PID 必填
- 东南亚/日韩部分细则官方原文未锚定，法规库已标 `[待核实]`，使用前须按库内指引复核

---

## 适配平台

| 平台 | 适配方式 | 状态 |
|------|----------|------|
| **OpenAI Codex** | 复制 `agents/trade-agent.md` 作为 system prompt | ✅ 已验证 |
| **Skyl / 百度智能体** | 导入 Skill 目录，配置触发词 | ✅ 支持 |
| **通用 ChatGPT / Claude** | 复制角色定义 + 工作流程作为 prompt | ✅ 支持 |
| **Dify / FastGPT** | 导入为 Agent Skill，配置工具调用 | ✅ 支持 |
| **其他大模型平台** | 使用 Markdown 格式导入 | ✅ 通用 |

---

## 脱敏说明

本 Skill 已做隐私脱敏处理：

- ❌ 不包含：客户邮箱、老板/同事私人联系方式、货代微信、真实工厂地址、报价底价、订单成本、佣金信息
- ✅ 全部替换为占位符：`[客户名称]`、`[货代对接人]`、`[目标港口]`、`[工厂名称]`
- ✅ 仅保留：流程框架、话术模板、工作逻辑、校验规则、公开法规依据

你可以根据实际业务替换占位符后直接使用。

---

## 版本历史

- **v2.0.0** (2026-10-26): 通用化升级 —— 覆盖巴西/美国/欧盟/东南亚/中东/日韩六区域、新增法规库（含官方依据与时效性标注）、新增 Word 报价单自动生成脚本与模板、新增法规核实门（Gate A/B/C）、核对表升级至 67 项
- **v1.0.0** (2026-10-26): 初始版本，基于巴西头盔清洗机项目和美国威斯康星州移动房屋项目实战复盘

---

## 贡献与反馈

欢迎提交 Issue 或 PR 改进这套 Skill：

- 发现流程漏洞或报错案例
- 补充新的国家/地区规则（附官方依据与时效性）
- 优化话术模板
- 增加多语言支持

---

## License

MIT License — 详见 [LICENSE](LICENSE) 文件。

---

> **一句话总结**：导入这套 Skill，输入"询价 巴西 Salvador"或"做报价"，Agent 会自动核实目的国法规（含官方依据与时效性）、引导你完成从询价到报价的全流程，并直接用脚本输出面向客户的 Word 报价单，避免报错、漏项、踩坑。