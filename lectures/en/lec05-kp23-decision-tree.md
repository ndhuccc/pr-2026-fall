# KP23 Decision Trees: OBCT, Splitting Criteria and Pruning

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.20

[Slides: read and download](../../slides/lec05-kp23-decision-tree-en.jbd.json) | [中文版](../lec05-kp23-decision-tree.md)

## Learning objectives

- Explain the structure of an OBCT and the four things fixed in training, and compute the impurity and the impurity decrease.
- Explain why the children are weighted, what happens when a tree is too large and how pruning works.
- Explain the high variance of decision trees and how bagging and random forests lower it.

## KP23 Decision Trees: OBCT, Splitting Criteria and Pruning

**One-sentence summary**: Instead of drawing a complex boundary, ask a series of simple yes/no questions, each cutting the feature space once. The size of the tree is the key, a single tree has a high variance and bagging averages it out.

### 1. A series of yes/no questions

**Plain explanation**: Can classification skip the boundary and ask a series of simple yes/no questions?

- **Decision tree**: a series of yes/no decisions along a path of nodes, ruling out classes step by step until a leaf is reached.

The most popular is the OBCT (ordinary binary classification tree): every node asks one feature, "$x_i\le\alpha$?", cutting the space into hyper-rectangles parallel to the axes. Strengths: especially good with many classes; often not every feature has to be tested; simple and easy to interpret; numeric and categorical features both work.

Figure `lec05-kp23-partition`: three regions on the left and the matching tree on the right.

![A series of yes/no questions](../../assets/figures/lec05-kp23-partition.png)

### 2. Four ingredients and the candidates

Training fixes four things: the set of candidate questions; the splitting criterion; the stop-splitting rule; the class-assignment rule for leaves. Candidates: if feature $x_k$ has $N_{tk}$ distinct values in the node, take midpoints of neighbouring values as thresholds, at most $N_{tk}-1$ (the book writes $N_{tk}$); over all features the list is finite. **Example** (designed here): 10 distinct values 1.0, 1.4, 2.2, …, 7.0 give 9 midpoints.

Figure `lec05-kp23-cands`: 10 values and 9 midpoints.

![Candidates](../../assets/figures/lec05-kp23-cands.png)

### 3. Impurity

**Impurity** (formal definition):

$$
I(t)=-\sum_{i=1}^{M}P(\omega_i|t)\log_2P(\omega_i|t),
$$

larger the more mixed the classes in the node. It is maximal when all classes are equal ($\log_2M$ for $M$ classes) and 0 when all are of one class (with $0\log0=0$); probabilities are estimated by $N_t^i/N_t$. Examples: $(4,4,2)$: 1.522 (the book writes 1.521); $(1,1,1)$: $\log_23=1.585$; $(5,0,0)$: 0.

Figure `lec05-kp23-entropy`: the two-class entropy curve and three examples.

![Impurity](../../assets/figures/lec05-kp23-entropy.png)

### 4. Impurity decrease

$\Delta I=I(t)-\tfrac{N_{tY}}{N_t}I(t_Y)-\tfrac{N_{tN}}{N_t}I(t_N)$; pick the question with the largest $\Delta I$. **Example 4.2**: $t=(4,4,2)$, Yes $(3,1,0)$, No $(1,3,2)$: $I(t)=1.522$, $I(t_Y)=0.811$, $I(t_N)=1.459$; $\Delta I=1.522-0.4\cdot0.811-0.6\cdot1.459=0.322$. The book prints $I(t_Y)=0.815$, $I(t_N)=1.472$, $\Delta I=0.315$, which disagrees with its own counts (its printed numbers give only 0.312); only this split was recomputed here.

Figure `lec05-kp23-ex42`: Example 4.2 recomputed against the book's numbers.

![Impurity decrease](../../assets/figures/lec05-kp23-ex42.png)

### 5. Why weighting

**Example** (designed here): a parent of 5 against 5 ($I=1$). Split A: Yes $(1,0)$, No $(4,5)$; split B: Yes $(4,1)$, No $(1,4)$. Weighted: A $=0.108$, B $=0.278$, so B is chosen. Unweighted (children simply averaged): A $=0.504$, B $=0.278$, so A is chosen; one pure point is mistaken for a big gain. **Common misconception**: a split is good whenever a child becomes pure; making only a tiny subset pure is worth little.

Figure `lec05-kp23-weight`: the scores of two splits with and without weighting.

![Why weighting](../../assets/figures/lec05-kp23-weight.png)

### 6. How large a tree

