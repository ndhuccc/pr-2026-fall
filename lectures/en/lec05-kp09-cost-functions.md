# KP09 Choosing the Cost Function

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.8

[Slides: read and download](../../slides/lec05-kp09-cost-functions-en.jbd.json) | [中文版](../lec05-kp09-cost-functions.md)

## Learning objectives

- Explain the two flaws of squared error and why a confidently wrong output cannot learn.
- Derive that with cross-entropy and a sigmoid or softmax the $\delta$ becomes $y-\hat y$, and explain that cross-entropy is the negative log-likelihood.
- Explain the idea and the price of discriminative learning and of Bayesian training.

## KP09 Choosing the Cost Function

**One-sentence summary**: Squared error is not the only choice. For classification the cross-entropy is often the better loss: the sigmoid slope does not squeeze it away and the worse the error the harder it fixes; with softmax the backpropagation $\delta$ is simply $y-\hat y$.

### Prerequisites and symbols

**Three things you need first**:

- **Sigmoid and the $\delta$ of backpropagation** (KP06): $\delta=-\partial J/\partial net$ and the update is $\eta\,\delta\times$input.
- **Probability**: the probability of an event lies between 0 and 1; probabilities of independent events multiply; $\ln$ turns a product into a sum.
- **Bayes' theorem** (Chapter 2): posterior $\propto$ likelihood $\times$ prior.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $net$ | weighted sum of the output unit | the $v$ of KP06 |
| $\sigma(v)$ | sigmoid | $1/(1+e^{-v})$ |
| $y$ | target | 0 or 1 for two classes; a vector with a single 1 for several |
| $\hat y$ | output | the network's estimate of the probability that the target is 1 |
| $J$ | cost | squared error in section 1, cross-entropy from section 3 |
| $\delta$ | error signal | $\delta=-\partial J/\partial net$ |
| $\eta$ | learning rate | |
| $v_k$, $\hat y_k$ | weighted sum and output of class $k$ in softmax | section 6 |

### 1. Two flaws of squared error

**Plain explanation**: The speed-ups of KP08 all rewrite the update rule, but where the update goes depends on the cost function itself.

- **Unfair**: errors are squared before summing, so big errors dominate. Errors $0.9$ and $0.1$ differ 9 times, but squared they are $0.81$ and $0.01$, 81 times.
- **It can stall**: when the output $\hat y$ is wrong at an extreme (target 1, output $0.001$) the squared error is only $0.499$ and never grows, so gradient descent can get stuck (source citing Witt 00). Contrast: another loss, $-\ln\hat y$, is $6.908$ at $\hat y=0.001$.

Figure `lec05-kp09-loss`: First see the squared-error curve for target 1 rise only to 0.499 as the output approaches 0; then see the other curve, −ln ŷ, shoot up to 6.908; the right side lists the two faults of the squared error: unfair and getting stuck. [Function: 1, 2]

![The two losses against the output ŷ for target 1: at ŷ = 0.001 the squared error is 0.499 and −ln ŷ is 6.908.](../../assets/figures/lec05-kp09-loss-en.png)

### 2. The plateau: δ goes to 0 when the output is wrong at an extreme

**Plateau**: a flat region where the cost is large but the gradient is almost 0, so gradient descent hardly moves on it.

For a single sigmoid output with squared error, $\delta=(y-\hat y)\,\hat y(1-\hat y)$. The closer $\hat y$ is to 0 or 1 the smaller the slope $\hat y(1-\hat y)$, squeezing even a big error into a small signal. With target $y=1$ and $net=-10$, $\hat y=0.000045$, the error is almost 1 and $\delta=0.000045$.

Figure `lec05-kp09-mse-delta`: First see δ almost 0 when net is very negative or very positive (the plateaus on both sides); then see that only a small middle stretch has a large δ; the right gives the formula δ = (y − ŷ)ŷ(1 − ŷ) and δ = 0.000045 at net = −10. [Function: 2]

![Squared-error δ against net (target 1): plateaus on both sides, and only 0.000045 at net = −10.](../../assets/figures/lec05-kp09-mse-delta-en.png)

### 3. Cross-entropy: cancel the slope

**Cross-entropy**: read the output $\hat y$ as the probability that the target is 1. **Formal definition**:

$$
J=-\bigl(y\ln\hat y+(1-y)\ln(1-\hat y)\bigr),
$$

which for $y=1$ is $-\ln\hat y$.

**Derivation, step by step**:

1. $\partial J/\partial\hat y=-(y-\hat y)/[\hat y(1-\hat y)]$.
2. The sigmoid slope is $\partial\hat y/\partial net=\hat y(1-\hat y)$.
3. By the chain rule they multiply and $\hat y(1-\hat y)$ cancels exactly, giving $\delta=-\partial J/\partial net=y-\hat y$.

The sign follows KP06 ($\delta=-\partial J/\partial net$); the source writes $\hat y-y$, which differs by a sign.

**Numbers**: at $net=-10$ the squared-error $\delta=0.00005$ and the cross-entropy $\delta=1.0000$.

