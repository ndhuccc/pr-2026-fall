# KP18 Probabilistic Neural Networks (PNN)

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4 §4.17

[Slides: read and download](../../slides/lec05-kp18-pnn-en.jbd.json) | [中文版](../lec05-kp18-pnn.md)

## Learning objectives

- Explain how a PNN moves the Parzen estimate into a network, and how unit-norm normalization turns a distance into an inner product.
- Write the hidden and output layers of a PNN and compute the output and the class on a small example.
- Explain the cost and the limits of a PNN: the hidden layer equals the training set, and normalization throws the length away.

## KP18 Probabilistic Neural Networks (PNN)

**One-sentence summary**: A Parzen estimate is already an average of kernel functions, so give each training point one neuron; once the vectors are normalized to length 1, the squared distance becomes an inner product and the formula takes exactly the form of a network. Training is copying the data, and the price is keeping every training point.

### Prerequisites and symbols

**Three things you need first**:

- **Parzen estimation and Bayes decision**: put a kernel function on each training point and average them to estimate the probability density; decide the class with the largest $P(\omega)\,p(x\mid\omega)$.
- **Inner product and length of vectors**: $x_i^Tx=\sum_jx_{ij}x_j$; the length is $\|x\|=\sqrt{x^Tx}$.
- **RBF network** (KP16): hidden nodes are Gaussians around centres.

**Symbol table** (fixed for this lecture):

| Symbol | Meaning | Note |
|---|---|---|
| $x$, $x_i$ | the test vector, the $i$-th training vector | both normalized to length 1 first |
| $l$ | dimension of the vectors | |
| $N$, $N_m$ | total number of training points, number in class $m$ | |
| $h$ | kernel width | the larger, the smoother |
| $P(\omega_m)$ | prior probability of class $m$ | 0.5 in most examples of this lecture |
| $y_k$ | output of the $k$-th hidden node | $y_k=\exp((x_k^Tx-1)/h^2)$ |
| $g(\omega_m)$ | score of class $m$ | the largest gives the class |

### 1. One point, one neuron

**Plain-words explanation**: Is there a network that needs almost no training?

- **Parzen estimate**: put a kernel function (here a Gaussian) on every training point and average them to estimate the probability density $\hat p(x\mid\omega)$ of each class.
- **Kernel width $h$**: the width of the kernel function; the larger, the smoother; the smaller, the closer it hugs individual training points.

The Bayes decision compares the maximum of $P(\omega_i)\,\hat p(x\mid\omega_i)$. The sum of kernel functions can be computed in parallel anyway, so each training point gets one neuron.

Figure `lec05-kp18-parzen`: First look at the five one-dimensional training points (dots), each with a small blue Gaussian on it; then at the thick red line: it is the average of the five small Gaussians, the estimated density, with one peak where each group of training points is dense. [Function: 1]

![Parzen estimate: five one-dimensional training points, one kernel each, averaged into the estimated density.](../../assets/figures/lec05-kp18-parzen.png)

The next question: how does the distance inside the Gaussian turn into the "weighted sum" form of a network?

### 2. Distance becomes an inner product

- **Unit-norm normalization**: divide each feature vector by its own length $\|x\|=\sqrt{\sum_jx_j^2}$, so that the length becomes 1.

Expanding the squared distance:

$$
\|x-x_i\|^2=\|x\|^2+\|x_i\|^2-2x_i^Tx,
$$

which for lengths all equal to 1 is $2-2x_i^Tx$.

**Example**: $x=(0.6,0.8)$, $x_i=(1,0)$.

1. The inner product is $x_i^Tx=0.6$, so the squared distance is $2-1.2=0.8$.
2. Computed directly: $(0.6-1)^2+0.8^2=0.16+0.64=0.8$, the same.

Figure `lec05-kp18-circle`: First look at the two vectors $x$ and $x_i$ on the unit circle (two arrows, both of length 1); then at the dashed line (the chord) joining the two arrow tips: its squared length is $2-2x_i^Tx=0.8$. [Function: 1]

![Distance becomes inner product: two vectors on the unit circle and the chord joining them.](../../assets/figures/lec05-kp18-circle.png)

### 3. The discriminant function

Substituting $\|x-x_i\|^2=2-2x_i^Tx$ and dropping the factor $1/((2\pi)^{l/2}h^l)$ common to all classes:

$$
g(\omega_m)=\frac{P(\omega_m)}{N_m}\sum_{i=1}^{N_m}\exp\Bigl(\frac{x_i^Tx-1}{h^2}\Bigr).
$$