**Example** (designed here): two noisy half-moons (sd 0.35), 100 training and 1000 new points per class, entropy criterion. Depth 1 (2 leaves): 76.5% training, 73.3% on new points; 2 (4): 89.0% / 83.7%; 4 (11): 90.0% / 82.2%; 8 (20): 99.0% / 85.2%; 12 (24): 100% / 85.1%. With more leaves training climbs to 100% while new points stay near 85%; a too-large tree learns the details of the training set.

Figure `lec05-kp23-depth`: tree depth and accuracy.

![How large a tree](../../assets/figures/lec05-kp23-depth.png)

### 7. Pruning

**Pruning**: grow a large tree first, then cut branches that are not worth their cost, judged by an error estimate plus complexity such as the leaf count (the source says stopping on an impurity-decrease threshold often stops too early or too late). On the same data, with pruning strength $\alpha$: 0 gives 24 leaves, 100% training and 85.1% on new points; 0.01: 22 leaves, 85.1%; 0.02: 10 leaves, 96.5% / 87.3%; 0.05: 7 leaves, 94.0% / 86.3%. One dataset and one run, a gain of about 2 points. Entropy and Gini over 20 draws (depth 4) give 86.1±2.3% and 86.1±3.1% on new points: the criterion hardly matters (as the source says).

Figure `lec05-kp23-prune`: pruning strength and accuracy.

![Pruning](../../assets/figures/lec05-kp23-prune.png)

### 8. Variance and bagging

**Bagging**: draw $B$ samples with replacement from the training set, grow a tree on each and take a majority vote. **Variance** (designed here): on 8 training sets of the same size every first cut is on the second feature, with thresholds 0.42, 0.11, 0.12, 0.09, 0.22, 0.26, 0.22, 0.29 and 22 to 33 leaves. Averages (20 training sets, new points): a single tree 84.4±1.4%; bagging with 25 trees 87.7±1.1%; a random forest (bagging plus random features per node) of 25 trees 87.8±1.1%. A tree is hierarchical, so an error high up reaches every leaf below; averaging lowers the variance. **To remember**: a decision tree makes hierarchical, sequential hard decisions while a neural network makes parallel soft ones; the MLP wins on error rate and the tree on training time (source).

Figure `lec05-kp23-bag`: the mean accuracy of three methods and 8 root thresholds.

![Variance and bagging](../../assets/figures/lec05-kp23-bag.png)

### Extension: oblique questions, practice and worked solution

**Oblique questions** (designed here): 300 points uniform on $[-1,1]^2$ with the class given by $x_1+x_2>0$; one oblique question $x_1+x_2\le0$ separates them exactly. Axis-parallel trees (3000 new points; 13 to 14 leaves are needed for about 95%): depth 1: 2 leaves, 75.0%; depth 3: 7, 89.6%; depth 6: 13, 95.4%; the full tree has 14 leaves, 100% training and 95.1% on new points. An oblique question $\sum c_kx_k\le\alpha$ cuts well but trains harder (source).

Figure `lec05-kp23-oblique`: the diagonal class boundary and the leaves of axis-parallel trees.

![Oblique questions](../../assets/figures/lec05-kp23-oblique.png)

**Practice**: node $t$ has 4 points of $\omega_1$ and 4 of $\omega_2$; split A: Yes $(3,1)$, No $(1,3)$; split B: Yes $(2,2)$, No $(2,2)$; given $I(3,1)=0.811$.

1. What is $\Delta I$ of split A?
2. What is $\Delta I$ of split B, and which split is better?

Figure `lec05-kp23-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp23-practice.png)

**Worked solution of questions 1 and 2**: (1) $I(t)=1$; both children of A have $I=0.811$; $\Delta I=1-\tfrac48\cdot0.811-\tfrac48\cdot0.811=0.189$. (2) Both children of B are $(2,2)$ with $I=1$; $\Delta I=1-0.5-0.5=0$. (3) Check: A is better; B removes no impurity at all; a split into $(4,0)$ and $(0,4)$ would give $\Delta I=1$.

Figure `lec05-kp23-practice-sol`: the computation.

![Practice solution](../../assets/figures/lec05-kp23-practice-sol.png)

## Terms and source

| 中文 | English |
|---|---|
| 決策樹 | Decision tree |
| 不純度 | Impurity |
| 剪枝 | Pruning |
| Bagging | Bagging |

Source: Chapter 4, KP23, §4.20 (read 2026-10-25). The OBCT, the four design ingredients, the candidate questions, the entropy impurity and impurity decrease, stopping and class assignment, pruning, the high variance, bagging and random forests, oblique questions and the comparison with neural networks follow the source; the candidate example, the weighting contrast, the depth and pruning experiments, the variance and bagging experiments, the oblique experiment and the practice were designed and recomputed for this lecture ([added], (program-computed)). The numbers of the book's Example 4.2 differ from a recomputation of its own counts, as marked in the text.
