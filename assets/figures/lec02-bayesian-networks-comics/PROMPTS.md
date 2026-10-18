# 貝氏網路：四格漫畫分鏡與提示詞

使用內建 imagegen，每個核心觀念分別生成一張圖。修訂提示詞與原提示詞均保留；最終圖片為同目錄的 01–12.png／.jpg。詳見[驗證報告](REPORT.md)。

## 01 機率表太大，關係也不能全刪

- 原播放步驟：`lec02bn-u01-p3`
- 核心觀念：維度詛咒與稀疏依賴的折衷

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「機率表太大，關係也不能全刪」. Meaning and constraints: A full distribution of l binary variables has 2^l−1 free parameters. Six need63; twenty1,048,575. Fully independent binary variables need l. Sparse BN can save parameters only if the independence assumptions fit; no guarantee sparse always right. Storyboard: P1 student faces six binary switches and a giant cabinet: 「6 個二元變數，要估 63 個參數！」 P2 cabinet expands beyond the room, board 「20 個變數：1,048,575 個參數」 and student 「資料快不夠了！」 P3 robot erases ALL links between SIX plain dots (exactly six unconnected dots) and says 「完全獨立，卻可能漏掉關聯」. P4 robot carries a small schematic connected toolkit and says 「保留必要依賴，改用稀疏網路！」. The schematic is symbolic, no edge-count claim and no classmates-friendship metaphor equated with directional probability.
```
## 02 拆成連乘，不代表省參數

- 原播放步驟：`lec02bn-u02-p2`
- 核心觀念：鏈鎖規則與全部先前條件

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「拆成連乘，不代表省參數」. Meaning and constraints: The chain rule is an identity with no independence assumption: p(a,b,c)=p(a)p(b|a)p(c|a,b). It reorganizes a joint distribution but doesn't remove free parameters. Storyboard: P1 student holds a huge box labelled 「聯合機率」 and asks 「一次看全部，太難？」 P2 robot splits it into THREE boxes labelled exactly 「p(a)」「p(b｜a)」「p(c｜a,b)」 with multiplication signs between them. Dialogue 「按順序拆開！」 P3 student peers at the last box containing cards a and b: 「後面的條件還是全保留！」 P4 robot shows board 「p(a,b,c)＝p(a)p(b｜a)p(c｜a,b)」 and takeaway 「只是重寫，參數沒有自動變少！」. No independence claim, no literal temporal or causal claim based on the order.
```
## 03 真正省下來的是父集合

- 原播放步驟：`lec02bn-u02-p3`
- 核心觀念：父節點子集合與條件獨立假設

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「真正省下來的是父集合」. Meaning and constraints: For a topological order, assume p(x_i|all predecessors)=p(x_i|parents). Use original node x5 has only parent x4. This doesn't imply x5 marginally independent of all other nodes. Storyboard: P1 robot offers x5 a bulky folder labelled 「所有前面變數」; student 「每次都要全看？」 P2 robot selects ONLY card 「x₄」 from that folder, puts it inside a clearly labelled box 「A₅＝{x₄}」. Dialogue 「假設給定父節點就夠！」 P3 a clean graph ONLY 「x₄ → x₅」 and formula 「p(x₅｜x₁,x₂,x₃,x₄)＝p(x₅｜x₄)」. P4 student happily uses a smaller table: 「父集合變小，條件表才變小！」. Brief caution text 「條件獨立是模型假設」. No claim omitted predecessors are marginally independent.
```
## 04 箭頭有方向，沿路不能繞回

- 原播放步驟：`lec02bn-u03-p1`
- 核心觀念：有向無環圖、根節點與拓樸排序

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「箭頭有方向，沿路不能繞回」. Meaning and constraints: DAG nodes are random variables, edges parent to child; no directed cycles. Topological order exists. Generic BN edges alone do not establish causality. Storyboard: P1 student sees a simple chain of THREE labelled nodes 「A → B → C」: 「節點是變數，箭頭有方向！」 P2 robot points to A, label 「根節點：沒有父節點」; label over A→B arrow 「父 → 子」. P3 compare two small diagrams: a valid chain A→B→C with green tick and a directed triangle A→B→C→A with red X; balloon 「沿箭頭，不能繞回起點！」. Ensure the bad triangle is CLEARLY crossed out. P4 robot lines up three cards 「A、B、C」 under heading 「拓樸排序」; balloon 「每條箭頭都由前往後」 and small readable caption 「箭頭不自動證明因果」. Do not add extra arrows or self-loops.
```
## 05 有圖，還得有機率表

