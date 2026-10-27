# KP11 Pruning, Regularization and Reported Simulations

!!! note "Self-study"
    This unit (KP11) is self-study: it is not taught in class, so please read it on your own.

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4

[Slides: read and download](../../slides/lec05-kp11-pruning-regularization-en.jbd.json) | [中文版](../lec05-kp11-pruning-regularization.md)

## Learning objectives

- Derive the "saliency" from a Taylor approximation and state the assumptions of the derivation.
- Compute by hand a penalty value, a deletion cost and a compensation example.
- Tell the source's reported simulation apart from this lecture's teaching calculations.

## KP11 Pruning, Regularization and Reported Simulations

**One-sentence summary**: Estimate the cost of deleting a connection first, then control the model with a penalty and validation data; neither the size of a weight nor the number of connections is the only criterion.

### Prerequisites and symbols

**Four things you need first**:

- **Cost and weights** (KP06): the cost $J$ changes with every weight $w_i$; the gradient $g_i=\partial J/\partial w_i$ is the slope of the cost along $w_i$.
- **Second derivative and curvature**: the second derivative says how fast the slope changes; with a large curvature, one small step changes the cost a lot.
- **Taylor expansion**: near one point, approximate the change of a function by its slope and curvature.
- **Validation data** (KP10): data that is not used to update weights and is kept for choosing the model.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $w_i$, $\delta w_i$ | the $i$-th weight and its change | deleting means $\delta w_i=-w_i$ |
| $J$, $\Delta J$ | the cost, and the cost after minus before deletion | $\Delta J$ is not the size of a weight |
| $g_i$ | local slope | $\partial J/\partial w_i$ |
| $H$, $H_{ii}$ | Hessian and its diagonal entry | matrix of second partial derivatives; $H_{ii}$ is the curvature along direction $i$ |
| $s_i$ | saliency | $s_i=\frac12H_{ii}w_i^2$ |
| $\alpha$ | weight of the penalty (regularization) | section 4; not the same as the momentum $\alpha$ |
| $\tau,\varepsilon$ | scale of the penalty, threshold of deletion | the two have different uses |
| $\rho(w)$ | saturating penalty | $\rho=w^2/(\tau^2+w^2)$ |

### 1. The size of a weight is not the cost of deleting it

**Plain-words explanation**: A trained network may be redundant, but you cannot judge which connection matters from the size of its weight alone.

- **Pruning**: remove some connections or units to reduce what the model can adjust; the performance must still be checked after the removal.

Look at one connection first. Setting its weight to zero means this input no longer contributes to the score. The goal is not "delete the most" but to get a simpler model at an acceptable loss.

- $w_i$ is the $i$-th weight and $\delta w_i$ its change. To make it zero, $w_i+\delta w_i=0$, so $\delta w_i=-w_i$.
- $J$ is the training cost and $\Delta J$ is the cost after deletion minus the cost before; it is not the size of the weight.
- If $w_i=0.2$, deleting adds $-0.2$. Do not treat "a small change" as "a certainly small effect".

**Curvature**: near the current weights, the curvature describes how fast the slope of the loss changes; here it is measured by the second derivative.

**Hessian**: arrange all second partial derivatives between the weights into a matrix $H$; $H_{ii}$ describes the curvature along direction $i$.

Figure `lec05-kp11-curvature`: First see the two charts on the left: A has weight 0.2 but a steep curve (curvature 100) and deletion cost 2; B has weight 1 but a flat curve (curvature 0.02) and deletion cost 0.01; the cards on the right define pruning, curvature and the Hessian. [Function: 2]

![Local quadratic losses: small-weight A costs 2 to delete, large-weight B costs 0.01.](../../assets/figures/lec05-kp11-curvature-en.png)

The next question: can we use the slope and curvature to estimate the deletion cost before actually deleting?

### 2. Saliency from the Taylor expansion

**The derivation, one step at a time**:

1. The change of the cost is approximately $\Delta J\approx\sum_i g_i\delta w_i+\frac12\sum_{i,j}H_{ij}\delta w_i\delta w_j$.
2. Near a minimum take $g_i\approx0$, so the first term vanishes.
3. The "diagonal approximation" ignores the interaction terms between different weights and gives $\Delta J\approx\frac12\sum_iH_{ii}(\delta w_i)^2$.
4. Substitute $\delta w_i=-w_i$ and define the **saliency** $s_i=\frac12H_{ii}w_i^2$, an estimate of the deletion cost; it is an approximation, not a measured loss.

