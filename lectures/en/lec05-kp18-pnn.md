# KP18 The Probabilistic Neural Network (PNN)

> Level: undergraduate, year 3
>
> Pattern Recognition | Chapter 4, §4.17

[Slides: read and download](../../slides/lec05-kp18-pnn-en.jbd.json) | [中文版](../lec05-kp18-pnn.md)

## Learning objectives

- Explain how a PNN moves the Parzen estimate into a network and how unit-norm normalization turns a distance into an inner product.
- Write the hidden and output layers of a PNN and compute the outputs and the class on a small example.
- Explain the cost and the limit of a PNN: a hidden layer as large as the training set and a normalization that discards the length.

## KP18 The Probabilistic Neural Network (PNN)

**One-sentence summary**: A Parzen estimate is an average of kernels, so give every training point one neuron; after normalizing the vectors to length 1 the squared distance becomes an inner product and the formula takes the form of a network. Training is copying the data, and the price is keeping every training point.

### 1. One neuron per point

**Plain explanation**: Is there a network that needs almost no training?

- **Parzen estimate**: a kernel (Gaussian here) on every training point, averaged to estimate the class density $\hat p(x\mid\omega)$.
- **Kernel width $h$**: the width of the kernel; larger is smoother and smaller hugs the individual training points.

The Bayes decision compares the largest $P(\omega_i)\,\hat p(x\mid\omega_i)$. A sum of kernels is easy to compute in parallel, so every training point gets one neuron.

Figure `lec05-kp18-parzen`: five one-dimensional training points with a kernel each, averaged into the estimated density.

![Parzen estimate](../../assets/figures/lec05-kp18-parzen.png)

### 2. Distance becomes inner product

**Unit-norm normalization**: divide every feature vector by its own length $\|x\|=\sqrt{\sum_jx_j^2}$ so that its length becomes 1. Expanding the squared distance

$$
\|x-x_i\|^2=\|x\|^2+\|x_i\|^2-2x_i^Tx,
$$

it equals $2-2x_i^Tx$ when both lengths are 1. **Example**: $x=(0.6,0.8)$, $x_i=(1,0)$: inner product $0.6$ and squared distance $2-1.2=0.8$; directly $(0.4)^2+0.8^2=0.8$, the same.

Figure `lec05-kp18-circle`: two vectors on the unit circle and the chord between them.

![Distance becomes inner product](../../assets/figures/lec05-kp18-circle.png)

### 3. The discriminant

**Formal definition**: after substituting $\|x-x_i\|^2=2-2x_i^Tx$ and dropping the common $1/((2\pi)^{l/2}h^l)$,

$$
g(\omega_m)=\frac{P(\omega_m)}{N_m}\sum_{i=1}^{N_m}\exp\Bigl(\frac{x_i^Tx-1}{h^2}\Bigr).
$$

Check ($h=0.8$): for the unit vector $x=(0.6,0.8)$ the distance form $\exp(-\|x-x_i\|^2/2h^2)$ and the inner-product form $\exp((x_i^Tx-1)/h^2)$ both give $0.5353$. **Common misconception**: the formula can be used without normalizing. For $x=(1.2,1.6)$, not a unit vector, the distance form gives $0.1312$ and the inner-product form $1.3668$, far apart; normalization is required.

Figure `lec05-kp18-kernels`: the two forms for a unit and a non-unit vector.

![The two forms](../../assets/figures/lec05-kp18-kernels.png)

### 4. The architecture

**Probabilistic neural network** (PNN): the formula above moved into a network. The input layer has $l$ nodes; the hidden layer has $N$ nodes, the weights of node $k$ are the $k$-th training vector and its output is $y_k=\exp((x_k^Tx-1)/h^2)$; the output layer has one linear combiner per class connected only to the hidden nodes of that class: $\text{output}_m=\tfrac{P(\omega_m)}{N_m}\sum y_k$, and the largest wins. This network needs almost no training: no gradient descent, no local minima, no epochs.

Figure `lec05-kp18-arch`: two inputs, five hidden nodes and two outputs.

![The architecture](../../assets/figures/lec05-kp18-arch.png)

### 5. A full worked example

**Example** (designed here): class A at $20°,40°,60°$, class B at $100°,120°$, test vector at $70°$, $h=0.5$, priors 0.5. Hidden outputs $y_k$: A: $0.2396,0.5851,0.9410$; B: $0.5851,0.2396$. Outputs: A $=\tfrac{0.5}{3}\times1.7658=0.2943$; B $=\tfrac{0.5}{2}\times0.8247=0.2062$; A wins.