- 原播放步驟：`lec02bn-u03-p3`
- 核心觀念：根機率、CPT與聯合分布因子分解

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「有圖，還得有機率表」. Meaning and constraints: Original 6-node graph: roots x1,x2; parents x3:{x2},x4:{x1,x2},x5:{x4},x6:{x4,x5}. Joint is product of exactly six factors, not marginals for nonroots. Storyboard: P1 student holds a graph sketch with labels 「結構圖」 and asks 「只畫箭頭就完成模型？」 P2 robot attaches two root-probability badges 「p(x₁)」「p(x₂)」, says 「根節點要有機率！」 P3 robot attaches a little table clearly labelled 「CPT：條件機率表」 to a node card 「x₄」; table header 「父條件：x₁、x₂」 and balloon 「其餘節點，看父節點的組合」. P4 large board in TWO tidy lines: first 「p(x)＝p(x₁)p(x₂)p(x₃｜x₂)」 second 「×p(x₄｜x₁,x₂)p(x₅｜x₄)p(x₆｜x₄,x₅)」. Balloon 「每個節點一項，乘成聯合機率！」. Formula must show all six factors once, no omissions, no added edges needed.
```

修訂提示詞：

```text
Correct ONLY the diagrams in panels 1 and 2, keeping all Chinese dialogue, four-panel layout, characters, CPT panel3 and full six-factor equation panel4 unchanged. Panel1: replace the complex six-node diagram (which has a missing edge and clipped x6) with a SIMPLE THREE-NODE LOCAL diagram: x1 and x2 at top, x4 below, EXACTLY TWO arrows x1→x4 and x2→x4. Label it 「局部結構」. No x3,x5,x6 in panel1. Panel2: show ONLY TWO ISOLATED root circles x1 and x2, each with its probability badge p(x1),p(x2) adjacent. NO arrows in panel2, including no arrows from badges. Remove x3,x4,x5,x6 from panel2. This avoids an incorrect partial reconstruction of the six-node graph. All text and drawing must fit inside each panel, with no object crossing a gutter. Keep exact six-factor formula in panel4.
```
## 06 全部取一，六個因子相乘

- 原播放步驟：`lec02bn-u03-p4`
- 核心觀念：六節點聯合機率數值例

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「全部取一，六個因子相乘」. Meaning and constraints: Original example .3*.6*.8*.9*.7*.85=.077112; rounded .0771 uses approximation sign. Root factors .3,.6; others conditional on all their specified parents being1. This isn't all marginals multiplied or normalized after the product. Storyboard: P1 student sets SIX switches to 「1」, asks 「全部取一的機率？」. P2 robot picks two cards marked 「根機率」 with values 「0.3、0.6」; balloon 「先取根節點的機率」. P3 robot picks FOUR cards marked 「對應父條件下的機率」 with values exactly 「0.8、0.9、0.7、0.85」; caption 「指定的父節點皆為 1」. P4 clear equation split over two lines if needed 「0.3×0.6×0.8×0.9×0.7×0.85」 then 「＝0.077112 ≈ 0.0771」. Student 「每一項，都用對條件！」. No claim actual empirical frequency, no claim full CPT normalization was verified from these six numbers alone.
```

修訂提示詞：

```text
Correct ONLY the added labels/graph to match the original Bayesian network example. Panel1: REMOVE the entire A→C→E and B→D→F graph. Replace it with just SIX toggle switches, ALL set to1, labelled exactly x1,x2,x3,x4,x5,x6. No graph and no arrows in panel1. Panel2: keep values0.3 and0.6 but replace badge A with x1 and B with x2. Panel3: keep values0.8,0.9,0.7,0.85; replace badges C,D,E,F respectively with x3,x4,x5,x6, and give every green card the simple correctly spelled heading 「條件機率」. Preserve the existing balloon about parents all being1. Preserve all other dialogue, exact multiplication and result 0.077112≈0.0771 in panel4, the four-panel layout and style. Do not invent another graph.
```
## 07 知道中介，資訊就不同