**Worked example**:

- A: $w_A=0.2$, $H_{AA}=100$, $s_A=\frac12\times100\times0.2^2=2$.
- B: $w_B=1$, $H_{BB}=0.02$, $s_B=\frac12\times0.02\times1^2=0.01$.
- Compare: $2/0.01=200$. By this local estimate delete B first, although its weight is larger.

Figure `lec05-kp11-saliency`: Read the four steps on the left from top to bottom: Taylor expansion, g≈0, the diagonal approximation, substituting δw=−w to get saliency; then see the bars for A (2) and B (0.01) on the log scale on the right, a 200-fold gap. [Function: 2]

![Four-step derivation of saliency, and the deletion costs 2 and 0.01 of A and B on a log scale.](../../assets/figures/lec05-kp11-saliency-en.png)

**Conditions of this estimate**:

- Far from a minimum, the first-order term need not be small.
- For a large deletion, the higher-order terms may not be negligible.
- Deleting several weights at once may couple them.
- If the Hessian has negative curvature, do not read a negative number directly as "safe".

So delete in small steps, measure the cost again, retrain the remaining weights, and keep the model with the best validation result.

The next question: how do we put this estimate into a real pruning procedure?

### 3. Putting the estimate into a checkable pruning procedure

Saliency is not a value measured after deletion, so the procedure must include re-evaluation and retraining; a ranking must not be treated as permanent truth.

1. Train to a suitable point first.
2. Estimate the saliency of each connection.
3. Delete a small number of low-saliency connections.
4. Retrain and check with validation data.

Figure `lec05-kp11-flow`: Follow the four-step loop across the top: train, estimate saliency, delete a few, retrain and check on validation data, then back to step 2; the four boxes below are cases where the estimate fails. [Function: 2]

![The four-step pruning loop and four cases where the saliency estimate fails.](../../assets/figures/lec05-kp11-flow-en.png)

Stop according to validation performance, the allowed loss increase or the resource budget; the smaller network after deletion is not guaranteed to be more accurate every time. Methods with the full Hessian can also account for how other weights compensate, at the price of more storage and computation.

### 4. Putting a model preference into the cost function

Pruning changes the structure; regularization changes the objective first.

- **Regularization**: add a restriction or preference on the model beyond the data error; it changes which solutions we are willing to accept.

$$
J_{\mathrm{total}}=J_{\mathrm{data}}+\alpha P(\mathbf w).
$$

The first term measures the data error, $P$ is the weight penalty, and $\alpha\ge0$ sets the relative weight. If the data error is a sum or a mean, its scale differs, and the same value of $\alpha$ acts differently; do not copy it across settings.

**Example** ($\alpha=0.1$):

| Model | Data error | Penalty $P$ | $J_{\text{total}}$ |
|---|---:|---:|---:|
| A | 0.10 | 4 | $0.10+0.1\times4=0.50$ |
| B | 0.20 | 1 | $0.20+0.1\times1=0.30$ |

This objective chooses B. With $\alpha=0$ it would choose A instead. Choose $\alpha$ with validation data; a smaller total cost does not mean the test error must be smaller.

Figure `lec05-kp11-reg`: First see the total-cost formula on top, then compare the stacked bars of the two panels: at α=0.1 A is 0.50 and B is 0.30, so B; at α=0 only the data error counts, so A. [Function: 2]

![Regularization: at α=0.1 model A totals 0.50 and B 0.30, so B; at α=0 only the data error counts, so A.](../../assets/figures/lec05-kp11-reg-en.png)

**Saturating penalty**: $\rho(w)=w^2/(\tau^2+w^2)$, where $\tau>0$ is a scale; for very large weights the penalty approaches 1, which is called saturation. The total penalty is $P=\sum_i\rho(w_i)$.

Take $\tau=1$:

| $w$ | 0.2 | 1 | 3 |
|---|---:|---:|---:|
| $\rho(w)$ | $0.04/1.04\approx0.0385$ | 0.5 | 0.9 |

To compare against the scale use absolute values: only $|w|\ll\tau$ is the range near zero.

