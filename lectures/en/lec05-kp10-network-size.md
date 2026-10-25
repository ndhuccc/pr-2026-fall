# KP10 Network size, generalization and early stopping

!!! note "Self-study"
    This unit (KP10) is self-study: it is not taught in class, so please read it on your own.

> Level: third-year undergraduate | Self-study | English edition

Read this independently with weighted scores, basic differentiation and matrices as prerequisites. New terms are introduced when needed.

[Open the matching slides](../../slides/lec05-kp10-network-size-en.jbd.json) | [中文版](../lec05-kp10-network-size.md)

## Learning objectives

- Count parameters and distinguish them from units.
- Select a checkpoint and distinguish three data roles.
- Explain why a cell bound is not a quality guarantee.

## KP10 Network size, generalization and early stopping

**One-sentence summary**：Select size and training duration using held-out evidence, not training fit alone.

**Plain explanation**：Separate memorizing training answers from predicting new data before discussing size. Parameter counts below belong to explicit architectures, not hidden-unit counts alone.

**Formal definition**：The sections define terms, symbols and assumptions while keeping symbols consistent for the same quantity.

**Example**：All new worked examples are [Added] and checked in Python. Source experiment reports are identified separately.

**Common misconception**：Fewer parameters and longer fitting do not independently guarantee better new-data performance.

**Practice**：The final section provides questions, hints and worked checks for use after your own attempt.

### What capacity can learn

Separate memorizing training answers from predicting new data before discussing size. Parameter counts below belong to explicit architectures, not hidden-unit counts alone.

**Generalization**: Correct prediction on data not used for fitting is generalization; memorizing training answers is different.

This continuous-prediction illustration exposes a trade-off also faced in classification. Find the main trend before treating sample fluctuations as rules.

![A smooth sine trend and six illustrative noisy samples; the piecewise interpolant is not a fitted neural network.](../../assets/figures/lec05-kp10-trend.png)

Figure `lec05-kp10-trend`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

**Free parameter**: A free parameter is an independently adjustable number; weights and biases both count.

Use two inputs, three hidden units and one output, with dense connections and one bias per computing unit.

Hidden layer: $(2+1)\times3=9$. Output layer: $(3+1)\times1=4$. There are $9+4=13$ parameters, not three.

**Underfitting**: Underfitting means the model misses important structure and can perform poorly even on training data.

**Overfitting**: Overfitting adapts to incidental training details at the expense of prediction on new data.

Size alone does not prove overfitting. Data, weight magnitudes, constraints and the fitting procedure also matter.

### Choose checkpoints using held-out data

Even a fixed architecture may adapt too closely to training data. Examine two loss curves, choose among five checkpoints, and distinguish validation from testing.

**Validation set**: Validation data do not update weights; they help choose a model or training checkpoint.

**Overtraining**: Overtraining occurs when further fitting of a fixed architecture starts hurting validation performance.

Training loss keeps falling; validation loss rises after its minimum at epoch 3. The curves need not cross or start together.

![Training and validation losses at five checkpoints: validation is lowest at epoch three and training at epoch five.](../../assets/figures/lec05-kp10-early.png)

Figure `lec05-kp10-early`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

**Early stopping**: Early stopping uses validation performance and restores the best checkpoint; implementation may allow patience.

Validation losses at epochs 1–5 are $0.55,0.35,0.25,0.28,0.40$. The minimum is $0.25$ at epoch 3.

Epoch 5 has lower training loss, but validation loss rises from $0.25$ to $0.40$: $0.40-0.25=0.15$.

**Training data** fit weights to patterns.

**Validation data** select size, penalty strength and checkpoints without directly fitting weights.

**Test set**: reserve it for evaluation after model selection. Reusing it to choose models breaks independence; avoid duplicate-subject and temporal leakage.

One error among ten gives $1/10=0.1$; two give $2/10=0.2$. One case changes the estimate by ten percentage points.

Repeated splits or cross-validation can support selection, but fitting and evaluation must remain separated. They do not create new independent data.

There is no best neuron count independent of the data and task.

### Geometric capacity versus an actual XOR construction

Held-out selection asks about prediction, while geometry counts possible cells. XOR makes the distinction between a maximum and an actual arrangement concrete.

**Cell-count bound**: K hyperplanes partition d-dimensional space into at most M cells. General position attains the maximum; degenerate arrangements may not.

$M_{\max}(K,d)=\sum_{m=0}^{d}\binom{K}{m}$. K counts hidden units and d input dimensions; $\binom{K}{m}=0$ when $m>K$.

General position excludes coincidences, parallelism and excessive intersections that reduce cell count; the precise condition depends on dimension.

![Maximum hyperplane cell counts versus hidden-unit count for input dimensions one, two and three.](../../assets/figures/lec05-kp10-regions.png)

