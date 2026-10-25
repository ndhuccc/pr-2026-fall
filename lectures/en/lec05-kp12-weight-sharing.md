# KP12 Weight sharing and transformation invariance

> Level: third-year undergraduate | Self-study | English edition

Read this independently with weighted scores, basic differentiation and matrices as prerequisites. New terms are introduced when needed.

[Open the matching slides](../../slides/lec05-kp12-weight-sharing-en.jbd.json) | [中文版](../lec05-kp12-weight-sharing.md)

## Learning objectives

- Compute a shared response, feature maps and parameter counts.
- Distinguish equivariance from invariance on one example.
- State conditions and limitations of translation and rotation sharing.

## KP12 Weight sharing and transformation invariance

**One-sentence summary**：Sharing reuses a rule, usually producing equivariant responses before a suitable readout yields invariance.

**Plain explanation**：Keeping an object in the same class after movement does not require every network value to remain unchanged. Define each local field, then reuse nine weights.

**Formal definition**：The sections define terms, symbols and assumptions while keeping symbols consistent for the same quantity.

**Example**：All new worked examples are [Added] and checked in Python. Source experiment reports are identified separately.

**Common misconception**：Sharing does not automatically guarantee invariance to every translation, rotation or scaling.

**Practice**：The final section provides questions, hints and worked checks for use after your own attempt.

### Build a local shared rule from a moving stroke

Keeping an object in the same class after movement does not require every network value to remain unchanged. Define each local field, then reuse nine weights.

**Transformation invariance**: For a specified transformation T, invariance means $c(Tx)=c(x)$. State which transformation is intended.

The same three-pixel stroke shifts right by two cells without cropping. Its class should stay the same; intermediate arrays need not.

![The same three-pixel vertical stroke shifts two columns right inside two six-by-six images without cropping.](../../assets/figures/lec05-kp12-shift.png)

Figure `lec05-kp12-shift`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

**Receptive field**: A receptive field is the input region directly visible to a unit; here it is a 3×3 patch.

The image is 6×6. A stride-one 3×3 window with no padding has $4\times4=16$ valid positions.

One position sees nine numbers. Positions see different data but can apply the same rule.

![An orange three-by-three receptive-field window inside the six-by-six stroke image.](../../assets/figures/lec05-kp12-patch.png)

Figure `lec05-kp12-patch`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

**Weight sharing**: Weight sharing constrains corresponding connections to use one adjustable value, updated as a single parameter.

**Kernel**: A kernel is the weight matrix reused across windows; this example has ones in the middle column, zeros elsewhere and zero bias.

A patch with middle column $1,1,1$ scores $1\times1+1\times1+1\times1=3$, a score for this local feature only.

![Reusable three-by-three kernel with ones in its center column, zeros elsewhere and bias zero.](../../assets/figures/lec05-kp12-kernel.png)

Figure `lec05-kp12-kernel`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

### Equivariant maps before invariant readout

Preserving position yields responses that move with the input. Suitable aggregation and assumptions may then discard position; this is the central conceptual turn.

**Feature map**: A feature map arranges local responses by position; this one is 4×4.

The maps show responses before and after image translation using the same weights. Both maxima are 3, at different locations.

The kernel evaluates local data; it does not automatically discard where the feature occurs.

![Two four-by-four response maps using the shared kernel; the maximum value three moves two columns and max pooling stays three.](../../assets/figures/lec05-kp12-maps.png)

Figure `lec05-kp12-maps`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

**Translation equivariance**: Translation equivariance means a translated input produces a correspondingly translated response: $F(Tx)=TF(x)$.

F maps an image to a feature map, and T is translation. Usually $F(Tx)\ne F(x)$ because the high-response position changes.

Integer shifts, stride, padding and boundary conditions must be compatible; cropping can also destroy the correspondence.

**Global max pooling**: Global max pooling retains only $z=\max_{i,j}F(x)_{ij}$ from the feature map.