- 原播放步驟：`lec02bn-u04-p4`
- 核心觀念：鏈狀網路的條件獨立與邊際相關

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「知道中介，資訊就不同」. Meaning and constraints: In chain x1→x2→x3, P(x2=1|x1=1)=.9, P(x2=1|x1=0)=.1, P(x3=1|x2=1)=.8, P(x3=1|x2=0)=.2. Unobserved x2 gives P(x3=1|x1)=.74 vs .26. Given x2=1, both x1 cases give .8. Storyboard: P1 simple exact THREE-node chain 「x₁ → x₂ → x₃」, middle node has a question-mark curtain, student 「還不知道 x₂！」. P2 robot shows table headed 「P(x₃＝1｜x₁)」 with two rows 「x₁＝1：0.74」「x₁＝0：0.26」 and says 「兩端仍然相關」. P3 robot lifts middle curtain to reveal 「x₂＝1」 and a NEW table headed 「P(x₃＝1｜x₂＝1,x₁)」 with two rows 「x₁＝1：0.80」「x₁＝0：0.80」. Balloon 「知道中介後，答案相同！」 P4 student takeaway 「給定 x₂ 後獨立，不等於原本獨立！」 and formula 「p(x₃｜x₂,x₁)＝p(x₃｜x₂)」. No claim conditioning always makes any graph independent; explicitly this chain.
```
## 08 數參數，要先數父節點

- 原播放步驟：`lec02bn-u05-p1`
- 核心觀念：二元CPT的自由參數計數

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「數參數，要先數父節點」. Meaning and constraints: For binary child and k binary parents, there are2^k parent configurations; each row needs ONE free probability for child=1 because child0=1-p. Don't count twice per row. All variables binary condition essential. Storyboard: P1 student stares at a CPT and asks 「這張表，要估幾個數？」 P2 robot displays one row with columns 「子節點＝1：p」 and 「子節點＝0：1−p」; says 「同一列，只需一個自由參數」. P3 a simple tally board headed 「父、子節點皆為二元」, three rows exactly 「0 個父節點 → 1 列」「1 個父節點 → 2 列」「2 個父節點 → 4 列」. P4 clear formula 「k 個二元父節點：2ᵏ 個自由參數」; student 「先數父組合，再數每列！」. No numerical CPT values added.
```
## 09 同樣六變數，六、十四、六十三

- 原播放步驟：`lec02bn-u05-p4`
- 核心觀念：逐節點參數加總與稀疏模型比較

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「同樣六變數，六、十四、六十三」. Meaning and constraints: Original parent counts0,0,1,2,1,2 yield1,1,2,4,2,4 total14; includes BOTH roots. Fulljoint63, independent6. Sparsegraph6 edges, fullyconnected DAG15edges but don't imply universal fixed saving or no accuracy loss. Sourcelecture notes13 if first root omitted, explicitly correct14. Storyboard: P1 robot inventories SIX node cards in two neat rows: 「x₁：1」「x₂：1」「x₃：2」「x₄：4」「x₅：2」「x₆：4」; student 「每個節點都算！」. P2 board exactly 「1＋1＋2＋4＋2＋4＝14」; robot emphasises 「根節點也不能漏！」. P3 THREE toolboxes labelled 「完全獨立：6」「本例網路：14」「完整聯合：63」, no fake proportional chart, no need countable graph. P4 student compares a small table and magnifier; board 「63÷14＝4.5」 and robot 「省參數，也要確認獨立假設！」. Never say the independent6 model is automatically naive Bayes, or that sparse model guarantees no accuracy loss.
```

修訂提示詞：

```text
Correct ONLY the unwanted network DIAGRAMS in panels2 and3, preserving ALL numbers, node parameter cards in panel1, Chinese dialogue, toolbox labels6/14/63 and calculation63÷14=4.5. The current diagrams do not match the source. Panel2: remove every network node and arrow below the sum. Replace with two simple root cards 「x1：根節點」「x2：根節點」, without any arrows. Keep 1+1+2+4+2+4=14 and 「根節點也不能漏！」 exactly. Panel3: under the first toolbox retain six isolated circles and 「每個節點各1個參數」. Under the MIDDLE toolbox remove the graph completely and replace with a simple text card 「父節點數：0、0、1、2、1、2」. Keep the rightmost probability-table illustration. Do not add ANY new network arrows. Four equal panels, original style.
```
## 10 從吸菸、疾病，連到檢測

- 原播放步驟：`lec02bn-u06-p1`
- 核心觀念：七變數醫療網路與六條有向邊

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「從吸菸、疾病，連到檢測」. Meaning and constraints: Illustrative source network ONLY S→C,S→H,C→C1,C→C2,H→H1,H→H2. Sevennodes sixedges; complete7nodeDAG21edges. Graph is model, not medical advice. No directS→tests, no C↔H edges. Storyboard: P1 robot introduces three icon cards 「S：吸菸」「C：肺癌」「H：心臟病」, student 「怎麼連成模型？」. P2 draw ONLY a three-node fork S at top, C bottom-left,H bottom-right with EXACTLY TWO arrows S→C and S→H. Caption 「模型中的依賴」. P3 a FULL CLEAN SEVEN-NODE diagram with top S, middle C left,H right, bottom C₁,C₂ under C and H₁,H₂ under H. EXACTLY SIX arrows: S→C,S→H,C→C₁,C→C₂,H→H₁,H→H₂. Bottom label 「四個檢測變數」. P4 robot says 「本例 7 節點，只用 6 條邊！」; board 「全連接 DAG：21 條邊」, short footer 「教學模型」. Each node appears exactly once per diagram; use only S,C,H,C₁,C₂,H₁,H₂ inside nodes to keep legible, no added causes or clinical claims.
```