**Check** ($h=0.8$): the two forms, the distance form $\exp(-\|x-x_i\|^2/2h^2)$ and the inner-product form $\exp((x_i^Tx-1)/h^2)$, on two test vectors:

| test vector | unit vector? | $\|x-x_i\|^2$ | distance form | inner-product form |
|---|---|---:|---:|---:|
| $(0.6,0.8)$, $x_i=(1,0)$ | yes | 0.8 | 0.5353 | 0.5353 |
| $(1.2,1.6)$, $x_i=(1,0)$ | no | 2.6 | 0.1312 | 1.3668 |

**Common misconception**: this formula can be used without normalizing. For a non-unit vector the two forms differ a lot (0.1312 against 1.3668); normalization is a necessary precondition.

### 4. The network architecture

- **Probabilistic neural network** (PNN): the formula above moved into a network.

Three layers:

1. **Input layer**: $l$ nodes.
2. **Hidden layer**: $N$ nodes; the weights of the $k$-th node are the $k$-th training vector, and its output is $y_k=\exp((x_k^Tx-1)/h^2)$.
3. **Output layer**: one linear combiner per class, connected only to the hidden nodes of that class: $\text{output}_m=\tfrac{P(\omega_m)}{N_m}\sum y_k$; the largest gives the class.

This network needs almost no training: no gradient descent, local minima or epochs.

Figure `lec05-kp18-arch`: First look at the two inputs $x_1,x_2$ on the left joined to the five hidden nodes $y_1,\dots,y_5$ in the middle (each hidden node is one training point); then at the two outputs A and B on the right: the blue $y_1,y_2,y_3$ connect only to A and the orange $y_4,y_5$ only to B. [Function: 1]

![Network architecture: two inputs, five hidden nodes, two outputs.](../../assets/figures/lec05-kp18-arch.png)

### 5. A complete calculation

**Setting** (designed for this lecture): vectors are given by angle, the unit vector $(\cos\theta,\sin\theta)$. Class A at $20°,40°,60°$, class B at $100°,120°$; test vector $70°$; $h=0.5$; priors 0.5 each.

**Hidden outputs** $y_k=\exp((x_k^Tx-1)/h^2)$ with $x_k^Tx=\cos(\theta_k-70°)$:

| class | training angle | $x_k^Tx$ | $y_k$ |
|---|---:|---:|---:|
| A | $20°$ | 0.6428 | 0.2396 |
| A | $40°$ | 0.8660 | 0.5851 |
| A | $60°$ | 0.9848 | 0.9410 |
| B | $100°$ | 0.8660 | 0.5851 |
| B | $120°$ | 0.6428 | 0.2396 |

**Output layer**:

- A: $\tfrac{0.5}{3}\times(0.2396+0.5851+0.9410)=\tfrac{0.5}{3}\times1.7658=0.2943$.
- B: $\tfrac{0.5}{2}\times(0.5851+0.2396)=\tfrac{0.5}{2}\times0.8247=0.2062$.

A wins ($70°$ is closer to the $60°$ and $40°$ of class A).

### 6. The effect of the kernel width

**Experiment setting** (designed for this lecture, reproducible):

- Data: the two classes are distinguished by "direction". The direction (angle) is normal $N(40°,25°^2)$ for class A and $N(110°,25°^2)$ for class B; the length is uniform in $[0.5,3.0]$; 50 training points per class (100 in all, seed 0) and 500 new points per class (1000 in all, seed 1).
- Model: unit-norm normalization first, then the PNN; priors are the class proportions.
- Baseline: a single cut at $75°$ gives 91.9% on the new points.

| kernel width $h$ | 0.02 | 0.05 | 0.1 | 0.3 | 1 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| training accuracy | 95% | 93% | 93% | 93% | 93% | 93% |
| new-point accuracy | 89.6% | 90.9% | 91.7% | 91.6% | 91.5% | 91.0% |

The two classes overlap to begin with, so training accuracy does not reach 100%. At $h=0.02$ training is 95% and the new points 89.6%: the kernel is too narrow and hugs individual training points. From $h=0.1$ to 1 the new points are about 91.6%, close to the 91.9% of a single cut at $75°$. This easy example is insensitive to $h$; only a very small one hurts.

Figure `lec05-kp18-hcurve`: First see that the horizontal axis is the kernel width $h$ (log scale) and there are two lines: blue for training, red for new points; then look at the dashed line (the 91.9% of a single cut): the red line hugs it from $h\ge0.1$ on, and only the far left ($h=0.02$) drops. [Function: 3]