Figure `lec05-kp11-rho`: First see the green curve stay near 0 for small w and saturate at 1 for large w, then read the three points: about 0.0385, 0.5 and 0.9 at w=0.2, 1 and 3; the orange curve is the derivative, zero at the origin, so a smooth penalty alone does not guarantee exactly zero weights. [Function: 2]

![The saturating penalty and its derivative; at w=0.2, 1, 3 the penalty is about 0.0385, 0.5, 0.9 and the derivative is zero at 0.](../../assets/figures/lec05-kp11-rho-en.png)

**Derivative**: $\rho'(w)=2\tau^2w/(\tau^2+w^2)^2$. At $w=0$ the derivative is 0, so a finite number of update steps is not guaranteed to land exactly on zero.

**Weight elimination**: during training encourage shrinking, then periodically set weights below a threshold to zero or delete them. The threshold is tested as $|w_i|<\varepsilon$; $\varepsilon$ is the deletion threshold and $\tau$ is the penalty scale, and the two have different uses.

The next question: is a single connection enough? How do unit outputs and weight norms affect complexity?

### 5. Unit outputs and weight norms also matter

One connection is not a whole unit, and one unit is not a whole signal path.

- The source also considers a penalty on neuron outputs, encouraging some units to respond less; it does not score only single connections.
- A small unit output can still be amplified by large weights in the next layer; check the whole path and the data performance after deletion.
- Deleting connections, deleting units and shrinking values are three different operations and must be recorded separately.

The source quotes a result for a two-layer sigmoid network: under conditions such as a small training error and a bound on the weight norm, the complexity term contains $A^3\sqrt{\log d/N}$. $A$ is a common bound on the sum of absolute weights of each unit, $d$ is the input dimension, and $N$ is the number of samples. This is only the source's order-of-magnitude summary, not a complete probability bound. With $d,N$ fixed, doubling $A$ makes this term $2^3=8$ times larger; it must not be read directly as a classification error rate.

Figure `lec05-kp11-ops`: Compare column by column: deleting connections, deleting units and shrinking values are three different operations; the last column is the source's complexity term, 8 times when A doubles, only an order-of-magnitude summary and not a classification error rate. [Function: 2]