Figure `lec05-kp10-regions`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

For $d=2,K=2$, $M_{\max}=1+2+1=4$. The three terms count choices of 0, 1 and 2 lines.

The XOR boundaries $x_1+x_2=0.5$ and $x_1+x_2=1.5$ are parallel: three actual bands, with both A points in the middle.

An upper bound of four accommodates three cells; sufficiency of two units still needs this explicit construction.

![Four XOR points and two parallel boundaries enclosing the positive band; three actual cells versus a maximum of four.](../../assets/figures/lec05-kp10-xor.png)

Figure `lec05-kp10-xor`：[Added] Compare the labelled alternatives, then check them against the numerical discussion. Schematic model drawings are not exact experimental traces.

### Three size-selection strategies

A cell bound does not find good weights. Return to practical model search and compare shrinking a network with growing one.

**Analytical methods** estimate capacity using algebra or statistics, often without optimization details.

**Pruning** fits a larger network, then removes less useful connections by a rule.

**Constructive methods** grow units from a small architecture. All routes need validation; the next KP studies pruning.

### Interpret the source demonstration within scope

With capacity and selection separated, the source sine demonstration becomes a case rather than a universal setting.

The source uses 15 training points and 10 independent test points for $y=\sin(2\pi x)+\epsilon$, where $\epsilon$ is observation noise.

$\hat y=\sum_{j=1}^{k}v_j\tanh(a_jx+b_j)+c$. Adjustable a, b, v and c give $3k+1$ parameters; k counts hidden units.

The source describes k around 3–5 as useful and possible overfitting at k=15. These are not universal choices; this training was not rerun here.

### Practice and worked checks

Cover the worked answers first, make both decisions, then check the numerical reasoning.

Question 1: training losses are $0.40,0.20,0.10$ and validation losses $0.45,0.25,0.30$. Choose a checkpoint by the validation minimum.

Question 2: count the maximum cells of three planar lines in general position using $\binom30+\binom31+\binom32$. Does parallelism attain it?

1. The minimum of $0.45,0.25,0.30$ is $0.25$: retain checkpoint 2, despite lower final training loss.

2. Three planar lines give $M_{\max}=1+3+3=7$. Three parallel lines give only four bands.

3. Validation loss rises by $0.30-0.25=0.05$. Cell count did not enter the checkpoint comparison.

#### Why does the cell count have this form?

In general position the K-th hyperplane splits some existing cells. The additional pieces correspond to the cells formed by the previous K−1 hyperplanes inside this new, lower-dimensional plane. Hence

$$
R(K,d)=R(K-1,d)+R(K-1,d-1).
$$

Start from $R(0,d)=1$ and $R(K,0)=1$. Pascal's identity gives $R(K,d)=\sum_{m=0}^d\binom Km$. This counts partitions; it does not ensure that the output layer separates arbitrary cell labels.

#### An executable checkpoint check

```python
validation = [0.55, 0.35, 0.25, 0.28, 0.40]
best_epoch = min(range(len(validation)), key=validation.__getitem__) + 1
assert best_epoch == 3
```

This selects from supplied checkpoints, not trained networks. Real fitting also needs saved and restored weights, a fixed data split and a specified assessment metric.

#### What mean squared error measures

The source sine example predicts continuous values with $L=\frac1N\sum_{n=1}^N(\hat y_n-t_n)^2$, where t is target, hat y prediction and N the number of examples in that split. Errors one and minus one give $L=(1^2+(-1)^2)/2=1$. Classification needs a threshold and an additional classification-error measure. The earlier five-checkpoint table is a teaching example, not an execution of the sine demo.


## Glossary and symbol reminders

| English | 中文 |
|---|---|
| Generalization | 泛化 |
| Free parameter | 自由參數 |
| Underfitting | 欠擬合 |
| Overfitting | 過擬合 |
| Validation set | 驗證集 |
| Overtraining | 過度訓練 |
| Early stopping | 早停 |
| Test set | 測試集 |
| Cell-count bound | 區域數上界 |

Read symbols by their local definitions. Distinguish weights, scores, predictions and loss; identically named hyperparameters in different experiments may have different roles.

## Sources and supplementary scope

- [Chapter 4, KP10](https://ndhuccc.github.io/CCC-LNS/PR_115/Ch04-nonlinear-classifiers/index.html#kp10), accessed 2026-10-25.
- The source groups validation with testing, describes stopping at divergence and infers sufficiency from a cell bound. This material separates data roles, validation minima and constructive sufficiency. Real training losses also need not decrease monotonically.
- Source reference code: [Mirc 89].
- Original Figures 4.14–4.16 were inspected. New teaching diagrams do not claim to be the original figures or exact experimental curves.
- Historical reference codes follow the source. Full papers, theorem conditions and experimental records were not all available; those limits are retained.