修訂提示詞：

```text
Change ONLY panel4 bottom-right: REMOVE the entire dense purple network diagram. It currently has two-headed arrows and cycles, so it is not a DAG. Replace that diagram with a clean counting equation 「7×6÷2＝21」 and short caption 「依拓樸順序，每對節點最多一條向前邊」, with no graph, nodes or arrows in this panel. Keep the large heading 「全連接 DAG：21 條邊」, the student's/robot's speech 「本例7節點，只用6條邊！」 and footer 「教學模型」. Preserve panels1,2,3 exactly, especially the CORRECT seven-node tree and its six downward arrows. Maintain four-panel layout, colours and large readable Traditional Chinese text.
```
## 11 看清楚，誰是已知條件

- 原播放步驟：`lec02bn-u06-p2`
- 核心觀念：條件機率方向與示範數字

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「看清楚，誰是已知條件」. Meaning and constraints: Source fictional example P(C=true|S=true)=.20 is cancer probability GIVEN smoking, not P(smoking|cancer). Do not depict20% as clinical statistic, severity, causal effect or lifetime risk. Storyboard: P1 student holds a probability card 「P(C＝1｜S＝1)＝0.20」 and asks 「這個 0.20 怎麼讀？」. P2 robot covers the right side of the conditional bar with an arrow/marker highlighting ONLY 「S＝1」: 「已知條件：吸菸」. P3 robot highlights ONLY 「C＝1」 on the LEFT of the bar: 「要問的是：肺癌是否發生」. P4 student says 「給定吸菸，肺癌機率為 0.20」; essential large footer 「虛構示範，非臨床統計」 and short note 「不能把條件反過來讀」. Do not draw20 sick people or use patient portraits, and do not add any medical recommendation.
```
## 12 完全獨立，和單純貝氏差在哪

- 原播放步驟：`lec02bn-u06-p4`
- 核心觀念：完全獨立與NaiveBayes類別條件獨立的區分

```text
Use case: illustration-story. Create ONE finished Traditional-Chinese educational comic for a university Bayesian-networks lecture, accessible to beginners. Landscape 16:9; aim for EXACT 2048×1152 pixels. Exactly FOUR equal rectangular panels in a strictly aligned 2×2 grid, one vertical gutter at 50% width and one horizontal gutter at 50% of the grid; generous white gutters and margins. Reading order 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right. Same cute protagonists throughout: a short-haired student wearing a mustard-yellow hoodie and a friendly round teal robot tutor. Clean ink, soft flat colours, clear backgrounds and expressive narrative action. Large crisp Traditional Chinese text, only short dialogue and essential formulas below. No watermark or signature; do not add invented statistics or decorative math. All graph arrows must be correct; no ambiguous extra edges. Title: 「完全獨立，和單純貝氏差在哪」. Meaning and constraints: Scientific correction to original page. Empty all parent sets in full BN gives unconditional product∏p(xj), not standard naiveBayes classifier. NB has class C as parent of everyfeature: P(C,x)=P(C)∏p(xj|C). Features independent conditional on C, can be marginally dependent. Keep correction educational, no editing source. Storyboard: P1 student erases arrows and leaves exactly THREE isolated feature circles 「x₁」「x₂」「x₃」: 「父集合全清空？」. P2 robot labels these isolated nodes 「完全獨立」 and board 「p(x)＝∏ⱼ p(xⱼ)」. P3 NEW small clean diagram: top circle 「C 類別」 with EXACTLY THREE arrows downward, one each to three feature circles 「x₁」「x₂」「x₃」, NO arrows between features. Robot: 「單純貝氏，還保留類別 C！」. P4 large clear board 「P(C,x)＝P(C)∏ⱼ p(xⱼ｜C)」; takeaway 「給定類別後，才假設特徵獨立！」. Distinguish the two graphs clearly. No arrow reversed, no rootC omitted in formula, no claim unconditional independence under NB.
```