Both images give $z=3$. A later classifier using only z receives the same feature for these two images.

This checks the example and translations preserving the feature. Pooling loses location and may be inappropriate for precise localization.

### Count and update shared parameters

Sharing reduces independent numbers, not all computations over positions. Each use contributes to the gradient of the same parameter.

Without sharing, sixteen positions each have nine weights and one bias: $16\times(9+1)=160$.

Sharing uses just nine weights and one bias: $9+1=10$. Computation still runs at all sixteen positions.

The reduction is useful only when the sharing assumption fits the task. Fewer parameters guarantee neither better accuracy nor proportional computation savings.

Let k be a shared weight, r_p the preactivation at position p, x_p its input, and $\delta_p=\partial J/\partial r_p$.

The chain rule gives $\partial J/\partial k=\sum_p\delta_px_p$. Contributions $0.2\times3$ and $-0.1\times1$ sum to $0.6-0.1=0.5$.

With learning rate $\eta=0.1$ and k=1, update $k=1-0.1\times0.5=0.95$. Every position then uses 0.95.

### Compare three routes to invariance

Local sharing is one architectural prior. Systems may combine invariant features and augmentation after checking whether transformations preserve labels.

Choose invariant features, accepting that some useful information may be discarded.

Constrain architecture with shared weights and suitable aggregation, specifying which computations should match.

Augment training data with valid transformations; a finite augmented sample usually does not guarantee exact invariance everywhere.

### Geometric tying of higher-order input products

Pixel products let pair geometry enter the model. Translation preserves displacement, while rotation preserves length; these imply different tying rules.

**Higher-order network**: A higher-order network includes input products in its preactivation, for example $v=b+\sum_i a_ix_i+\sum_{j,k}c_{jk}x_jx_k$.

x_i is a pixel value, a_i a single-pixel weight, c_jk a pair weight, and b a bias, followed by activation $f(v)$.

For binary pixels the product is one only when both are one. Pair terms can encode joint spatial evidence.

![Two segments share displacement one,one; a third has the same slope but displacement two,two, so it is not their pure translation.](../../assets/figures/lec05-kp12-pair.png)

Figure `lec05-kp12-pair`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

Translating endpoints by t preserves displacement: $(p_k+t)-(p_j+t)=p_k-p_j$.

The blue pairs both have displacement $(1,1)$ and can share as one displacement group. The orange pair $(2,2)$ has the same slope but is not its translation.

Matching slopes alone is too coarse. Whole-model invariance also requires compatible single-pixel terms, boundaries and readout.

Rotation preserves segment length, so equal-length pixel pairs can share second-order coefficients, encoding a geometric prior.

On a finite pixel grid, arbitrary rotations require interpolation or cropping. Exact invariance needs compatible transformations, terms and aggregation.

Sharing can reduce parameters, but the source notes limited adoption of these higher-order methods. Geometry alone is not a performance guarantee.

### A squared-norm special case and the historical architecture

A squared-norm term uses one extra coefficient, but an invariant term does not make the whole model invariant. Distinguish a shared principle from historical architecture details.

$v=b+\sum_i a_ix_i+c\sum_i x_i^2$. One shared coefficient c adds one parameter, not one per pixel.

The squared sum is $\|x\|^2$: both $(1,0)$ and $(0,1)$ give $1^2+0^2=1$. This term is invariant under orthogonal rotations.

The linear term can differ: for $a=(1,0)$, scores are $b+1+c$ and $b+c$. Reported generalization benefits are cited claims, not proved by this example.

![Points one,zero and zero,one both have squared norm one; an invariant term does not imply an invariant full model.](../../assets/figures/lec05-kp12-radius.png)

Figure `lec05-kp12-radius`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

The source describes three hidden layers, with feature maps in the first two. Units receive local windows and corresponding connections share weights within a map.

It shares the principle of our stroke example, not its architecture. The available description does not justify a full parameter count or accuracy claim.