With target $y=1$:

| $net$ | $\hat y$ | $\delta$ of squared error | $\delta$ of cross-entropy |
|---:|---:|---:|---:|
| $-10$ | 0.00005 | 0.00005 | 1.0000 |
| $-5$ | 0.0067 | 0.00660 | 0.9933 |
| $-2$ | 0.1192 | 0.09248 | 0.8808 |
| $0$ | 0.5000 | 0.12500 | 0.5000 |
| $2$ | 0.8808 | 0.01252 | 0.1192 |
| $5$ | 0.9933 | 0.00004 | 0.0067 |

The cross-entropy $\delta$ is not squeezed; squared error gives almost no signal at $net=-10$.

Figure `lec05-kp09-delta-table`: First see the three-step derivation of the cross-entropy on the left: the partial derivative, the sigmoid slope, and the chain rule where ŷ(1 − ŷ) cancels; then see the two δ for y = 1 and net from −10 to 5 on the right: the cross-entropy δ is not squeezed. [Function: 2]

![The three-step derivation for the cross-entropy and the two δ for net = −10 to 5: 0.00005 against 1.0000 at net = −10.](../../assets/figures/lec05-kp09-delta-table-en.png)

### 4. Training compared

**Experiment setup** (designed here, implemented in a program):

- Model: one sigmoid neuron $\hat y=\sigma(b+wx)$.
- Data: four points $x=-2,-1,1,2$ with targets $0,0,1,1$.
- Start: $w=-3$, $b=0$, so all four are wrong.
- Training: $\eta=0.5$, batch updates (each epoch uses the mean $\delta$ of the four points).
- "All right": the number of points with $\hat y>0.5$ agreeing with the target is 4.

**Result**: cross-entropy gets all four right in 5 epochs and squared error needs 85 (program).

**Common misconception**: only cross-entropy can classify correctly. Both costs end up correct; the difference is the speed from a very wrong start.

Figure `lec05-kp09-train`: First see the output at x = 2 rise with the epoch: the cross-entropy passes 0.5 at epoch 5 and the squared error only at epoch 85; the right shows the setup and the common myth. [Function: 2]

![The output at x = 2 against the epoch: all four points are right after 5 epochs for the cross-entropy and 85 for the squared error.](../../assets/figures/lec05-kp09-train-en.png)

### 5. Likelihood: cross-entropy is the negative log-likelihood

**Likelihood**: the probability of seeing this data if the model is right; larger is better and independent samples multiply. **Example**: outputs $0.9,0.8,0.3,0.1$ with targets $1,1,0,0$.

- The probability of each target: $0.9,\ 0.8,\ 1-0.3=0.7,\ 1-0.1=0.9$.
- Product: $0.9\times0.8\times0.7\times0.9=0.4536$, $-\ln0.4536=0.7905$.
- The four cross-entropies add up to $0.105+0.223+0.357+0.105=0.790$, the same.

Minimizing cross-entropy is maximizing likelihood.

Figure `lec05-kp09-likelihood`: First see the four samples on the left: output, target, probability of the target and −ln; then see the two green results: the product 0.4536 and −ln = 0.7905 equal the sum of the four cross-entropies. [Function: 2]

![Likelihood of four samples: the probabilities multiply to 0.4536 and −ln 0.4536 = 0.7905, equal to the sum of the four cross-entropies.](../../assets/figures/lec05-kp09-likelihood-en.png)

### 6. softmax

**softmax** for several classes:

$$
\hat y_k=\frac{e^{v_k}}{\sum_{k'}e^{v_{k'}}},
$$

every output lies between 0 and 1 and they sum to exactly 1.

**Example**: $v=(2,1,0.1)$.

- $e^{2}=7.389$, $e^{1}=2.718$, $e^{0.1}=1.105$, with sum $11.212$.
- $\hat y=(0.659,\ 0.242,\ 0.099)$.
- With target $y=(1,0,0)$: $J=-\ln0.659=0.417$.
- The $\delta_k=y_k-\hat y_k=(0.341,-0.242,-0.099)$ needed by backpropagation equals numerical differences (program check).

Figure `lec05-kp09-softmax`: First see the three bars of v, then ŷ after the softmax (summing to 1), and finally δ (positive for the target class, negative for the rest); the right shows the step-by-step calculation. [Function: 1, 2]

![v = (2, 1, 0.1) through the softmax gives ŷ = (0.659, 0.242, 0.099) and δ = (0.341, −0.242, −0.099).](../../assets/figures/lec05-kp09-softmax-en.png)

### 7. Discriminative learning

**Discriminative learning**: since the goal is a low classification error, focus on the largest posterior and push the decision surface to lower the error directly. **Contrast example** (designed here, implemented in a program): $x=-3,-2,-1$ are class 0; $x=1,2,3$ and the outlier $x=40$ are class 1.

- Squared error: the least-squares line $y\approx ax+b$ ($a=0.0165$, $b=0.477$), cut where the line equals 0.5, at $1.40$; $x=1$ is misclassified.
- Cross-entropy: one sigmoid output, gradient descent (start 0, $\eta=0.5$, 20000 rounds), cut at about $0$; all seven are right.

