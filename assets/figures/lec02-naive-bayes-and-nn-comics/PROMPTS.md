# 四格漫畫分鏡與提示詞

來源：`slides/lec02-naive-bayes-and-nn.jbd.json`。以內建 imagegen 生成，每概念一張獨立圖像；圖片及衍生簡報另見 [驗證報告](REPORT.md)。

## 01 高維機率表，塞爆了！

- 原步驟：`lec02nn-u01-p3`
- 核心觀念：指數成長與獨立假設的資料需求
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「高維機率表，塞爆了！」. Scientific meaning and constraints: Joint table has 2^10 combinations and 1023 independent probability values. The independent binary marginal table stores 10×2 entries, but only 10 are free; don't call the 20 entries free parameters. Four-panel storyboard: P1 student faces ten on/off feature switches: 「10 個二元特徵！」 P2 a huge stack of combination cards bursts out: 「2¹⁰＝1024 種組合！」 P3 robot packs separate two-cell tables into ten drawers, label 「各特徵分開估」 and 「10×2＝20 格」. P4 student carries a smaller case happily: 「獨立假設，資料需求大減！」. Show symbolic table stacks, no impossible exact grid counting. Do not reproduce the source's vague N^l sample formula as a universal law.
```

修訂提示詞：

```text
Edit ONLY the tiny probability-table labels in panels 3 and 4, and remove the faint watermark at bottom-right if present. Within EVERY small probability table with column labels 0 and 1, the probability below 0 must be 1−p and the probability below 1 must be p. This matches the convention p=P(feature=1) used throughout the lesson. Correct all ten little drawer tables in panel 3 and all little suitcase tables in panel 4 consistently. Preserve the 10 feature switches in panel1, all large Chinese speech balloons and formulas 2^10=1024 and 10×2=20, all four panels, characters, colours and layout. No new text, signatures or watermark.
```
## 02 對數：小數連乘變連加

- 原步驟：`lec02nn-u02-p2`
- 核心觀念：單調對數、下溢與先驗
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「對數：小數連乘變連加」. Scientific meaning and constraints: For strictly positive class scores, log is strictly increasing. General MAP score includes class prior. Equal priors may be omitted. Four-panel storyboard: P1 student multiplies a long train of tiny positive decimal blocks: 「小數一直乘，電腦快歸零！」 P2 robot switches multiplication gears to addition gears: 「取對數，改成連加！」 P3 chalkboard exactly 「sᵢ＝ln P(Cᵢ)＋Σⱼ ln p(xⱼ｜Cᵢ)」 and robot says 「先驗也要算進去」. P4 two podiums preserve their ordering: 「對數單調，勝出類別不變！」 with short caption 「比較正值分數」. No claim that raw log score is a probability.
```

修訂提示詞：

```text
Change ONLY the numerical multiplication illustration in panel 1 (top-left). Replace the added decimal numeric expression and its numeric result with a simple symbolic illustration: 「p₁×p₂×⋯×pₗ」 and a downward arrow to 「很小的正值」. Do not add any numerical product or numeric result. Preserve every other panel, all Traditional Chinese text, exact log-score formula and class ordering, characters, colours, image aspect ratio and 2×2 grid.
```
## 03 先知道類別，再假設獨立

- 原步驟：`lec02nn-u02-p3`
- 核心觀念：條件獨立與相關性限制
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「先知道類別，再假設獨立」. Scientific meaning and constraints: Independence is conditional on class, an assumption, not an empirical fact. Correlated duplicated evidence can exaggerate confidence. Four-panel storyboard: P1 student holds an email and two clue cards: 「線索能直接相乘嗎？」 P2 robot opens box labelled 「已知類別 C」; within it two separate feature drawers labelled 「x₁」「x₂」. Robot: 「先假設：給定類別後獨立」. P3 a clear board 「p(x₁,x₂｜C)＝p(x₁｜C)p(x₂｜C)」. P4 robot spots two linked duplicate clues; student surprised: 「高度相關，可能重複計算證據！」. Bottom short takeaway 「省資料，也可能估錯機率」. Linked clue illustration is an analogy, not a literal causal graph.
```
## 04 沒出現的字，也有一票

- 原步驟：`lec02nn-u03-p3`
- 核心觀念：Bernoulli特徵與未出現機率
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「沒出現的字，也有一票」. Scientific meaning and constraints: For binary word presence x=1 use p; absence x=0 use 1-p. Original email x=(1,1,0,1); third word ham presence=.4 so absence=.6. Four-panel storyboard: P1 email shows four little feature cards exactly 「1、1、0、1」. Student: 「第三個字沒出現，跳過？」 P2 robot points to an empty word slot: 「沒出現，也是線索！」 P3 a two-door probability cabinet: 「出現：p」 and 「未出現：1−p」. P4 robot writes exactly 「1−0.4＝0.6」, label 「非垃圾郵件：第三字詞未出現」. Student: 「0 也要乘進去！」. No claim every naive Bayes variant counts absent words; this comic concerns binary presence indicators.
```