First ask which transformations should preserve labels, then choose features, tying rules and readout instead of assuming sharing is always better.

### Practice and parameter-count checks

Change image size and recount, then describe the output using equivariance and invariance equations. Keep position count separate from parameter count.

Question 1: use an 8×8 input, 3×3 window, stride one, no padding and a shared bias. Find map size and shared versus unshared counts.

Question 2: high responses follow an input shift. Is this equivariance or invariance? Compare $F(Tx)=TF(x)$ with $F(Tx)=F(x)$.

1. Each direction has $8-3+1=6$ positions, giving $6\times6=36$: a 6×6 map.

2. Without sharing: $36\times(9+1)=360$. With sharing: $9+1=10$. A larger image adds uses, not parameters in this shared kernel.

3. A moving response is equivariance; suitable aggregation under the required conditions can yield an invariant feature.

![Two six-by-six feature maps from eight-by-eight inputs; response maxima shift by two columns and both remain three.](../../assets/figures/lec05-kp12-maps-practice.png)

Figure `lec05-kp12-maps-practice`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

#### The exact shared-window calculation

For image x, kernel K and bias b, use unflipped-kernel cross-correlation:

$$
r_{ij}=b+\sum_{a=0}^{2}\sum_{b'=0}^{2}K_{ab'}x_{i+a,j+b'}.
$$

i,j locate the patch; a,b′ locate offsets inside the kernel. The offset b′ differs from bias b. With a pointwise activation $\phi$, take $F(x)_{ij}=\phi(r_{ij})$; the running example uses r directly without an additional activation. Its complete maps are

$$
F(x)=\begin{bmatrix}2&0&0&0\\3&0&0&0\\2&0&0&0\\1&0&0&0\end{bmatrix},\qquad
F(Tx)=\begin{bmatrix}0&0&2&0\\0&0&3&0\\0&0&2&0\\0&0&1&0\end{bmatrix}.
$$

Response locations change while both maxima remain three. Global max pooling makes this example's feature invariant, not a case for discarding position in every task.

#### Finite-grid boundaries

The equivariance equation needs valid corresponding positions. Cropping, inconsistent padding or a shift incompatible with stride can restrict or break it. Image rotation can also require interpolation; equal-length coefficient groups do not eliminate sampling error.

#### Where the shared gradient comes from

One parameter k enters many scores $r_p$. The chain rule sums all paths: $\partial J/\partial k=\sum_p(\partial J/\partial r_p)(\partial r_p/\partial k)$. For a local linear score, the second factor is input $x_p$. Activation derivatives belong in $\delta_p=\partial J/\partial r_p$ and must neither be omitted nor counted twice.


## Glossary and symbol reminders

| English | 中文 |
|---|---|
| Transformation invariance | 轉換不變性 |
| Receptive field | 感受野 |
| Weight sharing | 權重共享 |
| Kernel | 卷積核 |
| Feature map | 特徵圖 |
| Translation equivariance | 平移等變性 |
| Global max pooling | 最大值彙整 |
| Higher-order network | 高階網路 |

Read symbols by their local definitions. Distinguish weights, scores, predictions and loss; identically named hyperparameters in different experiments may have different roles.

## Sources and supplementary scope

- [Chapter 4, KP12](https://ndhuccc.github.io/CCC-LNS/PR_115/Ch04-nonlinear-classifiers/index.html#kp12), accessed 2026-10-25.
- The source calls sharing translation invariant; this material distinguishes equivariance from aggregated invariance. Displacement replaces slope-only translation grouping. An invariant squared-norm term does not make the whole circular model invariant.
- Source reference codes: [Fuku 82], [Rume 86], [Fuku 92], [Lecu 89], [Ride 97].
- Original Figures 4.14–4.16 were inspected. New teaching diagrams do not claim to be the original figures or exact experimental curves.
- Historical reference codes follow the source. Full papers, theorem conditions and experimental records were not all available; those limits are retained.