![Deleting connections, deleting units and shrinking values, and the source's complexity term A cubed.](../../assets/figures/lec05-kp11-ops-en.png)

### 6. Cascade correlation adds new units to fit the residual

Another route starts from a small architecture: find responses related to the residual, freeze them, then let the output side reduce the error; the two stages must not be merged into one training objective.

- **Residual**: the true target minus the current prediction, $e_n=t_n-\hat y_n$, where $n$ indexes samples.
- **Cascade correlation**: each time add one hidden unit that responds to the current residual, then retrain the output.

The new unit receives the original inputs and the earlier hidden units; train its input-side weights first, then freeze them.

**Teaching score** (single output): for a candidate output $v$ and the residual $e$, $S=\left|\sum_n(v_n-\bar v)(e_n-\bar e)\right|$, where the bar means the sample mean.

- Take $e=(-1,1)$: the candidate $v=(-1,1)$ gives $S=|-1\times(-1)+1\times1|=2$.
- The constant candidate $v=(1,1)$ is zero after centering and gives $S=0$.

After choosing a candidate and freezing the input side, retrain the output-side weights to reduce the squared error. This $S$ is not divided by standard deviations, so it is not a Pearson coefficient.

Figure `lec05-kp11-cascade`: First see the stages and four steps on top (the two stages kept apart) and the definitions of residual and cascade correlation; below is the teaching score S: candidate v=(−1,1) gives 2 and the constant candidate 0. [Function: 2]

![The two stages and four steps of cascade correlation and the teaching score S: candidate (−1,1) gives 2, the constant candidate 0.](../../assets/figures/lec05-kp11-cascade-en.png)

### 7. Keeping the source's simulation report apart from this lecture's calculations

Below, the source's important settings and reported numbers are kept in full. The re-sampled scatter plot only checks the distribution; the weight bars only compare the reported counts; no teaching illustration is passed off as a re-run of the original experiment.

**Data setting** (source):

- Four means of class A: $(0.4,0.9),(2.0,1.8),(2.3,2.3),(2.6,1.8)$; class B: $(1.5,1.0),(1.9,1.0),(1.5,3.0),(3.3,2.6)$.
- 50 points per cluster, $8\times50=400$ points in total.
- Covariance $0.08I$ per cluster ($I$ is the 2-D identity), so the standard deviation is $\sqrt{0.08}\approx0.283$, not 0.08.

Figure `lec05-kp11-data`: First see the positions of the eight clusters (four of A, four of B) and how they interleave; the right side lists the data, network and two momentum settings. The chart is redrawn from the same distribution with the fixed seed 20261025, checks the distribution only, is not the original sample and no network was retrained. [Function: 1]

![400 samples redrawn from the source's eight means with 50 points per cluster and variance 0.08, fixed seed 20261025; not the original data.](../../assets/figures/lec05-kp11-data-en.png)

**Network and training settings** (source):

- The network is 2–3–2–1, the logistic activation has slope parameter 1, and the targets are 1/0; counting biases the number of parameters is $9+8+3=20$.
- Momentum setting: $\mu=0.05$, $\alpha=0.85$.
- Adaptive momentum: $\mu=0.01$, $\alpha=0.85$, $r_i=1.05$, $c=1.05$, $r_d=0.7$.
- Here $\mu$ is the learning rate, $\alpha$ the momentum coefficient, $r_i,r_d$ the factors that raise and lower the learning rate, and $c$ the cost-ratio threshold that triggers lowering; the same-named $\alpha$ has a different use in section 4.
- The source reports that in batch mode adaptive momentum is faster.

**Pruning report** (source): two hidden layers of 20 units each; a model with 480 weights is trained first, saliency is checked every 100 epochs, and finally 25 weights are kept.

- The fraction kept is $25/480\approx0.0521$, about 5.21%.
- Deleted: $480-25=455$, about 94.79%.
- The source reports improved performance, with the boundary changing from curved to nearly straight; this case does not guarantee that pruning improves generalization in general.

Figure `lec05-kp11-counts`: On the left see the three bars: 480 before pruning, 455 deleted, 25 kept, then the ratios: about 5.21% kept and 94.79% deleted; the right is the [supplementary] p=0.5 contour, not a training experiment. The source case reports weights cut from 480 to 25; this lecture does not claim to rerun it. [Function: 2]

![The source case reports weights cut from 480 to 25; the right is a supplementary p=0.5 contour, not a training experiment.](../../assets/figures/lec05-kp11-counts-en.png)

**Supplementary demonstration** (not a model trained by the source): take the input score $r=x_2-0.6x_1-1$ and the continuous output $p=1/(1+e^{-r})$ with threshold 0.5. Lay a $401\times401$ grid on the 2-D plane, compute $p$ at each point and draw the contour $p=0.5$; only the class value flips between 0 and 1. The grid resolution, the threshold and the coordinate range must be recorded; a smooth picture is not a comparison of accuracy.

### Extension: full second-order compensation, exercises and derivations

**Supplementary quadratic example**: $H=\begin{bmatrix}4&1\\1&2\end{bmatrix}$, delete $w_1=0.5$, so $\delta w_1=-0.5$.

- If $\delta w_2=0$: the cost is $\frac12\times4\times0.5^2=0.5$.
- Allowing compensation: $\Delta J=0.5-0.5\delta w_2+(\delta w_2)^2$.
- Differentiating with respect to $\delta w_2$ gives $-0.5+2\delta w_2=0$, so $\delta w_2=0.25$; the cost is $0.5-0.125+0.0625=0.4375$, smaller than 0.5.

Figure `lec05-kp11-comp`: Read three steps from left to right: deleting only w1 costs 0.5; allowing w2 to compensate brings in a cross term; the minimum gives δw2=0.25 and cost 0.4375; the right shows the parabola and the central-difference check. [Function: 2]

![Supplementary quadratic example: deleting only w1 costs 0.5, allowing w2 to compensate lowers it to 0.4375; the central difference gives H=2.](../../assets/figures/lec05-kp11-comp-en.png)

**Small exercises**:

1. C has weight 0.5 and curvature 8; D has weight 2 and curvature 0.1. By saliency, which is deleted first? Hint: compute $s=Hw^2/2$ first.
2. Take $\tau=2$, $w=2$ and compute $\rho(w)$. Does this mean the weight has been deleted? Hint: tell the penalty apart from the actual operation.

**Exercise 1, worked solution**: $s_C=\frac12\times8\times0.5^2=1$; $s_D=\frac12\times0.1\times2^2=0.2$. By the estimate, delete D first.

**Exercise 2, worked solution**: $\rho(2)=2^2/(2^2+2^2)=4/8=0.5$. The weight is still 2; only actually setting it to zero or removing it counts as deletion.

**Check**: a larger weight can also have a smaller saliency. The next KP asks: can many connections share a few parameters from the start?

Figure `lec05-kp11-solution`: Read the two boxes from left to right: saliency 1 and 0.2 for C and D, so D first; ρ(2)=0.5 and the weight is still 2; a penalty is not a deletion. [Function: 3]

![Exercise answers: saliency of C and D is 1 and 0.2; ρ(2)=0.5 and the weight is still 2.](../../assets/figures/lec05-kp11-solution-en.png)

**Stating the Taylor conditions in full**: write the current weight vector as $\mathbf w$ and the perturbation as $\delta\mathbf w$. If the cost is twice differentiable, nearby it can be written as

$$
J(\mathbf w+\delta\mathbf w)-J(\mathbf w)\approx\nabla J(\mathbf w)^T\delta\mathbf w+\frac12\delta\mathbf w^TH\delta\mathbf w.
$$

Only near a stationary point may the first term be dropped. The diagonal approximation is a computational simplification; it does not mean the weights of any neural network are really independent. If only one weight is deleted and the others are fixed, the second-order cross terms vanish because the other perturbations are zero; if the others are allowed to compensate, the off-diagonal entries must be considered again. The $2\times2$ example above shows exactly this difference.

**Derivative of the saturating penalty**: let $u=w^2$, $v=\tau^2+w^2$; by the quotient rule

$$
\rho'(w)=\frac{2w(\tau^2+w^2)-w^2(2w)}{(\tau^2+w^2)^2}=\frac{2\tau^2w}{(\tau^2+w^2)^2}.
$$

A positive weight has a positive derivative, so the penalty part of gradient descent pulls it toward zero; a negative weight is pulled back toward zero in the opposite direction. At very large weights the derivative is also small because the curve has saturated. This is not the convex L1 penalty, and it does not guarantee exact zero after a finite number of updates.

**A counting ambiguity in the source report**: the source reports a pruned model with two hidden layers of 20 units each and 480 weights, but does not fully explain how inputs, outputs and biases are counted. One unique architecture cannot be back-computed and then taken as a fact of the original text. The 400-sample 2–3–2–1 simulation and the 480→25 pruning demonstration are recorded separately, and are not assumed to use the same data.

**A numerical check without second derivatives**: change only the $i$-th weight by a small step $h$ with the others fixed, and estimate by the central difference

$$
H_{ii}\approx\frac{J(\mathbf w+h\mathbf e_i)-2J(\mathbf w)+J(\mathbf w-h\mathbf e_i)}{h^2}.
$$

$\mathbf e_i$ is the direction whose $i$-th coordinate is 1 and the others 0; $h$ is the difference step, not the deletion threshold. Take $J(w)=(w-0.5)^2$, current $w=0.5$, $h=0.1$: the three costs are $0.01,0,0.01$, and the estimate is $(0.01-2\times0+0.01)/0.01=2$, matching the analytic second derivative. A step that is too large brings approximation error, and one that is too small may suffer floating-point cancellation; the difference formula is not a perfectly exact black box.

## Terms and source

| 中文 | English |
|---|---|
| 剪枝 | Pruning |
| 曲率 | Curvature |
| 海森矩陣 | Hessian |
| 顯著度 | Saliency |
| 正則化 | Regularization |
| 飽和懲罰 | Saturating penalty |
| 權重消除 | Weight elimination |
| 殘差 | Residual |
| 級聯相關法 | Cascade correlation |
| 泰勒展開 | Taylor expansion |

Source: [Chapter 4 KP11](https://ndhuccc.github.io/CCC-LNS/PR_115/Ch04-nonlinear-classifiers/index.html#kp11) (read 2026-10-25); reference codes [Lecu 90], [Hass 93], [Wein 90], [Bart 98], [Fahl 90]. The 480→25, the check every 100 epochs and the two momentum settings are all reported by the source; this time those experiments were not re-run, and the original exact curves are not available. The Bartlett result is only the source's order-of-magnitude summary; the original full theorem was not read, so it is not an unconditional error certificate. The hand-worked examples, the re-sampled scatter plot and the exercises in this lecture are [Supplement] and were checked with Python.