修訂提示詞：

```text
Change ONLY the student's speech balloon in panel 4 (bottom-right). Replace 「0 也要乘進去！」 with the exact Traditional Chinese text 「未出現機率也要算！」. Preserve all other content, including the formula 1−0.4＝0.6, binary feature vector 1,1,0,1, cabinet probabilities p and 1−p, characters, art and layout.
```
## 05 先驗加權，才是分類分數

- 原步驟：`lec02nn-u03-p4`
- 核心觀念：概似、先驗、正規化與事後決策
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「先驗加權，才是分類分數」. Scientific meaning and constraints: Verify 0.4×.072=.0288; .6×.0006=.00036; sum .02916; spam posterior .0288/.02916=.98765432. Four-panel storyboard: P1 two mail carts labelled 「垃圾」「非垃圾」 carry 「概似 0.072」 and 「概似 0.0006」. Student asks 「還差什麼？」 P2 robot adds prior badges and board 「0.4×0.072＝0.0288」「0.6×0.0006＝0.00036」. Balloon 「乘上先驗！」 P3 clearly label these outputs 「未正規化分數」; normalization machine board 「0.0288＋0.00036＝0.02916」. P4 result stamp 「判為垃圾郵件」 with board 「0.0288÷0.02916 ≈ 98.77%」 and short takeaway 「同除分母，勝負不變」. These are model estimates, no claim certainty or empirical accuracy.
```
## 06 分數大，不等於機率大於一

- 原步驟：`lec02nn-u03-p6`
- 核心觀念：對數勝算與sigmoid
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「分數大，不等於機率大於一」. Scientific meaning and constraints: For binary log posterior odds g=4.382027, P(spam|x)=1/(1+e^-g)=.987654. Mapping is valid because g is this log odds, not an arbitrary linear score. Four-panel storyboard: P1 robot shows original four-word email score 「g＝4.382027」; student: 「機率超過 1？！」 P2 robot shakes head, clearly labels the score 「對數勝算」 and says 「這是分數！」. P3 a clean transformation gate with exact formula 「P＝1／(1＋e⁻ᵍ)」, caption 「二類別的對數勝算」. P4 the same email exits with badge 「P(垃圾｜郵件)≈0.987654」; student: 「約 98.77%，這才是機率！」. No graph needed; never imply all classifier scores use this mapping.
```

修訂提示詞：

```text
Correct ONLY the four-panel grid geometry: the four panels must be equal-sized rectangles in a strict aligned 2×2 grid. A single straight vertical white gutter at exactly 50% of the page width must continue from the top row to the bottom row. Keep title above grid, equal left/right widths and equal row heights, no cropping text or formulas. Preserve exact content and readable large Chinese text, formula P=1/(1+e^-g), g=4.382027 and result 0.987654. Recompose contents to fit equal panels.
```
## 07 二元線索，加權成直線

- 原步驟：`lec02nn-u03-p7`
- 核心觀念：Bernoulli單純貝氏線性權重與邊界
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「二元線索，加權成直線」. Scientific meaning and constraints: Weights w_i=ln[p_i(1-q_i)/(q_i(1-p_i))] for 0<p_i,q_i<1, bias includes priors. A two-feature decision boundary g=0 is a line, binary inputs are four corners not continuous probabilities. Four-panel storyboard: P1 student drops binary clue cards 「0」「1」 into a robot calculator: 「每個線索怎麼算？」 P2 each card receives a weight; board exactly 「wᵢ＝ln[pᵢ(1−qᵢ)／(qᵢ(1−pᵢ))]」. Short label 「0＜pᵢ,qᵢ＜1」. P3 board 「g(x)＝wᵀx＋w₀」 with balloon 「加權相加，偏項含先驗」. P4 very simple schematic two-dimensional plane without numeric ticks, a diagonal straight separator labelled 「g＝0」, orange side 「g＞0」 and blue side 「g＜0」, no plotted sample points. Student: 「兩個特徵，邊界就是直線！」. Geometry must have consistent class sides, do not include a curved boundary.
```
## 08 先找最近，再來投票

- 原步驟：`lec02nn-u04-p2`
- 核心觀念：kNN選鄰居與多數票
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「先找最近，再來投票」. Scientific meaning and constraints: Choose neighbors by distance ignoring labels. Original example k=11 with 7 red and 4 black, fractions are vote shares not calibrated true probabilities. Four-panel storyboard: P1 query star at centre of an unscaled map of coloured sample dots; student: 「新樣本該分哪一類？」 P2 robot uses a magnifier marked 「k＝11」: 「先依距離選最近 11 位」 and caption 「選鄰居時不看類別」. P3 show a ballot tally board exactly 「紅：7 票」「黑：4 票」; do not draw a countable point scatter requiring exact geometry. P4 red decision flag 「預測：紅類」 and takeaway 「7／11 是票數比例」. Add student balloon 「少數服從多數！」. Query has no known true class; majority prediction does not prove ground truth.
```