Figure `lec05-kp18-toy`: the five hidden outputs and the two class outputs.

![A full worked example](../../assets/figures/lec05-kp18-toy.png)

### 6. The kernel width

**Example** (designed here): two classes distinguished by direction (means $40°$ and $110°$, sd $25°$) with random lengths; 50 training and 500 new points per class, normalized and fed to a PNN. $h=0.02$ gives 95% on training (the classes overlap, so never 100%) and 89.6% on new points (hugging single points); $h=0.1\sim1$ gives about 91.6%; $h=5$ still gives 91.0%. A single cut at $75°$ gets 91.9% on new points and the PNN is close to it; this easy example is insensitive to $h$ and only a very small $h$ hurts.

Figure `lec05-kp18-hcurve`: accuracy against the kernel width $h$.

![The kernel width](../../assets/figures/lec05-kp18-hcurve.png)

### 7. How many points

The same data with $n$ training points per class, $h=0.3$, 20 random draws each. Mean accuracy on new points: $n=2$: 88.3% (sd 0.07); $n=10$: 91.8% (0.011); $n=50$: 92.0%; $n=200$: 92.0%. This easy data need not be kept in full; fewer points mean a smaller network.

Figure `lec05-kp18-nsub`: training points per class against accuracy on new points.

![How many points](../../assets/figures/lec05-kp18-nsub.png)

### 8. The cost

Each test point needs $N\cdot l$ multiply-adds and $N\cdot l$ stored numbers (8 bytes each): $N=100,l=2$: 200 operations, 1.6 KB; $N=10^4,l=10$: $10^5$ operations, 0.8 MB; $N=10^6,l=100$: $10^8$ operations, 0.8 GB. **To remember**: PNN = a parallel hardware version of the Parzen estimate; training is copying data and inference computes everything, moving the learning cost to the inference cost. It sits at one end of a spectrum with sparsification (KP21): keep all against keep only the support vectors (source).

Figure `lec05-kp18-cost`: the cost table for work and memory.

![The cost](../../assets/figures/lec05-kp18-cost.png)

### Extension: the price of normalization, practice and worked solution

**The price of normalization** (designed here): concentric rings whose classes differ only in radius (about 1.0 against 2.2), 200 points each, half for training and half for testing. After normalization both classes sit on the unit circle with the same angle distribution and the PNN gets only 49.5% on new points, which is guessing. Normalization discards the length; before using a PNN check that the class information lies in the direction and not in the length.

Figure `lec05-kp18-rings`: left two concentric rings, right after normalization.

![The price of normalization](../../assets/figures/lec05-kp18-rings.png)

**Practice**: training vectors $x_A=(1,0)$ and $x_B=(0,1)$, test vector $x=(0.8,0.6)$, priors 0.5; $y_k=\exp((x_k^Tx-1)/h^2)$.

1. For $h=1$, which class?
2. For $h=0.2$, which class, and how does the ratio of the outputs change?

Figure `lec05-kp18-practice`: the setup of the practice.

![Practice](../../assets/figures/lec05-kp18-practice.png)

**Worked solution of questions 1 and 2**: (1) $h=1$: $x_A^Tx=0.8$ and $x_B^Tx=0.6$; $y_A=e^{-0.2}=0.819$ and $y_B=e^{-0.4}=0.670$; outputs $0.409$ against $0.335$, class A. (2) $h=0.2$: $y_A=e^{-5}=0.0067$ and $y_B=e^{-10}=0.000045$; outputs $0.0034$ against $0.00002$, still class A, with the ratio growing from 1.22 to about 148. (3) Check: the smaller the $h$ the more a near training point is magnified and a far one suppressed.

Figure `lec05-kp18-practice-sol`: the calculations for the two widths.

![Practice solution](../../assets/figures/lec05-kp18-practice-sol.png)

## Terms and sources

| English | 中文 |
|---|---|
| Parzen estimate | Parzen 估計 |
| Kernel width | 核寬 |
| Unit-norm normalization | 單位範數正規化 |
| Probabilistic neural network (PNN) | 機率神經網路 |

Source: Chapter 4 KP18, §4.17 (read 2026-10-25). The Parzen estimate and the Bayes decision, the unit-norm simplification, the discriminant, the architecture, "almost no training" with its cost and the "to remember" line follow the source; the 70° toy, the kernel-width and training-size experiments, the cost table and the failure on concentric rings were designed and recomputed for this lecture ([added], (program)).