![Accuracy against the kernel width h.](../../assets/figures/lec05-kp18-hcurve.png)

### 7. How many points to keep

**Experiment setting**: the same data generator; $n$ training points per class (seeds 100 to 119, 20 different training sets), $h=0.3$, and the new points are the same 1000 as above.

| training points per class $n$ | 2 | 5 | 10 | 25 | 50 | 200 |
|---|---:|---:|---:|---:|---:|---:|
| mean new-point accuracy | 88.3% | 89.3% | 91.8% | 91.6% | 92.0% | 92.0% |
| standard deviation | 0.070 | 0.044 | 0.011 | 0.012 | 0.007 | 0.003 |

This simple data does not need every point kept; keep fewer and the network is smaller. After $n\ge10$ the accuracy hardly rises any more; the main change is that it gets steadier (smaller standard deviation).

Figure `lec05-kp18-nsub`: First see that the horizontal axis is the number of training points per class, the red dots are the means of the 20 sets and the black error bars the standard deviation; then look at the bars: very long at $n=2$, short from $n\ge10$. [Function: 3]

![Number of training points per class and the new-point accuracy.](../../assets/figures/lec05-kp18-nsub.png)

### 8. The cost

Each test needs $N\cdot l$ multiply-adds and the network stores $N\cdot l$ numbers (8 bytes each):

| training points $N$ | dimension $l$ | multiply-adds per test | memory |
|---:|---:|---:|---:|
| 100 | 2 | 200 | 1.6 KB |
| $10^4$ | 10 | $10^5$ | 0.8 MB |
| $10^6$ | 100 | $10^8$ | 0.8 GB |

**How to remember**: PNN = the parallel hardware version of the Parzen estimate; training = copying the data, inference = computing everything again, shifting the learning cost onto the inference cost. It and sparsification (KP21) are the two ends of a spectrum: keep everything versus keep only the support vectors (source).

### Extension: the cost of normalization, exercises and worked solutions

**The cost of normalization** (designed for this lecture): concentric rings whose two classes differ only in radius.

- Data: uniform angle; radius $N(1.0,0.15^2)$ for class A and $N(2.2,0.2^2)$ for class B; 200 points per class, 400 in all (`default_rng(0)`), split at random into 200 for training and 200 for testing; $h=0.3$.
- Result: after normalization both classes lie on the unit circle with the same angle distribution, and the PNN gets only 49.5% on the new points, which is guessing.

Normalization throws the length away; before using a PNN check that the class information is in the direction, not in the length.

Figure `lec05-kp18-rings`: First look at the left panel: two concentric rings (blue inner, orange outer); then the right panel: after normalization the two classes are mixed on the same circle and cannot be told apart. [Function: 1, 3]

![The cost of normalization: concentric rings on the left, after normalization on the right.](../../assets/figures/lec05-kp18-rings.png)

**Small exercises**: training vectors $x_A=(1,0)$, $x_B=(0,1)$, test vector $x=(0.8,0.6)$, priors 0.5 each; $y_k=\exp((x_k^Tx-1)/h^2)$.

1. For $h=1$, which class?
2. For $h=0.2$, which class? How does the ratio of the two class outputs change?

**Exercise 1, worked solution**: $h=1$: $x_A^Tx=0.8$, $x_B^Tx=0.6$; $y_A=e^{-0.2}=0.819$, $y_B=e^{-0.4}=0.670$; outputs $0.5\times0.819=0.409$ against $0.5\times0.670=0.335$, so A.

**Exercise 2, worked solution**: $h=0.2$ ($h^2=0.04$): $y_A=e^{-0.2/0.04}=e^{-5}=0.0067$, $y_B=e^{-0.4/0.04}=e^{-10}=0.000045$; outputs $0.0034$ against $0.00002$, still A; the ratio goes from $0.409/0.335\approx1.22$ to about 148.

**Check**: the smaller $h$, the more near training points are magnified and far ones suppressed.

## Terms and source

| 中文 | English |
|---|---|
| Parzen 估計 | Parzen estimate |
| 核寬 | Kernel width |
| 單位範數正規化 | Unit-norm normalization |
| 機率神經網路 | Probabilistic neural network (PNN) |

Source: Chapter 4 KP18, §4.17 (read 2026-10-25). The Parzen estimate and Bayes decision, the simplification by unit-norm normalization, the discriminant, the network architecture, "almost no training" and the cost, and "how to remember" follow the source; the $70°$ small example, the kernel-width and training-point-count experiments, the cost table and the failure on concentric rings were designed and recomputed for this lecture ([Supplement], computed by a program).