The contrast changes both the output and the cost; the error rate itself is not differentiable, so a smooth version is used, with a risk of local minima (source, which also mentions deterministic annealing).

Figure `lec05-kp09-lsfit`: First see the outlier x = 40 flatten the least-squares line in the left chart; then see the two boundaries in the zoom on the right: the squared-error cut at 1.40 (x = 1 wrong) and the cross-entropy cut at 0. [Function: 1, 3]

![The outlier bends the boundary: squared-error cut at 1.40, cross-entropy cut near 0.](../../assets/figures/lec05-kp09-lsfit-en.png)

### 8. Bayesian training

**Bayesian training**: set a prior $p(w)$ on the weights; with the data, Bayes' rule gives the posterior $p(w\mid Y)=p(Y\mid w)\,p(w)/p(Y)$; classifying averages over all $w$, $P(\omega_k\mid x;Y)=\int\phi_k(x;w)\,p(w\mid Y)\,dw$. **Example** (designed here, from the Gaussian formulas):

- Prior: $w\sim N(0,2^2)$.
- Every sample says $w\approx1.5$ with noise standard deviation 1; $n$ samples.
- Posterior precision (inverse variance) $=\tfrac14+n$ and posterior mean $=1.5n/(\tfrac14+n)$.

| $n$ | 0 | 1 | 5 | 20 |
|---:|---:|---:|---:|---:|
| posterior sd | 2 | 0.894 | 0.436 | 0.222 |
| posterior mean | 0 | 1.2 | 1.43 | 1.48 |

 Price: a high-dimensional integral is expensive; the source reminds us that replacing least squares often gives no real gain in practice.

Figure `lec05-kp09-posterior`: First see the wide bell of n = 0 (the prior), then see the bell narrow and its centre move toward 1.5 as n grows; the right gives the table of posterior standard deviation and mean. [Function: 1, 2]

![The posterior: for n = 0, 1, 5, 20 the standard deviation is 2, 0.894, 0.436, 0.222 and the mean 0, 1.2, 1.43, 1.48.](../../assets/figures/lec05-kp09-posterior-en.png)

### Extension: worse starts, practice and worked solution

**Worse starts**: with the data of section 4 and $\eta=0.5$ ($b=0$), epochs needed:

| Start $w$ | $-1$ | $-2$ | $-3$ | $-4$ | $-6$ | $-8$ | $-10$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| squared error | 11 | 31 | 85 | 227 | 1631 | 11950 | 88141 |
| cross-entropy | 2 | 4 | 5 | 6 | 9 | 12 | 14 |

The squared-error $\delta$ shrinks exponentially as the start gets worse and the epochs grow roughly exponentially; the cross-entropy $\delta$ stays near 1.

Figure `lec05-kp09-init`: First see the squared-error points climb on the log scale, then see the cross-entropy points stay almost flat; the right explains why the gap keeps growing. [Function: 2]

![Epochs needed as the start gets worse: at w = −10, 88,141 for the squared error and 14 for the cross-entropy.](../../assets/figures/lec05-kp09-init-en.png)

**Practice**: a single sigmoid output, target 1, $net=-4$.

1. What is $\hat y=\sigma(-4)$?
2. What are the squared-error $\delta=(1-\hat y)\,\hat y(1-\hat y)$ and the cross-entropy $\delta=1-\hat y$, and how many times larger is the cross-entropy one?

**Worked solution (question 1)**: $\hat y=1/(1+e^{4})=0.0180$.

**Worked solution (question 2)**:

- Squared error $\delta=0.9820\times0.0180\times0.9820=0.01735$.
- Cross-entropy $\delta=0.9820$.
- Ratio $0.9820/0.01735=56.6$.

**Check**: the ratio is exactly $1/[\hat y(1-\hat y)]$ and grows as the output gets more extreme; at $net=-10$ it is about 22000.

Figure `lec05-kp09-practice`: The left is Q1: ŷ = 0.0180 at net = −4; the right is Q2: squared-error δ = 0.01735, cross-entropy δ = 0.9820 and a factor of 56.6, each with its check. [Function: 3]

![Two exercises with worked answers: ŷ = 0.0180 and a δ ratio of 56.6.](../../assets/figures/lec05-kp09-practice-en.png)

## Terms and sources

| English | 中文 |
|---|---|
| Plateau | 高原 |
| Cross-entropy | 交叉熵 |
| Likelihood | 概似 |
| softmax | softmax |
| Discriminative learning | 判別式學習 |
| Bayesian training | 貝氏訓練 |

Source: Chapter 4 KP09, §4.8 (read 2026-10-25). The two flaws of squared error, the cross-entropy and softmax formulas, the simplified $\delta$, and the descriptions of discriminative learning and Bayesian training follow the source; the single-neuron training comparison, the outlier contrast, the Gaussian posterior example and every number were designed and recomputed for this lecture ([added], (program)). The sign of $\delta$ is fixed as $-\partial J/\partial net$.
