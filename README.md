# 研究项目模板

这是一个遵循 KISS 原则的人机协作研究模板。模板只规定必要的文件职责，不预建空的数据、脚本、图片或模块目录。

## 核心分工

- `AGENTS.md`：人维护的最高项目约束，记录工作流程和项目规范，agent 只读不改。
- `manual.md`：人维护的全文骨架，规定文章主线、章节顺序和跨模块关系。
- `modules/<模块>/manual.md`：人维护的模块内容。模块存在真实工作时再创建。
- `docs_graph/agent_notes.md`：agent 维护的项目进度、上下文入口、自动纠偏和用户画像（协作习惯）。
- `project_points/`：agent 维护的项目笔记与关系图，保存短技术点、证据状态、模型假设、否定结果和决策关系。
- 最终报告、检索记录、数据、脚本和图片：agent 执行并维护，人负责验收。

Agent 不在人工手稿旁维护第二份竞争性结构。对人工手稿的理解先在讨论中确认；执行进度和用户协作习惯进入 `docs_graph/agent_notes.md`，技术依据进入 `project_points/`，正式表达进入最终报告。

## 权威顺序

发生冲突时按照以下顺序处理：

```text
用户当前明确指令
> AGENTS.md
> 根目录 manual.md
> 模块 manual.md
> 已核验的原始证据和可复现数据
> docs_graph/agent_notes.md
> agent 推断
```

根目录与模块 `manual.md` 出现冲突时，agent 停止相关写作并向人说明，不自行选择。

## 推荐结构

```text
.
├── README.md
├── AGENTS.md
├── manual.md
├── docs_graph/
│   └── agent_notes.md
└── project_points/
    ├── README.md
    ├── skill.md
    ├── graph.py
    ├── nodes.jsonl
    ├── edges.jsonl
    └── index/
        └── README.md
```

真实工作出现后再增加：

```text
modules/<模块>/manual.md   # 人写的模块内容
sources/                  # 原始论文、标准和来源记录
data/                     # 输入数据和生成表格
scripts/                  # 可复现命令和程序
figures/                  # 有来源或脚本的图片
writing/                  # 正式稿和编译产物
```

## 协作模式

### 讨论模式

用户说“先讨论”“只看”“不要修改”时立即进入只读模式。Agent 可以读取文件、指出定义冲突和提出选项，但不编辑、不提交，也不启动会写入项目的生成程序。

### 定稿模式

把讨论结果分成：已接受、已否决、暂定假设、仍未确定、正文内容和附录内容。数学对象、概率事件、单位、坐标系、参考面和证据边界在这里确定。

### 执行模式

只有用户明确要求执行后，agent 才修改文件、调研、计算、编译和渲染。只读审计可在讨论模式或执行验收阶段进行。Git 提交是独立操作，执行授权不自动包含提交；用户当前指令或 `AGENTS.md` 必须明确要求提交。

## 人工手稿用法

根目录 `manual.md` 只描述全文主线和模块关系。具体内容写入对应模块的 `manual.md`：

```text
modules/
├── background/manual.md
├── physical_model/manual.md
├── manufacturing/manual.md
└── comparison/manual.md
```

模块名按项目实际内容确定，不要求使用上面的示例。Agent 默认只读人工 `manual.md`；需要改动时必须由用户明确授权。

## Project Points 用法

模板使用现有 `project_points` 实现管理项目笔记。它采用 JSONL 作为事实源，不依赖数据库、MCP 或 embedding。

常用命令：

```bash
python3 project_points/graph.py search "关键词"
python3 project_points/graph.py add "技术点" --kind claim --tags topic --evidence pending
python3 project_points/graph.py link P0001 P0002 --relation depends_on --note "依赖原因"
python3 project_points/graph.py node P0001
python3 project_points/graph.py neighborhood P0001
```

写入前先搜索，避免重复节点。节点保持简短；长推导、论文摘录、图片和数据放到对应项目文件中，再用 `source_hint` 或 `note` 指向它们。

## 初始化步骤

1. 修改项目名称、许可证和 Git remote。
2. 由人填写 `AGENTS.md` 的项目目标、范围、流程、交付物和停止条件。
3. 由人填写根 `manual.md`；存在具体模块时再创建模块 `manual.md`。
4. 由 agent 根据人工文件更新 `docs_graph/agent_notes.md`，记录进度、上下文入口、注意事项和简洁的用户画像。
5. 清空模板的 `project_points/nodes.jsonl` 与 `edges.jsonl`，再写入真实项目点。
6. 检查 `docs_graph/agent_notes.md`，确认当前进度和下一步。
7. 完成首次稳定提交。

项目合同、完整流程、根 `manual.md` 主线和当前任务仍为占位内容时，不开始实质研究或写作；用户明确限定的小型初始化任务除外。

## 完成标准

- 人工要求只存在于 `AGENTS.md` 和各级 `manual.md`，没有第二份 AI 手稿与其竞争。
- 关键事实可回到论文、标准、官方规格、源代码或原始数据本身；搜索平台只用于发现来源。
- 正文只呈现确定后的论证，搜索、纠错和 agent 思考过程留在项目记录中。
- 模型明确变量、单位、参考面、一般形式、近似条件、证据和复现方法。
- docs graph、project points、生成物与 Git 提交保持同步。