修訂提示詞：

```text
Correct panel 2 (top-right) ONLY. The currently drawn selected dots are incorrectly counted. Remove the entire selected-dot diagram, dashed spokes and surrounding coloured dots in this panel. Replace that diagram with a simple computer SEARCH WORKFLOW screen, no countable dots, no human crowds: two large cards connected by one arrow, reading 「依距離排序」 → 「取最近 11 位」. Keep robot, magnifier k=11 and the existing two text balloons 「先依距離選最近 11 位」「選鄰居時不看類別」. Do not show any countable neighbour-dot scatter in this panel. Preserve panels 1,3,4 exactly, especially the tally red 7, black 4 and red prediction. Keep the four equal panels, aspect ratio, original style.
```
## 09 誤差保證，要看前提

- 原步驟：`lec02nn-u04-p4`
- 核心觀念：最近鄰漸進誤差界與未核實數字
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「誤差保證，要看前提」. Scientific meaning and constraints: Under usual large-sample setting, 1NN asymptotic error is bounded between Bayes error and twice Bayes error. Source's kNN bound at PB=.01,k=3 is .01+1/sqrt(3e)=.36018064, an upper bound, not actual error; doesn't establish 1.03%. Four-panel storyboard: P1 student sees a big sign 「最近鄰，誤差有保證？」. P2 robot points to a horizon labelled 「1NN，N→∞」; board 「P_B ≤ P_NN ≤ 2P_B」 with short label 「P_B：貝氏最優誤差」. P3 student holds a note 「3NN：1.03%？」 and robot magnifies it: 「這個數字尚未核實」. P4 a clear board 「上界 ≠ 實際誤差」 and robot says 「有限資料，也不能直接套漸進保證！」. Keep only these formulas; no made-up percentage performance, no treating 36% as measured error.
```
## 10 奇數鄰居，也可能平手

- 原步驟：`lec02nn-u04-p5`
- 核心觀念：平票與奇數k的適用範圍
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「奇數鄰居，也可能平手」. Scientific meaning and constraints: Odd k prevents two-class equal-vote ties but not multiclass ties. Three classes with k=5 counts 2,2,1 yields top tie, even though 5 not multiple of 3. This is a boundary correction to a source heuristic. Four-panel storyboard: P1 two-class voting box shows 「k＝5」 and tally 「紅 3：藍 2」. Student: 「奇數能避開平手？」 P2 robot answers 「兩類別，奇數 k 可避免同票」. P3 three-class voting board with exactly 「紅 2」「藍 2」「綠 1」, title 「三類別，k＝5」. Student: 「咦，最高票還是平手！」 P4 robot prepares a rulebook labelled 「平票規則」: 「多類別仍須事先訂規則！」. Do not state that avoiding multiples of number of classes guarantees no ties. Use tally cards, not inaccurate crowds.
```
## 11 最近鄰，把空間分地盤

- 原步驟：`lec02nn-u05-p2`
- 核心觀念：Voronoi細胞與類別決策區域
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「最近鄰，把空間分地盤」. Scientific meaning and constraints: Euclidean 1NN cells contain points nearest each sample. Show exact trivial geometry with 3 collinear sites; borders at midpoints, same-class adjacent cells merge. Four-panel storyboard: P1 robot places THREE sample houses in one straight horizontal row, left red, middle red, right blue. Student: 「每個位置跟誰？」 P2 show exact Voronoi map: these three houses equally spaced left-to-right on a flat rectangle, TWO VERTICAL boundary lines exactly midway between adjacent houses, making three vertical strips. Label 「每個樣本一塊地盤」. P3 same map with left two red strips merged; remove ONLY boundary between the two red houses, keep right red/blue separating line unchanged. Label 「同類相鄰地盤合併」. P4 query star clearly on the blue strip right of the remaining border and close to the rightmost blue house, blue prediction badge; robot 「1NN：跟最近樣本的類別」. No curving borders, arbitrary polygons or inaccurate perpendicular geometry. Boundary itself is a tie.
```
## 12 鄰居多，未必分得好

- 原步驟：`lec02nn-u06-p3`
- 核心觀念：偏誤變異取捨與資料特定的k例子
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「鄰居多，未必分得好」. Scientific meaning and constraints: Small k follows noise high variance; large k oversmooths high bias. Source example only k1 4.50%,k7 .50%,k41 3.50%. Do not generalize optimum k=7, no universal U curve guarantee. Four-panel storyboard: P1 student follows one noisy neighbour with an exaggerated zigzag walking path, label 「小 k：變異大」 and balloon 「連雜訊都跟！」 P2 student buried in distant neighbours' advice, local pattern washed out, label 「大 k：偏誤大」 and balloon 「細節被抹平！」 P3 three experiment cards only, exactly 「k＝1：4.50%」「k＝7：0.50%」「k＝41：3.50%」; heading 「本例測試誤差」. P4 robot points to the middle card: 「本例 k＝7 最低」; student takeaway 「換資料，最佳 k 也可能不同！」. No claim test set should be repeatedly used for tuning; just report the source experiment.
```
## 13 三種分類器，各有代價

- 原步驟：`lec02nn-u07-p1`
- 核心觀念：高斯貝氏、單純貝氏與kNN的假設取捨
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「三種分類器，各有代價」. Scientific meaning and constraints: Source compares Gaussian density assumptions, naive Bayes conditional independence, kNN local voting. These assumptions aren't a strict subset hierarchy; flexibility does not guarantee accuracy; binary NB linearity has conditions. Four-panel storyboard: P1 robot tailor holds a bell-shaped mould tagged 「高斯貝氏」: 「假設密度是高斯」, student sees mismatched shapes outside the mould. P2 robot sorts clue drawers tagged 「單純貝氏」: 「給定類別，假設特徵獨立」, two linked clues are gently flagged. P3 robot asks a local group tagged 「kNN」: 「鄰近樣本直接投票」, a large sample library in background. P4 student compares three toolboxes: 「形狀不符、忽略相關、資料需求」, robot says 「看資料與代價選方法！」. Do not draw a strict arrow ordering saying all naive Bayes models are more flexible than all Gaussians, do not call all naive Bayes boundaries linear.
```
## 14 沒有訓練，查詢仍要忙

- 原步驟：`lec02nn-u07-p2`
- 核心觀念：kNN查詢成本與搜尋／原型精簡
- 生成提示詞：

```text
Use case: illustration-story. Create ONE finished educational four-panel comic for a Traditional-Chinese university pattern-recognition lecture, beginner-friendly. Exact landscape 16:9 canvas, preferably 2048×1152. Exactly FOUR equal panels in a 2×2 grid, wide white gutters and outer margins, numbered 1,2,3,4 reading top-left, top-right, bottom-left, bottom-right. Cute clean ink and soft flat colours; consistent protagonists: a short-haired student in a mustard-yellow hoodie and a round teal robot tutor. Large crisp Traditional Chinese lettering, short balloons, simple backgrounds. No watermark, no English translation paragraphs, no decorative formulas. Render mathematical minus signs, decimals and conditional bars correctly. All essential text below must be verbatim; do not add unrequested factual labels. Use panels as a causal story, not four text cards. Title: 「沒有訓練，查詢仍要忙」. Scientific meaning and constraints: Basic kNN stores data rather than fitting a parametric classifier; brute-force each query compares N sample distances. Complexity depends dimension and neighbor selection implementation; avoid presenting source O(kN) as universal. Efficient search and editing/condensing reduce burden but can have tradeoffs. Four-panel storyboard: P1 student stores a mountain of training cards in a cabinet: 「存好資料，就能分類？」 P2 new email/query arrives; robot runs between the query and all shelves: 「每次查詢，都要找近鄰！」 P3 robot holds a distance checklist labelled 「N 個樣本」 and sighs 「樣本多、維度高，工作量大」. P4 two helper tools labelled 「高效搜尋」「原型精簡」 lighten the workload; takeaway balloon 「減少搜尋負擔，也要檢查準確度！」. No Big-O formula, no claim zero preprocessing, no guarantee arbitrary deletion preserves predictions.
```

